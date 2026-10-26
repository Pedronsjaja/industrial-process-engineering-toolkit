# Architecture

## Data flow

The toolkit follows a simple pipeline:

1. Users maintain CSV files or export them from spreadsheets.
2. Small Python scripts validate input and calculate indicators.
3. Scripts write derived CSV outputs suitable for review and dashboard refresh.
4. Power BI or another analytics tool may consume the outputs; no dashboard product is required.

## Design constraints

- Python standard library only for the implemented command-line scripts.
- CSV data remains human-readable and portable.
- Scripts do not silently repair or overwrite source data.
- Reports distinguish calculations from engineering judgments.
- Examples are fictional and cannot be interpreted as site performance.

## Extending the toolkit

Preserve headers as stable interfaces, document any schema changes, validate external inputs, and add tests for edge cases. Keep optional integrations separate from the core.
