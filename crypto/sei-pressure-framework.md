---
title:         "SEI Inflation Analysis · June 2026 · Supply growing with nothing to take it back"
description:   "Sei issues ~32M SEI/90d staking emission plus ~111M of monthly vesting unlocks, with no buyback or burn. Framework reads +2.1% net; the monitor reads flat."
canonical_url: "https://mrnasdog.com/research/sei/inflation"
tags:          ["crypto", "sei", "layer1", "inflation"]
published:     true
---

*Originally published at [mrnasdog.com/research/sei/inflation](https://mrnasdog.com/research/sei/inflation).*

Sei issues about **32M SEI** of staking emission over 90 days and unlocks roughly **111M** more on two monthly vesting cliffs, while no buyback and no fee burn remove anything. The framework reads about **+2.1%** net to market. Our supply monitor reads essentially **flat** — a gap that comes from the circulating figure being frozen rather than stepped up for the monthly unlocks.

## The verdict, in one paragraph

For the 90-day window ending June 16 2026, the MrNasdog Pressure Framework reads **SEI at +2.1% net** on the forward view, driven by staking emission and a recurring monthly vesting unlock with no offset on the buy side. Our supply monitor reads the realized last-90-day change at **−0.0005%** — essentially flat — versus the framework's **+2.96%** gross read for the same window, a gap of about **3.0 percentage points** that ships a **⚠ monitor-gap chip**. The gap is on the data side, not the mechanism: the circulating supply the monitor uses has been frozen at a round **6.73B** and is not being stepped up for the monthly cliffs, while the published vesting calendar keeps releasing about **55.6M** a month. SEI is **structurally inflationary**: new supply arrives every block and every month, and nothing burns or buys it back.

## Sell pressure: where new SEI comes from

Two mechanisms add SEI. Sell #1 — protocol inflation — is the staking emission, about **32M SEI** over the next 90 days. Sei is a bonded proof-of-stake chain with a fixed **10B** cap; new SEI is minted to the active validator set on a 10-year emission curve, on the order of **130M** a year, and paid out as staking rewards. Sell #2 — vesting unlocks — is the larger flow, about **111M SEI**. A monthly cliff of roughly **55.6M** unlocks on the 15th, drawn from the team, early private and seed investors, and the ecosystem reserve; two of those firings land inside this window, on **Jul 15 2026** and **Aug 15 2026**.

Sell #3 — Foundation and unscheduled unlocks — is **zero** as a separate flow: the ecosystem reserve releases on the same dated monthly cliff already counted in Sell #2, and there is no evidence of a discretionary treasury release outside that schedule. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court-ordered distribution applies to SEI.

## Buy pressure: where new SEI goes

The buy side is **empty**. Buy #1 — programmatic buyback — is zero: Sei runs no protocol mechanism that spends revenue to buy SEI back off the market. Buy #2 — protocol fee burn — is zero because Sei is a Cosmos-SDK chain where gas fees flow to validators and the community pool rather than to a burn address, so activity does not destroy SEI. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no announced open-market buying and no new escrow in the window. With nothing on the buy side, the full weight of emission and unlocks reaches the market unopposed.

## Foundation and overhang

SEI's largest overhang is the unvested remainder of the **10B** cap — only about two-thirds is circulating, and the rest releases on the monthly schedule that drives Sell #2. The team, private and seed investor, and ecosystem reserve allocations are the buckets feeding the **55.6M** monthly cliff. These are not a static stockpile; they are a known, dated release that the framework already books as it fires. The framework re-checks the vesting calendar and chain emission on a roughly bi-weekly walk; if a reserve balance falls faster than the published schedule, the extra outflow enters Sell #3 at the next refresh.

## How SEI compares to other uncapped emission layer-1s

SEI belongs to the class of **capped-supply proof-of-stake L1s still early in their unlock schedule** — structurally close to peers like Sui or Aptos, where staking emission is modest but a large share of supply is still vesting. Unlike an uncapped continuous-emission chain, SEI has a hard **10B** ceiling, so the staking mint is bounded. But unlike a fully distributed token, SEI's near-term inflation is dominated by the vesting unlock, not the block reward — the monthly cliff is several times larger than the emission.

The contrast worth drawing is with exchange tokens and fee-burning chains that buy back or burn enough to go net-deflationary. SEI does neither: there is no buyback and no fee burn, so dilution is one-directional until the unlock schedule winds down. For an inflation lens specifically, that makes SEI read as clearly, steadily inflationary in the near term — the cap matters for the long run, but the active float keeps growing month by month.

## What to watch in the next 90 days

Watch the **Jul 15 2026** and **Aug 15 2026** unlocks — each releases about 55.6M SEI and together they are the single biggest driver of the forward reading. Watch whether the circulating-supply figure the monitor uses finally steps up to reflect those cliffs, which would close the monitor gap from the data side. Watch for any new buyback, fee-burn, or token-lock proposal through governance, since any of those would be the first real offset on the buy side. And note that the staking emission curve decays slowly over its 10-year life, so the block-reward share of inflation eases gradually rather than abruptly.

## Summary

SEI is a capped proof-of-stake layer-1 whose near-term supply grows from two sources: staking emission of about 32M over 90 days and a monthly vesting cliff of about 55.6M, roughly 111M of which lands in this window. With no buyback and no fee burn, nothing offsets that, so the framework reads about +2.1% net to market. Our supply monitor reads flat, but only because the circulating figure it uses is frozen and not stepped up for the monthly unlocks — the vesting calendar is the harder fact, so the scheduled unlocks are kept. SEI stays structurally inflationary until its unlock schedule winds down.

---

*MrNasdog Pressure Framework analysis of Sei (SEI), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 16, 2026.*
