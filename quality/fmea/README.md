# FMEA

Input CSV requires `severity`, `occurrence`, and `detection` integer ratings from 1 to 10. The tool calculates `RPN = Severity × Occurrence × Detection` and ranks records from highest RPN to lowest.

RPN is not a universal acceptance criterion. Define scoring tables, review rules, and escalation requirements for the organization and applicable technical context. A low RPN must not be used to dismiss severe consequences.
