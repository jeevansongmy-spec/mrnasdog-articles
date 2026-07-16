---
title:         "JST Inflation Analysis · July 2026 · Mixed last 90D, projected to shrink"
description:   "JST has no mint and no vesting left on TRON; JustLend DAO's quarterly buyback-and-burn has destroyed 13.7% of supply. Framework −2.50% net; monitor +0.27%."
canonical_url: "https://mrnasdog.com/research/jst/inflation"
tags:          ["crypto", "jst", "just", "defi"]
published:     true
---

*Originally published at [mrnasdog.com/research/jst/inflation](https://mrnasdog.com/research/jst/inflation).*

# JST Inflation Analysis · July 2026 · Mixed last 90D, projected to shrink

JST, the governance token of the JUST DeFi ecosystem on TRON, has **zero sell pressure**: the on-chain supply has read a flat **9.9B** since 2020, and the last vesting finished in April 2022. The only live mechanism is JustLend DAO's quarterly buyback-and-burn, which has already destroyed **1,356M JST** — **13.7%** of everything ever issued — and whose next round should remove about **213.6M JST**, a net of **−2.50%**. The trailing window reads **0.00%** only because the previous burn landed two days before it opened; our supply monitor reads **+0.27%**, a gap of **0.27 percentage points**, inside tolerance.

## The verdict, in one paragraph

For the 90-day window ending July 16 2026, the MrNasdog Pressure Framework reads **JST at 0.00% net** realised and **−2.50% net** on the forward view. The flat trailing number is a calendar artefact, not a change in the mechanism: JustLend DAO burned **271,337,579 JST** on April 15 2026, two days before this window opened, and no burn has fired since — so the window genuinely carries no flow in either direction. Our supply monitor reads the realised last-90-day change at **+0.27%** versus the framework's **0.00%**, a gap of about **0.27 percentage points**, inside the 0.5-point tolerance, so no monitor-gap chip is raised; the small positive is upstream derivation drift, since the on-chain unburned supply actually fell slightly across the same window. JST is **a fixed-issuance token being deflated by protocol revenue** — the cleanest structural shape the framework tracks, with the entire reading resting on one recurring event.

## Sell pressure: where new JST comes from

Nowhere. All four sell rows read **zero**, which is rare. Sell #1 — protocol inflation — is **zero** because JST has no emission curve, no block reward and no staking issuance: the token's on-chain total supply has read a flat **9,900,000,000** since it was issued in April 2020 and has never moved. One honest caveat: the JST contract does carry a mint function, and its owner key is still live rather than renounced. It has never been used once in six years, so we carry the row at zero and keep watching the key rather than calling it impossible.

Sell #2 — vesting unlocks — is **zero**. The Poloniex launch sale, the TRON airdrop, the mining and ecosystem allocations and the team tranche all finished releasing, with the last team vesting complete by **April 2022**. The chain settles the question independently: JST's unburned supply and its circulating supply now reconcile to under a thousand tokens, which means there is no locked bucket left anywhere that could unlock into the float. Sell #3 — Foundation and unscheduled unlocks — is **zero** on flow, though it carries a real overhang discussed below. Sell #4 — long-term locked or bankruptcy — is **zero**: no bankruptcy estate or court-ordered distribution touches JST.

## Buy pressure: where new JST goes

Buy #1 — the programmatic buyback — is the whole story. JustLend DAO spends protocol net revenue buying JST on the open market and then sends it to a burn address, where it is destroyed rather than held. The funding rule is precise and worth stating: an accrued reserve of roughly **$59.09M** was split **30%** deployed immediately and **70%** released across four quarters at **17.5%** each — about **$10.34M** per round — with each quarter adding that quarter's fresh net income on top. Three rounds have executed on chain: **559,890,753 JST** on October 19 2025, **525,000,000 JST** on January 14 2026, and **271,337,579 JST** on April 15 2026. Cumulatively that is **1,356,228,332 JST** burned, or **13.70%** of issuance, in nine months.

The next round is funded by second-quarter 2026 revenue and is due now, three months on from the last one. Sizing it two independent ways agrees closely: the mechanism arithmetic gives the fixed **$10.34M** reserve slice plus a quarter's net income — observed at **$10.19M** and **$10.96M** in the two disclosed quarters — for roughly **$20.9M**, while the plain history of what each round has spent lands at about **$21M**. At JST's current price that buys about **213.6M JST**, which is what the forward ledger books. The other buy rows are zero: Buy #2 — protocol fee burn — is **zero**, because JST has no automatic per-transaction burn and revenue is routed through the buyback instead; Buy #3 — Foundation buy — is **zero**, since the DAO's open-market buying is already Buy #1; and Buy #4 — new long-term lock — is **zero**, because bought-back JST is burned outright rather than locked.

## Foundation and overhang

Two overhangs are tracked. The first is the JustLend DAO wallet that executes the buyback-and-burn, which holds about **500M JST** — roughly **5.9%** of circulating — and which the upstream supply data counts as freely circulating. Its balance swings, and the swings are easy to misread: this build traced two lots of **200M JST** moving out to JustLend governance contracts as proposal deposits and returning when the votes closed, including one lot posted on July 6 2026 for the Comptroller upgrade proposal and returned on July 13 2026. Those are bonds, not buying, and no supply reached traders. Its only outflows in the entire recorded history go to the burn address. The second overhang is the dormant mint key on the token contract, which holds no JST and has never been exercised, refreshed on every rebuild.

Both carry the same trigger: if either overhang's balance falls to the open market between refreshes, the outflow enters Sell #3 at the next refresh. Until an outflow to a market venue is actually observed, both stay at zero — holding tokens is not the same as selling them.

## How JST compares to other revenue-buyback DeFi tokens

Structurally, JST sits at the strong end of its class. Compare it to a governance token like AAVE: both are capped with no protocol emission, but Aave's revenue buyback parks the bought tokens in a DAO treasury, so the supply is removed from active float while still legally existing and still counted as circulating by most upstream data. JST burns instead. A burn is irreversible; a treasury accumulation can be redeployed by a future vote. That difference is why JST's issuance has fallen 13.7% in nine months while treasury-accumulating peers show a much shallower realised decline.

Against exchange tokens with quarterly burns — the BNB model — JST shares the quarterly rhythm and the irreversibility but not the source. An exchange burn is funded by trading revenue on a venue the issuer controls; JustLend DAO's burn is funded by lending, liquid-staking and stablecoin revenue on a permissionless protocol, which is more volatile but also more legible on chain. Against tokens like PENDLE, where a buyback recycles tokens back to stakers rather than destroying them, JST's destination makes the difference between a distribution and a sink. And against uncapped continuous-emission chains, JST has no offsetting issuance at all to fight, which is why its net reads as pure deflation rather than a burn racing a mint.

The honest weakness of the model is concentration. JST's entire framework reading rests on one recurring discretionary event. If protocol revenue collapses or the DAO retires the programme after the reserve is exhausted at the end of 2026, the sell rows stay at zero but the buy row goes to zero too — and a token with no mint and no burn is simply flat.

## What to watch in the next 90 days

First, the fourth buyback-and-burn round, funded by second-quarter 2026 revenue and due around the middle of July 2026 — it is the single event that decides whether the **−2.50%** forward read materialises. Second, the size of that round in dollars: the reserve slice is fixed at about **$10.34M**, so any surprise comes from JustLend DAO's quarterly net income, which has run between **$10.19M** and **$10.96M**. Third, the terminal question — the reserve programme runs its final tranche in the fourth quarter of 2026, so watch for a governance proposal on whether revenue-funded burns continue into 2027 on income alone. Fourth, the balance of the DAO buyback wallet, whose ~500M JST is the only meaningful overhang. Fifth, the dormant mint key: any transaction from it would be the single most material supply event possible for this token.

## Summary

The MrNasdog Pressure Framework reads JST as a fixed-issuance token being actively deflated by protocol revenue. Every sell row is zero — no emission, no vesting, no estate — and the only flow is JustLend DAO's quarterly buyback-and-burn, which has destroyed **1,356M JST**, or **13.7%** of the original **9.9B** issuance, and whose next round should remove about **213.6M JST** for a forward net of **−2.50%**. The trailing window reads flat at **0.00%** purely because the April 15 2026 burn fell two days outside it, and our supply monitor's **+0.27%** sits within tolerance. The key risk is concentration rather than dilution: the burn is discretionary, revenue-dependent, and its reserve funding runs out at the end of 2026 — a token with no mint and no burn is flat, not deflationary.

---

*MrNasdog Pressure Framework analysis of JST, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 16 2026.*
