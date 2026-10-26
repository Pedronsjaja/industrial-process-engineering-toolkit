# 5S audit

## When to use
Investigate workplace organization using observable criteria before proposing actions.

## Input
[Copy the audit template](5s-audit-template.csv); see [fictional input](../../examples/first-improvement-cycle/audit.csv).

## Required fields
Parser-required: sense and score. sense accepts Seiri, Seiton, Seiso, Seiketsu, Shitsuke (trimmed/capitalized); score is numeric 0–5.
For a usable record, also fill audit_id, area, criterion, nonconformity when present, evidence, owner, due_date and status. Those context fields are not validated by this script.

## How to use
Agree local observable scoring criteria; copy the header-only template; add one row per criterion. Keep unique audit IDs for traceability. Run the report, review low-scoring findings and manually create actions.

## Command
Run from the repository root. Examples are fictional.

```text
python automation/generate_5s_report.py examples/first-improvement-cycle/audit.csv --output 5s-scores.csv
```

## Output
5s-scores.csv; no success stdout, exit 0. This is an executed fictional example:

```csv
sense,average_score,criteria_count
Seiri,4.00,1
Seiton,2.00,1
Overall,3.00,2
```
[Full expected file](../../examples/first-improvement-cycle/expected/5s-summary.csv).

## How to interpret
Seiton 2.00 is a prompt to inspect the finding. Overall is the arithmetic mean of all rows; criteria_count states its coverage.

## Limitations
No grouping by area or date, no requirement to cover all five senses, no action generation or compliance judgment. Filter the input deliberately before comparing scopes. Numeric bounds are fixed; local rating meanings are not.

## Related modules
[5W2H](../../process-management/5w2h/README.md), [PDCA](../../process-management/pdca/README.md), [KPI](../../process-management/kpi/README.md), [reports](../../reports/README.md).

[Start Here](../../docs/start-here.md)
