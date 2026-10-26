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
- Scripts do not silently repair or overwrite source data.
- Reports distinguish calculations from engineering judgments.
- Examples are fictional and cannot be interpreted as site performance.
- The scripts do not implement a separate action-management or document-governance application; those areas are represented by CSV schemas, validators, and documentation.

## Extending the toolkit

Preserve headers as stable interfaces, document any schema changes, validate external inputs, and add tests for edge cases. Keep optional integrations separate from the core.
