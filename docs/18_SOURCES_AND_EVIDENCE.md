# 18 — Sources and Evidence Register

**Research snapshot date:** 6 November 2026

## How to use this register

Every external claim in the final case study should link to a source and record:
- publisher / organisation;
- document or page title;
- URL;
- publication / update date (if available);
- access date;
- exact claim supported;
- limitations / interpretation.

Prefer primary sources: official notifications, product documentation, technical standards, and company-published material. News can add context but should not replace the underlying document for legal or technical claims.

## Sources reviewed for this version

| ID | Publisher | Source | What it supports | Limitation |
|---|---|---|---|---|
| S-001 | GNCTD Transport Department | [Notifications page](https://transport.delhi.gov.in/notifications) | Official listing of Delhi EV Policy 2026 and subsequent operational guideline notifications | Listing page is not a substitute for reading each policy clause or later amendment |
| S-002 | GNCTD Transport Department | [Operational Guidelines for Delhi EV Policy 2026](https://transport.delhi.gov.in/sites/default/files/Transport/circulars-orders/operating_guidelines.pdf) | Implementation guidelines for incentive and scrapping provisions | Guidelines are not the full policy text |
| S-003 | Gazette mirror | [Delhi EV Policy 2026 notification text](https://gazettetracker.com/g/SG-DL-E-30062026-273960) | Searchable text of the 30 June 2026 Gazette notification and policy provisions | Use official Gazette copy as controlling source; mirror is for searchability |
| S-004 | Kazam | [EV Fleet & Depot Management](https://kazam.energy/products/ev-fleet-depot-management-system) | Public claims about vehicle monitoring, charging queues, vehicle-to-charger mapping, alerts, cost analysis, and depot operations | Company marketing; not independent validation of actual performance |
| S-005 | Bolt.Earth | [Charger Management System](https://bolt.earth/charger-management-system) | Public claims about multi-location charger control, roles, fleet operators, and third-party OCPP charger onboarding | Company marketing; scope may differ from dispatch workflow |
| S-006 | Open Charge Alliance | [OCPP protocols](https://openchargealliance.org/protocols/open-charge-point-protocol/) | OCPP versions, positioning, and protocol feature overview | Check specific version specifications and errata before implementation |
| S-007 | Open Charge Alliance | [OCA FAQ](https://openchargealliance.org/faq/) | OCPP 1.6 / 2.0.1 compatibility clarification and OCPP 2.1 relationship | FAQ should be revisited as new editions and errata are released |
| S-008 | Open Charge Alliance | [OCPP download portal](https://openchargealliance.org/my-oca/ocpp/) | Published protocol editions and errata listing | Detailed specification downloads may require portal access |
| S-009 | Yano | [Company website](https://yano.energy/) | Starting point for further competitor verification | No feature-level claim made in this repository version |
| S-010 | MoEVing | [Company website](https://www.moeving.com/) | Starting point for further market / business-model verification | No feature-level claim made in this repository version |
| S-011 | Statiq | [Company website](https://www.statiq.in/) | Starting point for further ecosystem research | No feature-level claim made in this repository version |

## Evidence ledger

| ID | Claim | Evidence type | Source / participant | Date | Confidence | Limitation |
|---|---|---|---|---|---|---|
| E-001 | Kazam publicly markets vehicle monitoring and charging-queue capabilities | Company product page | S-004 | 2026-11-06 | High for marketing claim | Not independent product testing |
| E-002 | OCPP 1.6 and 2.0.1 are not backward-compatible | Standards-body FAQ | S-007 | 2026-11-06 | High | Recheck current edition / errata before engineering work |
| E-003 | Delhi EV Policy 2026 is listed by the Transport Department with a 1 July 2026 date | Government notification listing | S-001 | 2026-11-06 | High for listing date | Read full Gazette text before policy interpretation |

## Source quality

- **Primary:** official policy, standard, company product documentation, direct interview / observation.
- **Secondary:** reputable reporting or independent analysis.
- **Tertiary:** summaries, aggregators, unsourced commentary.

Use secondary sources for context and cross-checking. Do not treat company marketing as independent proof of product performance or customer outcomes.
