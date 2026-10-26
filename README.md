# Industrial Process Engineering Toolkit

[![Tests](https://github.com/Pedronsjaja/industrial-process-engineering-toolkit/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/Pedronsjaja/industrial-process-engineering-toolkit/actions/workflows/tests.yml)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)

An open-source, modular toolkit for industrial process engineering, process management, operational excellence, quality management, engineering documentation, inventory, industrial analytics, and lightweight automation.

Designed for small businesses, engineering teams, university projects, extension teams, laboratories, consultancies, students, and engineering professionals. The toolkit provides lightweight CSV-first tools and practical guidance; it is not a certified management system or a substitute for qualified engineering judgment.

## New here?

Start with the [Start Here guide](docs/start-here.md).

Documentation is currently written in English. Portuguese guides may be added in future versions.

## Typical workflow

Choose a problem → record evidence → calculate or validate → assign actions → verify → report. Follow [how the modules connect](docs/module-workflow.md) or the [first improvement cycle](docs/tutorials/first-improvement-cycle.md). Connections and report writing are manual.

## Project Status

**IMPLEMENTED** means working code exists; **DOCUMENTED** means guidance or a schema exists without implying automation; **EXAMPLE** identifies fictional sample data; **PLANNED** marks future work. No current feature is classified as experimental.

## Capabilities

| Area | Capability | Status |
|---|---|---|
| 5S | Audit score validation and average reports by sense and overall | IMPLEMENTED |
| 5S | Fictional workshop audit dataset | EXAMPLE |
| PDCA / 5W2H | Methodology, schemas, and action traceability from 5S findings | DOCUMENTED |
| 5W2H | Fictional sample actions | EXAMPLE |
| FMEA | 1–10 rating validation, RPN calculation, and ranking | IMPLEMENTED |
| FMEA | Fictional engineering dataset | EXAMPLE |
| Inventory | Validation of required values, duplicate IDs, quantities, and inspection dates | IMPLEMENTED |
| Inventory | Header-only CSV template | DOCUMENTED |
| Document control | Document register and naming/revision guidance | DOCUMENTED |
| Document control | Filename and calendar-date validator | IMPLEMENTED |
| Project structure | Generate the defined engineering directory structure; dry-run option | IMPLEMENTED |
| Drive governance | Folder structure, archive, permissions, and onboarding guidance | DOCUMENTED |
| Analytics | KPI CSV generation for supported inputs | IMPLEMENTED |
| Analytics | Data dictionary | DOCUMENTED |
| Reports | Academic and technical writing guides with editable Markdown templates | DOCUMENTED |
| Learning | End-to-end fictional improvement cycle with reproducible CSV outputs | EXAMPLE |
| Standards | Small reference indexes and official-source links | DOCUMENTED |

Feature boundaries and future work are documented in [ROADMAP.md](ROADMAP.md).

## Quick Start

Requires Python 3.10+. Runtime scripts use only the standard library. Install the development test dependency once:

```text
python -m pip install pytest
```

Run from the repository root. Fixed `--as-of` dates keep example results reproducible:

```text
python automation/calculate_fmea.py examples/engineering-project-case/fmea.csv --output fmea-ranked.csv
python automation/validate_inventory.py examples/inventory-case/inventory.csv --as-of 2026-10-26
python automation/generate_5s_report.py examples/5s-workshop-case/audit.csv --output 5s-scores.csv
python automation/generate_kpis.py --inventory examples/inventory-case/inventory.csv --actions examples/5s-workshop-case/actions.csv --fmea examples/engineering-project-case/fmea.csv --audit examples/5s-workshop-case/audit.csv --as-of 2026-10-26 --output kpis.csv
python -m pytest -q
```

Forward-slash paths work in Python on Windows, macOS, and Linux. See [docs/getting-started.md](docs/getting-started.md) for CSV conventions.

## Implemented Automation

| Script | Purpose |
|---|---|
| [`calculate_fmea.py`](automation/calculate_fmea.py) | Validates integer ratings from 1 to 10, calculates RPN, sorts descending, and adds rank. |
| [`generate_5s_report.py`](automation/generate_5s_report.py) | Validates 0–5 scores and reports averages by 5S sense and overall. |
| [`generate_kpis.py`](automation/generate_kpis.py) | Generates supported action, inventory, FMEA-threshold, and 5S KPIs from supplied CSVs. |
| [`validate_inventory.py`](automation/validate_inventory.py) | Checks required values, duplicate asset IDs, numeric non-negative quantities, and inspection dates. |
| [`check_file_names.py`](automation/check_file_names.py) | Checks document filename pattern and calendar date recursively. |
| [`generate_project_structure.py`](automation/generate_project_structure.py) | Creates the predefined project folders or prints them with `--dry-run`. |

The numeric scales in the current code are fixed: FMEA ratings are 1–10 and 5S scores are 0–5. Local criteria define the meaning of each level, not the numeric bounds. KPI formulas and limitations are in [docs/kpi-definitions.md](docs/kpi-definitions.md).

## Example Datasets

[`examples/`](examples/) contains fictional 5S workshop, inventory, and engineering FMEA records.

> Example data must not be interpreted as real company information, measured industrial performance, certified engineering records, or compliance evidence.

CSV files use UTF-8 encoding, a comma delimiter, and a period (`.`) as the decimal separator. For Brazilian Excel installations, import or export using UTF-8 and comma-delimited CSV settings; if Excel changes the delimiter or decimal format, verify the file before running scripts.

## Repository Structure

```text
automation/  data-analytics/  docs/  document-control/
drive-governance/  examples/  inventory/  process-management/
quality/  reports/  standards/  tests/  .github/workflows/
```

## Documentation

Browse the [documentation index](docs/README.md) and [report guides and templates](reports/README.md).

- [Getting started and CSV conventions](docs/getting-started.md)
- [Architecture and data flow](docs/architecture.md)
- [Engineering methodology](docs/methodology.md)
- [KPI definitions](docs/kpi-definitions.md)
- [Terminology](docs/terminology.md)
- [Quality](quality/README.md), [process management](process-management/README.md), [inventory](inventory/README.md), [document control](document-control/README.md), [drive governance](drive-governance/README.md), and [standards](standards/README.md)
- [Roadmap](ROADMAP.md), [changelog](CHANGELOG.md), [contributing](CONTRIBUTING.md), and [third-party credits](THIRD_PARTY_CREDITS.md)

Standards files are limited reference indexes, not reproductions or compliance determinations. They currently contain three ISO entries and two NR entries; the ABNT index and standards matrix are header-only. Check current editions and applicability at official sources. No protected standards text is included.

## License and Attribution

Released under the [MIT License](LICENSE). Original project work is maintained by Pedro Henrique Barbosa de Freitas Soares. Third-party material, when incorporated, must be documented in [THIRD_PARTY_CREDITS.md](THIRD_PARTY_CREDITS.md) with source and license information.

## Maintainer

Pedro Henrique Barbosa De Freitas Soares — Mechanical Engineering student, UFTM


GitHub: [@Pedronsjaja](https://github.com/Pedronsjaja)
