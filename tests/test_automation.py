import sys
from argparse import Namespace
from datetime import date
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "automation"))

from calculate_fmea import calculate
from check_file_names import is_valid_name
from csv_utils import DataError
from generate_5s_report import summarize
from generate_kpis import collect
from generate_project_structure import DIRECTORIES
from validate_inventory import validate


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


def test_project_structure_has_expected_directories():
    assert DIRECTORIES == (
        "00_Management", "01_Requirements", "02_Engineering", "03_CAD",
        "04_Electronics", "05_Software", "06_Testing", "07_Data",
        "08_Reports", "09_Deliverables", "99_Archive",
    )


def test_example_inventory_passes_validation():
    from csv_utils import read_csv

    _, rows = read_csv(ROOT / "examples" / "inventory-case" / "inventory.csv", (
        "asset_id", "item", "quantity", "location", "status", "next_inspection",
    ))
    assert validate(rows, date(2026, 10, 26)) == []


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
