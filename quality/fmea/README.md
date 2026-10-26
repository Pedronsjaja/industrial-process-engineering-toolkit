# FMEA

## When to use
Review ways a process/design can fail, their consequences and the controls before prioritizing engineering action.

## Input
[Copy the FMEA template](fmea-template.csv); [fictional input](../../examples/first-improvement-cycle/fmea.csv).

## Required fields
Parser-required: severity, occurrence, detection, each an integer 1–10. Document process, function, failure_mode, effect, cause, current_control, owner, recommended_action, due_date and status for a meaningful review.
Severity describes consequence; Occurrence the likelihood/frequency category; Detection the difficulty of detection by current controls. Define local level criteria and use higher detection ratings for poorer detectability. These ratings are not measured probabilities.

## How to use
Record failure modes and evidence with the team, agree rating definitions, then calculate. Keep a stable risk reference. The tutorial adds optional risk_id; the script preserves extra columns but does not validate their meaning or uniqueness.

## Command
Run from the repository root. Examples are fictional.

```text
python automation/calculate_fmea.py examples/first-improvement-cycle/fmea.csv --output fmea-ranked.csv
```

## Output
fmea-ranked.csv retains the input columns, adds rpn and risk_rank and sorts descending by RPN. The fictional ratings 8,5,5 produce rpn 200 and risk_rank 1. [Full executed output](../../examples/first-improvement-cycle/expected/fmea-ranking.csv). Success is exit 0 with no stdout.

## How to interpret
RPN = Severity × Occurrence × Detection. Review high severity even when its RPN is lower. For ties the input order is retained and distinct sequential ranks are assigned; rank is not a unique risk ID.

## Limitations
No universal risk threshold, automatic action or risk acceptance. Ranking cannot verify control effectiveness. Use the original rating input for recalculation; generated RPN/rank columns are output fields, not an input template.

## Related modules
[5W2H](../../process-management/5w2h/README.md), [KPI](../../process-management/kpi/README.md), [engineering analysis](../../reports/technical/engineering-analysis-report.md).

[Start Here](../../docs/start-here.md)
