# 00 — Product Brief

## Executive summary

ShiftReady is a proposed B2B product for last-mile EV fleet operations. It investigates a narrow operational question: how can a depot team determine which scheduled vehicles are ready for dispatch, identify what is preventing readiness for the rest, and coordinate the next action before the shift cutoff?

The initial concept is a dispatch-readiness and exception-management workspace. Its value must be established through customer discovery; it is not assumed from the existence of EV adoption or from the availability of vehicle/charger data.

## Problem hypothesis

For some depot-based delivery fleets, vehicle readiness information may be distributed across manual checks, spreadsheets, driver communications, telematics tools, and charging or battery-swap systems. This fragmentation may make exceptions difficult to identify and resolve before dispatch.

**Hypothesis:** a single operational view with transparent data provenance and actionable exception ownership could reduce coordination effort and improve readiness decisions.

This hypothesis remains unvalidated until relevant operators describe recent, concrete incidents and their current processes.

## Target segment hypothesis

Initial focus: Delhi-NCR last-mile delivery operators with:
- recurring dispatch shifts;
- depot-based or depot-coordinated EV fleets;
- a manager responsible for vehicle allocation or dispatch readiness;
- charging and/or battery replenishment coordination;
- sufficient operational complexity to have recurring readiness workflows.

Do not impose a fleet-size threshold before learning how operational complexity and buying behaviour vary by segment.

## Stakeholders

| Role | Relationship to product | Main questions |
|---|---|---|
| Fleet owner / Head of Operations | Economic buyer / sponsor hypothesis | Is this problem costly enough to fund? Who approves software? |
| Depot manager / dispatcher | Primary daily user hypothesis | What must be known before the shift? What actions are possible? |
| Driver / rider | Frontline contributor | How is vehicle status communicated? What creates friction? |
| IT / telematics / charging partner | Technical stakeholder | Which data can be accessed, at what reliability and cost? |

## Proposed outcome

Help the operator make a timely, defensible dispatch-readiness decision and route unresolved exceptions to an accountable person.

## Product principles

1. **Dispatch-first:** organise information around upcoming shifts and cutoffs, not generic fleet dashboards.
2. **Trustworthy status:** every critical signal carries source, timestamp, and confidence/freshness state.
3. **Action over alerts:** an exception should have an owner, next action, and status.
4. **Graceful degradation:** missing integrations must not create false readiness.
5. **Minimum workflow burden:** do not create another driver task unless it solves a real problem.
6. **Evidence-led scope:** defer features unsupported by discovery.

## Proposed solution components

- Operator workspace: fleet register, upcoming shifts, readiness board, exception queue.
- Lightweight driver interaction: check-in or issue reporting, only if discovery supports it.
- Operational record: source and timestamp for readiness data, change history, exception ownership.
- Shift summary: explain what was ready, delayed, or unresolved at cutoff.

## Explicit non-goals for the first concept

- Public charging-station discovery.
- Consumer EV marketplace.
- Route optimisation or delivery-order dispatch.
- Payment processing.
- Direct remote control of charging hardware.
- Battery-health prediction.
- AI-based scheduling.
- Full telematics or fleet-management replacement.

## Key unknowns

- Which fleet segment experiences the most acute and frequent problem?
- Is the main workflow about plug-in charging, battery swapping, or mixed replenishment?
- Which data sources are available and trusted at dispatch time?
- Who owns the operational decision and budget?
- Is a new product preferable to improving existing systems or process?
- Would operators adopt a coordination layer without hardware integration?

## Decision gate

Proceed to a prototype only after discovery identifies a recurring, consequential workflow and a plausible low-friction way to support it. Pivot or stop if the problem is infrequent, already well-served, inaccessible to software, or not valuable enough to justify adoption.
