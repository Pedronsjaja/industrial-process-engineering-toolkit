# Document Control

## When to use
Identify engineering documents and distinguish drafts, reviewed revisions and approved records.

## Input
[Document register](document-register.csv), [naming rules](naming-standard.md), [revision guidance](revision-control.md) and [report templates](../reports/README.md).

## Required fields
The manual register has doc_id,title,type,area,owner,revision,date,validity,next_review,status,location,approver. Fill applicable fields and explain unavailable values; no register parser is implemented.
The filename checker expects PROJECT-TYPE-DESCRIPTION-RNN-YYYY-MM-DD.ext: uppercase letters/digits for project/type, letters/digits for description, at least two revision digits and a valid calendar date.

## How to use
Write a report, assign an ID, record author/reviewer and status, then check names in a controlled-document directory. For example PRJ-RPT-ServoTest-R01-2026-10-26.pdf follows the pattern; the toolkit does not produce that PDF. Update the register and retain previous revisions when issuing a reviewed change.

## Command
Run from the repository root. Examples are fictional.

```text
python automation/check_file_names.py --directory examples/first-improvement-cycle/controlled-documents
```

## Output
Exit 0 prints All files follow the naming pattern: followed by the scanned path. On Windows the tutorial path is examples\\first-improvement-cycle\\controlled-documents; POSIX uses forward slashes. Invalid names print invalid: paths and exit 1; a missing directory exits 2.

## How to interpret
A passing filename/calendar-date check only establishes naming validity. Confirm report contents, metadata consistency, reviewer decisions and approval separately.

## Limitations
No automatic register validation, approval workflow, PDF export or signature. Do not scan the entire source repository: README.md and code files are not controlled-document filenames.

## Related modules
[Reports](../reports/README.md), [Drive Governance](../drive-governance/README.md), [test reports](../reports/technical/test-report.md).

[Start Here](../docs/start-here.md)
