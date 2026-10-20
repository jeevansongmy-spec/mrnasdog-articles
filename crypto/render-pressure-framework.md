---
title: "RENDER Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description: "RENDER supply is roughly steady: 1.43M RENDER reached the market in 90 days while job burns took out 368K, so net supply grows +0.19%, about the same next."
canonical_url: "https://mrnasdog.com/research/render/inflation"
tags: ["crypto", "render", "render-network", "solana"]
published: true
---
# RENDER Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

*Originally published at [mrnasdog.com/research/render/inflation](https://mrnasdog.com/research/render/inflation).*

<!-- main-page -->
This is the long supply read. For the signal, the price drivers and the questions people ask about Render Network, see [mrnasdog.com/research/render](https://mrnasdog.com/research/render).

RENDER supply is roughly steady, growing slowly. In the 90 days to **Oct 11 2026**, **1.43M RENDER** reached the market — **180,000** from the monthly mint for node operators and **1.25M** released from the Render Network Foundation's reserve — while paid rendering and AI jobs burned **367,955 RENDER**. That leaves net supply up **+0.19%** over 90 days and about the same for the next 90, against a monitor reading of **−0.20%**. The burn-mint equilibrium only tips to shrinking when job burns outgrow the fixed monthly mint.

## The verdict, in one paragraph

Our ledger reads RENDER at **+0.19%** net over the last 90 days: 1.43M coins in, 367,955 coins burned, measured against **554.12M** circulating RENDER on Solana and Ethereum together. The forward 90 days project the same **+0.19%**. The monitor reads **−0.20%**, a gap of **0.40 percentage points**, inside our 0.5-point limit, so no warning chip is shown. The monitor follows a supply figure tied to the old Ethereum token, which barely moved in the window, so its small negative number is price noise rather than a burn signal; our reading comes from the Solana chain, where RENDER now lives. In one line: Render Network is a slow-growth burn-mint token whose job burns cover about a quarter of new supply.

## Sell pressure: where new RENDER comes from

Protocol inflation is **180,000 RENDER**. Under the Year 3 budget passed by the community (5.9M RENDER for Dec 20 2025 to Dec 19 2026), the network mints **492,132 RENDER** a month. We read every mint in the window on-chain: Jul 23, Aug 23 and Sep 23 2026. Each time, 60,000 RENDER went straight to the vault that pays node operators, and that part enters the market at once. The other 432,132 went to the Foundation's emission reserve, which the project itself does not count as circulating.

Vesting unlocks are **0**. The original sale, team and escrow allocations were released years ago, and no unlock is dated for the next 90 days. The Solana mint also created 1.04M RENDER to back holders moving old RNDR over from Ethereum and Polygon; those coins were already counted on the old chain, so they add nothing new.

Foundation and unscheduled unlocks are the largest sell row at **1.25M RENDER**. The Foundation moved 1.0M out of its reserve on Aug 10 2026 and 0.25M on Aug 27 2026, after 2.0M on Feb 26 2026 and 2.0M on May 11 2026. That is about one release a quarter, used to fund operations, grants and node rewards, so we project one more release of about **1.25M** by early Nov 2026. Long-term locks and bankruptcy estates are **0**: no court, trustee or long lock holds RENDER for release.

## Buy pressure: where new RENDER goes

The protocol fee burn is **367,955 RENDER** in 90 days, about 4,088 a day. In Render's burn-mint equilibrium, a customer pays for each rendering or AI compute job, and the network destroys RENDER of the same value, keeping a 5% fee. We counted every burn transaction on-chain: the rendering burn account destroyed **355,094 RENDER** and the AI compute account **12,860 RENDER**. The burn ran faster in September and early October than in July, as more paid work came through.

The programmatic buyback row is **0** on purpose. Most customers pay in dollars, and the network uses that money to buy RENDER on the market and burn it straight away — those coins are counted once, in the burn. The Foundation buy row is **0**: the Foundation sells and spends RENDER, and any coins it sends to the burn account are already inside the burn number. New long-term locks are **0**, because RENDER has no staking or lock-up program.

## Foundation and overhang

The emission reserve is the one team balance outside the float. It holds **3.00M RENDER** after the Sep 23 2026 mint and grows by 432,132 each month until the next release. A large partner vault holds **81.90M RENDER**, about 16% of circulating supply; it sent out about 5.07M between Apr 27 and Jul 16 2026 and was quiet afterwards. It is already counted as circulating, so a sale from it would move coins between holders rather than add new supply, but it is the biggest single wallet to watch. The node-reward vault holds 0.84M, the Foundation treasury vault 24.7K RENDER plus about $909,000 in dollar coins, and on the old Ethereum token one wallet holds **14.76M RNDR** that is not counted as circulating; it did not move in the window.

We read these balances on-chain at every rebuild. If the reserve, the partner vault or the old-token wallet falls between two checks, the outflow enters the Foundation and unscheduled unlocks row at the next check.

## How RENDER compares to other DePIN compute tokens

RENDER belongs to the group of decentralized physical infrastructure tokens that pay hardware owners for real work. Its burn-mint equilibrium is close to Helium's design, where users burn the token to buy network credits while a fixed emission pays the people who run the hardware. In both, supply only shrinks when paid usage burns more than the schedule mints; at Render today the burn covers about a quarter of what reaches the market.

Other compute networks lean on staking inflation instead. Akash pays its stakers from new tokens, and Filecoin mints block rewards to storage providers who must lock collateral. Those designs tie new supply to staking or storage rather than to paid jobs, and they lock part of the float. RENDER has no staking, so nothing takes coins out of the market except the job burn.

RENDER also has a hard ceiling that many compute tokens lack: a maximum of about 644M, with about 107M added over the life of the network through the yearly budgets. Today's pace — 5.9M a year — is small next to that cap, which is why the net reading stays near zero.

## What to watch in the next 90 days

The next monthly mints are due around **Oct 23 2026**, **Nov 23 2026** and **Dec 23 2026**, each adding 60,000 RENDER for node operators and 432,132 to the reserve.

The next Foundation reserve release is expected around **Nov 7 2026** on the quarterly pattern; a larger or earlier release would raise the sell side.

Year 3 of the emission budget ends on **Dec 19 2026**. No Year 4 budget proposal has been posted yet; it will set the size of the December mint and every mint in 2027.

The Salad network, approved to join Render as a third subnet, has published its plan for on-chain burns every day. When those burns go live, the burn side could rise quickly; the same plan pulls some future emissions forward to pay Salad's GPU owners.

## Summary

Render Network's RENDER is roughly steady, growing about **+0.19%** every 90 days. New supply comes from a fixed monthly mint and quarterly releases from the Foundation's reserve, about 1.43M RENDER in 90 days, while paid rendering and AI jobs burn about 368,000. The key risk is the 81.90M partner vault and any larger reserve release; the key upside is a jump in paid usage, such as the Salad subnet's burns. A hard cap of about 644M limits how far supply can ever grow.

---

*MrNasDog Pressure Framework analysis of RENDER, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 11 2026.*
