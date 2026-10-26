# Getting started

## Requirements

Python 3.10 or newer. Runtime scripts use only the standard library. Install the development test dependency with:

```text
python -m pip install pytest
```

## Quick Start commands

Run these from the repository root. The fixed `--as-of` date makes inspection and overdue-action checks reproducible:

```text
python automation/calculate_fmea.py examples/engineering-project-case/fmea.csv --output fmea-ranked.csv
python automation/validate_inventory.py examples/inventory-case/inventory.csv --as-of 2026-10-26
python automation/generate_5s_report.py examples/5s-workshop-case/audit.csv --output 5s-scores.csv
python automation/generate_kpis.py --inventory examples/inventory-case/inventory.csv --actions examples/5s-workshop-case/actions.csv --fmea examples/engineering-project-case/fmea.csv --audit examples/5s-workshop-case/audit.csv --as-of 2026-10-26 --output kpis.csv
python -m pytest -q
```

These commands use forward slashes, supported by Python on Windows, macOS, and Linux. Output files are generated in the current directory and do not modify source examples; `.gitignore` excludes the documented report filenames.

Other scripts:

```text
python automation/check_file_names.py --directory controlled-documents
python automation/generate_project_structure.py --root sample-project
python automation/generate_project_structure.py --root sample-project --dry-run
```

Use `--help` for script options.

## CSV conventions

Use UTF-8 encoding, a header row, comma delimiters, and a period (`.`) for decimal values. Dates use ISO `YYYY-MM-DD`. For Brazilian Excel installations, select CSV UTF-8 and comma-delimited import/export settings; check that Excel has not changed the delimiter or decimal separator before using a file with these scripts. The scripts do not automatically detect semicolon delimiters.

FMEA ratings are numerically restricted to integers 1–10; 5S audit scores are restricted to 0–5. Organizations define the meaning and evidence criteria for each level, but the current numeric bounds are fixed in code.
