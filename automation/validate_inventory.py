import argparse
import math
import sys
from collections import Counter
from datetime import date

from csv_utils import DataError, parse_iso_date, read_csv


REQUIRED_COLUMNS = ("asset_id", "item", "quantity", "location", "status", "next_inspection")
REQUIRED_VALUES = ("asset_id", "item", "location", "status")


def validate(rows, as_of):
    issues = []
    counts = Counter(row.get("asset_id", "").strip() for row in rows)
    for row_number, row in enumerate(rows, start=2):
        asset_id = row.get("asset_id", "").strip()
        if not asset_id:
            issues.append(f"row {row_number}: asset_id is required")
        elif counts[asset_id] > 1:
            issues.append(f"row {row_number}: duplicate asset_id {asset_id!r}")
        for field in REQUIRED_VALUES[1:]:
            if not row.get(field, "").strip():
                issues.append(f"row {row_number}: {field} is required")
        try:
            quantity = float(row.get("quantity", ""))
        except ValueError:
            issues.append(f"row {row_number}: quantity must be numeric")
        else:
            if not math.isfinite(quantity):
                issues.append(f"row {row_number}: quantity must be finite")
            elif quantity < 0:
                issues.append(f"row {row_number}: quantity cannot be negative")
        inspection = row.get("next_inspection", "").strip()
        if inspection:
            due_date = parse_iso_date(inspection, "next_inspection", row_number)
            if due_date < as_of:
                issues.append(f"row {row_number}: inspection overdue since {inspection}")
    return issues


def main():
    parser = argparse.ArgumentParser(description="Validate inventory CSV records.")
    parser.add_argument("input", help="Inventory CSV file")
    parser.add_argument("--as-of", type=date.fromisoformat, default=date.today(), help="Date used for overdue checks (YYYY-MM-DD)")
    args = parser.parse_args()
    try:
        _, rows = read_csv(args.input, REQUIRED_COLUMNS)
        issues = validate(rows, args.as_of)
    except DataError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if issues:
        for issue in issues:
            print(f"error: {issue}", file=sys.stderr)
        return 1
    print(f"Inventory valid: {len(rows)} row(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
