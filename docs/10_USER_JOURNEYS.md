# 10 — User Journeys

> Proposed future-state journeys. Validate the current-state workflow through observation before treating these as requirements.

## Journey A — Dispatcher prepares a shift

1. Dispatcher opens the upcoming shift.
2. System lists vehicles assigned to that shift.
3. Each vehicle displays a readiness state, reason, source, and timestamp.
4. Dispatcher filters vehicles that are at risk, blocked, or unknown.
5. Dispatcher opens an exception or creates one if needed.
6. Dispatcher assigns an owner and next action.
7. Dispatcher reviews outstanding exceptions before the cutoff.
8. At cutoff, dispatcher records the readiness outcome.

**Critical failure cases:** missing energy data, stale status, contradictory status sources, vehicle reassignment, shift cancellation, duplicate exception, no available owner.

## Journey B — Driver reports a vehicle issue

1. Driver views assigned vehicle and shift information.
2. Driver reports a problem using the minimum required fields.
3. System acknowledges the report and creates an exception.
4. Dispatcher reviews and assigns the next action.
5. Driver receives only the relevant status update.

This journey should be built only if research demonstrates that driver reporting is the right point in the workflow. Do not make drivers duplicate data already available elsewhere.

## Journey C — Operator reviews a shift

1. Operator selects site and date range.
2. Operator sees scheduled vehicles and final readiness outcomes.
3. Operator filters delay reasons and unresolved exceptions.
4. Operator exports a report for operational review.

Do not infer financial savings from delay counts without a validated cost model.
