"""Keep the published fictional tutorial consistent with executed CLI outputs."""
import csv
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "examples" / "first-improvement-cycle"


def run(script, *arguments):
    return subprocess.run(
        [sys.executable, str(ROOT / "automation" / script), *map(str, arguments)],
        cwd=ROOT, capture_output=True, text=True, check=False,
    )


def rows(path):
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.reader(stream))


@pytest.mark.parametrize("script,inputs,expected", [
    ("generate_5s_report.py", ["audit.csv"], "5s-summary.csv"),
    ("calculate_fmea.py", ["fmea.csv"], "fmea-ranking.csv"),
    ("generate_kpis.py", [
        "--actions", "actions.csv", "--inventory", "inventory.csv",
        "--fmea", "fmea.csv", "--audit", "audit.csv",
        "--as-of", "2026-10-26", "--high-risk-rpn-threshold", "200",
    ], "kpi-summary.csv"),
])
def test_tutorial_outputs_match_published_csv(tmp_path, script, inputs, expected):
    arguments = [CASE / value if value.endswith(".csv") else value for value in inputs]
    output = tmp_path / expected
    result = run(script, *arguments, "--output", output)
    assert result.returncode == 0, result.stderr
    assert result.stdout == ""
    assert rows(output) == rows(CASE / "expected" / expected)


def test_tutorial_inspection_is_intentionally_overdue():
    result = run("validate_inventory.py", CASE / "inventory.csv", "--as-of", "2026-10-26")
    assert result.returncode == 1
    assert result.stderr.strip() == "error: row 3: inspection overdue since 2026-10-20"


def test_tutorial_action_points_to_a_recorded_finding():
    with (CASE / "audit.csv").open(encoding="utf-8", newline="") as stream:
        findings = {row["audit_id"]: row for row in csv.DictReader(stream)}
    with (CASE / "actions.csv").open(encoding="utf-8", newline="") as stream:
        actions = list(csv.DictReader(stream))
    assert actions
    for action in actions:
        assert findings[action["source_id"]]["nonconformity"]
        assert action["status"] == "Open"


def test_tutorial_report_name_is_valid():
    result = run("check_file_names.py", "--directory", CASE / "controlled-documents")
    assert result.returncode == 0, result.stderr
    assert "All files follow the naming pattern:" in result.stdout
