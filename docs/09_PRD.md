# 09 — Product Requirements Document

**Product:** ShiftReady  
**Version:** 0.1 — proposal for discovery and prototype  
**Status:** Draft; requirements are provisional until customer discovery.  
**Owner:** Product case-study author  
**Audience:** Product, design, engineering, and research reviewers

## 1. Summary

ShiftReady is a proposed dispatch-readiness and exception-management workspace for depot-based last-mile EV fleets. It aims to help a dispatcher review upcoming shifts, identify vehicles that do not meet defined readiness criteria, and coordinate corrective action.

## 2. Problem statement

**Hypothesis:** fleet teams may not have a timely, trustworthy, consolidated view of whether scheduled vehicles are ready for dispatch, and may discover energy or operational blockers too late to recover efficiently.

Evidence status: **not yet validated in this repository**. See the discovery plan.

## 3. Goals

- Make upcoming shift readiness understandable at a glance.
- Expose why a vehicle is marked ready, at risk, blocked, or unknown.
- Show status source and timestamp.
- Provide an accountable workflow for operational exceptions.
- Support a low-friction prototype without proprietary system integrations.

## 4. Non-goals

- Direct charger or battery hardware control.
- Automated energy scheduling.
- GPS or route optimisation.
- Payment processing.
- Predictive maintenance / battery-health prediction.
- Replacing a full fleet-management or telematics platform.
- Claiming real-world operational impact before a pilot.

## 5. Users and permissions

| Role | Proposed permissions |
|---|---|
| Fleet admin | Manage sites, vehicles, shifts, users, configuration |
| Dispatcher | View fleet readiness, create / assign / close exceptions |
| Driver | View assigned shift; submit permitted check-in / issue information |
| Viewer | Read-only operational view |

Permissions must be validated against real organisational roles.

## 6. Core concepts

**Scheduled vehicle:** a vehicle assigned or expected for a shift.

**Readiness cutoff:** operator-defined time by which readiness is assessed.

**Readiness state:** Ready / At risk / Blocked / Unknown. State definitions are configurable and must not silently assume one universal SOC threshold.

**Signal:** a data point with source, captured timestamp, received timestamp (where available), and method (manual / import / integration).

**Exception:** an issue that may prevent readiness or create operational risk, with severity, owner, status, and timestamps.

## 7. Proposed P0 scope

1. Vehicle and site register.
2. Shift schedule and vehicle assignment.
3. Readiness board with explicit state and reason.
4. Manual or imported status entry with source and timestamp.
5. Exception creation, assignment, update, and closure.
6. Basic audit history for status and exception changes.
7. Clear empty, stale, missing, and conflicting-data states.

## 8. Proposed P1 scope

- Charging / replenishment task assignment if discovery shows this is central.
- Shift-level reports and export.
- Basic configurable readiness rules.
- CSV import and validation.
- Multi-site filtering.

## 9. Explicitly deferred

- Automated charging optimisation.
- Predictive downtime.
- Direct OCPP charger control.
- Live BMS or telematics data.
- GPS tracking and routing.
- Advanced analytics / AI recommendations.

## 10. Functional requirements

See [Requirements and Acceptance Criteria](11_REQUIREMENTS_AND_ACCEPTANCE.md) for requirement IDs, test cases, failure states, and acceptance details.

## 11. Metrics

Primary outcome candidate: dispatch-ready rate by cutoff, with strict definition of denominator, eligibility, and status provenance. Supporting and guardrail metrics are in [Metrics and Analytics](12_METRICS_AND_ANALYTICS.md).

No baseline or product improvement is claimed.

## 12. Technical assumptions and constraints

- Prototype data may be synthetic or manually entered and must be visibly labelled.
- Every status must have a source and timestamp.
- Missing or stale signals must not be treated as ready.
- The system must not control charging hardware in the prototype.
- Integrations depend on vendor APIs, permissions, connectivity, security, and commercial arrangements.

## 13. Risks

- Poor source data creates false readiness.
- Another tool adds duplicate entry.
- Existing vendors already solve the workflow.
- Dispatch readiness is operationally defined differently by each fleet.
- Drivers may be burdened with reporting tasks.
- Software may not control the underlying cause of downtime.

## 14. Open decisions

- Initial vehicle / replenishment segment.
- Actual readiness criteria and who configures them.
- Required source systems and data latency.
- Whether driver interaction is required.
- Buyer, procurement path, and value model.
- Data retention, privacy, and security requirements.

## 15. Release gate

A prototype is justified only when a specific recurring workflow and user need are supported by research. A pilot requires an agreed operator, data permissions, operational owner, baseline, and safety / privacy review.
