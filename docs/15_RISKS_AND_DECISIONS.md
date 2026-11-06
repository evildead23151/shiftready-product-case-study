# 15 — Risks and Decision Log

## Risk register

| Risk | Likelihood / impact | Mitigation / evidence needed |
|---|---|---|
| Existing products already solve the target workflow | High uncertainty / high impact | Competitive validation and operator interviews |
| Readiness data is stale or inaccurate | High / high | Provenance, freshness, unknown state, manual checks |
| Additional workflow creates duplicate work | Medium-high / high | Observe actual process; minimise re-entry |
| Buyer and user incentives differ | Medium / high | Interview both; map procurement and daily usage |
| Integration access is limited | High / high | Validate APIs, contracts, costs before committing |
| Shift readiness is defined differently by fleet | High / medium | Configurable policy and segment focus |
| Driver app adds burden | Medium / medium | Defer until a driver job is proven |
| Product claims exceed evidence | Medium / high | Evidence labels and release review |
| Sensitive operational / driver data exposure | Medium / high | Data minimisation, permissions, retention, security review |

## Decision records

Use the [decision record template](../templates/DECISION_RECORD_TEMPLATE.md) for any material choice. Each record should capture context, evidence, alternatives, decision, consequences, owner, and revisit trigger.

## Initial decisions

### D-001 — Position around dispatch readiness, not consumer charging discovery

**Status:** proposed.  
**Rationale:** the target customer hypothesis is a fleet operator preparing managed vehicles for shifts, not an individual finding a public charger.  
**Revisit when:** discovery shows the operator's main pain is actually charging access / procurement rather than dispatch readiness.

### D-002 — No AI in initial MVP

**Status:** proposed.  
**Rationale:** the riskiest unknown is the workflow and data quality, not model performance. An algorithm cannot repair missing or untrusted source data.  
**Revisit when:** there is a well-defined repeated decision, adequate historical data, and a measurable advantage over simpler rules.

### D-003 — No direct charger control in prototype

**Status:** proposed.  
**Rationale:** hardware control creates integration, safety, protocol, and partner dependencies before the product problem is validated.  
**Revisit when:** a pilot partner and technical / safety review establish a justified use case.

### D-004 — Readiness must carry source and timestamp

**Status:** proposed product principle.  
**Rationale:** source freshness changes how an operator should interpret status.  
**Revisit when:** data architecture and user testing refine the representation, not whether provenance matters.
