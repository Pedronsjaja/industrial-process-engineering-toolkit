# First improvement cycle

## Scenario and preparation
A **wholly fictional** workshop has unmarked tool locations, an overdue fixture inspection, a pending action and a recorded failure mode. Nothing below is measured industrial performance.

Use Python 3.10+ and run every command from the repository root. [Setup and CSV conventions](../getting-started.md) explain UTF-8, commas and decimal points.
The filled files in [examples/first-improvement-cycle](../../examples/first-improvement-cycle/README.md) are ready to run. To practice entering data, copy the linked header-only templates in your file manager to a separate working folder, preserve headers, and fill them from these examples. The commands below use the checked-in files so results remain reproducible.
Outputs use different filenames from inputs; rerunning replaces those outputs. Preserve each real run separately.

## STEP 1 — Record the 5S audit
Copy [5s-audit-template.csv](../../quality/5s/5s-audit-template.csv). Fill audit_id, area, criterion, sense, score, nonconformity, evidence, owner, due_date and status.
The calculator requires only sense and score; the other fields make the record useful for engineering traceability.
Here are both rows from the [filled input](../../examples/first-improvement-cycle/audit.csv):

```csv
audit_id,area,criterion,sense,score,nonconformity,evidence,owner,due_date,status
AUD-DEMO-001,Demo workshop,Tools have marked storage positions,Seiton,2,Storage positions missing,Fictional observation only,Demo Coordinator,2026-10-25,Open
AUD-DEMO-002,Demo workshop,Unused materials separated,Seiri,4,,Fictional observation only,Demo Coordinator,2026-11-02,Open
```

Use distinct audit_id values for findings, observable criteria and evidence references. Define the local meaning of each score before rating. The script accepts 0–5, not a percentage. Blank nonconformity means no finding was recorded, not verified compliance.

## STEP 2 — Generate the 5S report

```text
python automation/generate_5s_report.py examples/first-improvement-cycle/audit.csv --output 5s-scores.csv
```

Exit code **0**; no success text is printed. Open 5s-scores.csv:

```csv
sense,average_score,criteria_count
Seiri,4.00,1
Seiton,2.00,1
Overall,3.00,2
```

Compare with [expected output](../../examples/first-improvement-cycle/expected/5s-summary.csv).
Overall is the mean of the two criteria, not an equally weighted mean of five senses. This miniature audit does not cover all five senses.

## STEP 3 — Turn the finding into a 5W2H action
Copy [fivew2h-template.csv](../../examples/5s-workshop-case/fivew2h-template.csv). The [filled action](../../examples/first-improvement-cycle/actions.csv) links source_id AUD-DEMO-001 to action_id ACT-DEMO-001.

| Field | Tutorial value / interpretation |
|---|---|
| what / why | Assign storage labels / make tool return unambiguous |
| where / who | Demo workshop / Demo Coordinator |
| when / due_date | 2026-10-25 in both fields; KPI reads due_date only |
| how / how_much | Trial and review / UNKNOWN until estimated with basis and currency |
| priority / status | Medium / Open; locally reviewed |
| evidence / closed_date | Blank: implementation and effectiveness have not been verified |

This is a manual decision and data entry step. source_id is a traceability convention; no script creates the action, verifies the link, sends reminders or proves that it worked.

## STEP 4 — Record inventory
Copy [inventory-template.csv](../../inventory/templates/inventory-template.csv). The [filled input](../../examples/first-improvement-cycle/inventory.csv) includes two assets.
Mandatory columns: asset_id, item, quantity, location, status, next_inspection.
asset_id/item/location/status must be nonblank; quantity must be finite and nonnegative. next_inspection may be blank, but its column must exist.

ASSET-DEMO-001 is a caliper, quantity 1, Cabinet A, Available, next inspection 2027-03-01.
ASSET-DEMO-002 is a fixture, quantity 1, Bench B, Maintenance, next inspection 2026-10-20.
Owner and notes provide context. No real price, supplier or calibration is implied by the empty fields.

## STEP 5 — Validate inventory

```text
python automation/validate_inventory.py examples/first-improvement-cycle/inventory.csv --as-of 2026-10-26
```

Expected stderr:

```text
error: row 3: inspection overdue since 2026-10-20
```

Exit code **1 is expected**: the date is valid but overdue at 2026-10-26. Do not change it to a future date without an actual inspection record and justified next date.
The checker does not inspect equipment or authorize use. Decide how to handle the fixture under local procedures.
A malformed date/input error exits 2; a valid inventory exits 0. [Existing valid sample](../../examples/inventory-case/inventory.csv) demonstrates the success path.

## STEP 6 — Record the FMEA
Copy [fmea-template.csv](../../quality/fmea/fmea-template.csv). Record process, function, failure_mode, effect, cause, current_control, severity, occurrence, detection, owner, recommended_action, due_date and status.
The [filled risk](../../examples/first-improvement-cycle/fmea.csv) adds optional risk_id FMEA-DEMO-001; the calculator preserves extra columns.

Severity rates consequences, Occurrence rates the likelihood/frequency category, and Detection rates how difficult it is for the current control to detect the failure under the locally agreed scale. A larger detection rating should represent poorer detectability when using this prioritization convention.
The scripts accept **integers 1–10**. Define what every level means locally; these are ordinal ratings, not measured probabilities.
The fictional ratings 8, 5, 5 give RPN = 8 × 5 × 5 = 200. Review severity independently; RPN does not replace engineering judgment.

## STEP 7 — Calculate FMEA

```text
python automation/calculate_fmea.py examples/first-improvement-cycle/fmea.csv --output fmea-ranked.csv
```

Exit **0**, no success text. fmea-ranked.csv preserves the input columns and appends rpn and risk_rank.
The executed result for FMEA-DEMO-001 has rpn **200**, risk_rank **1**. [Full output](../../examples/first-improvement-cycle/expected/fmea-ranking.csv).
Risk rank is a changing ordering, not an identifier or approval. This risk needs a separate reviewed action; the storage-label action does not resolve inspection ownership.

## STEP 8 — Generate KPIs from all four inputs

```text
python automation/generate_kpis.py --actions examples/first-improvement-cycle/actions.csv --inventory examples/first-improvement-cycle/inventory.csv --fmea examples/first-improvement-cycle/fmea.csv --audit examples/first-improvement-cycle/audit.csv --as-of 2026-10-26 --high-risk-rpn-threshold 200 --output kpis.csv
```

Exit **0**; kpis.csv contains:

```csv
metric,value,unit
Open Actions,1,actions
Overdue Actions,1,actions
Inventory Availability,0.5000,ratio
FMEA Items At/Above RPN 200,1,items
5S Score,3.00,score (0-5)
```

Compare with [expected output](../../examples/first-improvement-cycle/expected/kpi-summary.csv).
The generator does not run full inventory validation or join the four datasets. A successful KPI command can coexist with the inventory finding in Step 5.

## STEP 9 — Interpret the indicators
| Indicator | Meaning here | Decision still needed |
|---|---|---|
| Open Actions = 1 | One status is not closed/complete/completed | Check owner, scope and evidence |
| Overdue Actions = 1 | That open action is due before 2026-10-26 | Review reason and escalation; due today would not be overdue |
| Inventory Availability = 0.5000 | One of two rows has an available status | 50% of records, not quantities, uptime, readiness or inspection approval |
| FMEA Items At/Above RPN 200 = 1 | One rating product meets illustrative threshold 200 | Review consequences and controls; threshold is not universal |
| 5S Score = 3.00 | Average of the two recorded criteria | Review individual findings; an average can hide a poor criterion |

See [exact definitions and empty-input behavior](../kpi-definitions.md). Keep scope, definitions and observation periods consistent for a later comparison.

## STEP 10 — Apply PDCA
Copy [pdca-template.csv](../../examples/5s-workshop-case/pdca-template.csv). Use a cycle_id and reference action_id ACT-DEMO-001.
- **Plan:** define the label/return problem and baseline; agree an observation window, criteria and reviewer before changing anything.
- **Do:** carry out the agreed trial and record implementation evidence.
- **Check:** repeat comparable observations, inspect the evidence, and assess whether tools return to the right locations. A closed action alone is not effectiveness.
- **Act:** standardize a successful approach or revise the action and repeat. Address fixture inspection independently.

No follow-up data is supplied. post_indicator remains blank with evidence annotated NOT_MEASURED; do not enter a better score to complete the exercise.
[PDCA guidance](../../process-management/pdca/README.md) covers manual decisions.

## STEP 11 — Write the final review report
Copy the [technical report template](../../reports/templates/technical-report-template.md), or choose the [academic template](../../reports/templates/academic-report-template.md) for a course/project.
Consolidate the problem, source files, calculations, findings, actions, verification plan and limitations. State that effectiveness is still pending when no post-change evidence exists.
The [filled workshop review](../../examples/first-improvement-cycle/controlled-documents/DEMO-RPT-WorkshopReview-R01-2026-10-26.md) demonstrates an honest baseline conclusion; it is not a completed improvement claim.

The example follows [document naming](../../document-control/naming-standard.md). Check its name with:

```text
python automation/check_file_names.py --directory examples/first-improvement-cycle/controlled-documents
```

Exit **0**, with “All files follow the naming pattern:” and the directory path (separator depends on OS). The check validates names/calendar dates, not report contents or approval.
Manually register document ID, revision, location, owner and reviewer in [document-register.csv](../../document-control/document-register.csv). Retain the baseline and issue a new revision after verification.

## What to try next
Explain why KPI generation succeeds when inventory validation reports an overdue inspection. Then propose a verification criterion for the label action without inventing follow-up data.
