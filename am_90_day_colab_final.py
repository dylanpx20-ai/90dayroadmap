"""90-day strategic roadmap V7 for a newly assigned ad-tech Account Manager.
Paste this entire file into ONE Google Colab cell and run it.
Standard library only. No uploads, downloads, command-line arguments, or files created.

This is a PLANNING model, not a simulation of client decisions or task completion.
All account data and events are synthetic. Monthly budget != billed spend != platform revenue.
"""
import base64
import collections
import csv
import datetime as dt
import io
import math
import zlib

# Exact synthetic portfolio and illustrative event schedule from earlier versions,
# embedded so Colab does not need external CSV files.
ACCOUNTS_B64 = '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'
EVENTS_B64 = 'eNq9lk1T2zAQhu+d4T/oSGc2RZJtnExPDOGQC6d+nIW9JJooktGHgX/fdRKnOZQStcBNB+t5te++K3muIsJPxDVcNY1LNrLFHL5p9HDTo4203CBrXIjsfPUZFjai7zxGFbWzZ58kl/WEiwkvQcDV/MeEc0Gra7XplF5a1qLRPfpnpkNICOJLBQtjUoieAD0y5b3ulfnKXIqNI6Vk19Y9HpMvR7IsoIBro+lU9JnqlTbqziC7YBvEqO2SeQzNCttksKVNuULTUUjUIOHmqVM2UJFMDzVjiPlIURBoiyw5lPDd4lOHTcSW3aV2iZF1KgUkgYek/TPwfHdENSpUHKqXfc/mzsjrnevyt+seHxIZEViH/t75jbINMqrJKLvNQ76OrMmXXW4q2v0H02UeUg5RrPbIgpCvmZ7Pr0b+NidvzhccLvfnn9LukwOfLyRHITnLmazsmJJUDfWR1GueiWz+9MCv3i+uBbUcZke9ucVHFqJa48qZFv0QWu/a1GzhMhsuR/hxEe/Qj2LI8F6qHKbl9Es1X4pSRoneaQ2T81fP/qEUipYQH9F7uhIPQiJDKDsHdOOK8dkQ5NgbTwsJlAcBqkiebll+dwr6G9g/JMWUrvqXHqhMk8phWEawKP/zuf4Ffrz+cg=='

def decode_csv(encoded):
    return list(csv.DictReader(io.StringIO(zlib.decompress(base64.b64decode(encoded)).decode('utf-8-sig'))))

ACCOUNTS = decode_csv(ACCOUNTS_B64)
EVENTS = decode_csv(EVENTS_B64)
START = dt.date(2027, 1, 4)  # illustrative Monday; change to customize the calendar
WEEKLY_CAPACITY = 40
OPERATIONS = 10  # standing meetings, CRM, reporting, email, internal coordination
CONTINGENCY = 4  # protected for unpredictable work, not assumed to be consumed
STRATEGIC = WEEKLY_CAPACITY - OPERATIONS - CONTINGENCY

PHASES = [
    ('Understand the inherited book', 'Portfolio understanding', 'Audit all 50 account records; map budget concentration, performance signals, key contacts, open issues and review dates.', 'Complete a 50-account desk audit and a ranked exception register.'),
    ('Establish client relationships', 'Introductions and coverage', 'Introduce the new account owner to priority contacts; schedule remaining introductions and confirm contact preferences.', 'Send priority introductions; assign every account a relationship owner and appropriate cadence.'),
    ('Assess campaign health', 'Campaign diagnostics', 'Review spend pacing versus budget, campaign performance, delivery blockers and measurement gaps.', 'Produce a performance exception list with proposed owners and next checks.'),
    ('Create account strategies', 'Account planning', 'Segment accounts by commercial exposure, health, review urgency and opportunity—not by tier alone.', 'Document risk-based plans for priority accounts and lighter-touch plans for the rest.'),
    ('Stabilize at-risk accounts', 'Risk response', 'Progress open issues from diagnosis to action, owner, checkpoint and escalation criteria.', 'Agree on internal action plans and client follow-up dates for material concerns.'),
    ('Improve campaign delivery', 'Performance improvement', 'Coordinate fixes for underdelivery and performance issues; verify whether changes are measurable.', 'Record optimization hypotheses, responsible teams and next measurement dates.'),
    ('Protect retention', 'Commercial continuity', 'Prepare for upcoming account reviews and contractual renewals where applicable; confirm client objectives.', 'Create a milestone tracker and clear next steps for upcoming commercial reviews.'),
    ('Reassess portfolio priorities', 'Midpoint review', 'Revisit the original risk map, coverage plan, capacity use and unresolved blockers.', 'Publish an updated priority register and second-half coverage plan.'),
    ('Qualify growth opportunities', 'Expansion discovery', 'Identify accounts with healthy delivery, room to scale and a plausible business case for more budget.', 'Shortlist qualified growth hypotheses; distinguish interest from committed spend.'),
    ('Advance commercial conversations', 'Expansion conversations', 'Use performance evidence and client goals to frame specific proposals and follow-ups.', 'Progress qualified conversations and record decisions still pending.'),
    ('Strengthen relationship coverage', 'Stakeholder alignment', 'Close important contact gaps, confirm decision makers and check unresolved expectations.', 'Refresh stakeholder maps and identify remaining relationship gaps.'),
    ('Forecast the next quarter', 'Spend outlook', 'Create a range-based outlook for advertiser spend using observed pacing and explicit assumptions.', 'Produce base/downside/upside spend scenarios and an assumptions log.'),
    ('Deliver the 90-day business review', 'Next-quarter planning', 'Summarize book understanding, actions recommended, unresolved exposure and growth pipeline.', 'Present a 90-day business review and prioritized next-quarter operating plan.'),
]

# Proactive 26-hour allocations. These are strategic capacity GUIDELINES, not a claim
# that meetings took place or clients responded. Operations and contingency add to 40.
ALLOCATION = [
    {'Portfolio analysis': 15, 'Client relationships': 5, 'Risk & performance': 4, 'Commercial milestones': 2},
    {'Client relationships': 14, 'Portfolio analysis': 4, 'Risk & performance': 5, 'Commercial milestones': 3},
    {'Campaign diagnostics': 14, 'Client relationships': 4, 'Risk & performance': 5, 'Commercial milestones': 3},
    {'Account planning': 14, 'Client relationships': 4, 'Risk & performance': 5, 'Commercial milestones': 3},
    {'Risk resolution': 13, 'Campaign oversight': 6, 'Client relationships': 4, 'Commercial milestones': 3},
    {'Campaign optimization': 13, 'Risk resolution': 5, 'Client relationships': 4, 'Commercial milestones': 4},
    {'Reviews & retention': 13, 'Risk & performance': 6, 'Client relationships': 4, 'Portfolio planning': 3},
    {'Portfolio reassessment': 12, 'Risk & performance': 6, 'Client relationships': 4, 'Commercial milestones': 4},
    {'Growth qualification': 11, 'Risk & performance': 5, 'Client relationships': 5, 'Commercial milestones': 5},
    {'Commercial conversations': 12, 'Risk & performance': 5, 'Client relationships': 5, 'Portfolio planning': 4},
    {'Relationship coverage': 12, 'Risk & performance': 5, 'Commercial milestones': 5, 'Portfolio planning': 4},
    {'Spend forecasting': 13, 'Commercial milestones': 5, 'Risk & performance': 5, 'Client relationships': 3},
    {'Business review & next quarter': 14, 'Risk & performance': 4, 'Client relationships': 4, 'Commercial milestones': 4},
]
assert all(sum(x.values()) == STRATEGIC for x in ALLOCATION)

for a in ACCOUNTS:
    a['budget'] = int(float(a['Monthly budget ($)']))
    a['spend'] = float(a['Illustrative current monthly spend ($)'])
    a['tier'] = int(a['Tier'])
    a['days_since'] = int(float(a['Days since meaningful contact']))
    try:
        a['review_date'] = dt.date.fromisoformat(a['Renewal / review date'])
    except ValueError:
        a['review_date'] = None


# All scores use only the initial synthetic portfolio snapshot. No assumed
# progress, changing client sentiment, future decisions or inferred renewals.
# Weeks are recommendations conditional on rechecking the real CRM each Monday.
TIERS = {1:(7,8000,10000),2:(10,6000,7000),3:(15,4000,5000),4:(8,2000,3000),5:(10,0,1000)}

# FICTIONAL SERVICE POLICY, not a contractual SLA or a universal industry standard.
# Targets are ELAPSED CLOCK HOURS, including nights, weekends and holidays:
# 24 hours means one calendar day, not three eight-hour business days.
# The clock starts at documented receipt/assignment and measures first meaningful
# response, not resolution. A company adopting these targets must arrange coverage
# or on-call handoff outside ordinary AM working hours. No live tickets are modeled.
SERVICE_POLICY = {
    1: ('AM-owned', 24), 2: ('AM-owned', 24),
    3: ('AM-owned', 48), 4: ('AM-owned / Support-assisted', 48),
    5: ('Support-first for routine issues', None),
}

def service_route(tier, critical=False, commercial=False, support_escalated=False):
    """Return routing policy, not a claim that a ticket exists or was answered."""
    if critical:
        return 'URGENT: immediate triage/escalation regardless of tier; use incident policy'
    if tier == 5:
        if commercial or support_escalated:
            return 'AM escalation: commercial decision or unresolved Support escalation'
        return 'Support-first: routine ticket; AM monitors escalations'
    owner, target = SERVICE_POLICY[tier]
    return '%s; first meaningful response within %d elapsed hours' % (owner, target)

# An illustrative tier-5 issue without verified severity stays with Support.
# The frozen portfolio contains no verified incident severity or actual ticket clock.
def strategic_eligible_service(a, focus, sig):
    if a['tier'] != 5:
        return True
    # Commercial strategy may include a small account if there is a plausible
    # business case, but a routine issue does not become an AM spotlight.
    if focus in ('Expansion discovery', 'Expansion conversations'):
        return sig['ready']
    # No fabricated critical escalations: T5 routine risk, pacing and contact
    # flags do not by themselves qualify for a strategic AM spotlight.
    return False


def signals(a, monday):
    condition = a['Starting condition'].lower()
    issue = a['Open issue'].strip().lower()
    performance = a['Campaign performance'].lower()
    expansion = a['Expansion potential'].lower()
    ratio = a['spend'] / a['budget'] if a['budget'] else 0
    days_to = (a['review_date'] - monday).days if a['review_date'] else None
    risk = ('concern' in condition or 'urgent' in condition or 'immediate' in condition
            or issue not in ('', 'none', 'closed', 'n/a'))
    poor_delivery = ('below' in performance or 'under' in performance or ratio < .85)
    contact_gap = a['days_since'] >= 25 or a['Client responsiveness'].lower() in ('unresponsive', 'slow')
    # An opportunity is a hypothesis, never a confirmed expansion. A poor-performing
    # account is not considered ready for a commercial proposal without validation.
    growth_signal = expansion in ('high', 'medium')
    ready_for_discovery = growth_signal and not risk and not poor_delivery
    imminent = days_to is not None and 0 <= days_to <= 30
    return dict(risk=risk, poor=poor_delivery, gap=contact_gap,
                growth=growth_signal, ready=ready_for_discovery,
                days_to=days_to, imminent=imminent, ratio=ratio)

def phase_score(a, week, focus):
    monday = START + dt.timedelta(weeks=week-1)
    s = signals(a, monday)
    exposure = 3.0 * a['budget']/10000
    risk, poor, gap = int(s['risk']), int(s['poor']), int(s['gap'])
    due = s['days_to']
    milestone = 4 if due is not None and 0 <= due <= 14 else 2 if due is not None and 14 < due <= 45 else 0
    # Account value is a tie-breaker, not an excuse to neglect small urgent accounts.
    if focus == 'Portfolio understanding': return 7*risk + 4*poor + 4*gap + milestone + exposure
    if focus == 'Introductions and coverage': return 8*gap + 3*risk + milestone + exposure
    if focus in ('Campaign diagnostics','Performance improvement'): return 9*poor + 3*risk + milestone + exposure
    if focus == 'Account planning': return 5*risk + 4*poor + 3*gap + milestone + exposure
    if focus == 'Risk response': return 12*risk + 3*poor + milestone + exposure
    if focus == 'Commercial continuity': return 9*int(s['imminent']) + 4*risk + 2*poor + exposure
    if focus == 'Midpoint review': return 5*risk + 4*gap + 3*poor + milestone + exposure
    if focus in ('Expansion discovery','Expansion conversations'):
        if not s['ready']:
            return None  # Ineligible for growth shortlist; consider for risk work separately
        high = a['Expansion potential'].lower() == 'high'
        return 12 + (5 if high else 2) + min(s['ratio'],1.25)*3 + exposure
    if focus == 'Stakeholder alignment': return 12*gap + 2*risk + exposure
    if focus == 'Spend outlook': return 4*poor + 4*risk + milestone + exposure*3
    return 4*risk + 3*poor + 3*gap + milestone + exposure*2

def priority_reasons(a, week, focus):
    s = signals(a, START + dt.timedelta(weeks=week-1))
    r = []
    if focus in ('Expansion discovery','Expansion conversations'):
        r.append(a['Expansion potential'].lower()+' expansion hypothesis (unconfirmed)')
        r.append('no baseline risk/underdelivery flag')
        r.append('verify business case and client interest')
    elif focus == 'Stakeholder alignment':
        if s['gap']: r.append('historical stakeholder/contact gap')
        if s['risk']: r.append('baseline account concern')
    else:
        if s['risk']: r.append('baseline account concern/open issue')
        if s['poor']: r.append('baseline campaign/pacing exception')
        if s['gap']: r.append('historical contact gap')
        if s['imminent']: r.append('review milestone in %d days (verify type)' % s['days_to'])
    if not r: r.append('managed budget exposure and appropriate account coverage')
    return '; '.join(r[:3])

def recommended_action(a, focus):
    if focus == 'Portfolio understanding': return 'Desk-audit account record; record exceptions and owner'
    if focus == 'Introductions and coverage': return 'Confirm stakeholders, introduce ownership and agree on cadence'
    if focus == 'Campaign diagnostics': return 'Validate pacing against budget and document any delivery exception'
    if focus == 'Account planning': return 'Set risk-based account objective, contact cadence and next checkpoint'
    if focus == 'Risk response': return 'Confirm issue status; assign action, owner, follow-up and escalation threshold'
    if focus == 'Performance improvement': return 'Validate root cause with campaign team; agree measurement checkpoint'
    if focus == 'Commercial continuity': return 'Confirm milestone type, client objective and decision timeline'
    if focus == 'Midpoint review': return 'Check actual CRM progress and re-rank based on new evidence'
    if focus == 'Expansion discovery': return 'Validate capacity to scale, client goals and evidence for budget growth'
    if focus == 'Expansion conversations': return 'Only if qualified: discuss evidence-led proposal and capture next step'
    if focus == 'Stakeholder alignment': return 'Verify decision maker and close relationship coverage gap'
    if focus == 'Spend outlook': return 'Compare budget to actual billed spend if available; document assumptions'
    return 'Update next-quarter account priorities, owners and unresolved decisions'

def print_portfolio_snapshot():
    total = sum(a['budget'] for a in ACCOUNTS)
    baseline = [signals(a,START) for a in ACCOUNTS]
    print('BASELINE PORTFOLIO SNAPSHOT (categories overlap; no outcomes inferred)')
    for tier,(count,lo,hi) in TIERS.items():
        aa = [a for a in ACCOUNTS if a['tier']==tier]
        assert len(aa)==count and all(lo <= a['budget'] <= hi for a in aa)
        print('  Tier %d: %2d accounts | $%s/mo budgets' % (tier,len(aa),format(sum(a['budget'] for a in aa),',')))
    for label, key in [('Account concerns/open issues','risk'),('Campaign/pacing exceptions','poor'),('Historical contact gaps','gap'),('Growth potential flags','growth'),('Initial growth discovery candidates','ready')]:
        print('  %-38s %2d accounts' % (label, sum(s[key] for s in baseline)))
    print('  Total monthly advertiser budgets: $%s (not billed spend or net revenue)' % format(total,','))
    print('  Baseline is frozen. Re-check signals with actual CRM/campaign evidence each week.')
    print()


# STRATEGIC SPOTLIGHT POLICY
# A spotlight is NOT the full set of accounts receiving ordinary service.
# Selection history records recommendations, not work completed or client responses.
# Eligibility is phase-specific; exposure matters, but does not trump phase fit.
# Repeated spotlights carry an opportunity cost. Genuine time-critical milestones
# can override the rotation penalty in the commercial-continuity phase;
# this is a scheduling priority, NOT evidence of a contractual renewal or crisis.

def phase_eligible(a, week, focus):
    sig = signals(a, START + dt.timedelta(weeks=week-1))
    if not strategic_eligible_service(a, focus, sig):
        return False
    if focus in ('Expansion discovery', 'Expansion conversations'):
        return sig['ready']
    if focus in ('Campaign diagnostics', 'Performance improvement'):
        return sig['poor']
    if focus == 'Risk response':
        return sig['risk']
    if focus == 'Introductions and coverage':
        return sig['gap'] or sig['risk']
    if focus == 'Stakeholder alignment':
        return sig['gap']
    if focus == 'Commercial continuity':
        due = sig['days_to']
        return (due is not None and 0 <= due <= 45) or sig['risk']
    if focus == 'Spend outlook':
        return sig['poor'] or sig['risk'] or a['budget'] >= 6000
    return True

def time_critical(a, week, focus):
    sig = signals(a, START + dt.timedelta(weeks=week-1))
    due = sig['days_to']
    return focus == 'Commercial continuity' and due is not None and 0 <= due <= 7

def select_spotlights(week, focus, history, previous_growth=None, limit=5):
    """Phase fit and business impact first; rotation only resolves close calls.

    Week 10 follows Week 9 discovery candidates conditionally. Their presence
    is NOT proof of client interest, qualification, or an actual conversation.
    """
    candidates = []
    for a in ACCOUNTS:
        if not phase_eligible(a, week, focus):
            continue
        base = phase_score(a, week, focus)
        if base is None:
            continue
        aid = a['Account ID']
        previous = history.get(aid, [])
        recent = sum(1 for w in previous if week-w <= 3)
        # Moderate rotation adjustment: never let rotation overwhelm a
        # major difference in phase fit or monthly budget exposure.
        penalty = min(7.0, 2.0*recent + 0.9*len(previous))
        override = time_critical(a, week, focus)
        adjusted = base if override else base-penalty
        candidates.append((adjusted, base, override, a))

    candidates.sort(key=lambda x:(-int(x[2]), -x[0], -x[1], -x[3]['budget'], x[3]['Account ID']))

    if focus == 'Expansion conversations' and previous_growth:
        # Commercial continuity takes precedence over rotation. Carry forward
        # the previous week's discovery shortlist, pending LIVE qualification.
        by_id = {a['Account ID']: row for row in candidates for a in [row[3]]}
        carried = [by_id[aid] for aid in previous_growth if aid in by_id]
        selected = carried[:limit]
        selected_ids = {row[3]['Account ID'] for row in selected}
        selected += [row for row in candidates if row[3]['Account ID'] not in selected_ids][:limit-len(selected)]
    else:
        selected = candidates[:limit]

    for _,_,_,a in selected:
        history[a['Account ID']].append(week)
    return selected

def roadmap():
    assert len(ACCOUNTS) == 50
    assert collections.Counter(a['tier'] for a in ACCOUNTS) == {1:7,2:10,3:15,4:8,5:10}
    total = sum(a['budget'] for a in ACCOUNTS)
    assert total == 215850
    history = collections.defaultdict(list)
    growth_discovery_ids = []
    print('='*91)
    print('FIRST 90 DAYS | NEWLY ASSIGNED AD-TECH ACCOUNT MANAGER | STRATEGIC ROADMAP V8')
    print('='*91)
    print('50 inherited accounts | $%s/mo advertiser budgets | 13 weeks | 40h/week' % format(total,','))
    print('26h strategic priorities + 10h recurring operations + 4h protected contingency.')
    print('This is a baseline planning roadmap, NOT a simulation of completed work.')
    print('Budget != billed advertising spend != platform net revenue.')
    print('SPOTLIGHT RULE: phase fit + business impact first; light rotation as tie-breaker.')
    print('A spotlight is extra strategic attention, not a limit on routine client service.')
    print('SERVICE: T1-2 first response within 24 elapsed hours; T3-4 within 48 elapsed hours.')
    print('T5 routine issues go to Support first; severe incidents override tier routing.')
    print('Response target is first meaningful acknowledgement, NOT resolution.')
    print('Synthetic signals stay frozen; review and re-rank from real CRM data every Monday.')
    print()
    print_portfolio_snapshot()
    print('FICTIONAL SERVICE RESPONSE POLICY (no live tickets or response times modeled)')
    for tier in TIERS:
        print('  T%d: %s' % (tier, service_route(tier)))
    print('  SEVERITY OVERRIDE: critical outage or urgent contractual issue -> immediate triage.')
    print('  Clock starts at documented receipt/assignment; nights/weekends/holidays count.')
    print('  Meeting these targets outside AM hours requires designated team/on-call coverage.')
    print('  Routine Support work and AM first responses are handled within recurring operations;')
    print('  if actual demand exceeds 10h, reallocate capacity and record the trade-off.')
    print()
    for week,(goal,focus,aim,deliverable) in enumerate(PHASES,1):
        monday=START+dt.timedelta(weeks=week-1)
        selected=select_spotlights(week,focus,history,previous_growth=growth_discovery_ids)
        if week == 9:
            growth_discovery_ids = [a['Account ID'] for _,_,_,a in selected]
        print('-'*91)
        print('WEEK %02d | %s | %s' % (week,monday,goal.upper()))
        print('PRIMARY AIM: '+aim)
        print('DELIVERABLE TO VERIFY: '+deliverable)
        print('STRATEGIC TIME BUDGET (planning guidance, not hours worked):')
        for label,hours in ALLOCATION[week-1].items():
            print('  %-31s %2dh' % (label,hours))
        print('  %-31s %2dh' % ('Recurring operations',OPERATIONS))
        print('  %-31s %2dh' % ('Protected contingency',CONTINGENCY))
        print('STRATEGIC ACCOUNT SPOTLIGHTS (separate from routine service and ticket response):')
        if not selected:
            print('  No baseline accounts match this phase; check live CRM evidence.')
        for adjusted,base,override,a in selected:
            aid=a['Account ID']
            earlier=history[aid][:-1]
            note=('W9 DISCOVERY CARRY-FORWARD (conditional)' if week==10 and aid in growth_discovery_ids else
                  ('UPCOMING REVIEW PRIORITY: %d day(s) to milestone; verify type' % signals(a,monday)['days_to']) if override else
                  'new spotlight' if not earlier else
                  'returning spotlight; prior week(s): '+', '.join(map(str,earlier)))
            print('  %s | T%d | $%s/mo | %s' % (aid,a['tier'],format(a['budget'],','),note))
            print('     WHY: '+priority_reasons(a,week,focus))
            print('     NEXT: '+recommended_action(a,focus))
        if selected:
            exposed=sum(a['budget'] for _,_,_,a in selected)
            print('SPOTLIGHT BUDGET EXPOSURE: $%s/mo (%.1f%% of book; not revenue)' % (format(exposed,','),100*exposed/total))
        if week in (1,2):
            trade='Complete book-wide foundations; spotlight rotation never replaces coverage of all 50 accounts.'
        elif week in (5,6,7):
            trade='Handle material risks and near-term reviews; other open issues remain in recurring coverage.'
        elif week in (9,10):
            trade='Protect growth discovery; a baseline candidate needs live qualification before a proposal.'
        elif week==11:
            trade='Validate unresolved contact gaps before outreach; avoid duplicating earlier introductions.'
        elif week==12:
            trade='Forecast billed spend only with observed spend data; otherwise document data gaps and scenarios.'
        else:
            trade='Use live evidence to change priorities; do not treat prior spotlight as work completed.'
        print('TRADE-OFF: '+trade)
        if week==1: print('BOOK-WIDE: desk-audit ALL 50 account records, not just the spotlights.')
        if week==2: print('BOOK-WIDE: establish an introduction/cadence plan for ALL 50, not 50 live meetings.')
        if week==8: print('MIDPOINT: verify actual CRM progress; this frozen example cannot know which issues closed.')
        if week==9: print('GROWTH GATE: discovery candidates require live client and performance validation.')
        if week==10: print('CONTINUITY GATE: carry forward W9 discovery candidates ONLY IF qualified by live evidence;')
        if week==10: print('                 otherwise return to discovery or substitute another eligible candidate.')
        if week==13: print('END CHECK: report only actual observed outcomes, never model-assumed success.')
        print()
    counts=collections.Counter({aid:len(weeks) for aid,weeks in history.items() if weeks})
    assert sum(counts.values()) == 65
    assert sum(1 for v in counts.values() if v > 0) == len(counts)
    print('='*91)
    print('90-DAY STRATEGIC ATTENTION AUDIT (recommendations, NOT client contact or completed work)')
    print('  Unique accounts receiving a spotlight: %d/50' % len(counts))
    print('  Spotlight appearances: %d' % sum(map(len,history.values())))
    print('  Max appearances by any account: %d' % max(counts.values()))
    print('  ADV-014 appearances: %d | weeks: %s' % (len(history.get('ADV-014', [])), ', '.join(map(str,history.get('ADV-014', []))) or 'none'))
    print('  Accounts spotlighted 1x / 2x / 3x / 4x+: %d / %d / %d / %d' % (
        sum(v==1 for v in counts.values()),sum(v==2 for v in counts.values()),
        sum(v==3 for v in counts.values()),sum(v>=4 for v in counts.values())))
    print('  Remaining accounts still receive recurring service and appropriate coverage.')
    print('  Rotation is a minor tie-breaker, not a mandate for 50/50 spotlight coverage.')
    print('  Routine T5 issues: Support-first; urgent incidents and commercial decisions: escalate.')
    print('  Service targets use elapsed hours, NOT business hours; no ticket outcomes simulated.')
    print()
    print('TOP PRIORITY BY MONTH (one major recommendation per month)')
    print('  MONTH 1 | WEEKS 01-04 | ESTABLISH CONTROL OF THE BOOK')
    print('    PRIORITY: Complete the 50-account baseline audit and establish ownership,')
    print('              contact coverage, and risk-ranked account plans before deep optimization.')
    print('  MONTH 2 | WEEKS 05-08 | PROTECT RETENTION AND DELIVERY')
    print('    PRIORITY: Concentrate strategic capacity on material campaign issues and')
    print('              upcoming reviews; verify progress and re-rank using live evidence.')
    print('  MONTH 3 | WEEKS 09-13 | QUALIFY GROWTH AND SET THE NEXT-QUARTER PLAN')
    print('    PRIORITY: Advance only evidence-qualified expansion opportunities and use')
    print('              observed spend and open risks to build a credible next-quarter plan.')
    print('  Month labels are planning phases, not claims of completed work.')
    print('METHOD: phase eligibility + business exposure + mild recency tie-breaker')
    print('        + service routing + commercial continuity from W9 to W10.')
    print('LIMITATIONS: synthetic frozen baseline; no live tickets, response-time results,')
    print('             verified severity, or inferred task completion, client sentiment,')
    print('             trust, churn, renewal, expansion, or causal business outcomes.')
    print('='*91)
    return history

if __name__ == '__main__':
    roadmap()
