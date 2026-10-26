# Inventory

The inventory CSV uses `asset_id,category,item,description,quantity,location,owner,project,status,supplier,value,acquisition_date,last_inspection,next_inspection,notes`. The validator requires asset ID, item, quantity, location, status, and next inspection; optional fields may be blank.

```powershell
python automation\validate_inventory.py examples\inventory-case\inventory.csv
```

Inspection dates use `YYYY-MM-DD`. The validator reports duplicate IDs, missing required values, non-numeric or negative quantities, malformed dates, and overdue inspections. It does not infer asset availability or financial value.
