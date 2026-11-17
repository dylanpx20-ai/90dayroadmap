# Results: From Task Bloat to a 90-Day Account Management Strategy
## The problem I was trying to solve
#vOne of the biggest questions in Account Management is "How will you prioritize?"

It's easy to answer in an interview with something like focus on the highest-value accounts and address urgent issues first. It's much harder when you actually inherit 50 advertiser accounts, all with different budgets, client relationships, campaign performance, open issues, and growth potential—and you still only have 40 hours in a week.

I built this project to see whether Python could help structure that decision. The scenario is a newly assigned Ad-Tech Account Manager inheriting 50 accounts representing $215,850 in monthly advertiser budgets, with 13 weeks to establish control of the portfolio, protect retention, and identify credible opportunities for growth.

This was different from my Monte Carlo project. A simulation is largely about defining inputs, modeling uncertainty, and interpreting numerical outputs. Here, the hard part was deciding what a useful output should look like when the subject is human judgment, competing responsibilities, and client relationships.
Where I started: a schedule that tried to do everything
My first approach was to break Account Management into individual tasks and fit them into a 13-week, 40-hour schedule.

On paper, that seemed reasonable. If the model could assign enough time to every activity, it should produce a workable plan.

It didn't.

In V1, the script allocated all 520 available hours and still left 77.5 hours of tasks backlogged. Only 2 of 13 weekly objectives were met by the schedule. The result was detailed, but it was also overloaded and difficult to use.

In V2, I improved the scheduling logic enough to reduce the backlog to just 0.5 hours. That looked like a major numerical improvement—until I looked at what the plan was actually doing. Important objectives still fell through the cracks, including client introductions, growth qualification, and commercial follow-up.

That was the turning point.

A schedule can be almost perfectly filled and still be a poor strategy. I was optimizing how much work fit into the calendar instead of deciding which work mattered most.
Changing the question: from tasks to priorities
For V3, I stopped trying to generate a giant to-do list and rebuilt the project around a 13-week strategic roadmap.

Instead of asking, "What should the AM do every hour?", the model now asked:
What should the AM focus on this week, which accounts deserve additional attention, and why?

Each week received a primary objective, a tangible deliverable, an allocation of time, and a shortlist of accounts worth a closer look. The model also reserved time for recurring operations and unexpected issues, rather than pretending that all 40 hours could be spent on planned strategic work.

That made the output much easier to follow. But moving from task scheduling to strategic planning revealed a new set of problems.
Making the recommendations realistic
The next challenge was ensuring that the model's account choices made business sense—not just mathematical sense.

V3 → V4: Better business rules, too much repetition. I introduced phase-specific scoring, growth eligibility checks, and a portfolio snapshot. Growth weeks would no longer automatically prioritize accounts with serious baseline performance or risk concerns. However, one high-risk account appeared in 11 of the 13 weekly spotlight lists. The scoring was consistent, but it was crowding out other priorities.

V4 → V5: Rotation helped, then went too far. I added account history so the model could avoid selecting the same accounts repeatedly. That reduced repetition, but sometimes pushed very small accounts into strategic spotlights mainly because they hadn't appeared recently. It also disrupted continuity: the five growth candidates selected in Week 9 were completely different from those in Week 10. The model was spreading attention more evenly, but not necessarily more intelligently.

V5 → V6: Business importance came first. I adjusted the selection logic so phase relevance, account risk, budget exposure, and commercial milestones mattered more than rotation. I also connected Week 9 growth discovery to Week 10 commercial follow-up. Candidates could carry forward, but only conditionally—real campaign and client evidence would still need to justify a proposal.

V6 → V7: Strategic attention isn't the same as client service. I clarified the fictional tier-based response policy, separated routine service from the weekly account spotlights, and corrected the final audit so it counted only accounts actually selected. An account not appearing in a spotlight list still needs appropriate support and relationship coverage.

V7 → V8 and final cleanup: Make the strategy explainable. By this point, the weekly model was much more credible, but the final output still read mainly as 13 individual weeks. I added one major recommendation for each month and replaced approximate day ranges with Month 1, Month 2, and Month 3 labels. The final cleanup changed the presentation, not the underlying prioritization logic.

The biggest lesson from these iterations was that good prioritization is not the same as doing the most tasks, ranking everything by budget, or giving every account equal attention.
Where I ended up: three clear monthly priorities
The final script still produces a complete 13-week roadmap, but its overall direction can be explained in three recommendations.
Month 1 — Establish control of the book (Weeks 1–4)
Understand the portfolio before trying to optimize everything.

Audit all 50 accounts, establish ownership and contact coverage, identify performance issues and upcoming milestones, and create risk-ranked account plans. The goal is to know where attention is needed and why.
Month 2 — Protect retention and campaign delivery (Weeks 5–8)
Address material problems and protect existing relationships.

Focus on meaningful campaign issues, account concerns, and upcoming reviews. Reassess priorities using current evidence rather than assuming the original risk picture is still accurate.
Month 3 — Qualify growth and prepare the next-quarter plan (Weeks 9–13)
Pursue growth where the evidence supports it.

Identify accounts with healthy delivery and plausible expansion potential, carry qualified opportunities into commercial conversations, and build the next-quarter plan around observed spend, unresolved risks, and realistic assumptions.

This is a much simpler message than the original task-by-task schedule: understand the book, protect the business, then pursue qualified growth.
Final model: what the output actually shows
Measure	Final result
Inherited advertiser accounts	50
Monthly advertiser budgets	$215,850
Planning horizon	13 weeks
Weekly capacity	40 hours
Total nominal capacity	520 hours
Strategic priorities per week	26 hours
Recurring operations per week	10 hours
Protected contingency per week	4 hours
Strategic account spotlight appearances	65
Unique accounts spotlighted	25
Maximum spotlight appearances for one account	6


Every week includes a primary aim, a deliverable to verify, five recommended account spotlights with reasons, time allocations, and an explicit trade-off.

Why were only 25 of 50 accounts spotlighted? Because a spotlight means additional strategic attention, not basic service eligibility. The other accounts still require appropriate coverage. The model deliberately prioritizes commercial materiality, account health, relationship gaps, and timing rather than forcing equal representation.
How this could help in the real world
In Account Management, it's easy to become reactive—working on whichever email, client request, or campaign issue feels most urgent that day. A week-by-week roadmap gives an AM a more proactive way to manage their book. It creates space for foundational account reviews, relationship building, retention work, and growth planning while still leaving capacity for routine service and unexpected problems. The point isn't to follow a script blindly; it's to have a clear direction so spontaneous daily demands don't quietly replace the bigger priorities.
What the model doesn't claim
This is a planning framework, not a simulation of completed work or business results.

The account data is synthetic, and the baseline signals remain frozen. The script cannot know whether a client responded, an issue was resolved, a renewal closed, or a growth opportunity converted. Its weekly recommendations would need to be checked against actual CRM notes, campaign performance, client feedback, and current commercial priorities before anyone acted on them.

The $215,850 figure represents monthly advertiser budgets, not actual billed advertising spend or platform revenue. The 520 hours represent available planning capacity, not verified hours worked.
Final takeaway
I started this project thinking a better roadmap meant a more detailed schedule. After several iterations, I reached almost the opposite conclusion.

The useful result wasn't a longer list of tasks. It was a clearer set of decisions.

Python helped me organize the competing signals and make the trade-offs visible. But it couldn't—and shouldn't—pretend to replace the judgment required to manage real clients. For me, that's what made this project different, and what made the final version more useful than the first.
