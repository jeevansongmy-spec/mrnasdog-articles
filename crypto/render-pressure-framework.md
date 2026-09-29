---
title: "RENDER Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description: "Mixed flows, supply roughly steady: 1.43M new RENDER reached the market in 90 days while paid jobs burned 335,705, so RENDER reads +0.21% net."
canonical_url: "https://mrnasdog.com/research/render/inflation"
tags: ["crypto", "render", "render-network", "solana"]
published: true
---

# RENDER Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

*Originally published at [mrnasdog.com/research/render/inflation](https://mrnasdog.com/research/render/inflation).*

RENDER supply is roughly steady and rising slowly: over the last 90 days **1.43M RENDER** reached the market while paid jobs burned **335,705 RENDER**, a net rise of **+0.21%**, and we expect about the same in the next 90 days. Render Network runs a burn-mint equilibrium, so every paid rendering or AI job destroys RENDER while a fixed monthly emission pays node operators, grants and the Render Network Foundation. Today the burn covers under a quarter of the new RENDER that reaches the market, and most of the new supply comes from the Foundation's emission reserve, not from vesting.

## The verdict, in one paragraph

Our primary reading puts RENDER at **+0.21%** over the last 90 days (Jul 1 to Sep 29 2026) and **+0.21%** for the next 90 days. The inflation monitor reads **+0.03%** for the same window, so the gap is **0.18 percentage points** — inside our 0.5-point line, so no warning chip is shown. That agreement is weaker than it looks: the circulating figure the monitor follows is counted on the old Ethereum token, and it cannot see RENDER minted or burned on Solana, so it barely moves at all. The flows we measured on-chain are what drive our number. The label that fits: **a slowly inflating burn-mint coin whose burn has not yet caught up with its emission**.

## Sell pressure: where new RENDER comes from

RENDER's protocol inflation is a fixed emission, not a staking reward. Under the year-3 plan approved by the Render Network community (RNP-022, running Dec 20 2025 to Dec 19 2026), the network mints **5.9M RENDER** a year, in monthly mints of **492,132 RENDER** around the 23rd. Each mint has two parts. **60,000 RENDER** goes straight to the Foundation vault that pays node operators, so it reaches the market at once: **180,000 RENDER** from the Jul 23, Aug 23 and Sep 23 2026 mints. That is Sell #1, protocol inflation.

The larger part, **432,132 RENDER** a month, lands in the emission reserve. The project itself counts that reserve as not yet circulating, so those coins only count as new supply when the Foundation moves them out. It does that in lumps: **2.0M RENDER** on Feb 26 2026, **2.0M** on May 11 2026, then **1.0M** on Aug 10 and **250,000** on Aug 27 2026. The August releases, **1.25M RENDER**, are Sell #3 for this window, and they are the single biggest source of new RENDER on the market. With one release roughly every quarter, we count one more release of the same size in the next 90 days.

Vesting unlocks are zero: RENDER has no investor or team vesting left, and unlock trackers list it as fully unlocked — the "unlocks" they show each month are the same emission counted above. There is no bankruptcy estate or long-term lock releasing RENDER either. One more flow looks large but adds nothing: holders keep swapping the old Ethereum RNDR token for Solana RENDER. About **1.04M** were swapped in this window, and **1.0M** new RENDER were minted into the swap pool on Sep 24 2026, but each new RENDER replaces an old token that is locked, so the token upgrade is not new supply. About **82.48M** old tokens are still waiting to be swapped.

## Buy pressure: where new RENDER goes

RENDER leaves the market one way: the burn. Every paid job on Render Network is settled by destroying RENDER, and we read every transaction of the two burn wallets in the window rather than a summary. The rendering burn wallet destroyed **323,333 RENDER** and the newer AI-compute burn wallet (the Dispersed marketplace) destroyed **12,372 RENDER**, for a protocol fee burn of **335,705 RENDER** — about **3,730 RENDER a day**. We checked it two ways: the burn wallet's balance moved by exactly what the transactions say, and over a timed interval the total supply of RENDER fell by exactly the one burn we could see.

Where the burned RENDER came from matters. **250,000 RENDER** was sent to the rendering burn wallet by a Foundation treasury vault on Aug 26, Sep 18 and Sep 22 2026; about **104,000 RENDER** was bought with dollars inside the burn transactions themselves; and **118,673 RENDER** still sits in the burn wallet waiting to be destroyed. So most of this window's burn was the Foundation returning coins, not fresh buying from customers. There is no separate programmatic buyback, the Foundation did not buy RENDER on the market, and RENDER has no staking lock, so the other buy rows are zero.

## Foundation and overhang

The main overhang is the emission reserve: **2.999M RENDER** not yet released, refilled by 432,132 RENDER every month and emptied in quarterly lumps. We read it on-chain at every rebuild. The Render Network Foundation also holds coins that already count as circulating: a large partner vault with **81.90M RENDER** (it did not move in the window), the node-reward vault with **930,124 RENDER**, a treasury vault with **78,300 RENDER**, a payments wallet with **162,348 RENDER**, and smaller reward and burn wallets. Moving these coins does not add new supply, because they are already in the circulating count. On the old Ethereum side, one wallet with **14.76M** tokens is left out of circulating; it did not move either. If the emission reserve or that old-chain wallet falls between our checks, the outflow goes into Sell #3 at the next check.

## How RENDER compares to other DePIN compute tokens

Most decentralized compute tokens pay providers from a fixed emission and hope usage grows into it. RENDER is different because the payment itself destroys the coin: under burn-mint equilibrium, customers price work in dollars and the matching RENDER is burned, while providers are paid from a capped emission. In theory, once jobs burn more RENDER than the network mints, supply shrinks. Today it is far from that point — the burn is under a quarter of new supply reaching the market.

Compared with proof-of-stake chains, where new coins go to anyone who stakes and staked coins still count as circulating, RENDER's new coins go to a narrow group: node operators, grant receivers and the Foundation. That makes the Foundation's release timing the biggest swing factor on a 90-day view. Compared with tokens that run a buyback funded by fees, RENDER has no buyback at all; the burn is the only buyer, and its size follows paid rendering and AI jobs rather than a treasury decision — except when the Foundation chooses to send its own coins to the burn, as it did this window.

## What to watch in the next 90 days

First, the next emission-reserve release: the last came on Aug 10 and Aug 27 2026, so another lump is likely by late November; its size decides most of the next 90 days. Second, the monthly mints on about Oct 23, Nov 23 and Dec 23 2026. Third, the year-4 emission plan: year 3 ends on Dec 19 2026 and no year-4 proposal has been published yet, so a new rate could apply to the December mint. Fourth, the Salad integration approved under RNP-023: its own burn wallets are not live on-chain yet, and it may pull future emissions forward to pay Salad's GPU providers. Fifth, whether the **118,673 RENDER** sitting in the burn wallet is destroyed, and whether the Foundation keeps sending its own coins to the burn.

## Summary

RENDER supply is roughly steady, rising about **0.21%** per 90 days: **1.43M RENDER** reached the market from the monthly emission and a Foundation reserve release, while paid jobs burned **335,705 RENDER**. The mechanism is burn-mint equilibrium on Solana, with a year-3 emission of 5.9M RENDER a year. The key risk is release timing: the Foundation's emission reserve holds **2.999M RENDER** and moves out in quarterly lumps. The ceiling is the long-run supply cap of about 644M RENDER, and supply only shrinks if paid jobs one day burn more than the network mints.

---

*MrNasdog Pressure Framework analysis of RENDER, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 30 2026.*
