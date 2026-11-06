# ShiftReady
### EV Fleet Dispatch Readiness & Energy Coordination

**An independent B2B product-management case study for last-mile EV fleet operations in Delhi-NCR.**

ShiftReady explores how fleet operators prepare vehicles for scheduled shifts, coordinate energy replenishment, and respond to operational exceptions. The product concept is intentionally narrow: help depot teams make better dispatch-readiness decisions using operational information they can trust.

> **Project status — discovery / product-definition concept.** This repository documents a proposed product and its research plan. It is not a deployed product. Customer interviews, pilots, integrations, live telemetry, commercial outcomes, and measured impact are not claimed unless explicitly recorded as completed evidence.

---

## The product question

**Can a lightweight, dispatch-first workflow help depot teams identify which vehicles are ready for the next shift, understand what is blocking the rest, and coordinate the next action across fragmented operational systems?**

This is a hypothesis to investigate, not a validated market fact.

### Why this problem space

Last-mile fleets operate against shift start times, vehicle availability, energy constraints, and delivery commitments. A vehicle that is technically present but not sufficiently charged, checked in, or otherwise operationally cleared may not be dispatch-ready. Yet “readiness” is not a single battery-percentage threshold: it depends on the planned duty, vehicle requirements, data freshness, and operator policy.

The project examines the problem from the perspective of three distinct stakeholders:

- **Economic buyer:** fleet owner / head of operations.
- **Primary workflow user:** depot manager / dispatcher.
- **Frontline contributor:** delivery driver / rider.

The initial ideal-customer hypothesis is a Delhi-NCR last-mile delivery operator with depot-based EVs, recurring shifts, and responsibility for coordinating vehicle readiness and energy replenishment.

## Proposed product direction

A web-based operator workspace, complemented by a lightweight driver workflow:

1. Maintain a fleet and shift register.
2. View readiness against a defined dispatch cutoff.
3. See the source and timestamp behind each readiness signal.
4. Triage delayed vehicles and operational exceptions.
5. Assign and track the next action.
6. Review shift-level operational outcomes.

The first prototype should use clearly labelled synthetic or manually entered data. Direct charger control, live BMS/telematics integrations, automated energy optimisation, and predictive maintenance are outside the initial scope.

## What this repository demonstrates

This is designed as a **product-management portfolio case study**, not a claim of production delivery. It contains the reasoning artifacts that support product work across Product Manager, Associate PM, Technical PM, Product Analyst, Product Operations, and product-strategy interviews:

| PM capability | Evidence in this repository |
|---|---|
| Problem framing | Product brief, assumptions, scope boundaries |
| Market understanding | Competitor landscape and source register |
| Customer discovery | Interview plan, guide, note-taking and synthesis templates |
| Product strategy | Positioning hypotheses, opportunity framing, trade-offs |
| Requirements | PRD, user stories, acceptance criteria, edge cases |
| Prioritisation | MVP boundaries, prioritisation approach, decision log |
| Technical fluency | Data provenance, freshness, integration and reliability constraints |
| Product analytics | Metric tree, definitions, guardrails, instrumentation plan |
| Execution | Roadmap, backlog, risks and decision records |
| Communication | Executive summary and interview walkthrough structure |

## Repository map

```text
.
├── README.md
├── PROJECT_STATUS.md
├── CHANGELOG.md
├── GITHUB_ISSUES.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── docs/
│   ├── 00_PRODUCT_BRIEF.md
│   ├── 01_MARKET_AND_CONTEXT.md
│   ├── 02_COMPETITIVE_LANDSCAPE.md
│   ├── 03_DISCOVERY_PLAN.md
│   ├── 04_INTERVIEW_GUIDE.md
│   ├── 05_RESEARCH_SYNTHESIS.md
│   ├── 06_PERSONAS_AND_JTBD.md
│   ├── 07_OPPORTUNITY_SOLUTION_TREE.md
│   ├── 08_PRODUCT_STRATEGY.md
│   ├── 09_PRD.md
│   ├── 10_USER_JOURNEYS.md
│   ├── 11_REQUIREMENTS_AND_ACCEPTANCE.md
│   ├── 12_METRICS_AND_ANALYTICS.md
│   ├── 13_TECHNICAL_FEASIBILITY.md
│   ├── 14_ROADMAP_AND_RELEASES.md
│   ├── 15_RISKS_AND_DECISIONS.md
│   ├── 16_EXPERIMENTS_AND_USABILITY.md
│   ├── 17_FINAL_CASE_STUDY.md
│   └── 18_SOURCES_AND_EVIDENCE.md
├── templates/
│   ├── INTERVIEW_NOTE_TEMPLATE.md
│   ├── ASSUMPTION_LEDGER.md
│   ├── DECISION_RECORD_TEMPLATE.md
│   └── USABILITY_TEST_TEMPLATE.md
├── scripts/
│   └── check_markdown_links.py
└── .github/
    ├── ISSUE_TEMPLATE/
    ├── pull_request_template.md
    └── workflows/docs-check.yml
```

## How to read the case study

A reviewer should be able to follow the chain:

**Context → customer problem → evidence → opportunity → product choice → requirements → measurement → learning.**

Start with the [product brief](docs/00_PRODUCT_BRIEF.md), then read the [discovery plan](docs/03_DISCOVERY_PLAN.md), [competitive landscape](docs/02_COMPETITIVE_LANDSCAPE.md), and [PRD](docs/09_PRD.md).

## Evidence and integrity policy

To keep the case study defensible:

- **Fact** means supported by a cited public source or verifiable artifact.
- **Observation** means directly observed during research or testing, with date and context.
- **Validated finding** means supported by documented participant evidence or a completed test.
- **Hypothesis** means plausible but not yet established.
- **Proposal** means a recommended product or execution decision.
- **Unknown** means the evidence is currently insufficient.

Do not convert a hypothesis into a finding because it makes the narrative more attractive. Do not add invented participant quotes, customer names, sample sizes, market sizes, conversion rates, pilots, revenue, or performance improvements. Synthetic prototype data must be labelled as synthetic.

## Current limitations

- No completed customer interviews are represented in the initial repository.
- No customer problem or willingness-to-pay hypothesis is yet validated.
- No production application or clickable prototype is claimed.
- No live charger, BMS, GPS, or telematics integration is claimed.
- No operational impact or commercial result is measured.
- Competitor analysis is based on publicly documented positioning and requires continued verification; it is not a hands-on product teardown.

These are active work items, not hidden weaknesses.

## Next milestones

1. Verify public market and competitor claims; maintain source dates.
2. Recruit and interview relevant fleet operators and depot users.
3. Synthesize evidence without treating repeated assumptions as facts.
4. Revisit the target segment and product wedge based on evidence.
5. Freeze MVP requirements and acceptance criteria.
6. Build and usability-test a clearly labelled prototype.
7. Update the case study with actual findings, changes, and limitations.

See [PROJECT_STATUS.md](PROJECT_STATUS.md) for the current status and [GITHUB_ISSUES.md](GITHUB_ISSUES.md) for a suggested execution backlog.

## About

An independent product research and strategy project. The product concept is named **ShiftReady**. This repository is a portfolio artifact and does not imply affiliation with any EV operator, charging provider, OEM, or government agency.
