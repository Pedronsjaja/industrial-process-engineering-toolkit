# KPI definitions

`automation/generate_kpis.py` emits only metrics for input files supplied on the command line. CSV headers are case-sensitive. Counts and formulas below describe the current implementation; they are not universal engineering definitions.

| KPI | Formula and fields | Status considered | Unit | Limitations |
|---|---|---|---|---|
| Open Actions | Count rows in the actions CSV whose `status`, after trimming and lowercasing, is not `closed`, `complete`, or `completed`. Requires `action_id`, `status`, and `due_date` columns. | Every value other than the three closed values is counted as open, including a blank status. | actions | Does not validate unique IDs, ownership, or action effectiveness. |
| Overdue Actions | Count open action rows with a nonblank `due_date` earlier than `--as-of` (defaults to the machine's current date). Dates use ISO `YYYY-MM-DD`. | Uses the same open-status rule as Open Actions. Blank due dates are not overdue. | actions | The as-of date must be fixed for reproducible reports. The metric does not establish whether an action's priority warrants escalation. |
| Inventory Availability | Number of inventory rows whose trimmed, lowercase `status` is `available`, `in stock`, or `active`, divided by all rows. Requires `asset_id` and `status` columns. | Those three values are available; every other value is not available. | ratio from 0 to 1 | Does not check quantity, location, reservation, condition, or asset uniqueness. An empty file produces 0. |
| FMEA items at/above RPN threshold | Count rows where `severity × occurrence × detection >= --high-risk-rpn-threshold` (default 200). Requires three integer ratings in the inclusive 1–10 range. | All FMEA rows count; there is no status filter. | items | The default threshold is an example, not a universal risk criterion. Define criteria locally; RPN does not replace severity-based review. |
| 5S Score | Arithmetic mean of all `score` values in the supplied audit CSV. Requires `sense` and `score`; the score must be finite and in the inclusive 0–5 range. | Includes every audit row, regardless of area, status, or sense. | score (0–5) | This KPI is an overall mean, not a weighted score; it does not group by area or require all five senses. Empty audit input emits no 5S row. |

These definitions document current behavior, including limitations. Any future change to status semantics, denominators, or grouping should be explicit, tested, and recorded in the changelog.
