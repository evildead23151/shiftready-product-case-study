# 07 — Opportunity Solution Tree

> Initial hypothesis tree. Reorder or discard opportunities after discovery.

## Desired outcome hypothesis

Increase the proportion of scheduled vehicles that satisfy the operator's defined readiness criteria by the dispatch cutoff, without creating unacceptable driver burden, cost, or safety risk.

## Opportunity hypotheses

1. **Readiness uncertainty:** dispatcher cannot confidently determine which vehicles meet the requirements for the upcoming shift.
2. **Late exception discovery:** blockers are found too close to dispatch for effective recovery.
3. **Fragmented coordination:** vehicle, driver, replenishment, and depot information must be reconciled manually.
4. **Unclear ownership:** exceptions lack a named owner and next action.
5. **Data trust:** stale, manually entered, and live signals are treated as equivalent.

## Candidate solution directions

| Opportunity | Candidate intervention | Key risk |
|---|---|---|
| Readiness uncertainty | Shift-based readiness board | False confidence if data is stale |
| Late exception discovery | Exception queue with cutoff and severity | Alert fatigue / poor signal quality |
| Fragmented coordination | Import or reconcile existing records | Integration and duplicate-entry burden |
| Unclear ownership | Assignment, status, and audit trail | Workflow overhead |
| Data trust | Source, timestamp, freshness, unknown state | Users may still need physical checks |

## Experiment before commitment

- Observe an actual shift-preparation workflow.
- Ask the dispatcher to reconstruct a recent delayed vehicle case.
- Test a paper / spreadsheet mock-up before a full prototype.
- Measure task completion and errors, not stated enthusiasm.
- Check whether a non-software process change solves the issue more simply.

## Decision principle

Do not jump from an opportunity to a feature. Generate multiple interventions, test the riskiest assumptions, and select the lowest-complexity solution that changes the target outcome.
