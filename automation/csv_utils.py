import csv
import sys
from datetime import date
from pathlib import Path


class DataError(ValueError):
    pass


def read_csv(path, required_columns):
    try:
        with Path(path).open("r", encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            headers = reader.fieldnames or []
            missing = [column for column in required_columns if column not in headers]
            if missing:
                raise DataError(f"{path}: missing required columns: {', '.join(missing)}")
            rows = list(reader)
    except OSError as exc:
        raise DataError(f"Cannot read {path}: {exc}") from exc
    return headers, rows


def write_csv(path, headers, rows):
    try:
        with Path(path).open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=headers, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)
    except OSError as exc:
        raise DataError(f"Cannot write {path}: {exc}") from exc


def parse_iso_date(value, field_name, row_number):
    try:
        return date.fromisoformat(value)
    except (TypeError, ValueError) as exc:
        raise DataError(
            f"row {row_number}: {field_name} must be an ISO date (YYYY-MM-DD), got {value!r}"
        ) from exc


def fail(message):
    print(f"error: {message}", file=sys.stderr)
