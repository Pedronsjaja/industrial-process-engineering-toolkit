import csv
import subprocess
import sys
from argparse import Namespace
from datetime import date
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "automation"))

from calculate_fmea import calculate
from check_file_names import is_valid_name, main as check_file_names_main
from csv_utils import DataError, read_csv
from generate_5s_report import summarize
from generate_kpis import ACTION_REQUIRED_COLUMNS, collect, main as generate_kpis_main
from generate_project_structure import DIRECTORIES, main as generate_project_structure_main
from validate_inventory import main as validate_inventory_main, validate


def test_fmea_calculates_and_ranks_rpn():
    rows = [
        {"severity": "5", "occurrence": "2", "detection": "3", "failure_mode": "lower"},
        {"severity": "8", "occurrence": "4", "detection": "2", "failure_mode": "higher"},
    ]
    result = calculate(rows)
    assert [(row["failure_mode"], row["rpn"], row["risk_rank"]) for row in result] == [
        ("higher", "64", "1"),
        ("lower", "30", "2"),
    ]


def test_fmea_rejects_rating_outside_scale():
    with pytest.raises(DataError, match="from 1 to 10"):
        calculate([{"severity": "11", "occurrence": "2", "detection": "3"}])


def test_5s_summary_includes_sense_and_overall():
    report = summarize(
        [
            {"sense": "Seiri", "score": "4"},
            {"sense": "Seiri", "score": "2"},
            {"sense": "Seiton", "score": "5"},
        ]
    )
    assert report == [
        {"sense": "Seiri", "average_score": "3.00", "criteria_count": "2"},
        {"sense": "Seiton", "average_score": "5.00", "criteria_count": "1"},
        {"sense": "Overall", "average_score": "3.67", "criteria_count": "3"},
    ]


def test_inventory_reports_duplicate_negative_and_overdue():
    issues = validate(
        [
            {"asset_id": "A-1", "item": "Tool", "quantity": "-1", "location": "A", "status": "Available", "next_inspection": "2026-01-01"},
            {"asset_id": "A-1", "item": "Tool 2", "quantity": "1", "location": "A", "status": "Available", "next_inspection": "2027-01-01"},
        ],
        date(2026, 6, 1),
    )
    assert any("duplicate asset_id" in issue for issue in issues)
    assert any("cannot be negative" in issue for issue in issues)
    assert any("inspection overdue" in issue for issue in issues)


def test_inventory_rejects_malformed_inspection_date():
    with pytest.raises(DataError, match="ISO date"):
        validate(
            [{"asset_id": "A-1", "item": "Tool", "quantity": "1", "location": "A", "status": "Available", "next_inspection": "tomorrow"}],
            date(2026, 6, 1),
        )


def test_inventory_inspection_value_may_be_blank_but_column_is_required(tmp_path):
    row = {
        "asset_id": "A-1",
        "item": "Tool",
        "quantity": "1",
        "location": "Store",
        "status": "Available",
        "next_inspection": "",
    }
    assert validate([row], date(2026, 10, 26)) == []
    incomplete = tmp_path / "inventory-missing-column.csv"
    incomplete.write_text(
        "asset_id,item,quantity,location,status\nA-1,Tool,1,Store,Available\n",
        encoding="utf-8",
    )
    with pytest.raises(DataError, match="missing required columns: next_inspection"):
        read_csv(incomplete, ("asset_id", "item", "quantity", "location", "status", "next_inspection"))


def test_project_structure_has_expected_directories():
    assert DIRECTORIES == (
        "00_Management", "01_Requirements", "02_Engineering", "03_CAD",
        "04_Electronics", "05_Software", "06_Testing", "07_Data",
        "08_Reports", "09_Deliverables", "99_Archive",
    )


def test_example_inventory_passes_validation():
    _, rows = read_csv(ROOT / "examples" / "inventory-case" / "inventory.csv", (
        "asset_id", "item", "quantity", "location", "status", "next_inspection",
    ))
    assert validate(rows, date(2026, 10, 26)) == []


def test_5w2h_template_has_columns_required_by_kpi_script():
    template = ROOT / "examples" / "5s-workshop-case" / "fivew2h-template.csv"
    headers, rows = read_csv(template, ACTION_REQUIRED_COLUMNS)
    assert not rows
    assert set(ACTION_REQUIRED_COLUMNS).issubset(headers)


def test_kpis_use_input_sources_and_configured_rpn_threshold(tmp_path):
    actions = tmp_path / "actions.csv"
    inventory = tmp_path / "inventory.csv"
    fmea = tmp_path / "fmea.csv"
    actions.write_text(
        "action_id,status,due_date\nA-1,Open,2026-01-01\nA-2,Closed,2026-01-01\n",
        encoding="utf-8",
    )
    inventory.write_text(
        "asset_id,status\nI-1,Available\nI-2,In use\n",
        encoding="utf-8",
    )
    fmea.write_text(
        "severity,occurrence,detection\n5,5,5\n",
        encoding="utf-8",
    )
    metrics = collect(
        Namespace(
            actions=str(actions),
            inventory=str(inventory),
            fmea=str(fmea),
            audit=None,
            as_of=date(2026, 6, 1),
            high_risk_rpn_threshold=100,
        )
    )
    assert metrics == [
        {"metric": "Open Actions", "value": "1", "unit": "actions"},
        {"metric": "Overdue Actions", "value": "1", "unit": "actions"},
        {"metric": "Inventory Availability", "value": "0.5000", "unit": "ratio"},
        {"metric": "FMEA Items At/Above RPN 100", "value": "1", "unit": "items"},
    ]


def test_filename_checker_rejects_invalid_calendar_date():
    assert is_valid_name("GAIA-REL-TesteServo-R02-2026-10-26.pdf")
    assert not is_valid_name("GAIA-REL-TesteServo-R02-2026-02-30.pdf")


def test_kpi_audit_cli_writes_overall_score(tmp_path, monkeypatch):
    output = tmp_path / "audit-kpis.csv"
    audit = ROOT / "examples" / "5s-workshop-case" / "audit.csv"
    monkeypatch.setattr(
        sys,
        "argv",
        ["generate_kpis.py", "--audit", str(audit), "--output", str(output)],
    )
    assert generate_kpis_main() == 0
    with output.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    assert rows == [{"metric": "5S Score", "value": "3.00", "unit": "score (0-5)"}]


def test_project_structure_creates_directories(tmp_path, monkeypatch):
    root = tmp_path / "project"
    monkeypatch.setattr(sys, "argv", ["generate_project_structure.py", "--root", str(root)])
    assert generate_project_structure_main() == 0
    assert {path.name for path in root.iterdir()} == set(DIRECTORIES)


def test_project_structure_dry_run_prints_without_creating(tmp_path, monkeypatch, capsys):
    root = tmp_path / "dry-project"
    monkeypatch.setattr(
        sys,
        "argv",
        ["generate_project_structure.py", "--root", str(root), "--dry-run"],
    )
    assert generate_project_structure_main() == 0
    assert not root.exists()
    assert capsys.readouterr().out.splitlines() == [str(root / name) for name in DIRECTORIES]


def test_filename_checker_cli_checks_temporary_directory(tmp_path, monkeypatch, capsys):
    (tmp_path / "GAIA-REL-TesteServo-R02-2026-10-26.pdf").write_text("example", encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["check_file_names.py", "--directory", str(tmp_path)])
    assert check_file_names_main() == 0
    assert "All files follow" in capsys.readouterr().out

    (tmp_path / "bad-name.pdf").write_text("example", encoding="utf-8")
    assert check_file_names_main() == 1
    assert "invalid:" in capsys.readouterr().err


def test_inventory_cli_exit_codes_for_invalid_row_and_bad_date(tmp_path, monkeypatch, capsys):
    inventory = tmp_path / "inventory.csv"
    inventory.write_text(
        "asset_id,item,quantity,location,status,next_inspection\n"
        "A-1,Tool,-1,Store,Available,\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(
        sys,
        "argv",
        ["validate_inventory.py", str(inventory), "--as-of", "2026-10-26"],
    )
    assert validate_inventory_main() == 1
    assert "cannot be negative" in capsys.readouterr().err

    inventory.write_text(
        "asset_id,item,quantity,location,status,next_inspection\n"
        "A-1,Tool,1,Store,Available,not-a-date\n",
        encoding="utf-8",
    )
    assert validate_inventory_main() == 2
    assert "ISO date" in capsys.readouterr().err


def test_quick_start_script_commands_smoke(tmp_path):
    commands = [
        [
            sys.executable, "automation/calculate_fmea.py",
            "examples/engineering-project-case/fmea.csv",
            "--output", str(tmp_path / "fmea-ranked.csv"),
        ],
        [
            sys.executable, "automation/validate_inventory.py",
            "examples/inventory-case/inventory.csv", "--as-of", "2026-10-26",
        ],
        [
            sys.executable, "automation/generate_5s_report.py",
            "examples/5s-workshop-case/audit.csv",
            "--output", str(tmp_path / "5s-scores.csv"),
        ],
        [
            sys.executable, "automation/generate_kpis.py",
            "--inventory", "examples/inventory-case/inventory.csv",
            "--actions", "examples/5s-workshop-case/actions.csv",
            "--fmea", "examples/engineering-project-case/fmea.csv",
            "--audit", "examples/5s-workshop-case/audit.csv",
            "--as-of", "2026-10-26",
            "--output", str(tmp_path / "kpis.csv"),
        ],
    ]
    for command in commands:
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
        assert result.returncode == 0, f"{command!r}: {result.stderr}"
    assert (tmp_path / "fmea-ranked.csv").is_file()
    assert (tmp_path / "5s-scores.csv").is_file()
    assert (tmp_path / "kpis.csv").is_file()
