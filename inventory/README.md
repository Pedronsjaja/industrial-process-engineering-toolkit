# Inventory

## When to use
Locate assets/tools and identify incomplete records, duplicate IDs or inspection dates needing review.

## Input
[Copy the inventory template](templates/inventory-template.csv); [fictional input](../examples/first-improvement-cycle/inventory.csv).

## Required fields
Required columns: asset_id,item,quantity,location,status,next_inspection. Nonblank values: asset_id,item,location,status. quantity must be a finite nonnegative number (fractions are accepted). next_inspection may be blank; otherwise use YYYY-MM-DD. Keep asset_id unique.
Other template fields provide category, description, owner, project, supplier, value, acquisition_date, last_inspection and notes; the validator does not check these.

## How to use
Populate records, confirm physical identity/location, set inspection dates according to local criteria, then validate. Review every finding; do not simply edit dates to silence an overdue warning.

## Command
Run from the repository root. Examples are fictional.

```text
python automation/validate_inventory.py examples/first-improvement-cycle/inventory.csv --as-of 2026-10-26
```

## Output
Expected stderr from the fictional two-row inventory:

```text
error: row 3: inspection overdue since 2026-10-20
```
Exit 1 is the intended finding. A passing example is shown below:

```text
python automation/validate_inventory.py examples/inventory-case/inventory.csv --as-of 2026-10-26
```

```text
Inventory valid: 2 row(s)
```
The latter exits 0. Malformed input/date errors exit 2.

## How to interpret
ASSET-DEMO-002 requires an inspection decision. The result checks records, not asset condition. A blank date being accepted does not establish that inspection is unnecessary.

## Limitations
No inspection scheduling, calibration validation, physical availability or valuation. Duplicate checks and dates do not certify readiness. A due date equal to --as-of is not overdue.

## Related modules
[KPI](../process-management/kpi/README.md), [inspection report](../reports/technical/inspection-report.md), [5W2H](../process-management/5w2h/README.md).

[Start Here](../docs/start-here.md)
