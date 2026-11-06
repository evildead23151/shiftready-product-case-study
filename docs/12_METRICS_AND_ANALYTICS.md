# 12 — Metrics and Analytics

## Outcome metric candidate

**Dispatch-ready rate by cutoff**

`Eligible scheduled vehicles meeting the configured readiness criteria by cutoff / Total eligible scheduled vehicles × 100`

This definition requires an operator-approved readiness policy. A universal SOC threshold is not appropriate because requirements depend on vehicle, planned duty, route, conditions, and replenishment model.

## Supporting metrics

| Metric | Definition | Interpretation caution |
|---|---|---|
| Energy-related missed-dispatch rate | Eligible shifts with a documented energy-related readiness failure / eligible shifts | Requires consistent reason coding |
| Readiness delay | Time between planned readiness cutoff and first verified ready state | Cannot infer cause from timestamps alone |
| Exception resolution time | Time from exception creation to closure | Closure quality must be checked |
| Unresolved exceptions at cutoff | Count of open exceptions at cutoff | Separate severity and age |
| Manual coordination effort | Time spent on defined coordination tasks | Requires a consistent time-study method |
| Vehicle utilisation | Operational use relative to availability period | Define active hours and exclusions carefully |

## Guardrails

- Incorrect “Ready” declarations.
- Stale-data share among vehicles marked Ready.
- Additional driver reporting time.
- Dispatcher workload and alert volume.
- Safety-policy violations.
- Energy cost and peak-demand impacts where relevant.
- Data completeness and coverage by source.

## Instrumentation proposal

Potential events:
- shift_created
- vehicle_assigned
- readiness_status_viewed
- status_recorded
- status_marked_stale
- exception_created
- exception_assigned
- exception_updated
- exception_closed
- shift_cutoff_reached
- readiness_outcome_recorded

Events should include account/site ID, vehicle ID, shift ID, actor role, timestamp, source type, and relevant status. Avoid collecting unnecessary personal data.

## Baseline and impact evaluation

Before a pilot:
1. Agree the operational definition with the fleet.
2. Measure baseline for a defined period.
3. Record fleet / depot / shift mix and major confounders.
4. Agree data quality and missingness rules.
5. Define comparison method and success threshold in advance.
6. Review guardrails and unintended consequences.

Do not claim a causal impact from before/after movement alone if operational volume, fleet mix, staffing, routes, or charging infrastructure changed.

## Prototype analytics

A static prototype may demonstrate metric definitions using synthetic data. Label every chart and dataset “Illustrative synthetic data — not measured operational results.”
