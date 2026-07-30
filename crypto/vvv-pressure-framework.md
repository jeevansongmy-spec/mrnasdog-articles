---
title:         "VVV Inflation Analysis · July 2026 · Supply growing, projected to keep growing"
description:   "Venice mints ~0.99M VVV to stakers plus ~0.93M team vesting per 90 days, while its buyback burns only ~69K. Framework +3.89% net; monitor +3.56%. Uncapped and inflationary."
canonical_url: "https://mrnasdog.com/research/vvv/inflation"
tags:          ["crypto", "vvv", "venice", "ai"]
published:     true
---

*Originally published at [mrnasdog.com/research/vvv/inflation](https://mrnasdog.com/research/vvv/inflation)*

**Venice Token (VVV)** is one of the more inflationary tokens the MrNasdog Pressure Framework tracks, and the reason is structural: it has **no supply cap** and mints new VVV every day to stakers. Over the trailing 90 days about **0.99M VVV** was minted and another **0.93M** vested from the team's allocation, roughly **1.92M** reaching the market, against a revenue buyback that burned only about **69K** — around **6%** of the mint. That puts the framework at **+3.89%** net for the trailing window and **+3.28%** forward, after a Jul 1 2026 emission cut to **3M a year**.

## The verdict, in one paragraph

For the 90-day window opening **Jul 31 2026**, the MrNasdog Pressure Framework reads **VVV at +3.28% net** forward, cooling from the **+3.89%** it measured over the trailing 90 days because the emission was cut to **3M VVV a year** on **Jul 1 2026** and that lower rate now carries the whole forward window. Our supply monitor reads **+3.56%** over the trailing window, a gap of just **0.34 percentage points**, inside the framework's 0.5-point tolerance, so no monitor-gap chip is needed. Both the mint and the burn are read directly on-chain from Base, and both sides agree that Venice is still issuing far more than it destroys. VVV is best characterised as **a structurally inflationary, uncapped emission token whose buyback is real but an order of magnitude too small to offset the mint**.

## Sell pressure: where new VVV comes from

Sell #1 — protocol inflation — is the core of the story at about **0.99M VVV** over the trailing 90 days. Venice AI runs an **uncapped** token: new VVV is minted daily and **100%** of the emission is paid to stakers as yield. This is genuine new supply, not an unlock — the raw on-chain total supply on Base is observed rising from **113.50M** to **114.49M** over the window. Venice has cut the emission aggressively, from **14M** a year at the January 2025 launch down through **6M**, **5M** and **4M** to **3M** a year on **Jul 1 2026**. Because that final cut lands inside the trailing window, the framework re-bases the forward projection to the post-cut **3M**-a-year run rate — confirmed on-chain at about **8,294 VVV a day** — which is roughly **0.74M** over the next 90 days.

Sell #2 — vesting unlocks — adds about **0.93M VVV** per 90 days. Venice granted its founding team **10M VVV** at genesis, with **25%** unlocked upfront and the remaining **7.5M** vesting linearly to **Jan 27 2027**. That schedule produces a steady drip of about **0.93M** a quarter, and because the vest ends after the next window closes, the same pace carries forward. No readable on-chain vesting escrow was located this session, so the framework books the published schedule rather than a realised-escrow read.

Sell #3 — foundation and unscheduled unlocks — is **zero** this window, monitored. Sell #4 — long-term locked or bankruptcy — is **zero** permanently: no bankruptcy estate, trustee schedule or court-ordered distribution holds VVV.

## Buy pressure: where new VVV goes

Buy #1 — programmatic buyback — is the only thing pulling VVV out of supply, and over the trailing 90 days it removed about **69K VVV**. Part of Venice's platform revenue buys VVV on the open market and sends it to the burn address on Base permanently; the null-address balance is observed rising from **33.72M** to **33.79M** over the window. The important number is the ratio: that **69K** burn is only about **6%** of the roughly **0.99M** minted in the same window. The burn is ramping — the last 30 days ran near **37K**, and a new API-revenue burn taking **$5 of every $100** of API spend was added on **Jul 18 2026** — so the framework projects the forward burn near **0.11M**, still a fraction of the mint. It is worth flagging that the widely-quoted "**250K a month**" figure is the buyback's dollar budget region, not the amount of VVV actually destroyed, which is far smaller.

Buy #2 — protocol fee burn — is **zero**: there is no separate per-transaction fee burn, and the only destruction path is the revenue buyback above, counted once. Buy #3 — foundation buy — is **zero** as a distinct row, since the company's open-market buying is that same revenue buyback. Buy #4 — new long-term lock — is **zero**: staking VVV earns freshly minted yield rather than locking supply away, and the unstake cooldown is measured in days, not years.

## Foundation and overhang

The team-controlled overhang on Venice is substantial. Beyond the vesting team allocation already counted above, the **Venice.ai** company treasury holds over **30M VVV**, there is a **10M** incentive fund, and the July 2026 **$65M** Series A — which valued Venice at **$1B** — attached a **1.5M VVV** investor grant plus warrants for **5M** more, locked for one year to about **Jul 2027** and then releasing linearly over three years. None of these released off-schedule this window, so each books zero, but all are read every rebuild. If any of these balances leaves its wallet into the market between refreshes, the outflow enters Sell #3 at the next refresh.

## How VVV compares to other uncapped emission tokens

VVV belongs to the uncapped, continuous-emission class — tokens that mint new supply on a policy schedule with no hard ceiling — rather than to the halving-model chains with a fixed cap. A proof-of-work chain like Bitcoin cannot exceed its cap and its issuance falls on a schedule nobody controls; Venice, by contrast, can mint indefinitely and sets the rate itself. What separates Venice from a typical inflationary Layer 1 is that it pairs the emission with a **revenue-funded buyback-and-burn**, which structurally puts it in the same family as an exchange token that burns a slice of fees.

The difference from those exchange tokens is scale. A mature exchange token often burns enough to shrink supply outright; Venice's burn currently offsets only about **6%** of its mint. So while the mechanism is the right one, on today's numbers VVV behaves much more like an ordinary uncapped emission token than like a deflationary buyback token. Its distinguishing feature within the uncapped class is the speed and credibility of its emission cuts — from **14M** to **3M** a year in eighteen months — which is a faster taper than most continuous-emission peers have managed.

The honest reading is that VVV's inflation is fully knowable and, for now, clearly positive. The entire investment question is whether Venice's revenue — growing behind a $1B-valued private-AI business — can scale the buyback fast enough to close a roughly **15-to-1** gap between what is minted and what is burned, while the emission keeps stepping down. Until that happens, the token dilutes.

## What to watch in the next 90 days

Watch the on-chain burn rate at the Venice null address: the buyback is the only lever that can bend the net, and the Jul 18 2026 API-revenue burn should show up as an accelerating burn if API usage is growing. Watch for a fourth emission cut — Venice has cut three times in 2026 and any further step below **3M** a year would directly lower the sell side. Watch the team vest, which keeps adding about **0.93M VVV** a quarter until it ends on **Jan 27 2027**. And watch the Series A overhang — the **1.5M** investor grant unlocks around **Jul 2027**, outside this window but on the horizon.

## Summary

Venice Token is an uncapped, continuously-minted access token whose supply grows because Venice pays **100%** of a daily emission to stakers and the founding team's **7.5M** allocation is still vesting to **Jan 27 2027**. About **1.92M VVV** reached the market over the trailing 90 days against a buyback that burned only about **69K**, leaving the framework at **+3.89%** net trailing and **+3.28%** forward after the Jul 1 2026 cut to **3M** a year. Our supply monitor agrees at **+3.56%**, a **0.34-point** gap well inside tolerance. The mechanism to fix the dilution exists — a revenue buyback-and-burn — but it is currently about a fifteenth of the size it would need to be, so VVV remains structurally inflationary until Venice's revenue scales the burn.

*MrNasdog Pressure Framework analysis of Venice Token (VVV), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 31, 2026.*
