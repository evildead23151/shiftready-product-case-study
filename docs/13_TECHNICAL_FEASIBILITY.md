# 13 — Technical Feasibility

## Purpose

Identify the technical dependencies and failure modes that determine whether ShiftReady can provide trustworthy dispatch-readiness information.

## Data domains

- Fleet / vehicle identity and state.
- Shift schedule and vehicle assignment.
- Energy status or replenishment event.
- Depot / charger / swapping station state, where relevant.
- Operational exception and ownership.
- User, role, and audit history.

## Data provenance is a product requirement

For each critical signal, represent:
- source system or user;
- source record identifier where available;
- captured timestamp;
- received / ingested timestamp;
- method: manual, file import, or integration;
- validity and freshness state;
- transformation / rule version used.

A manually entered battery value is not equivalent to a live telematics signal. The UI must not imply otherwise.

## Readiness logic

Do not define readiness as “SOC greater than X” globally. The operator-approved rule may depend on:
- vehicle type and capacity;
- planned route / duty and reserve policy;
- expected distance and load;
- environmental and operating conditions;
- current vehicle faults or safety restrictions;
- replenishment model;
- data freshness and confidence.

When required inputs are absent or stale, status should be Unknown or require manual verification—not Ready by default.

## Integration considerations

### Charger management

OCPP is a communications protocol family between charging stations and management systems. Version and feature compatibility matter. OCPP 1.6 and OCPP 2.0.1 are not directly backward-compatible; do not claim generic “OCPP integration” without identifying version, supported functions, security profile, vendor implementation, and certification / testing requirements.

### Vehicle telemetry / BMS

Vehicle telemetry access is separate from charger-management integration. It may depend on OEM APIs, telematics provider contracts, device installation, data ownership, latency, and permissions.

### Prototype approach

- Use synthetic records or user-entered sample data.
- Keep data source labels visible.
- Do not connect to real vehicles or chargers.
- Do not issue hardware commands.
- Demonstrate stale, missing, conflicting, and malformed data states.

## Reliability and safety

- Fail closed for critical missing readiness inputs.
- Distinguish unavailable from zero.
- Preserve timestamps and time zones.
- Record manual overrides and reasons.
- Show last successful sync and source health.
- Avoid automated decisions that could create unsafe dispatch behaviour.
- Treat the product as decision support, not a replacement for required physical inspection or operator safety procedures.

## Security and privacy questions

- Role-based access and least privilege.
- Tenant and site isolation.
- Encryption in transit and at rest.
- Audit logging for critical changes.
- Retention and deletion policies.
- Consent and legal basis for driver-related data.
- Incident response and access reviews.
- Vendor data processing and contractual controls.

These controls are design considerations, not implemented capabilities.
