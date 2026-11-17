# 90-Day Account Management Strategy | Ad-Tech Portfolio Prioritization

## Introduction

One of the biggest questions in Account Management is also one of the hardest to answer:

**"How will you prioritize?"**

It's a simple question on the surface, but when you're responsible for 50 advertiser accounts, each with different budgets, relationships, performance issues, and commercial opportunities, the answer gets complicated quickly.

This project was different from my other Python projects.

In my Monte Carlo simulation, the challenge was largely mathematical: define the inputs, model uncertainty, run the simulation, and analyze the outputs. The results could be evaluated against a relatively clear set of numerical assumptions.

This project required a different approach.

I wanted to model something much more human: how a newly assigned Account Manager should approach their first 90 days after inheriting an existing portfolio of advertiser accounts.

An Account Manager can't simply rank every account by revenue potential and work down the list. A high-budget client might have an urgent performance issue. A smaller account might have an upcoming review. A healthy account could represent a meaningful growth opportunity, but pursuing that opportunity too early might come at the expense of a relationship that needs attention.

And all of those decisions have to fit into a 40-hour workweek.

The goal wasn't to create a script that tells an Account Manager exactly what to do every hour. It was to build a realistic strategic framework that balances **retention, account health, client relationships, and growth** while recognizing that priorities change as new information becomes available.

## The Business Scenario

A newly assigned Account Manager has completed product training and shadowing and is now responsible for an inherited portfolio of 50 advertiser accounts.

The portfolio represents **$215,850 in monthly advertiser budgets** across five account tiers.

The challenge is to develop a 13-week strategy that answers:

**Given 50 accounts representing $215,850 in monthly advertising budgets, how should a newly assigned Account Manager structure their first 90 days, working 40 hours per week, to balance revenue retention, account health, client relationships, and growth opportunities?**

## How the Model Works

The Python script uses a synthetic portfolio with different account budgets, campaign health signals, relationship gaps, commercial milestones, and potential expansion opportunities.

Rather than relying on account tier alone, it evaluates accounts according to the priorities of each stage of the 90-day plan.

The model produces:

- A portfolio-level snapshot of account exposure and potential concerns.
- A strategic objective and tangible deliverable for each of the 13 weeks.
- Five recommended account spotlights per week, with explanations for why those accounts deserve additional attention.
- Weekly time allocations totaling 40 hours, including recurring operations and protected contingency.
- A closing audit of how strategic attention was distributed.
- One major management recommendation for each month.

The weekly recommendations are not intended to replace routine client service. All 50 accounts still require appropriate coverage, even when only a smaller group receives additional strategic attention.

## The 90-Day Strategy

| Phase | Primary Focus | Management Priority |
|---|---|---|
| Month 1 — Weeks 1–4 | Understand the inherited portfolio | Establish account ownership, relationship coverage, and risk-ranked plans |
| Month 2 — Weeks 5–8 | Protect retention and campaign delivery | Address material issues, prepare for reviews, and reassess priorities |
| Month 3 — Weeks 9–13 | Qualify growth and plan ahead | Advance evidence-supported opportunities and prepare the next-quarter strategy |

Each week allocates:

- **26 hours** to strategic priorities
- **10 hours** to recurring account operations
- **4 hours** to protected contingency

These are planning allocations, not simulated hours worked.

## What Made This Challenging

The hardest part wasn't generating a list of priorities. It was making sure those priorities made business sense over time.

Early versions of the model were too focused on individual tasks. Later versions introduced strategic phases, but revealed other problems.

Through eight iterations, I refined the model from an overloaded task scheduler into a more realistic 90-day strategic roadmap.

Some accounts appeared too frequently simply because their baseline risk scores were high. Attempts to improve account rotation then created the opposite problem: smaller, lower-impact accounts sometimes received attention mainly because they hadn't appeared recently.

Another challenge was continuity. If an Account Manager identifies promising expansion opportunities in Week 9, those opportunities shouldn't disappear in Week 10 just because the scoring weights change.

Across the development process, I refined the model to account for these trade-offs.

The final version prioritizes business materiality and phase relevance, uses account rotation as a secondary consideration, and carries growth candidates forward conditionally when there is evidence to support further commercial discussion.

This was an important distinction: **good prioritization isn't the same as distributing attention equally.**

## What I Learned

This project reinforced something I learned through working in Account Management: prioritization is not a one-time exercise.

A strong plan needs structure, but it also needs room for judgment.

A model can identify which accounts deserve a closer look based on the information available. It cannot know whether a client has become frustrated, whether an internal issue has been resolved, or whether a growth conversation is genuinely ready to advance unless that information is updated.

That's why the roadmap uses a frozen synthetic baseline and explicitly recommends checking actual CRM and campaign evidence before making weekly decisions.

The script doesn't simulate successful renewals, client satisfaction, increased spend, or completed work. It produces a defensible starting plan.

For me, that was the point of the project: **using Python to support better management decisions, rather than pretending Python can replace the human judgment behind them.**

## Running the Project

The project is designed to run in a single Google Colab cell.

1. Open Google Colab.
2. Create a new notebook.
3. Paste the contents of the Python script into one cell.
4. Run the cell to generate the full 13-week roadmap and strategic attention audit.

The synthetic account data is embedded directly in the script, so no external datasets or additional Python packages are required.

## Limitations

This is a planning model, not a prediction of business outcomes.

The account portfolio is synthetic, the baseline signals do not change automatically, and the script does not simulate real client interactions, incoming support requests, campaign improvements, renewals, or expansion results.

The monthly figures represent advertiser budgets, not actual billed advertising spend or platform revenue.

In a real account management environment, the roadmap would need to be updated continuously using current account data, client feedback, internal team capacity, and changing commercial priorities.
