# PDCA

## When to use
Structure a small improvement trial and assess whether it actually worked.

## Input
[Copy the existing PDCA template](../../examples/5s-workshop-case/pdca-template.csv) and link the action register.

## Required fields
Manual process fields: cycle_id, phase, problem, context, cause, current_indicator, target, action_id, owner, due_date, post_indicator, evidence, comparison, standardization, lesson_learned, next_action, status. No parser enforces these fields.
Do not enter a hypothetical post_indicator as a result; leave unavailable numeric fields blank and explain NOT_MEASURED in evidence.

## How to use
Plan: state the problem, baseline, hypothesis, scope and acceptance criterion. Do: implement a bounded trial and record evidence. Check: compare equivalent periods/conditions, review uncertainty and contrary evidence. Act: standardize a supported improvement or revise the plan.

## Output
A cycle record with a verification decision and linked report. In the [tutorial](../../docs/tutorials/first-improvement-cycle.md), follow-up data is absent, so the decision remains pending.

## How to interpret
A completed task and a better-looking KPI do not establish cause or effectiveness. Check the original finding and comparable conditions before closing the cycle.

## Limitations
No automated PDCA workflow, causal inference or approval. Targets, observation periods and acceptance criteria require local judgment.

## Related modules
[5W2H](../5w2h/README.md), [KPI](../kpi/README.md), [reports](../../reports/README.md).

[Start Here](../../docs/start-here.md)
