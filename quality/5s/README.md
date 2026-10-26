# 5S audit

The audit CSV uses `audit_id,area,criterion,sense,score,nonconformity,evidence,owner,due_date,status`. Senses are `Seiri`, `Seiton`, `Seiso`, `Seiketsu`, and `Shitsuke`; ratings are fictional example values from 0 to 5. Establish observable criteria and rating definitions before use.

Generate averages by sense with:

```powershell
python automation\generate_5s_report.py examples\5s-workshop-case\audit.csv --output 5s-scores.csv
```
