import argparse
from pathlib import Path


DIRECTORIES = (
    "00_Management",
    "01_Requirements",
    "02_Engineering",
    "03_CAD",
    "04_Electronics",
    "05_Software",
    "06_Testing",
    "07_Data",
    "08_Reports",
    "09_Deliverables",
    "99_Archive",
)


def main():
    parser = argparse.ArgumentParser(description="Generate a standard engineering project folder structure.")
    parser.add_argument("--root", default="PROJECT", help="Project directory to create")
    parser.add_argument("--dry-run", action="store_true", help="Print planned directories without creating them")
    args = parser.parse_args()
    root = Path(args.root)
    for name in DIRECTORIES:
        target = root / name
        if args.dry_run:
            print(target)
        else:
            target.mkdir(parents=True, exist_ok=True)
            print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
