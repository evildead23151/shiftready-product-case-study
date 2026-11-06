# 02 — Competitive Landscape

## Purpose and method

Understand what operators can already buy or use. This is a **desk-research snapshot** based on publicly described capabilities, not hands-on product testing or independently verified performance. Product pages change; every claim should be revisited before external presentation.

## Competitor / adjacent solution map

| Company | Publicly documented positioning reviewed | Implication for ShiftReady | Confidence / limitation |
|---|---|---|---|
| Kazam | Its EV Fleet & Depot Management page describes live vehicle monitoring, smart alerts, cost analysis, vehicle-to-charger mapping, charging queues, trip-adherence analytics, and depot operations. | Strong direct overlap. Generic fleet visibility, queueing, and readiness dashboards cannot be claimed as unique. | High confidence in the vendor's public marketing claims; no independent performance validation. |
| Bolt.Earth | Its Charger Management System page describes multi-location charger management, role-based access, fleet-operator functionality, and third-party OCPP charger onboarding. | Relevant infrastructure / charger-management layer and potential integration dependency. | High confidence in public marketing claims; not proof it replaces dispatch management. |
| Yano | Retain as an adjacent market participant to investigate. | Could be relevant to fleet energy coordination; exact overlap should be established from current product documentation and operator references. | Feature-level claims intentionally withheld pending direct source verification. |
| MoEVing | Retain as an adjacent EV fleet / logistics ecosystem participant to investigate. | May compete as an operator, service provider, or technology-enabled fleet solution; clarify the actual buying alternative. | Business model and software boundaries need primary-source verification. |
| Statiq | Retain as an adjacent charging-network participant to investigate. | Relevant to charging access and ecosystem integrations; a network is not automatically a dispatch-workflow substitute. | Feature-level claims intentionally withheld pending direct source verification. |

**Sources reviewed:** [Kazam Fleet & Depot Management](https://kazam.energy/products/ev-fleet-depot-management-system) and [Bolt.Earth Charger Management System](https://bolt.earth/charger-management-system). Additional market participants are research leads, not fully benchmarked competitors in this version.

## Core competitive conclusion

Do **not** claim that ShiftReady is differentiated merely because it offers:
- live fleet visibility;
- state-of-charge display;
- charging queues;
- shift scheduling;
- smart charging;
- maintenance alerts;
- an operator dashboard.

Kazam's public product page alone already advertises several of these capabilities. Bolt.Earth also markets charger operations, multi-site control, fleet-operator functions, and OCPP-compatible third-party charger onboarding.

## Differentiation hypotheses to test

| Hypothesis | Evidence required | Disconfirming evidence |
|---|---|---|
| Vendor-neutral reconciliation | Operators manually reconcile multiple tools and value a consolidated workflow | Existing platform already integrates all critical sources |
| Lightweight deployment | Buyers avoid solutions needing expensive or slow integrations | Hardware integration is mandatory for trustworthy operation |
| Exception-first workflow | Operators spend more time resolving exceptions than reviewing dashboards | Main pain is energy optimisation or capacity planning instead |
| Segment-specific workflow | A narrowly defined fleet segment is poorly served | Competitors already serve it effectively |
| Better data transparency | Operators need to distinguish live, stale, manual, and unknown status | Users do not trust or act on any available status without physical checks |

## Competitive research protocol

For each company, record:
- source URL and date accessed;
- target customer and use case;
- publicly stated capabilities;
- integrations and dependencies;
- commercial model, only where publicly disclosed;
- geography and customer evidence;
- what is unknown;
- confidence in each claim.

Do not infer feature absence from a marketing page's silence. Use “not found in reviewed public material,” not “does not support.”

## Strategic implication

The product should compete on a validated workflow gap, not a feature checklist. A coordination layer may be useful only if it can coexist with existing systems, reduce operational friction, and avoid becoming another system that requires duplicate data entry.
