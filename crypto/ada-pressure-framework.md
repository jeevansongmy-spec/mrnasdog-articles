---
title:         "ADA Inflation Analysis · August 2026 · Supply was growing, trend cooling"
description:   "Supply growing, trend cooling: Cardano added ~485M ADA in 90 days — 115M reserve release plus 390M voted from its treasury. No burn, no buyback. Net +1.29%."
canonical_url: "https://mrnasdog.com/research/ada/inflation"
tags:          ["crypto", "ada", "cardano", "layer1"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/ada/inflation](https://mrnasdog.com/research/ada/inflation)*

# ADA Inflation Analysis · August 2026 · Supply was growing, trend cooling

Over the last 90 days about **484.8M ADA** reached the tradable float on Cardano — **114.8M** released from the Cardano protocol reserve and a far larger **389.6M** voted out of the on-chain Cardano treasury, against only **19.6M** handed back. The MrNasdog Pressure Framework reads ADA at **+1.29%** net for the window and **+0.31%** forward; our independent supply monitor reads **+1.32%**, a gap of **0.03 percentage points**. Cardano is hard-capped at 45 billion ADA and mints nothing above it — but the cap is a ceiling, not a brake, and the treasury, not the reserve, is now the bigger of Cardano's two taps.

## The verdict, in one paragraph

For the 90-day window ending **Aug 22 2026**, the Pressure Framework reads Cardano at **+1.29%** net new supply — total sell pressure of **504.4M ADA** against buy pressure of **19.6M ADA**, divided by a circulating supply of **37,492M ADA**. Our independent supply monitor reads **+1.32%** for the same window, a gap of only **0.03 percentage points** — comfortably inside tolerance, so no data-conflict flag is raised on the ADA overview. The two readings agree because they measure the same quantity from opposite ends: the framework sums the on-chain flows into the float, while the monitor measures the float itself. That agreement matters here, because it is what lets the forward call carry weight. Looking ahead the framework reads **+0.31%**, and the reason is not the reserve — it is that Cardano's treasury spending has run out of approved things to spend on. ADA in August 2026 is a **capped chain with a discretionary tap**: the protocol half of its inflation is decaying on schedule, and the governance half is now the whole story.

## Sell pressure: where new ADA comes from

Cardano's protocol inflation contributed **114.8M ADA** over the window. Cardano never mints above its 45 billion cap. Instead new ADA is released from a protocol reserve: every five-day epoch a fixed fraction of what is left in that reserve moves into a reward pot, one fifth of the pot is taken by the on-chain Cardano treasury, and the rest is paid to stake pools and delegators. The reserve fell by **182.1M ADA** over the window, but **67.2M** of that never reached the market — it was absorbed by the treasury, which is not circulating supply. Only the remaining **114.8M** is real sell pressure, and an independent read of the staking rewards actually distributed epoch by epoch lands on the same figure. Because the release is a fraction of a shrinking reserve, this tap gets smaller every epoch by construction — Cardano's protocol inflation is disinflationary without needing a halving.

Vesting unlocks contributed **zero**. Cardano has no vesting cliff left to unlock: the public sale and the three founding-organisation allocations finished releasing in 2019, so there is no schedule, no cliff and no locked tranche pending. This is one of the few large-cap tokens where the unlock question is genuinely closed.

The Foundation and unscheduled-unlock row is where Cardano's real inflation lives: **389.6M ADA**, from **26** treasury withdrawal governance actions enacted on-chain inside the window. Two of them dominate: a **131.5M ADA** development budget batch that enacted on **May 29 2026**, and the **120.0M ADA** "Cardano PRIME" open-market liquidity withdrawal, ratified **Aug 12 2026** with 80.1% of voting stake in favour and enacted at the epoch boundary on **Aug 17 2026**. That last one is worth stating plainly: it is realised, not pending. The Cardano treasury balance fell by **116.4M ADA** net at that boundary, and the ADA is now inside the circulating float — even though most of it sits with an administrator behind staggered release gates rather than on an order book. The framework books ADA when it leaves the non-circulating treasury, not when someone sells it.

Long-term locked or bankruptcy supply contributed **zero**. No bankruptcy estate, trustee or court-supervised distribution releases ADA on a schedule, so there is nothing arriving from that side and nothing to watch.

## Buy pressure: where new ADA goes

There is no programmatic buyback on Cardano — **zero**. No protocol contract buys ADA, and no treasury-funded buyback has been deployed. A 2026 funding model under which the Cardano treasury would take stakes in ecosystem projects and recycle returns into open-market ADA purchases has been publicly discussed, but nothing has been voted on-chain and no purchase has been observed, so it scores nothing.

Protocol fee burn is also **zero**, and this is structural rather than incidental. Cardano destroys nothing. Every transaction fee is pooled at the end of the epoch and recycled — one fifth to the on-chain treasury, the rest to stakers. Where an Ethereum-style base-fee burn converts network usage into supply reduction, Cardano converts network usage into staking yield. Usage on Cardano can rise without the supply curve bending at all, and that is the single biggest structural difference between ADA and the burn-model chains it is usually compared to.

Foundation buying is **zero**, and the disclosed direction of travel is the other way. The Cardano Foundation's latest published accounts show **561M ADA** held at the last year-end, down from **599M**, with ADA falling to **51.6%** of roughly **$361M** in total assets while bitcoin and cash took a larger share. No open-market ADA purchase is disclosed anywhere.

New long-term locks are **zero** as well. Cardano staking is non-custodial and non-locking: delegated ADA never leaves the owner's wallet and can be spent at any time, so the roughly **21.5B ADA** shown as active stake removes nothing from tradable float. A large staking ratio is a security number on Cardano, not a supply number. The only genuine offset in the window is a fifth row: **19.6M ADA** donated back into the on-chain treasury, almost all of it in a single transfer on **Jun 28 2026**. That ADA does leave circulation — but a future spending vote can release it again.

## Foundation and overhang

Two identified overhangs sit behind ADA. The first is the **on-chain Cardano treasury**, which still held **1,341.1M ADA** at the close of the window. It is not a multisig or a custodial wallet but a protocol-level pot, readable directly on-chain and refreshed on every rebuild, and it has no fixed release schedule — every ADA leaving it does so by governance vote. The second is the **Cardano Foundation's** own reserves, **561M ADA** at the last published year-end. That holding is opaque at wallet level — no per-address disclosure exists — so it is tracked through the Foundation's published accounts rather than on-chain. It is worth being precise about why the Foundation's ADA scores zero rather than a sale estimate: those coins are already inside the circulating float, so a Foundation disposal moves price, not supply. The Cardano treasury and the Cardano protocol reserve are different — both sit outside circulating supply, which is exactly why their outflows are booked as new float.

What is deliberately not listed is the **6,166.6M ADA** protocol reserve itself. It is not a team-controlled overhang: no entity can accelerate it, it is released mechanically by the consensus rules, and it is already booked continuously in the protocol inflation row. There is no unscheduled-unlock pool, no buyback accumulation wallet, no separately identified founding-entity multisig with a published balance, and no bankruptcy-estate residual. If either the treasury balance or the Foundation's disclosed ADA holding falls between refreshes, that outflow enters the Foundation and unscheduled-unlock row at the next refresh.

## How ADA compares to other proof-of-stake layer-1 chains

Against uncapped proof-of-stake layer-1s, Cardano's protocol half looks good and its governance half looks unusual. Chains like Ethereum, Solana and Avalanche mint new units against no ceiling; Cardano cannot exceed 45 billion ADA, and its reserve release is a fraction of a shrinking pool, so the protocol tap approaches zero without any scheduled event. That is a genuinely stronger cap story than most of its peers can tell. But Cardano is also one of the very few large chains where a second, discretionary tap sits alongside the protocol one: a treasury that voters can open. Over this window the treasury released more than three times what the protocol did.

Against the burn-model chains, the contrast is sharper still. Ethereum burns its base fee, so usage removes supply; BNB runs a quarterly programmatic burn; several exchange tokens buy back and destroy. Cardano has neither burn nor buyback, and it never will without a protocol change, because fees are recycled to stakers and the treasury by design. That means ADA has no mechanism at all that can turn a busy quarter into a shrinking supply — the best case for ADA is a supply that stops growing, not one that shrinks. Against halving-model chains with hard caps such as Bitcoin and Litecoin, Cardano shares the cap and the decaying issuance but adds the treasury, which is the part a halving chain simply does not have. The right mental model for ADA is a capped chain with a parliament: the issuance curve is predictable and the spending curve is a vote.

## What to watch in the next 90 days

The single biggest item is **Sep 1 2026**, when five of Cardano's eight constitutional-committee seats expire. That would leave three against a protocol minimum of five, and below the minimum no treasury withdrawal, protocol-parameter change or hard fork can be ratified until seats are refilled. The on-chain renewal action stood at **39%** of DRep stake and **11%** of pool stake as of **Aug 23 2026**, against bars of 67% and 51% — so the base case is that Cardano treasury spending pauses. Second, the two remaining live spending votes, together worth **4.3M ADA**, close on **Sep 16 2026**; they are the entire live queue. Third, watch for a new net change limit: no spending ceiling for the current epoch range has ever been ratified — three attempts failed, the most recent expiring on **Aug 2 2026** — while more than 600M ADA of funding requests are reportedly waiting. Fourth, the Cardano protocol reserve keeps draining regardless of governance, and a rebuild should re-read it every cycle. Fifth, the Cardano Foundation publishes its accounts annually in the spring; a materially smaller ADA holding there is the trigger to revisit the Foundation row.

## Summary

Cardano added about **+1.29%** to its ADA float over the 90 days to **Aug 22 2026**, and roughly four fifths of that came from governance rather than from the protocol: **389.6M ADA** of enacted treasury withdrawals against **114.8M** of reserve release, offset only by **19.6M** returned to the treasury. Our independent monitor reads **+1.32%**, so the reading is corroborated rather than contested. The structural risk in ADA is not the emission curve — that decays on its own under a 45 billion hard cap — it is that Cardano has no burn and no buyback, so the only thing that can slow supply growth is the electorate deciding not to spend. That, for now, is what appears to be happening: with committee seats lapsing on **Sep 1 2026**, no ratified spending ceiling, and a live queue of just **4.3M ADA**, the framework projects **+0.31%** for the next 90 days. Quiet by circumstance, not by design.

---

*MrNasdog Pressure Framework analysis of ADA, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 23 2026.*
