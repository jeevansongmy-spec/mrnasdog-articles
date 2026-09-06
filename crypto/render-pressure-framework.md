---
title: "RENDER Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description: "Mint beats burn 5 to 1: Render Network created 1.48M RENDER over 90 days and destroyed 0.28M on 14,413 job payments. The framework reads +0.23% net supply."
canonical_url: "https://mrnasdog.com/research/render/inflation"
tags: ["crypto", "render", "render-network", "solana"]
published: true
---

> Originally published at **[mrnasdog.com/research/render/inflation](https://mrnasdog.com/research/render/inflation)** by MrNasdog.

**TL;DR.** Render Network runs a burn-and-mint equilibrium, and the mint side is still several times the burn side. Over the 90 days to **Sep 6 2026** the Render Network created **1.48M RENDER** — three fixed emission tranches of **492,132** RENDER plus a **5,000** RENDER grant mint — and destroyed **0.28M RENDER** across **14,413** GPU rendering and AI compute job payments worth **$235,547**. That is **5.4** RENDER minted for every one burned. The MrNasdog Pressure Framework reads RENDER at **+0.23% net** supply growth against a supply monitor reading of **−0.11%** — a gap of **0.34 percentage points**, inside tolerance, so no data-conflict flag ships this month.

## The verdict, in one paragraph

The Render Network burn is real, and it is still far too small to turn its own supply around. The Pressure Framework reads the 90 days to Sep 6 2026 at **+0.23%** net new RENDER against a circulating base of **518.77M**, and projects **+0.23%** for the next 90 days on the same emission budget. The supply monitor reads **−0.11%** over the same window, a difference of **0.34 percentage points** — small enough that the two measures agree, which is worth noting because last month they did not. That earlier disagreement came from treating the Render Network bridge wallet's **996,178** RENDER draw-down as a release; this build proved it is a one-for-one chain swap, because the legacy Ethereum bridge address took in **996,178** RNDR across **4,707** transfers over the identical window and sent out nothing. RENDER is structurally inflationary on a fixed, governed emission budget, with a burn that scales only with paid GPU demand.

## Sell pressure: where new RENDER comes from

All of RENDER's sell pressure is protocol inflation, and all of it is one mechanism. Sell #1 is **1,481,396** RENDER: three identical burn-and-mint emission tranches of **492,132** RENDER minted on **Jul 1 2026**, **Jul 23 2026** and **Aug 23 2026**, each splitting **432,132** into the node-reward vault and **60,000** into the operations vault, plus a single **5,000** RENDER grant mint on **Sep 1 2026**. One key on Solana is the only account that can create a RENDER coin, and all **101** signatures it has produced since December 2023 were walked for this reading, so the mint count is complete rather than sampled. Governance proposal **RNP-022** fixes the year-three budget at **5.9M** RENDER between Dec 20 2025 and Dec 19 2026; twelve tranches of 492,132 comes to 5,905,584, so chain and governance agree to under 0.1%.

Sell #2, vesting unlocks, is **zero**: every allocation from the original RNDR distribution is released and no unlock tracker carries a remaining cliff for this window or the next. Sell #3, Foundation and unscheduled unlocks, is also **zero** — the interesting zero on this page, explained in full below. Sell #4, long-term locked or bankruptcy supply, is **zero** because Render Network has no estate, no trustee schedule and no unwinding lock releasing coins.

## Buy pressure: where new RENDER goes

Buy #2, the protocol fee burn, is RENDER's entire buy side at **275,805.49** RENDER. In the burn-and-mint equilibrium a rendering or AI compute job is priced in fiat, settled by the customer, and the RENDER it converts to is destroyed. Two settlement escrows did that work across **14,413** transactions in this window: the main buy-and-burn escrow destroyed **264,499.74** RENDER against **$218,964** of stablecoin taken in, and a second dispersed-burn escrow destroyed **11,305.75** against **$16,583**. Both were reconciled against their own on-chain balances at each end of the window and both close to the decimal, which matters on this token because the Render Network's own per-burn export is known to return self-consistent zeros. The pace is easing slightly: **3,073** RENDER a day over the first half of the window against **2,804** over the second.

Buy #1, programmatic buyback, is **zero** even though a genuine open-market bid exists. Customer stablecoin is swapped into RENDER on a Solana decentralized exchange and burned inside the same transaction signature, so the purchase and the destruction are one flow, not two; booking it in both rows would double the entire buy side of a coin whose buy side is the whole argument. It is counted once, in the fee-burn row. Buy #3, Foundation buy, is **zero**: no wallet on the Render Network Foundation's own published list bought RENDER and kept it this window. Buy #4, new long-term lock, is **zero** because Render Network has no staking and no lock contract to put coins into.

## Foundation and overhang

The Render Network Foundation publishes its own registry of **18** team wallets, and all 18 were read at both ends of this window. Their combined balance moved from **96,925,190** RENDER to **96,369,303** — and that end figure reproduces the Foundation's own published total exactly, which is what makes the enumeration checkable. The largest single overhang is a partner treasury vault holding **81,897,507** RENDER, about **15.8%** of circulating supply, on no published release schedule; it moved **6,361** RENDER in 90 days. Behind it sit the bridge escrow at **9,767,165**, the node-emissions vault at **2,566,770**, a second treasury vault at **478,300**, the operations vault at **900,124** and a burn-rewards escrow of **570,425** that has not moved since December 2023.

Sell #3 is nonetheless zero, and the arithmetic is the reason. Excluding the bridge conduit and the two burn escrows, the Render Network Foundation perimeter **grew** by **454,953** RENDER over the window while taking in 1,481,396 RENDER of fresh emission — so every payout it made was funded by coins already counted as protocol inflation above, and nothing held before the window was let go. The bridge escrow's **996,178** RENDER draw-down is a chain swap, matched to a tenth of a coin by legacy RNDR locked on Ethereum in the same window. Exchange custodial wallets and unlabelled large holders are deliberately excluded — none appears on the Foundation registry, so those coins belong to depositors or to no identified group. If any registry balance falls between refreshes, that outflow enters Sell #3 at the next refresh.

## How RENDER compares to other burn-and-mint DePIN networks

RENDER belongs to the burn-and-mint class of DePIN tokens, where the token is destroyed to buy network work and re-issued to pay the suppliers of that work. The class promises that demand can eventually outrun issuance and flip the token deflationary. Mechanically that only happens when burn exceeds mint, and RENDER is currently **5.4** to one the other way. Helium runs the same structure with data credits and has spent years in the same position; the shape is normal for the class rather than a mark against Render Network specifically.

Against an uncapped continuous-emission Layer 1, RENDER is better placed: its issuance is a fixed annual budget set by a governance vote, not a perpetual staking yield, and the budget steps down over time rather than compounding with the token's own market value. Against a hard-capped, halving-model chain like Bitcoin, it is worse placed: RENDER's mint authority is live, its freeze authority is live, and its **644.17M** ceiling is a governance commitment rather than a protocol-enforced cap. Against an exchange token that buys and burns from revenue, RENDER is structurally different in an important way — an exchange token's burn scales with trading volume it already captures, while RENDER's burn scales only with GPU jobs actually paid for, so the buy side tracks GPU jobs settled rather than market activity.

## What to watch in the next 90 days

The next emission tranche of about **492,132** RENDER is due in **late Sep 2026** on the roughly 30-day pattern the mint authority has kept all year; three tranches fall inside the next 90 days. The year-three budget under RNP-022 expires **Dec 19 2026**, and a fresh governance vote must set year four — the single most consequential dated item on this token, because the last two budgets cut issuance by about 35%. Watch the burn rate, currently **2,804** RENDER a day and drifting down; a sustained move above **4,000** a day would be the first sign the burn side is closing on the mint. Watch the partner treasury vault holding **81,897,507** RENDER, whose only movement in 90 days was 6,361 coins. And watch the Solana-to-Ethereum bridge balance, which stayed neutral this window; any divergence between the two sides would change how much of the float is genuinely tradable.

## Summary

The MrNasdog Pressure Framework reads RENDER at **+0.23%** net supply growth over the 90 days to Sep 6 2026 and **+0.23%** for the next 90 days — mixed flows, supply roughly steady rather than shrinking. The structural mechanism is a burn-and-mint equilibrium in which a governed **5.9M** RENDER annual emission budget is spent on node rewards and operations while paid GPU work destroys coins, and the mint side is currently **5.4** times the burn side. The key risk is the **81,897,507** RENDER partner treasury vault sitting on no published release schedule, roughly 15.8% of circulating supply, alongside a live mint authority that means no part of this supply is protocol-locked. The ceiling is **644.17M** RENDER against **518.77M** circulating today — real headroom, and a governance commitment rather than a hard cap.

---

*MrNasdog Pressure Framework analysis of RENDER, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 6 2026.*
