# Contributing

Contributions are welcome. Keep changes focused and suitable for small engineering teams.

1. Create a focused branch from the current development target and submit a small, traceable pull request; do not work directly on `main`.
2. Use clear commits that describe the change. Explain scope and validation in the PR.
3. Install test dependencies with `python -m pip install pytest`; run `python -m pytest -q` and add tests for behavior changes.
4. Keep scripts readable, validate inputs, return non-zero status for invalid data, and document CSV schema/naming changes.
5. Label work accurately as IMPLEMENTED, DOCUMENTED, EXAMPLE, or PLANNED. Do not describe a planned feature as implemented.
6. Use fictional or anonymized examples. Never submit confidential client/company information or sensitive real-world datasets.
7. Verify licenses before reusing third-party code or materials and record source, license, component, changes, and attribution in `THIRD_PARTY_CREDITS.md`.
8. Do not copy protected text, tables, or figures from ABNT, ISO, NR, or other standards. Link to official sources instead.
9. Update relevant documentation and the changelog when user-facing behavior changes.

The project is released under the MIT License. Contributions are expected to be submitted under that license.
