---
title:         "GRASS Inflation Analysis · August 2026 · Supply growing sharply on monthly unlocks"
description:   "Grass mints nothing — the whole 1B was created at launch — yet the vesting calendar releases ~76.0M GRASS per 90 days against four zero buy rows. Framework +11.61% net; monitor +11.39%."
canonical_url: "https://mrnasdog.com/research/grass/inflation"
tags:          ["crypto", "grass", "solana", "depin"]
published:     true
---

*Originally published at [mrnasdog.com/research/grass/inflation](https://mrnasdog.com/research/grass/inflation)*

# GRASS Inflation Analysis · August 2026 · Supply growing sharply on monthly unlocks

Grass mints nothing. The entire **1B** GRASS supply was created at launch on Solana and the on-chain token still reads **999.99M** — yet the float grows faster than almost anything else in the framework, because the vesting calendar releases about **25.3M GRASS** every month. Over the 90 days to **Aug 10 2026** that is **76.0M GRASS** of scheduled unlocks against a buy ledger that is entirely **zero** — no buyback, no burn, no lock — for a net of **+11.61%** on a **654.6M** circulating supply. Our supply monitor independently reads **+11.39%**, a gap of only **0.22 percentage points**, so the two agree and no data-conflict chip ships. The one thing that changes this picture is a date: **Oct 28 2026**, when the early-investor stream — a quarter of all GRASS — finishes.

## The verdict, in one paragraph

For the 90-day window ending **Aug 10 2026** the MrNasdog Pressure Framework reads **GRASS at +11.61% net**, produced entirely by Sell #2, the vesting unlocks, with every other row on both sides of the ledger sitting at **zero**. Our supply monitor reads the realised change in circulating GRASS at **+11.39%**, so the gap is **0.22 percentage points** — inside tolerance, and **no ⚠ chip ships**. The residual is the published calendar running a little ahead of what physically reached holders, which is normal for a schedule-based row. The framework's label for GRASS is precise and unusual: **a fixed-supply token that inflates by release, not by minting**. Nothing is being created; a very large share of what already exists is simply being handed to the people who were promised it, month after month, into a market with no mechanism at all to absorb it.

## Sell pressure: where new GRASS comes from

Sell #1, protocol inflation, is **zero**, and that is the fact most readers get wrong about Grass. The Grass token is an SPL token on Solana with its full ceiling minted at genesis; the on-chain supply reads **999.99M** against a **1B** cap, the difference being under **7K GRASS** burned in the token's entire life. There is no staking emission, no block reward and no reward inflation. The Grass Foundation went further in July 2026 and moved participant rewards off the token entirely — Stage 2 node-operator rewards are funded from network revenue and paid in a dollar stablecoin, which the Foundation described as introducing zero net new emissions and leaving the circulating supply of GRASS completely unaltered. Running the Grass network, in other words, no longer costs the token anything.

All of the sell pressure is Sell #2, the vesting unlocks, at **76.0M GRASS** over 90 days. Grass allocated **252M** GRASS, a full **25.2%** of supply, to early investors on a one-year cliff followed by a one-year monthly vest, and **220M** — another **22%** — to contributors on a one-year cliff followed by a three-year monthly vest. Both streams began releasing in late October 2025 and pay on the 28th of each month. Each tranche carries roughly **19.4M GRASS** for early investors and **6.0M** for contributors, about **25.3M** a month, and three of those tranches fall inside every 90-day window — **Aug 28 2026**, **Sep 28 2026** and **Oct 28 2026** in the forward window. The contributor stream is roughly **27%** complete, which matches the ten monthly payments made since the cliff and confirms the schedule is running exactly as written.

Sell #3, Foundation and unscheduled unlocks, is **zero** for a bookkeeping reason rather than an absence of movement, and it is worth being explicit about it. The Grass treasury account is the wallet the scheduled allocations are physically paid out of, so its outflows are the same tokens already counted in Sell #2; booking them twice would invent supply that does not exist. Sell #4, long-term locked or bankruptcy, is **zero** because GRASS has no bankruptcy estate, no trustee and no court-ordered distribution anywhere in its history — everything still locked is ordinary vesting.

## Buy pressure: where new GRASS goes

Nowhere, and this is what makes the GRASS reading as heavy as it is. Buy #1, programmatic buyback, is **zero**. Grass is a genuinely revenue-generating network — roughly **$33M** annualised from selling bandwidth and web data to AI buyers — and a governance vote passed on **Jul 7 2026** to route a share of that revenue to GRASS stakers. But the revenue is denominated in a dollar stablecoin and is distributed as one; the vote created a yield, not a bid. No contract buys GRASS on the open market, so a bigger business does not shrink the float by a single token.

Buy #2, protocol fee burn, is **zero**: there is no burn mechanism in the Grass token at all, and the lifetime burn of under **7K GRASS** is a rounding error against a **1B** supply. Buy #3, Foundation buy, is **zero**: the treasury holds about a quarter of the entire supply and has never bought GRASS on the market — its balance has only ever moved down. Buy #4, new long-term lock, is **zero**: GRASS staking exists and pays a stablecoin yield, but it unstakes in **seven days** and staked tokens are still counted as circulating, so it withdraws nothing from the tradable float. Four buy rows, four zeros, and the entire ledger comes down to a release calendar with nothing standing against it.

## Foundation and overhang

The biggest single overhang on GRASS is the treasury account, which held about **259.5M GRASS** at the **Aug 10 2026** refresh — more than a quarter of the total supply in one place, controlled by the same key that controls minting. It is not dormant: it paid out roughly **4.8M** on **May 25 2026**, **13.3M** on **Jun 10 2026**, **4.8M** on **Jun 23 2026** and **4.8M** on **Jul 27 2026**, a near-monthly rhythm that tracks the vesting calendar it funds. Behind it sits the **228M** Foundation and Ecosystem Growth allocation, which vests into that same treasury on a five-year line and is therefore capacity rather than scheduled market supply. The remaining unvested investor and contributor tokens, roughly **86M**, sit in lock contracts and drain on the published schedule already counted in Sell #2.

The framework reads this account on chain at every refresh, and the rule is simple: if the treasury balance falls for any reason other than the published vesting calendar, that outflow enters Sell #3 at the next refresh as genuine new market supply. That is the single thing most likely to make the GRASS reading worse than the calendar suggests, because the treasury alone could double the float. It is also the reason the framework tags this row live rather than dismissing it — a static reserve is only static until the day it is not.

## How GRASS compares to other fixed-supply unlock-driven tokens

GRASS belongs to a class the framework sees constantly and rewards rarely: **fixed-supply tokens whose inflation is a distribution schedule rather than a mint**. Its structural peers are the 2024-vintage Solana and Ethereum launches that shipped a fully-minted cap with roughly half the supply behind cliffs — the DePIN, AI-data and layer-two tokens now working through year-two vesting. Against a proof-of-work chain like Bitcoin, the contrast is stark in both directions. Bitcoin mints new coins forever but only at **+0.20%** a quarter, and it can never surprise anyone, because the mined total equals the circulating total. GRASS mints nothing at all and yet prints **+11.61%** of new tradable float per quarter, because the gap between total supply and circulating supply — currently about **345M GRASS** — is the real emission schedule.

The second comparison is with tokens that have a buy side. An exchange token that burns a share of quarterly profit, or a layer-one that burns base fees, can push net supply negative when usage is strong; those chains convert business performance directly into scarcity. Grass has the business — **$33M** annualised revenue is more than most tokens on the framework earn — but it deliberately routes it around the token, paying node operators and stakers in a dollar stablecoin for regulatory reasons. That is a defensible product decision and a poor supply decision. It means GRASS gets none of the reflexive benefit that a buyback or burn would deliver, while carrying one of the heaviest unlock calendars in the catalog.

The third comparison is with what GRASS itself becomes. Unlock-driven inflation is temporary by construction, which is exactly what separates it from an uncapped continuous-emission chain. A validator-paying layer-one inflates forever unless governance intervenes; GRASS inflates on a calendar that visibly ends. The early-investor stream stops on **Oct 28 2026**, and once it does the monthly release falls to the contributor tranche alone, roughly **6.0M** instead of **25.3M**. On today's float that would take the quarterly reading from **+11.61%** to somewhere near **+2.7%** — still inflationary, but a different asset entirely.

## What to watch in the next 90 days

**Aug 28 2026** and **Sep 28 2026** — the routine monthly tranches, about **25.3M GRASS** each, split roughly **19.4M** to early investors and **6.0M** to contributors. **Oct 28 2026** is the one that matters: the final early-investor tranche, after which a quarter of the supply has fully vested and the monthly release collapses by about three quarters. Watch whether the market front-runs that date or relieves on it.

Watch the treasury balance, currently about **259.5M GRASS**. Any outflow beyond the vesting calendar — an ecosystem grant programme, a market-maker allocation, an exchange deposit — enters Sell #3 at the next refresh and would materially worsen the reading. Watch whether the **Jul 7 2026** revenue-share vote is ever extended from a stablecoin distribution into an actual GRASS buyback; that single change is the only realistic route to a non-zero buy row, and it would move the framework verdict more than anything else on this list. Finally, watch the Stage 2 reward claim window, which closes **Jan 22 2027** — unclaimed rewards are retained, and because they are paid in a stablecoin rather than GRASS, that deadline moves dollars, not supply.

## Summary

The MrNasdog Pressure Framework reads GRASS at **+11.61%** net over the 90 days to **Aug 10 2026**, with our supply monitor at **+11.39%** — a **0.22 percentage point** gap, so the readings agree. The mechanism is unusual and worth stating plainly: Grass creates no new tokens, and every point of that inflation is the vesting calendar moving **76.0M GRASS** from locked allocations into the tradable float, against a buy ledger of four zeros. The key risk is the treasury, which holds about **259.5M GRASS** under a single key and has no published schedule of its own. The ceiling is real — **1B** GRASS, fully minted, never to grow — and the release calendar visibly ends, with the early-investor stream finishing on **Oct 28 2026** and the monthly outflow falling by roughly three quarters the month after.

---

*MrNasdog Pressure Framework analysis of GRASS, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 10 2026.*
