# Drive Governance

## When to use
Give a project a predictable file layout and clear responsibilities for access, retention and approved records.

## Input
[Folder structure](folder-structure.md), [permissions](permissions.md), [archive policy](archive-policy.md), [onboarding](onboarding.md).

## Required fields
The local folder generator takes --root (default PROJECT) and optional --dry-run. There is no CSV input.
For governance, manually define project owner, access roles, approved-document location, retention/review rules and archive responsibility.

## How to use
Preview the folders before creating them. Then assign access using the actual storage provider's controls and verify it with the responsible people; a folder name does not grant access.

## Command
Run from the repository root. Examples are fictional.

```text
python automation/generate_project_structure.py --root tutorial-project --dry-run
python automation/generate_project_structure.py --root tutorial-project
```

## Output
Both commands print 11 directory paths; only the second creates them. First/last output on Windows: tutorial-project\\00_Management and tutorial-project\\99_Archive. POSIX prints forward slashes. The exact list is in [folder-structure.md](folder-structure.md). Both exit 0.

## How to interpret
Keep original datasets and reviewed reports discoverable. Use 07_Data for project data and 08_Reports for reports; document your raw/derived separation inside them.

## Limitations
Only local folder creation is automated. Existing directories are retained; the script does not clean them. No cloud provisioning, permission audit, archive enforcement or synchronization is implemented. Adapt the guidance to organizational requirements.

## Related modules
[Document Control](../document-control/README.md), [reports](../reports/README.md), [project workflow](../docs/common-workflows.md).

[Start Here](../docs/start-here.md)
