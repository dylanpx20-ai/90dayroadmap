[PORTFOLIO.md](https://github.com/user-attachments/files/34992108/PORTFOLIO.md)
# Portfolio Snapshot & Monthly Priorities

> A companion reference to the 90-day Account Management roadmap. All 50 advertiser accounts are **synthetic**. The numbers are illustrative planning inputs, not client results.

## The three monthly recommendations

| Phase | Weeks | Main recommendation |
|---|---|---|
| **Month 1 — Establish control** | 1–4 | Audit all 50 accounts, establish ownership and contact coverage, and build risk-ranked plans before deep optimization. |
| **Month 2 — Protect retention and delivery** | 5–8 | Focus on material campaign issues and upcoming reviews; verify progress and re-rank accounts using current evidence. |
| **Month 3 — Qualify growth and plan ahead** | 9–13 | Advance only evidence-qualified expansion opportunities and use observed spend and unresolved risks to build the next-quarter plan. |

These are **planning phases**, not exact calendar months or claims that the work has been completed.

## The inherited book

The scenario is a newly assigned Ad-Tech Account Manager responsible for **50 accounts** with a combined **$215,850 in monthly advertiser budgets**. These are budget allocations, **not actual billed spend or platform revenue**.

| Tier | Accounts | Monthly budget range per account | Total monthly budgets | Coverage approach |
|---|---:|---:|---:|---|
| T1 | 7 | $8,000–$9,300 | $59,300 | High-touch; AM-owned service and strategic attention |
| T2 | 10 | $6,150–$6,900 | $65,600 | High-touch; AM-owned service and strategic attention |
| T3 | 15 | $4,100–$4,950 | $68,300 | Regular AM coverage; escalate material risks |
| T4 | 8 | $2,050–$2,950 | $18,700 | Lighter-touch AM coverage, with Support assistance |
| T5 | 10 | $0–$1,000 | $3,950 | Support-first for routine issues; AM handles escalations and commercial decisions |
| **Total** | **50** | — | **$215,850** | All accounts retain appropriate routine coverage |

**Illustrative service routing:** T1–T2 receive an AM-owned first meaningful response target of 24 elapsed hours; T3–T4 have a 48-elapsed-hour target; routine T5 issues are Support-first. Critical issues override tier routing. These are **fictional policy assumptions**, not measured response times; after-hours coverage would require a designated team.

## The underlying 50-account dataset

The roadmap script embeds the full synthetic account dataset. The table below makes the main decision-making inputs visible without having to decode the Python data. For the complete original columns—including industry, contact cadence, CRM notes, and tenure—see [`synthetic_accounts.csv`](synthetic_accounts.csv).

**Reading the table:** “Spend” is illustrative current monthly spend in the synthetic baseline, **not observed or billed spend**. “Review” is an illustrative milestone date whose exact commercial type must be verified. “Issue” is a baseline flag, not evidence of a current unresolved live incident.

| Account | Tier | Monthly budget | Illustrative spend | Condition | Campaign | Last contact (days) | Open issue | Expansion | Review date |
|---|---:|---:|---:|---|---|---:|---|---|---|
| ADV-001 | T1 | $8,200 | $8,938 | Healthy / stable | On target | 6 | None | Medium | 2027-03-20 |
| ADV-002 | T1 | $8,500 | $8,585 | Healthy / stable | On target | 13 | None | Medium | 2027-07-03 |
| ADV-003 | T1 | $8,000 | $6,400 | Performance concern | Below target | 25 | Investigating | Unknown | 2027-04-04 |
| ADV-004 | T1 | $8,800 | $6,688 | Immediate attention | Below target | 47 | Open | Low | 2027-02-03 |
| ADV-005 | T1 | $8,250 | $7,178 | Healthy / stable | On target | 2 | None | Medium | 2027-02-18 |
| ADV-006 | T1 | $9,300 | $9,951 | Growth opportunity | Above target | 12 | None | High | 2027-02-03 |
| ADV-007 | T1 | $8,250 | $5,775 | Performance concern | Below target | 26 | None | Unknown | 2027-02-18 |
| ADV-008 | T2 | $6,850 | $6,508 | Healthy / stable | On target | 9 | None | Low | 2027-10-31 |
| ADV-009 | T2 | $6,150 | $5,228 | Immediate attention | Below target | 12 | Open | Low | 2027-03-05 |
| ADV-010 | T2 | $6,600 | $6,336 | Healthy / stable | On target | 8 | None | Medium | 2027-09-01 |
| ADV-011 | T2 | $6,600 | $5,742 | Healthy / stable | On target | 22 | None | Low | 2027-02-18 |
| ADV-012 | T2 | $6,250 | $5,500 | Engagement concern | Mixed | 19 | None | Unknown | 2027-02-03 |
| ADV-013 | T2 | $6,400 | $5,568 | Growth opportunity | Above target | 4 | None | High | 2027-06-03 |
| ADV-014 | T2 | $6,800 | $5,304 | Immediate attention | Below target | 13 | Open | Low | 2027-02-18 |
| ADV-015 | T2 | $6,150 | $6,888 | Healthy / stable | On target | 26 | None | Medium | 2027-03-05 |
| ADV-016 | T2 | $6,900 | $4,899 | Performance concern | Below target | 17 | Investigating | Unknown | 2027-02-18 |
| ADV-017 | T2 | $6,900 | $6,762 | Healthy / stable | On target | 19 | None | Medium | 2027-02-18 |
| ADV-018 | T3 | $4,400 | $3,300 | Performance concern | Below target | 11 | Investigating | Unknown | 2027-03-05 |
| ADV-019 | T3 | $4,450 | $3,694 | Performance concern | Below target | 9 | None | Unknown | 2027-03-05 |
| ADV-020 | T3 | $4,800 | $3,456 | Performance concern | Below target | 4 | Investigating | Unknown | 2027-02-03 |
| ADV-021 | T3 | $4,300 | $4,171 | Engagement concern | Mixed | 47 | None | Unknown | 2027-04-04 |
| ADV-022 | T3 | $4,800 | $4,608 | Growth opportunity | Above target | 13 | None | High | No fixed renewal date |
| ADV-023 | T3 | $4,750 | $4,418 | Growth opportunity | Above target | 9 | None | High | 2027-06-03 |
| ADV-024 | T3 | $4,400 | $3,036 | Performance concern | Below target | 5 | Investigating | Unknown | 2027-02-18 |
| ADV-025 | T3 | $4,800 | $4,176 | Healthy / stable | On target | 15 | None | Low | 2027-05-04 |
| ADV-026 | T3 | $4,100 | $3,936 | Growth opportunity | Above target | 22 | None | High | 2027-05-04 |
| ADV-027 | T3 | $4,650 | $4,650 | Engagement concern | Mixed | 21 | None | Unknown | 2027-10-31 |
| ADV-028 | T3 | $4,950 | $4,257 | Immediate attention | Below target | 18 | Open | Low | 2027-09-01 |
| ADV-029 | T3 | $4,100 | $3,772 | Healthy / stable | On target | 24 | None | Medium | No fixed renewal date |
| ADV-030 | T3 | $4,300 | $4,773 | Healthy / stable | On target | 14 | None | Medium | 2027-04-04 |
| ADV-031 | T3 | $4,700 | $4,042 | Healthy / stable | On target | 2 | None | Medium | 2027-04-04 |
| ADV-032 | T3 | $4,800 | $3,840 | Growth opportunity | Above target | 20 | None | High | 2027-04-04 |
| ADV-033 | T4 | $2,950 | $2,773 | Growth opportunity | Above target | 12 | None | High | 2027-02-03 |
| ADV-034 | T4 | $2,100 | $1,911 | Healthy / stable | On target | 4 | None | Low | 2027-02-03 |
| ADV-035 | T4 | $2,050 | $1,742 | Growth opportunity | Above target | 26 | None | High | 2027-10-31 |
| ADV-036 | T4 | $2,400 | $1,536 | Performance concern | Below target | 24 | None | Unknown | 2027-10-31 |
| ADV-037 | T4 | $2,150 | $1,806 | Healthy / stable | On target | 18 | None | Low | No fixed renewal date |
| ADV-038 | T4 | $2,150 | $2,086 | Engagement concern | Mixed | 47 | None | Unknown | 2027-03-05 |
| ADV-039 | T4 | $2,850 | $2,878 | Healthy / stable | On target | 8 | None | Low | 2027-06-03 |
| ADV-040 | T4 | $2,050 | $1,845 | Healthy / stable | On target | 24 | None | Medium | 2027-05-04 |
| ADV-041 | T5 | $300 | $312 | Growth opportunity | Above target | 24 | None | High | 2027-10-31 |
| ADV-042 | T5 | $750 | $705 | Healthy / stable | On target | 22 | None | Low | 2027-03-05 |
| ADV-043 | T5 | $100 | $102 | Engagement concern | Mixed | 48 | None | Unknown | 2027-03-20 |
| ADV-044 | T5 | $1,000 | $900 | Healthy / stable | On target | 3 | None | Medium | 2027-02-18 |
| ADV-045 | T5 | $50 | $48 | Healthy / stable | On target | 20 | None | Medium | 2027-03-20 |
| ADV-046 | T5 | $500 | $510 | Healthy / stable | On target | 9 | None | Low | 2027-04-04 |
| ADV-047 | T5 | $550 | $434 | Healthy / stable | On target | 15 | None | Medium | 2027-02-18 |
| ADV-048 | T5 | $200 | $182 | Healthy / stable | On target | 26 | None | Low | 2027-02-18 |
| ADV-049 | T5 | $0 | $0 | Healthy / stable | On target | 7 | None | Low | 2027-10-31 |
| ADV-050 | T5 | $500 | $415 | Healthy / stable | On target | 1 | None | Medium | 2027-07-03 |

## How these inputs influence the roadmap

The model does not simply work from T1 down to T5. It weighs **budget exposure, account concerns, campaign performance, relationship gaps, upcoming reviews, and expansion potential** differently as the 13-week strategy progresses. High-risk or high-impact accounts receive extra strategic attention when relevant; other accounts continue to receive routine service.

Growth candidates are **hypotheses**, not guaranteed opportunities. Week 9 discovery candidates only move into Week 10 commercial discussions if live client and performance evidence supports that decision.

## What the final roadmap produces

- **13 weekly strategic objectives**, with a tangible deliverable and realistic time budget for each week.
- **26 hours/week** for strategic priorities, **10 hours** for recurring operations, and **4 hours** protected for contingency (40 total).
- **Five strategic account spotlights per week**, for **65 spotlight appearances** across **25 unique accounts**.
- A closing strategic attention audit and the three monthly recommendations shown above.

**Important limitation:** This is a frozen, synthetic starting point. It does not simulate completed tasks, client replies, renewals, churn, increased budgets, or business outcomes. In real use, an AM would recheck CRM and campaign evidence each week and adjust the priorities accordingly.
