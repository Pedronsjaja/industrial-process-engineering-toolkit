# Architecture

## Data flow

The implemented architecture is limited to:

```text
CSV input → Python validation/calculation → CSV report/output
                                      → optional spreadsheet or BI consumption
```

CSV is the primary data exchange format. Spreadsheet editors can prepare input and consume generated reports. BI consumption is optional and no packaged dashboard or direct BI integration is implemented.

## Design constraints

- Python standard library only for the implemented command-line scripts.
- CSV data remains human-readable and portable.
- Scripts do not repair input data. Output writers can overwrite existing files; always use separate input and output paths and preserve raw data.
- Reports distinguish calculations from engineering judgments.
- Examples are fictional and cannot be interpreted as site performance.
- The scripts do not implement a separate action-management or document-governance application; those areas are represented by CSV schemas, validators, and documentation.

## Documentation layer

[Report guides](../reports/README.md) and Markdown templates support manual interpretation and writing. They do not generate PDF/Word reports, approve documents, join module records, or validate physical performance. [Module connections](module-workflow.md) describe a human workflow.

## Extending the toolkit

Preserve headers as stable interfaces, document any schema changes, validate external inputs, and add tests for edge cases. Keep optional integrations separate from the core.
