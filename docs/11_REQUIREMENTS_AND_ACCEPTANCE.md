# 11 — Requirements and Acceptance Criteria

All requirements below are **proposed** for a prototype. Priority must be revisited after discovery.

## P0 — Core workflow

### FR-001 — Vehicle register

**User story:** As a fleet admin, I want to maintain a vehicle register so that shifts can reference identifiable vehicles.

**Acceptance criteria**
- Admin can create, edit, deactivate, and view a vehicle.
- Vehicle identifier is unique within the account.
- Required fields are validated before save.
- Deactivated vehicles cannot be assigned to future shifts by default.
- Empty fleet state explains how to add the first vehicle.

### FR-002 — Shift schedule

**User story:** As a dispatcher, I want to view upcoming shifts and assigned vehicles so that I can prepare dispatch.

**Acceptance criteria**
- Dispatcher can view shifts by site and date.
- Each assignment references one active vehicle.
- Duplicate assignment conflicts are surfaced.
- Cancelled shifts are visually distinct and excluded from readiness denominator.
- No-shift and no-assignment states are explicit.

### FR-003 — Readiness state

**User story:** As a dispatcher, I want to see a readiness state and reason for each scheduled vehicle.

**Acceptance criteria**
- State is one of Ready, At risk, Blocked, or Unknown.
- State includes a human-readable reason.
- State includes source and timestamp for relevant inputs.
- Missing critical inputs result in Unknown, not Ready.
- Stale inputs are visibly stale and cannot silently remain valid.
- Readiness criteria are configurable by an authorised operator.
- The UI does not apply a universal battery SOC threshold.

### FR-004 — Status capture

**User story:** As an authorised user, I want to add or import status data with provenance.

**Acceptance criteria**
- Each record stores source type (manual, file import, integration placeholder).
- Each record stores captured time and recorded time.
- Invalid values are rejected with actionable feedback.
- Future timestamps, impossible values, and duplicate imports are handled.
- Imported data does not overwrite newer data without an explicit rule.
- Synthetic demo records are clearly labelled in the prototype.

### FR-005 — Exception workflow

**User story:** As a dispatcher, I want to create and track an exception so that blockers have an owner and next action.

**Acceptance criteria**
- Exception has category, description, severity, status, owner, created time, and updated time.
- Status transitions are controlled and recorded.
- Closed exceptions retain history.
- Duplicate or related exceptions can be identified.
- Reopening requires a reason.
- Unassigned exceptions are visible.

### FR-006 — Audit trail

**User story:** As an operator, I want to understand who changed a critical status and when.

**Acceptance criteria**
- Critical status and exception changes record actor and timestamp.
- Previous and new values are retained for relevant fields.
- Audit history is read-only for ordinary users.
- The interface distinguishes system-generated from user-entered events.

## P1 — Conditional scope

### FR-101 — Replenishment task coordination

Only include after discovery confirms that task assignment is a core problem.

**Acceptance criteria**
- Task references vehicle, site, time window, and owner.
- Task status is visible.
- Conflicts and missed windows are surfaced.
- The product does not issue charger commands.

### FR-102 — Shift summary

**Acceptance criteria**
- Summary shows scheduled, eligible, ready, at-risk, blocked, and unknown counts.
- Denominator and exclusions are visible.
- Results are exportable.
- A summary cannot imply causation or savings without evidence.

## Shared quality requirements

- Clear time zone and timestamp display.
- Accessible status labels; colour is not the only signal.
- Responsive layout for the intended operator device.
- Role-based access and least privilege.
- Safe handling of personally identifiable and operationally sensitive data.
- Graceful error states for unavailable imports or services.
