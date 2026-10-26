# First improvement cycle — fictional training data

All people, assets, observations, ratings and dates here are invented for learning. Computed outputs are calculations on fictional inputs, not measured workshop performance.

Follow the [11-step tutorial](../../docs/tutorials/first-improvement-cycle.md) with fixed date 2026-10-26.
The inventory validator should exit **1** because ASSET-DEMO-002 has an overdue inspection. This is an intended finding; do not erase it just to pass validation.

| File | Role |
|---|---|
| [audit.csv](audit.csv) | Two 5S observations; not a complete five-sense audit |
| [actions.csv](actions.csv) | Pending action linked to AUD-DEMO-001 |
| [inventory.csv](inventory.csv) | Two asset records; one overdue inspection |
| [fmea.csv](fmea.csv) | One fictional risk |
| [expected/](expected/) | Actual script outputs at the fixed date |
| [Sample report](controlled-documents/DEMO-RPT-WorkshopReview-R01-2026-10-26.md) | Manual composition; verification pending |

The FMEA template has no risk ID. This example adds optional risk_id for manual traceability. The calculator preserves it but does not check uniqueness or create links. The toolkit does not join source_id to audit_id automatically.
