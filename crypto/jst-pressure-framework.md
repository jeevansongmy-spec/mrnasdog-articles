---
title:         "JST Inflation Analysis · July 2026 · Supply shrinking, projected to keep shrinking"
description:   "JST has no mint and no vesting left on TRON; JustLend DAO's buyback-and-burn destroyed 355M JST on Jul 17 2026. Framework −4.34% net; monitor −4.18%."
canonical_url: "https://mrnasdog.com/research/jst/inflation"
tags:          ["crypto", "jst", "just", "defi"]
published:     true
---

*Originally published at [mrnasdog.com/research/jst/inflation](https://mrnasdog.com/research/jst/inflation).*

# JST Inflation Analysis · July 2026 · Supply shrinking, projected to keep shrinking

JST, the governance token of the JUST DeFi ecosystem on TRON, has **zero sell pressure**: the on-chain supply has only ever fallen since 2020, and the last vesting finished in 2022. The only live mechanism is JustLend DAO's quarterly buyback-and-burn, which destroyed **355.0M JST** on **July 17 2026** — inside this window — for a MrNasdog Pressure Framework net of **−4.34%** against the inflation monitor's **−4.18%**. Cumulative burns now reach **1,711M JST**, or **17.3%** of everything ever issued, and the next round should remove roughly **212M JST** more.

## The verdict, in one paragraph

For the 90-day window ending **July 31 2026**, the MrNasdog Pressure Framework reads **JST at −4.34% net** — total sell pressure of **0 JST** against total buy-side removal of **355.0M JST** on a circulating base of about **8.19B JST**. The inflation monitor reads the realised 90-day supply change at **−4.18%**, a gap of just **0.16 percentage points** — comfortably inside the 0.5-point tolerance, so no monitor-gap chip is raised. The two agree because the reading rests on one clean event: JustLend DAO burned **355.02M JST** on **July 17 2026**, and the monitor's own supply series fell by almost exactly that amount, from about **8.544B** to **8.187B**. JST is **a fixed-issuance token being actively deflated by protocol revenue** — the cleanest structural shape the framework tracks, with a mint that has never fired and a burn that fires every quarter.

## Sell pressure: where new JST comes from

Nowhere. All four sell rows read **zero**, which is rare. Sell #1 — protocol inflation — is **zero** because JST has no emission curve, no block reward and no staking issuance: the token was issued with a fixed **9,900,000,000** supply in 2020 and the on-chain figure has only ever moved downward, through burns. One honest caveat keeps this from being a settled zero: the JST contract still carries a mint function whose owner key is live rather than renounced. It has never been used once in six years, so we book the row at zero and keep watching the key instead of calling it impossible.

Sell #2 — vesting unlocks — is **zero**. The launch sale, the airdrop, the mining and ecosystem allocations and the team tranche all finished releasing, with the last vesting complete by 2022. The chain settles the question independently: JST's total supply and its circulating supply now read the same **8.19B**, which means there is no locked bucket left anywhere that could unlock into the float — the only gap to the 9.9B cap is the **1,711M JST** already burned. Sell #3 — Foundation and unscheduled unlocks — is **zero** on flow, though it carries a real overhang discussed below. Sell #4 — long-term locked or bankruptcy — is **zero**: no bankruptcy estate or court-ordered distribution touches JST.

## Buy pressure: where new JST goes

Buy #1 — the programmatic buyback — is the whole story. JustLend DAO spends protocol net revenue buying JST on the open market and then sends it to a burn address, where it is destroyed rather than held. Four rounds have executed on chain: **559.89M JST** on October 19 2025, **525.00M JST** on January 14 2026, **271.34M JST** on April 16 2026, and **355.02M JST** on **July 17 2026**. That most recent round is the one that lands inside this framework window, and it was the largest yet at about **$34.6M** of value: roughly **248M JST** from the regular second-quarter 2026 revenue buyback plus a one-off **107M JST** special burn of historical USDJ stability fees. Cumulatively the four rounds have destroyed **1,711M JST**, or **17.3%** of issuance, in nine months.

The forward ledger does not simply extrapolate that **355M**, because it carried a non-recurring component. The next round is funded by third-quarter 2026 revenue, budgeted in the JustLend DAO Q2 report at about **$21.55M**, and is due on the same quarterly rhythm around **October 2026** — inside the next 90-day window. At JST's current price that buys roughly **212M JST**, which is what the forward view books, for a projected net near **−2.6%**. The other buy rows are zero: Buy #2 — protocol fee burn — is **zero**, because JST has no automatic per-transaction burn and revenue is routed through the quarterly buyback instead; Buy #3 — Foundation buy — is **zero**, since the DAO's open-market buying is already Buy #1; and Buy #4 — new long-term lock — is **zero**, because bought-back JST is burned outright rather than locked.

## Foundation and overhang

Two overhangs are tracked. The first is the JustLend DAO wallet that executes the buyback-and-burn, which holds about **500M JST** — roughly **6%** of circulating — and which the upstream supply data counts as freely circulating. Its balance swings, and the swings are easy to misread: this build traced a **200,000,001 JST** proposal bond moving out to a JustLend governance contract and returning when the vote closed, including one lot returned on **July 13 2026**. Those are governance deposits, not buying, and no supply reached traders — mistaking a reclaimed bond for a buyback is the specific trap this row guards against. The wallet's only recorded outflows in its entire history go to the burn address. The second overhang is the dormant mint key on the token contract, which holds no JST and has never been exercised, refreshed on every rebuild.

Both carry the same trigger: if either overhang's balance falls to the open market between refreshes, the outflow enters Sell #3 at the next refresh. Until an outflow to a market venue is actually observed, both stay at zero — holding tokens is not the same as selling them.

## How JST compares to other revenue-buyback DeFi tokens

Structurally, JST sits at the strong end of its class. Compare it to a governance token like AAVE: both are capped with no protocol emission, but Aave's revenue buyback parks the bought tokens in a DAO treasury, so the supply is removed from active float while still legally existing and still counted as circulating by most upstream data. JST burns instead. A burn is irreversible; a treasury accumulation can be redeployed by a future vote. That difference is why JST's issuance has fallen **17.3%** in nine months while treasury-accumulating peers show a much shallower realised decline.

Against exchange tokens with quarterly burns — the BNB model — JST shares the quarterly rhythm and the irreversibility but not the source. An exchange burn is funded by trading revenue on a venue the issuer controls; JustLend DAO's burn is funded by lending, liquid-staking and USDD stablecoin revenue on a permissionless protocol, which is more volatile but also more legible on chain. Against tokens like PENDLE, where a buyback recycles tokens back to stakers rather than destroying them, JST's destination makes the difference between a distribution and a sink. And against uncapped continuous-emission chains like TRON's own TRX, JST has no offsetting issuance at all to fight, which is why its net reads as pure deflation rather than a burn racing a mint.

The honest weakness of the model is concentration. JST's entire framework reading rests on one recurring discretionary event. If JustLend DAO's protocol revenue collapses or the DAO retires the programme, the sell rows stay at zero but the buy row goes to zero too — and a token with no mint and no burn is simply flat, not deflationary.

## What to watch in the next 90 days

First, the fifth buyback-and-burn round, funded by third-quarter 2026 revenue and due around **October 2026** — it is the single event that decides whether the **−2.6%** forward read materialises. Second, the size of that round in dollars: JustLend DAO budgeted about **$21.55M** in the Q2 report, but the figure floats with lending, liquidation and USDD stabilisation revenue, so a weak quarter shrinks the burn directly. Third, whether the round again carries a one-off special burn like the **107M JST** historical USDJ component in July — extras of that kind push the realised number well past the recurring run-rate. Fourth, the balance of the DAO buyback wallet, whose ~500M JST is the only meaningful overhang, and any move out of it that does not go to the burn address. Fifth, the dormant mint key: any transaction from it would be the single most material supply event possible for this token.

## Summary

The MrNasdog Pressure Framework reads JUST (JST) at **−4.34% net** over the 90 days to July 31 2026 — every sell row zero, against **355.0M JST** bought back and burned by JustLend DAO on July 17 2026. The structural mechanism is one-sided: JST has a fixed 9.9B issuance, a mint that has never fired, and no vesting left, so its supply moves only when protocol revenue funds a quarterly burn. That burn has now destroyed **1,711M JST**, or **17.3%** of issuance, and the next round should remove about **212M JST** more for a forward net near **−2.6%**. The key risk is concentration rather than dilution: the burn is discretionary and revenue-dependent, so a weak quarter or a retired programme would leave a token with no mint and no burn — flat, not deflationary — with the 9.9B cap the only hard ceiling in play.

*MrNasdog Pressure Framework analysis of JUST (JST), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 31 2026.*
