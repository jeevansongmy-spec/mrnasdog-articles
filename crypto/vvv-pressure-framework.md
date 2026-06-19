---
title:         "VVV Inflation Analysis · June 2026 · Supply growing, projected to keep growing"
description:   "Venice Token mints ~0.78M VVV / 90D as staking yield (falling to 3M/yr Jul 1 2026) vs a ~0.05M buy-and-burn. Framework reads +1.56% net; monitor +4.30%."
canonical_url: "https://mrnasdog.com/research/vvv/inflation"
tags:          ["crypto", "vvv", "venice", "ai"]
published:     true
---

*Originally published at [mrnasdog.com/research/vvv/inflation](https://mrnasdog.com/research/vvv/inflation)*

Venice Token (VVV), the access key to Venice.ai's private AI inference API on Base, mints new VVV as staking yield on a falling schedule — about **0.78M VVV** over the next 90 days against a revenue buy-and-burn of roughly **0.05M VVV**. The Pressure Framework reads **+1.56% net** inflation for the forward window; the inflation monitor reads **+4.30%** on the trailing window, before the June and July emission cuts land. VVV is mildly inflationary today and bending toward net deflation by design.

## The verdict, in one paragraph

For the next 90 days the framework reads **VVV at +1.56% net** inflation — about **0.78M VVV** minted as staking yield minus roughly **0.05M VVV** bought back and burned, over a circulating base near **46.8M VVV**. The inflation monitor reads **+4.30%** over the trailing 90 days, a gap of **2.74 percentage points**. That gap clears the 0.5-point tolerance, so a monitor-gap chip is raised — but the gap is mechanical, not an error: the monitor's trailing window ran at a 5M-to-6M VVV/yr emission rate, while the forward window steps down to 4M/yr now and 3M/yr on Jul 1 2026 per the official Venice schedule. VVV is structurally inflationary on the active float today, with a deliberate path toward a burn-led, net-deflationary model.

## Sell pressure: where new VVV comes from

New VVV comes from one place: the staking-yield emission. **Protocol inflation** books **~0.78M VVV** for the window — newly minted VVV paid to stakers as yield. The emission rate is on a published, falling path: it began at 14M VVV per year at launch, stepped to 6M in February 2026, to 5M on May 1, to 4M on Jun 1, and cuts again to 3M on Jul 1 2026. Across the Jun 20 to Sep 18 window that is 11 days at 4M/yr and 80 days at 3M/yr, which sums to about 0.78M VVV — sharply lower than the trailing window. **Vesting unlocks** are zero: VVV is fully unlocked, with airdrop, team and treasury allocations already released and no cliff in the window. **Foundation and unscheduled unlocks** are zero in booked value: the Venice company treasury exists but has shown no discretionary outflow event in the trailing year. **Bankruptcy** is zero — no estate distributes VVV.

## Buy pressure: where new VVV goes

The buy side is a genuine, on-chain offset. **Programmatic buyback** books **~0.05M VVV** for the window: Venice spends subscription and API revenue to buy VVV on Base and send it to the burn address, through both a per-subscription burn (tiered by plan since Apr 26 2026) and a discretionary monthly buyback executed as an hourly TWAP. The dollar run-rate has been climbing — recent months have burned more than $190k to $237k each — which at recent prices works out to roughly 0.05M VVV over 90 days. **Protocol fee burn** is zero as a separate row: there is no base-fee burn; the buy-and-burn is the only mechanism that removes VVV. **Foundation buy** is zero as a separate row: Venice funds the buy-and-burn already counted above, with no distinct treasury accumulation programme. **New long-term lock** is zero as a booked row: staking VVV for yield and compute access sequesters a large share of supply, but staking is demand-side holder behaviour, not a protocol-enforced lock with an announced quantum, so the framework monitors it rather than booking it.

## Foundation and overhang

VVV carries one identified team-controlled overhang: the **Venice company treasury**, sized near **35M VVV** at genesis (a 10M team allocation, a 25M incentive fund, plus a 5M liquidity allocation), already unlocked and partly deployed. The framework books it at zero because no discretionary deploy event has been observed in the trailing year — capacity is not cadence. It is monitored on a periodic walk rather than read from a single published address. The burn destination, by contrast, is fully on-chain: bought-back VVV flows to the 0x000 burn address, whose balance stands near **33.8M VVV** and only grows. If the treasury's balance falls between refreshes — an actual sale or distribution — that outflow enters Sell #3 at the next refresh; until then it stays a watched overhang, not a booked flow.

## How VVV compares to other AI and emission-driven tokens

VVV sits at the intersection of two token classes. Like an uncapped, continuous-emission token, it has no hard supply cap and mints new units on a schedule — but unlike a pure liquidity-mining token, its emission is paid as staking yield tied to real product usage rather than to bootstrap a DEX. And like an exchange or revenue token with a buyback-burn, it routes platform revenue into purchasing and destroying its own supply. The combination is what makes VVV distinctive: it is an uncapped emitter that is actively trying to become deflationary by simultaneously cutting issuance and raising burns.

Against a fixed-supply AI or utility token, VVV still inflates — new VVV reaches stakers each day, so the active float grows. Against a continuous-emission L1, VVV's issuance is far smaller and is shrinking on a committed calendar rather than holding a steady percentage. The mechanism that defines VVV is the crossover: emissions falling 4M to 3M VVV/yr while a revenue buy-and-burn rises. The framework books the live arithmetic — about +1.6% net over 90 days — and the trend points down, toward the day burns exceed emissions.

## What to watch in the next 90 days

Three things move the reading. First, the **Jul 1 2026** emission cut from 4M to 3M VVV/yr — a hard, dated step-down that lowers the bulk of the forward window's issuance. Second, the **buy-and-burn run-rate**: burns scale with Venice subscription and API revenue, so a rising user base lifts the offset and pulls net inflation toward zero, while a price rally lowers the VVV-count bought for the same dollars. Third, the **company treasury**: any observed sale or distribution from the ~35M overhang would enter Sell #3 and change the reading materially. The structural watch line is the crossover point — the date monthly burns first exceed monthly emissions.

## Summary

Venice Token is an uncapped AI-access token on Base whose only supply flow is a falling staking-yield emission — about **0.78M VVV** over the next 90 days, against a revenue buy-and-burn of roughly **0.05M VVV**, for a framework reading of **+1.56% net** inflation. The inflation monitor reads **+4.30%** on the trailing window, a 2.74-point gap that raises a chip but is explained entirely by the June and July emission cuts not yet reflected in a backward-looking measure. There are no vesting cliffs and no bankruptcy estate; the one overhang is the ~35M VVV company treasury, monitored but not booked. VVV is mildly inflationary now and engineered to turn net deflationary as issuance keeps falling and burns keep rising.

---

*MrNasdog Pressure Framework analysis of VVV, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 20, 2026.*
