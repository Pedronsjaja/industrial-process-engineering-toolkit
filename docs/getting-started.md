# Getting started

## Requirements

Python 3.10+; no runtime package installation is required. Install pytest separately only if it is not already available in your development environment.

## Commands

Run from the repository root:

```powershell
python automation\calculate_fmea.py examples\engineering-project-case\fmea.csv --output fmea-ranked.csv
python automation\validate_inventory.py examples\inventory-case\inventory.csv
python automation\generate_5s_report.py examples\5s-workshop-case\audit.csv --output 5s-scores.csv
python automation\generate_kpis.py --inventory examples\inventory-case\inventory.csv --actions examples\5s-workshop-case\actions.csv --fmea examples\engineering-project-case\fmea.csv --output kpis.csv
python automation\check_file_names.py --directory .\controlled-documents
python automation\generate_project_structure.py --root .\sample-project
python -m pytest -q
```

Use `--help` for script options. Replace `.\controlled-documents` with the directory containing files governed by the naming standard. Output files are generated where specified and do not modify source examples.

## CSV conventions

UTF-8 with a header row is recommended. Dates use ISO `YYYY-MM-DD`. Numeric scales and required fields are described in each module README and example header.
