# 08 — Product Strategy

## Strategy statement

If discovery confirms that a defined depot-based EV fleet segment struggles to make reliable dispatch-readiness decisions using fragmented operational information, ShiftReady could provide a lightweight coordination layer that makes status, exceptions, and ownership visible around shift cutoffs.

This strategy is conditional on evidence.

## Positioning hypothesis

For last-mile fleet operations teams that need to prepare EVs for recurring shifts, ShiftReady is a dispatch-readiness workspace that helps teams identify blockers and coordinate next actions. Unlike a generic charging dashboard, the concept is organised around the shift decision and transparent data freshness.

This is not a verified competitive advantage. Competitors may already serve this need; validation must establish a segment-specific gap.

## Why not build a charging-station finder?

A public charging finder solves a different customer job. The proposed audience is an operator coordinating a managed fleet and its depots, not an individual EV driver searching for a public charger.

## Strategic choices

| Choice | Current proposal | Why / uncertainty |
|---|---|---|
| Customer | Depot-based last-mile EV fleet operators | Need to validate segment intensity and buyer |
| User | Dispatcher / depot manager | Likely owns shift workflow; validate |
| Wedge | Readiness and exception workflow | Must prove it is not already adequately solved |
| Interface | Operator web workspace first | Better suited to multi-vehicle operations; validate access patterns |
| Driver app | Minimal / deferred | Avoid burden until a driver-facing job is proven |
| Data integration | Manual/imported/simulated for prototype | No real integration claimed |
| AI | Out of MVP | No evidence that prediction or optimisation is the riskiest bottleneck |

## Business model hypotheses

Potential options to test:
- per depot / site subscription;
- per active vehicle tier;
- enterprise contract with integrations and support.

Do not publish prices until buyer interviews, procurement research, and competitor evidence support a plausible range. Consider implementation, onboarding, support, and integration costs—not only software hosting.

## Build / buy / partner considerations

- Build the workflow and operational logic that represent the validated product wedge.
- Integrate with existing fleet / charger / telematics systems where APIs, commercial terms, and reliability allow.
- Partner where hardware access, certification, or field operations exceed the scope of a software-only product.
- Do not build a charger network or vehicle telematics stack as an MVP dependency.

## Strategic kill criteria

Reconsider the concept if:
- the target problem is infrequent or immaterial;
- current vendors solve it adequately for the chosen segment;
- data access makes trustworthy readiness impossible;
- adoption requires duplicative workflows operators reject;
- buyer value cannot justify implementation and ongoing support.
