import argparse
import sys

from csv_utils import DataError, read_csv, write_csv


RATING_COLUMNS = ("severity", "occurrence", "detection")


def calculate(rows):
    scored = []
    for row_number, row in enumerate(rows, start=2):
        ratings = {}
        for column in RATING_COLUMNS:
            try:
                value = int(row[column])
            except (TypeError, ValueError) as exc:
                raise DataError(f"row {row_number}: {column} must be an integer from 1 to 10") from exc
            if not 1 <= value <= 10:
                raise DataError(f"row {row_number}: {column} must be from 1 to 10")
            ratings[column] = value
        scored.append({**row, "rpn": str(ratings["severity"] * ratings["occurrence"] * ratings["detection"])})
    scored.sort(key=lambda row: -int(row["rpn"]))
    for rank, row in enumerate(scored, start=1):
        row["risk_rank"] = str(rank)
    return scored


def main():
    parser = argparse.ArgumentParser(description="Calculate and rank FMEA RPN values from CSV.")
    parser.add_argument("input", help="Input FMEA CSV with severity, occurrence, detection columns")
    parser.add_argument("--output", required=True, help="Destination CSV")
    args = parser.parse_args()
    try:
        headers, rows = read_csv(args.input, RATING_COLUMNS)
        write_csv(args.output, [*headers, "rpn", "risk_rank"], calculate(rows))
    except DataError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
