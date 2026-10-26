# Fictional workshop review

## Identification
Document ID: DEMO-RPT-WorkshopReview. Revision: R01. Date: 2026-10-26.
Author: Demo Analyst. Reviewer: NOT_REVIEWED. Status: training draft.
Scope: demonstrate toolkit interpretation, not certify a workshop.
Equipment: ASSET-DEMO-001 and ASSET-DEMO-002. Test ID: NOT_APPLICABLE.

## Problem and evidence
Tool locations are unmarked (AUD-DEMO-001); ACT-DEMO-001 is pending.
Fixture inspection date: 2026-10-20.
Sources: [audit](../audit.csv), [actions](../actions.csv), [inventory](../inventory.csv), [FMEA](../fmea.csv). All data is FICTIONAL.

## Analysis
The [KPI snapshot](../expected/kpi-summary.csv) calculates one open and overdue action, availability 0.5000, one FMEA item at/above RPN 200 and 5S score 3.00.
The score covers two criteria. Availability reflects status labels, not inspection approval. RPN is not an acceptance decision.

## Actions and verification
ACT-DEMO-001 addresses tool locations. The fixture inspection requires a separate owner and technical decision; labels do not resolve FMEA-DEMO-001.
Agree observable return/label criteria, observation period, reviewer and inspection release criteria before the trial.
Post-change data: NOT_MEASURED. Effectiveness: NOT_VERIFIED. Linked requirement: UNKNOWN.

## Conclusion and limitations
The baseline identifies follow-up work. No improvement or safe release is demonstrated.
No real equipment was inspected. Attach actual evidence and issue a new revision after review; preserve this baseline.

## Reproduction
Software: toolkit Python CLI; record exact runtime/repository versions with each run.
The [tutorial](../../../docs/tutorials/first-improvement-cycle.md) gives the commands and fixed date.
Report written manually; there is no automatic report-generation engine.

## Revision history
| Revision | Date | Change | Approval |
|---|---|---|---|
| R01 | 2026-10-26 | Fictional baseline for training | NOT_REVIEWED |
