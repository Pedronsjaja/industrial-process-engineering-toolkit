# KPI

## When to use
Summarize the current state of actions, assets, FMEA ratings and audits using explicit formulas.

## Input
Use the [fictional input set](../../examples/first-improvement-cycle/README.md) or selected sources. Define each metric's purpose, formula, unit, source, owner, refresh frequency, target rationale and data-quality limits.

## Required fields
At least one input: actions → action_id,status,due_date; inventory → asset_id,status; FMEA → severity,occurrence,detection; audit → sense,score. Headers are case-sensitive.
Use ISO dates and a fixed --as-of date. FMEA ratings are integers 1–10; audit scores finite 0–5. See [exact definitions](../../docs/kpi-definitions.md).

## How to use
Validate each source with its module first. Choose a consistent scope, declare a local FMEA threshold, generate the snapshot and retain date/source definitions for comparisons.

## Command
Run from the repository root. Examples are fictional.

```text
python automation/generate_kpis.py --actions examples/first-improvement-cycle/actions.csv --inventory examples/first-improvement-cycle/inventory.csv --fmea examples/first-improvement-cycle/fmea.csv --audit examples/first-improvement-cycle/audit.csv --as-of 2026-10-26 --high-risk-rpn-threshold 200 --output kpis.csv
```

## Output
kpis.csv, exit 0 without stdout. Executed fictional result:

```csv
metric,value,unit
Open Actions,1,actions
Overdue Actions,1,actions
Inventory Availability,0.5000,ratio
FMEA Items At/Above RPN 200,1,items
5S Score,3.00,score (0-5)
```
[Expected file](../../examples/first-improvement-cycle/expected/kpi-summary.csv).

## How to interpret
Availability 0.5000 means 50% of rows carry an available status. It does not measure stock quantity or uptime. Overdue means an open action dated before --as-of. The illustrative threshold 200 is inclusive.

## Limitations
No full source validation, cross-file joins, trend history, targets, dashboard or OEE calculation. Blank status counts open; blank due date does not count overdue. Empty inventory yields 0, while an empty audit emits no score row; do not interpret missing data as proven poor performance. The KPI audit path does not validate sense vocabulary; run the 5S report first.

## Related modules
[5W2H](../5w2h/README.md), [inventory](../../inventory/README.md), [FMEA](../../quality/fmea/README.md), [5S](../../quality/5s/README.md), [PDCA](../pdca/README.md).

[Start Here](../../docs/start-here.md)
