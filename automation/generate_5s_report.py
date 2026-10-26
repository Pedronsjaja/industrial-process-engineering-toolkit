import argparse
import sys
from collections import defaultdict

from csv_utils import DataError, read_csv, write_csv


SENSES = ("Seiri", "Seiton", "Seiso", "Seiketsu", "Shitsuke")
REQUIRED = ("sense", "score")


def summarize(rows):
    totals = defaultdict(list)
    for row_number, row in enumerate(rows, start=2):
        sense = row["sense"].strip().capitalize()
        if sense not in SENSES:
            raise DataError(f"row {row_number}: sense must be one of {', '.join(SENSES)}")
        try:
            score = float(row["score"])
        except (TypeError, ValueError) as exc:
            raise DataError(f"row {row_number}: score must be a number from 0 to 5") from exc
        if not 0 <= score <= 5:
            raise DataError(f"row {row_number}: score must be from 0 to 5")
        totals[sense].append(score)
    report = [
        {"sense": sense, "average_score": f"{sum(scores) / len(scores):.2f}", "criteria_count": str(len(scores))}
        for sense in SENSES
        if (scores := totals[sense])
    ]
    all_scores = [score for scores in totals.values() for score in scores]
    if all_scores:
        report.append(
            {
                "sense": "Overall",
                "average_score": f"{sum(all_scores) / len(all_scores):.2f}",
                "criteria_count": str(len(all_scores)),
            }
        )
    return report


def main():
    parser = argparse.ArgumentParser(description="Summarize 5S audit scores from CSV.")
    parser.add_argument("input", help="Audit CSV with sense and score columns")
    parser.add_argument("--output", required=True, help="Destination summary CSV")
    args = parser.parse_args()
    try:
        _, rows = read_csv(args.input, REQUIRED)
        write_csv(args.output, ["sense", "average_score", "criteria_count"], summarize(rows))
    except DataError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
