import argparse
import math
import sys
from datetime import date

from csv_utils import DataError, parse_iso_date, read_csv, write_csv


ACTION_REQUIRED_COLUMNS = ("action_id", "status", "due_date")


def collect(args):
    metrics = []
    if args.actions:
        _, actions = read_csv(args.actions, ACTION_REQUIRED_COLUMNS)
        open_actions = [row for row in actions if row["status"].strip().lower() not in {"closed", "complete", "completed"}]
        overdue = []
        for row_number, row in enumerate(actions, start=2):
            if (
                row["status"].strip().lower() not in {"closed", "complete", "completed"}
                and row["due_date"].strip()
                and parse_iso_date(row["due_date"], "due_date", row_number) < args.as_of
            ):
                overdue.append(row)
        metrics.extend(
            [
                {"metric": "Open Actions", "value": str(len(open_actions)), "unit": "actions"},
                {"metric": "Overdue Actions", "value": str(len(overdue)), "unit": "actions"},
            ]
        )
    if args.inventory:
        _, assets = read_csv(args.inventory, ("asset_id", "status"))
        available = sum(row["status"].strip().lower() in {"available", "in stock", "active"} for row in assets)
        ratio = available / len(assets) if assets else 0
        metrics.append(
            {"metric": "Inventory Availability", "value": f"{ratio:.4f}", "unit": "ratio"}
        )
    if args.fmea:
        _, risks = read_csv(args.fmea, ("severity", "occurrence", "detection"))
        threshold = args.high_risk_rpn_threshold
        high_risk = 0
        for row_number, row in enumerate(risks, start=2):
            try:
                ratings = [int(row[column]) for column in ("severity", "occurrence", "detection")]
            except ValueError as exc:
                raise DataError(f"row {row_number}: FMEA ratings must be integers") from exc
            if any(not 1 <= value <= 10 for value in ratings):
                raise DataError(f"row {row_number}: FMEA ratings must be from 1 to 10")
            high_risk += int(ratings[0] * ratings[1] * ratings[2] >= threshold)
        metrics.append(
            {
                "metric": f"FMEA Items At/Above RPN {threshold}",
                "value": str(high_risk),
                "unit": "items",
            }
        )
    if args.audit:
        _, audit = read_csv(args.audit, ("sense", "score"))
        if audit:
            try:
                scores = [float(row["score"]) for row in audit]
            except ValueError as exc:
                raise DataError("5S audit scores must be numeric") from exc
            if any(not math.isfinite(score) or not 0 <= score <= 5 for score in scores):
                raise DataError("5S audit scores must be from 0 to 5")
            metrics.append(
                {"metric": "5S Score", "value": f"{sum(scores) / len(scores):.2f}", "unit": "score (0-5)"}
            )
    return metrics


def main():
    parser = argparse.ArgumentParser(description="Generate KPI rows from supplied CSV data.")
    parser.add_argument("--actions", help="Actions CSV (action_id,status,due_date)")
    parser.add_argument("--inventory", help="Inventory CSV (asset_id,status)")
    parser.add_argument("--fmea", help="FMEA CSV (severity,occurrence,detection)")
    parser.add_argument("--audit", help="5S audit CSV (sense,score)")
    parser.add_argument("--output", required=True, help="Destination KPI CSV")
    parser.add_argument(
        "--high-risk-rpn-threshold",
        type=int,
        default=200,
        help="Locally configurable RPN threshold; default is an example, not a universal risk criterion",
    )
    parser.add_argument("--as-of", type=date.fromisoformat, default=date.today(), help="Date for overdue checks (YYYY-MM-DD)")
    args = parser.parse_args()
    if not any((args.actions, args.inventory, args.fmea, args.audit)):
        parser.error("provide at least one input CSV")
    if args.high_risk_rpn_threshold < 1:
        parser.error("--high-risk-rpn-threshold must be positive")
    try:
        write_csv(args.output, ["metric", "value", "unit"], collect(args))
    except DataError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
