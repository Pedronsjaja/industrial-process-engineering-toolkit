# Engineering analysis report

Use for structural, thermal, fluid or mechanism analysis, CAD/design evaluation, simulation results or design comparison. Copy the [analysis template](../templates/engineering-analysis-template.md).

Problem → Assumptions → Input data → Method → Model → Results → Verification → Limitations → Engineering interpretation → Recommendation.

Record geometry/material/load or other inputs with units and provenance; do not infer unavailable physical properties from a CAD appearance.
State assumptions, governing equations, boundary/initial conditions, simplifications and software/version. For numerical work record mesh/time-step/solver configuration where applicable and evaluate convergence or sensitivity.
Separate verification (checking the implementation/solution) from validation against relevant physical/reference evidence. Their scope depends on the question.

Compare alternatives under consistent requirements, loads and criteria; explain uncertainty, sensitivity and conditions where the recommendation may not hold. Label SIMULATED/CALCULATED/ESTIMATED results and preserve raw/model files.
Simulation requires validation appropriate to its use. Software does not replace engineering judgment.

Link [FMEA](../../quality/fmea/README.md), [test evidence](test-report.md), [actions](../../process-management/5w2h/README.md) and [document control](../../document-control/README.md) when applicable.
