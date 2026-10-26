import argparse
import re
import sys
from datetime import date
from pathlib import Path


PATTERN = re.compile(
    r"^[A-Z0-9]+-[A-Z0-9]+-[A-Za-z0-9]+-R\d{2,}-\d{4}-\d{2}-\d{2}\.[A-Za-z0-9]+$"
)


def is_valid_name(name):
    if not PATTERN.fullmatch(name):
        return False
    date_text = "-".join(name.rsplit("-", 3)[1:]).rsplit(".", 1)[0]
    try:
        date.fromisoformat(date_text)
    except ValueError:
        return False
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Check files against PROJECT-TYPE-DESCRIPTION-REVISION-YYYY-MM-DD.ext."
    )
    parser.add_argument("--directory", default=".", help="Directory to scan recursively")
    args = parser.parse_args()
    root = Path(args.directory)
    if not root.is_dir():
        print(f"error: not a directory: {root}", file=sys.stderr)
        return 2
    invalid = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if not is_valid_name(path.name):
            invalid.append(path)
    if invalid:
        for path in invalid:
            print(f"invalid: {path}", file=sys.stderr)
        return 1
    print(f"All files follow the naming pattern: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
