# Inventory

The inventory CSV uses `asset_id,category,item,description,quantity,location,owner,project,status,supplier,value,acquisition_date,last_inspection,next_inspection,notes`. The validator requires the `asset_id`, `item`, `quantity`, `location`, `status`, and `next_inspection` columns. The `next_inspection` column must exist, but its value may be blank; a blank value is skipped by date validation.

```text
python automation/validate_inventory.py examples/inventory-case/inventory.csv --as-of 2026-10-26
```

Nonblank inspection dates must use ISO `YYYY-MM-DD`. A malformed date raises a validation error and exits with status 2; a valid but past date is reported as overdue and exits with status 1. The validator also reports duplicate IDs, missing required values, non-numeric or negative quantities. It does not infer asset availability or financial value.
