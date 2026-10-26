# Engineering reports

**DOCUMENTED:** these original Markdown guides/templates support manual report writing. There is no automatic narrative, PDF, DOCX, citation-formatting or academic-compliance generator. CSV calculation outputs are supporting attachments, not finished engineering reports.

## Choose a report
| Need | Guide | Copy |
|---|---|---|
| Course, laboratory or research submission | [Academic reports](academic/README.md) | [Academic template](templates/academic-report-template.md) |
| Inspection, maintenance, progress or recommendation | [Technical reports](technical/README.md) | [Technical template](templates/technical-report-template.md) |
| Structural, thermal, fluid, mechanism or design analysis | [Engineering analysis](technical/engineering-analysis-report.md) | [Analysis template](templates/engineering-analysis-template.md) |
| Test, commissioning or validation evidence | [Test report](technical/test-report.md) | [Test template](templates/test-report-template.md) |

Copy a template, remove sections that do not apply with a short reason, replace placeholders with evidence and obtain the appropriate review. UNKNOWN, NOT_MEASURED and NOT_APPLICABLE mean different things; do not silently replace them with zero.

## Minimum traceability
For a short report retain title/document ID, author, date, objective, source references, result and conclusion/limitations.
Add revision, reviewer, source file, test/equipment IDs, dataset, software/version, linked action, risk and requirement when applicable. Keep a stable source record reference, not just a changing FMEA rank.
The templates provide these fields; a simple note need not become a large approval package.

## Data and results
- Keep original raw records separately from derived tables/plots; never overwrite the original silently.
- Record units, acquisition/calculation method, timestamps when relevant and software/version.
- Identify MEASURED, CALCULATED, SIMULATED, ESTIMATED and ASSUMED information; mark this toolkit's teaching cases FICTIONAL.
- Retain dataset filenames/revisions and, when useful, checksums plus scripts/configuration needed to reproduce calculations.
- Record measurement uncertainty, instrument calibration status, model assumptions and numerical sensitivity where relevant.
- Report exclusions, missing values, deviations and unfavorable results. Keep observations separate from interpretations.
- Retain revision history, reviewed conclusions and evidence. A higher score or a closed action does not alone prove improvement.

## Connect reports to management
Use [Inventory](../inventory/README.md) asset IDs for equipment; [FMEA](../quality/fmea/README.md) for risk context; [5W2H](../process-management/5w2h/README.md) for actions; [PDCA](../process-management/pdca/README.md) for effectiveness; and [KPI](../process-management/kpi/README.md) for defined snapshots.
Register the report through [Document Control](../document-control/README.md). Use the existing naming rule, for example PRJ-RPT-ServoTest-R01-2026-10-26.pdf (fictional name, not a generated file). Store project reports in 08_Reports and data in 07_Data under the [project layout](../drive-governance/folder-structure.md).
The [module workflow](../docs/module-workflow.md) explains the manual links.

## References and attribution
Cite external methods, applicable standards and their editions, software documentation, datasets and reused material. Check current applicability at [official standards sources](../standards/README.md) and institutional instructions; do not assume a universal ABNT or other format.
Preserve attribution and record incorporated third-party material in [THIRD_PARTY_CREDITS.md](../THIRD_PARTY_CREDITS.md). Do not invent sources or reproduce protected tables, figures or standards text.

## Professional responsibility
These templates support documentation. They do not replace technical review, qualified professional responsibility, applicable legal requirements or ART/RRT where required, internal procedures, mandatory standards or appropriate experimental validation. A template or filename does not confer legal or regulatory validity.

[Worked fictional review](../examples/first-improvement-cycle/controlled-documents/DEMO-RPT-WorkshopReview-R01-2026-10-26.md) · [Start Here](../docs/start-here.md)
