---
title:         "XDC Inflation Analysis · June 2026 · Slow masternode emission, no real offset"
description:   "Slow masternode emission, no real offset: XDC mints ~21.4M XDC/90d (+0.11%) with no buyback and a negligible fee burn. Framework reads +0.11% net (monitor −0.11%, no chip)."
canonical_url: "https://mrnasdog.com/research/xdc/inflation"
tags:          ["crypto", "xdc", "xdcnetwork", "rwa"]
published:     true
---

*Originally published at [mrnasdog.com/research/xdc/inflation](https://mrnasdog.com/research/xdc/inflation)*

XDC Network mints **5.5 XDC per block** at ~2-second blocks — about **21.4M XDC** over 90 days, or roughly **+0.11%**. There is no buyback, the EIP-1559 fee burn is negligible at sub-penny fees, and no vesting cliff lands in the window, so the framework reads about **+0.11% net** — near-flat. Our supply monitor reads **−0.11%**, a gap of about **0.22 percentage points** — well within tolerance, so no warning chip.

## The verdict, in one paragraph

For the 90-day window ending June 16 2026, the MrNasdog Pressure Framework reads **XDC at about +0.11% net**, essentially flat. The entire sell side is one number: masternode block-reward emission of **5.5 XDC per block**, which mints roughly **21.4M XDC** a quarter against the ~19.95B already circulating. There is no vesting unlock in the window, no foundation release, no buyback and no meaningful burn, so almost nothing pushes the other way. Our supply monitor reads the realized last-90-day change at **−0.11%** — a gap of about **0.22 percentage points** from the framework's +0.11%, comfortably inside the 0.5-point tolerance, so XDC ships with **no monitor-gap chip**. The monitor reads slightly negative because the small fee burn and fresh masternode lock-ups trimmed circulating just below the gross emission this window. XDC is best read as **structurally near-flat with mild, uncapped inflation**.

## Sell pressure: where new XDC comes from

Sell #1 — protocol inflation — is the whole story, and it is modest. XDC Network runs an **XDPoS** delegated proof-of-stake consensus with 108 masternodes, and each block mints a fixed **5.5 XDC** for the operators that validate it. With blocks closing about every two seconds, that is roughly **86.7M XDC a year**, or **~21.4M XDC** over 90 days — about **+0.43% a year** on the ~19.95B circulating float. This is genuine new issuance: XDC has no hard cap, so the emission grows total supply rather than being paid out of a reserve. It is the network's only source of new XDC.

Sell #2 — vesting unlocks — is **zero** this window. XDC vests its non-circulating allocations on yearly cliffs, and the most recent one released **841M XDC on Feb 5 2026** — before this 90-day window opened — while the next cliff is not until **Feb 5 2027**. So no scheduled unlock reaches the market between those two dates. Sell #3 — foundation and unscheduled unlocks — is also zero: there is a large non-circulating reserve, but no discretionary release was observed in the window. Sell #4 — long-term locked or bankruptcy — is zero, with no estate or court distribution applying to XDC; the only large lock is masternode collateral, which removes supply rather than adding it.

## Buy pressure: where new XDC goes

There is almost nothing to count. Buy #1 — programmatic buyback — is **zero**: XDC has no protocol mechanism that buys XDC back from the market. Buy #2 — protocol fee burn — is real but booked **zero**: the January 2026 Cancun hard fork added an EIP-1559-style base-fee burn (the burn share is set by the XDCDAO), and 20% of transaction fees are permanently destroyed, but XDC's sub-penny fees make the 90-day quantum negligible and not cleanly quantifiable, so it is monitored rather than estimated. Buy #3 — foundation buy — and Buy #4 — new long-term lock — are both zero, with no accumulation programme and no new escrow announced with a stated quantum in the window.

## Foundation and overhang

XDC carries a large structural overhang. Total supply is about **38B XDC** against roughly **20B circulating**, which leaves close to **18B XDC non-circulating** across treasury, foundation and ecosystem allocations. That reserve is released on a partial yearly schedule — the Feb 5 2026 cliff is the most recent precedent, and the next is Feb 5 2027 — so it is best read as a slow, scheduled drip rather than a discretionary stockpile that could hit the market at any moment. We track this overhang on a regular walk; if its balance falls between refreshes, the outflow enters Sell #3 at the next refresh. For this window, no part of it moved, which is why every sell row below #1 reads zero.

## How XDC compares to other uncapped Layer 1 chains

XDC belongs to the class of **uncapped, continuous-emission Layer 1s** that pay validators out of new issuance rather than out of fees alone — the same structural family as many staking-reward chains. Unlike a hard-capped proof-of-work coin, XDC has no supply ceiling, so its block reward keeps minting new coins indefinitely; but unlike high-inflation staking chains that issue several percent a year, XDC's **5.5-per-block** reward works out to only about **0.43% a year** on the current float, which is low for an uncapped chain.

The closest analogue on the offset side is the set of chains that added an **EIP-1559 base-fee burn** to counter issuance. On a chain with heavy fee activity, that burn can flip the net deflationary; on XDC, fees are sub-penny because the chain is built for enterprise trade-finance settlement rather than speculative throughput, so the burn is real in design but tiny in practice. The result is a chain that looks structurally near-flat today — mild positive issuance, a burn that could one day matter if volume scales, and a reserve that unlocks on a predictable yearly cliff.

## What to watch in the next 90 days

The main scheduled item is simply the absence of one: the next vesting cliff is **Feb 5 2027**, so no large unlock lands in the next quarter and the supply read should stay near-flat. Watch the XDC-Community reward-mechanism upgrade proposal, which would replace the current per-block reward with fixed per-node payments — it is still under discussion and needs a security audit plus a hard fork, but if it activates it changes the Sell #1 math. Watch on-chain fee volume: the EIP-1559 burn only becomes a meaningful offset if trade-finance settlement volume rises enough to move sub-penny fees into real numbers. And watch the masternode count, since each new node locks 10M XDC out of the float.

## Summary

XDC is an uncapped XDPoS Layer 1 that mints 5.5 XDC per block — about 21.4M XDC over 90 days, roughly +0.43% a year. With no vesting cliff in the window, no buyback, and an EIP-1559 fee burn too small to count at sub-penny fees, the framework reads about +0.11% net — near-flat. Our supply monitor reads −0.11% realized, a gap of about 0.22 percentage points that stays inside tolerance, so no warning chip. The key risks are the large ~18B non-circulating reserve, which unlocks on a yearly cliff (next Feb 5 2027), and a possible reward-mechanism upgrade that would re-cut the per-block emission. XDC stays structurally near-flat with mild, uncapped inflation.

*MrNasdog Pressure Framework analysis of XDC (XDC Network), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 16, 2026.*
