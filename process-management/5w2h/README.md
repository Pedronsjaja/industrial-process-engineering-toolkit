# 5W2H action planning

## When to use
Translate a finding or reviewed risk into a specific owned action.

## Input
[Copy the existing action template](../../examples/5s-workshop-case/fivew2h-template.csv); [filled fictional action](../../examples/first-improvement-cycle/actions.csv).

## Required fields
For action planning, fill what, why, where, when, who, how and how_much (estimate/basis/currency or UNKNOWN). Also record action_id, source_id, priority, status, evidence, created_date, due_date and closed_date when applicable.
The KPI reader requires only action_id, status and due_date columns; it does not validate the complete plan. Keep when consistent with due_date; only due_date is read for overdue calculations.

## How to use
Copy the source finding ID to source_id, assign an owner and deadline, agree acceptance evidence, then track implementation. Example: AUD-DEMO-001 → ACT-DEMO-001 assigns tool locations. Record costs as unknown if unavailable. Close only after appropriate verification.

## Output
A manually maintained action register. The [KPI module](../kpi/README.md) can count its open/overdue rows; it cannot create or close actions.

## How to interpret
An action is a commitment, not evidence of effectiveness. source_id enables manual navigation to the finding; check that the referenced record exists.

## Limitations
No action-management engine, reminder, automatic join or closure approval. Blank or unrecognized status counts as open in KPI; blank due_date is not counted overdue.

## Related modules
[5S](../../quality/5s/README.md), [FMEA](../../quality/fmea/README.md), [PDCA](../pdca/README.md), [technical reports](../../reports/technical/README.md).

[Start Here](../../docs/start-here.md)
