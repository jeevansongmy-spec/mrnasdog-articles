---
title: "SHIB Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description: "SHIB cannot mint and nothing vests. Burns removed 4,107.3M SHIB in 90 days, 0.0007% of a 589.2T float, so the Pressure Framework reads -0.00% net."
canonical_url: "https://mrnasdog.com/research/shib/inflation"
tags: ["crypto", "shib", "shiba-inu", "memecoin"]
published: true
---

> Originally published at **[mrnasdog.com/research/shib/inflation](https://mrnasdog.com/research/shib/inflation)** by MrNasdog.

Shiba Inu's SHIB is flat: the Pressure Framework reads it at **-0.00%** over the trailing 90 days and **-0.00%** over the next 90, and the inflation monitor agrees at **+0.07%**. The SHIB token contract on Ethereum has no mint function and nothing vests, so sell pressure is **0**; the only flow is burning, which removed **4,107.3M SHIB** — real, but just **0.0007%** of a **589.2T SHIB** circulating supply. Supply can only fall, and at this burn rate it falls too slowly to show.

## The verdict, in one paragraph

Against a circulating base of **589.2T SHIB**, the framework books **0** of sell pressure and **4,107.3M SHIB** of buy pressure over the trailing 90 days — a net of **-0.0007%**, which displays as **-0.00%** — and projects **-0.0002%** for the next 90 days, when only the steady part of the burn is expected to repeat. The inflation monitor reads **+0.07%** for the same window, a gap of **0.07 percentage points**, inside the framework's 0.5pp tolerance, so the overview page ships with no monitor-gap warning. The label for SHIB is a **fixed-supply token with a burn too small to move it**: nothing can be added, something is always being removed, and the net is a rounding error on a 589-trillion base.

## Sell pressure: where new SHIB comes from

Nowhere. Sell #1, protocol inflation, is **0**, and it is the one row on this page that is closed rather than watched. The SHIB token contract exposes twelve functions — transfers, approvals, the standard read-outs, and a burn — and none of them can create a token. It has no owner, no pause switch and no upgrade path, so no future vote or team decision can add a mint. Across the whole window not one SHIB was minted, and the count of SHIB in existence went down rather than up.

Sell #2, vesting unlocks, is **0**. Shiba Inu launched in August 2020 by sending half of the supply to Vitalik Buterin and the other half into a trading pool. There was never a team tranche, an investor round or a treasury allocation, so there is no unlock calendar and nothing waiting in a vesting contract.

Sell #3, Foundation and unscheduled unlocks, is **0**: no Shiba Inu treasury holds SHIB on chain, and no watched wallet released any. Sell #4, long-term locked or bankruptcy, is also **0**, and this is the row with the most interesting near-miss. The US government holds **54,897.1M SHIB** seized in the FTX and Alameda case. On **Jul 15 2026** it moved the entire stash to a freshly created wallet. Recovered FTX assets have usually been sold for cash, but that wallet has not sent a single SHIB since. Moving coins between wallets is not sell pressure; delivering them to an exchange would be.

## Buy pressure: where new SHIB goes

Buy #1, programmatic buyback, is **0**: no team, foundation or contract spends money repurchasing SHIB. Buy #3, Foundation buy, is **0** for the same reason. Buy #4, new long-term lock, is **0**, and staking moved the other way — the main SHIB staking contract fell from **3,552,086M** to **3,480,071M SHIB** as holders withdrew.

Buy #2, protocol fee burn, is **0**, and it needs the most explanation, because the burn exists and it fired. Shibarium, Shiba Inu's own network, uses part of its gas fees to buy SHIB and destroy it, and **117.4M SHIB** were destroyed that way this window. But those SHIB live on Shibarium as a bridged copy, backed by real SHIB locked in a bridge contract on Ethereum — and a 2025 bridge hack drained that backing. The bridge now holds **90.9M** real SHIB against **92,353.5M** copies. Destroying a copy removes no real SHIB from Ethereum; no Ethereum burn address moved with it, so the framework counts none of it.

What does count is Buy #5, community and app burns, at **4,107.3M SHIB**. The framework read four separate places at both ends of the window — two dead addresses, the token contract's own balance, where SHIB sent by mistake or on purpose can never move again, and the count of SHIB in existence, which falls when anyone calls the burn function — and then traced every single transfer into them. Each total matched to the last decimal, and a second independent pass returned exactly the same transfers. **3,112.0M** of the burn came from one app that locks trading pools paired with SHIB and burns part of the fees they earn; almost all of it landed between **Jul 25** and **Jul 27** in a single catch-up. The remaining **995.2M** is a steady trickle of about **330M** a month from ordinary holders and small apps, and that is the only part projected forward.

## Foundation and overhang

The overhang on SHIB is small and mostly not controlled by the project. The original deployer wallet holds **50.5M SHIB**, unchanged all window. The Shibarium bridge contract holds **90.9M SHIB** of user deposits, also unchanged. The treasury that funds repayments to the bridge-hack victims has no published wallet, so it is tracked through official disclosures rather than on chain. The largest single overhang is not Shiba Inu's at all: the **54,897.1M SHIB** seized by the US government, now in a new wallet. All on-chain balances are refreshed at every rebuild. If any of these balances falls between refreshes by more than ordinary noise, that outflow enters Sell #3 — or Sell #4 for the seized stash — at the next refresh.

## How SHIB compares to other meme coins

On issuance, SHIB sits at the strict end of the meme-coin range. Dogecoin has no cap and mints a fixed 5 billion DOGE a year forever, so its supply grows by a steady, slowly shrinking percentage. SHIB mints nothing and can never mint. Like other no-mint, no-vest meme tokens, its sell side is empty by design, and the only question is how much leaves.

That is where SHIB is often oversold. Its burn is famous, but it is a voluntary, fragmented one: holders, apps and an ecosystem tracker sending tokens to dead addresses, not a protocol rule tied to usage. Compare an exchange token with a quarterly auto-burn sized by a fixed rule, where removals can reach whole percentage points a year and the reading turns clearly negative. For SHIB to register even **-0.01%** in a quarter, burns would need to be roughly fourteen times this window's total — and this window already held the strongest July in some time.

The third comparison is layer-2 burns. Many ecosystems advertise a fee burn on their own network. Whether it matters depends on whether the token burned there is the real asset or a bridged claim. On Shibarium today it is a claim whose backing is gone, so the network's activity, however it grows, does not reach the SHIB supply until the bridge is made whole.

## What to watch in the next 90 days

First, the US government wallet holding **54,897.1M SHIB** since **Jul 15 2026**: a transfer to an exchange would be the single largest sell event on this page. Second, the fee-locking app behind the late-July burst — another catch-up collection could add billions to the burn without warning. Third, Shibarium's bridge: any plan that restores its backing would turn the network's fee burn into a real removal of SHIB. Fourth, the teased Shiba Inu announcement that has circulated since **Aug 21 2026**, which nobody on the team has tied to supply; the page changes only if it does. Fifth, the steady background burn of about **330M SHIB** a month, the one flow expected to continue.

## Summary

The MrNasdog Pressure Framework reads SHIB at **-0.00%** over the trailing 90 days and **-0.00%** projected forward: mixed flows, supply roughly steady. The structural mechanism is a token that cannot grow — no mint function, no owner, no vesting — paired with a voluntary burn that removed **4,107.3M SHIB** in 90 days, only **0.0007%** of **589.2T** in circulation. The key risk is not new supply but old supply moving: **54,897.1M** seized SHIB sits one transaction from an exchange. The ceiling is absolute — SHIB can only shrink — but at this pace it shrinks too slowly for a holder to notice.

---

*MrNasdog Pressure Framework analysis of SHIB, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 15 2026.*
