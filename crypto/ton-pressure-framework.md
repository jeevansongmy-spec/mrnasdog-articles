---
title:         "TON Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description:   "TON pays for its speed in new coins: a flat block reward minted 50.80M TON in 90 days against a 0.11M fee burn. Framework reads +3.87% net supply growth, monitor +4.44%."
canonical_url: "https://mrnasdog.com/research/ton/inflation"
tags:          ["crypto", "ton", "theopennetwork", "layer1"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/ton/inflation](https://mrnasdog.com/research/ton/inflation)*

# TON Inflation Analysis · September 2026 · Supply growing, projected to keep growing

TON, the native coin of The Open Network and the asset Telegram settles in, grows its supply on three legs at once. The Open Network mints a flat reward into every block, and since the Catchain 2.0 upgrade of **Apr 9 2026** those blocks arrive about six times faster at an unchanged reward, so protocol inflation alone added **50.80M TON** in ninety days. An early-supporter escrow released **16.81M TON** and a Telegram-labelled treasury wallet sent out **40.20M TON**. The only offset is a fee burn worth **0.11M TON** — one part in **465** of the mint. The MrNasdog Pressure Framework reads TON at **+3.87% net** over the last 90 days and **+3.54%** over the next. The coin was renamed **Gram** on **Jun 15 2026**: a label change, not a supply change.

## The verdict, in one paragraph

For the 90-day window ending **Sep 6 2026**, the Pressure Framework reads **TON at +3.87% net**: **107.81M TON** of sell-side supply against **0.11M** removed, on a circulating base of **2.78B TON** out of **5.24B** total, uncapped. The supply monitor reads **+4.44%** — a gap of **0.57 percentage points** that crossed the half-point line and triggered a full source walk. The walk closed it: the monitor divides a market value by a price rounded to two decimals, putting about **±9.4M TON** of noise on a series whose true day-to-day move is near **1.2M**. At full precision over the identical window the same classifier grew **+4.02%**, and the framework's **+107.70M TON** accounts for **100.2%** of it. TON ships with **no data-conflict flag**. The label is **structurally inflationary on an uncompensated block reward**.

## Sell pressure: where new TON comes from

Sell #1, protocol inflation, is **50.80M TON** — the largest line on the page. The Open Network mints a fixed creation fee into every block, **1.7 TON** on the masterchain and **1.0 TON** on the basechain, paid straight to validators. Both constants were read from the live protocol configuration and matched the block accounts on all **13,200** blocks sampled across the window, so the reward has not been cut. What changed is time: Catchain 2.0, activated **Apr 9 2026**, took The Open Network from roughly a **2.5 second** block to about **0.4**, and nothing re-scaled the reward to compensate. So the framework counts blocks rather than dividing an annual rate — **18.97M** masterchain blocks at **0.410 seconds** each and **18.56M** basechain blocks at **0.419**. That is why TON now mints near **3.9%** of total supply a year while tokenomics pages written before the upgrade still quote **0.60%**.

Sell #2, vesting unlocks, is **16.81M TON** — and the number the framework did **not** book is the interesting one. An early-supporter escrow holds **1.26B TON** and pays out in **36** monthly slices to **Oct 2028**. Three slices came due here, worth **109.78M TON** on the published schedule; only **16.81M** left the contract, because vesting on The Open Network is a right to claim, not a transfer. Claiming is easing: **6.22M**, then **6.38M**, then **4.20M TON**. Sell #3, foundation and unscheduled unlocks, is **40.20M TON** from a Telegram-labelled treasury wallet that fired six dated tranches — **5.00M** on **Jun 15 2026**, **0.20M** on **Jun 19**, **5.00M** on **Jun 22**, then **10.00M** each on **Jul 3**, **Aug 8** and **Aug 29**. Sell #4 is **zero**: no estate, and the **1,081.39M TON** frozen in dormant genesis mining wallets stays frozen until **Feb 21 2027**, past both windows.

## Buy pressure: where new TON goes

The Open Network runs no buyback, so Buy #1 is **zero**. The largest listed holder of TON grew its **230.5M TON** position out of staking rewards, and the repurchase plan it announced on **Jul 1 2026** buys back its own shares, not the coin. Buy #3, foundation buying, is **zero** and then some — the treasury wallet is a net seller, down **40.20M TON**. Buy #4, new long-term locks, is **zero**: staking returns stake at each election round, so it is not a lock, and although the legacy TON bridges closed on **Sep 1 2026** leaving **11.35M TON** unredeemable, nobody stated that balance is destroyed, so it is watched as an overhang rather than booked.

That leaves two burns on two mechanisms. Buy #2, the protocol fee burn, destroys exactly **half** of every transaction fee at the masterchain — read off the block accounts rather than a document, where the burned amount is always half the fee left once the block subsidies come out. That came to **0.11M TON**, near **1,214 TON** a day, against **50.80M** minted. Buy #5 is separate: holders sent **3.92K TON** to the unspendable zero address, lifting its balance to **10.64K**. Either can fire while the other stays flat, so they are two flows, not two views of one. TON's entire buy side offsets about **0.2%** of its own mint.

## Foundation and overhang

Four TON overhangs are tracked, and the first two are distinct things that are easy to blur. The early-supporter escrow holds **1.26B TON**, of which **308.98M** has already vested and simply has not been claimed and **951.44M** has not vested; that undrawn **308.98M** is claimable on demand and is the largest overhang on The Open Network. The Telegram-labelled treasury wallet is a different address entirely, holding **112.42M TON**. Third, the governance-frozen genesis mining wallets hold **1,081.39M TON** until **Feb 21 2027** — the largest of them moved **2.6 TON** in ninety days, so the freeze is real. Fourth, **11.35M TON** sits stranded in the two retired bridge contracts. Exchange custody wallets and unlabelled holders are excluded by rule. All four are re-read on the chain at every refresh, and if any balance falls between refreshes the outflow enters Sell #3 at the next refresh.

## How TON compares to other uncapped Layer 1 chains

TON sits in the uncapped continuous-emission Layer 1 class, and inside it TON is unusual because its emission is indexed to **blocks** rather than to time. Most proof-of-stake Layer 1s pay a target annual rate spread across an epoch, so a faster chain changes nothing — the same yearly budget is divided into more slices. The Open Network pays a flat fee per block, which makes block speed and issuance the same lever, and Catchain 2.0 pulled it hard. A capped proof-of-work chain is the opposite: its subsidy halves on a schedule and supply walks toward a ceiling, while TON has no maximum supply at all.

The fee side is the second contrast. Chains whose burn outruns their mint have a large fee economy relative to market value; The Open Network does not. Total transaction fees run near **2,502 TON** a day, about **0.033%** of market capitalisation a year, and because only half is burned the burn line itself is about **0.016%**. Those are two different measurements and are frequently confused — the fee economy is twice the burn. Either way, a burn worth **0.11M TON** cannot bend a mint worth **50.80M**. Exchange-linked tokens that destroy reserve coins quarterly, and perpetual-DEX tokens that route revenue into open-market buying, shrink their float outright; TON has neither.

## What to watch in the next 90 days

First, the block-reward cut: a proposal to take the masterchain reward from **1.7** to **0.35 TON** and the basechain from **1.0** to **0.2** went to validators in **June 2026** and has **not** executed — the live configuration still reads the old constants on **Sep 6 2026**. If it activates it removes roughly four-fifths of the largest line on this page. Second, escrow slices land on **Sep 7 2026**, **Oct 7 2026** and **Nov 6 2026**, each vesting **36.59M TON** against a claim rate near **5.6M** a month. Third, the Telegram treasury wallet has settled into a **10.00M TON** rhythm and the forward column projects three more firings, **30.00M TON** in all. Fourth, block speed itself — a collator activation on **Aug 17 2026** tightened the masterchain interval from **411** to **405 milliseconds**, and the forward column is re-based on it, lifting the forward mint to **51.78M TON**. Fifth, the **Feb 21 2027** thaw of the **1,081.39M TON** genesis freeze is the largest dated supply event ahead.

## Summary

The MrNasdog Pressure Framework reads TON at **+3.87% net** over the trailing 90 days and **+3.54%** over the next, on **107.81M TON** of sell-side supply against **0.11M** removed. The structural mechanism is an uncompensated, block-indexed reward: The Open Network mints **1.7 TON** per masterchain block and **1.0** per basechain block, and Catchain 2.0 made those blocks roughly six times more frequent without repricing them. The key risk is that this is a policy choice — the un-executed proposal to cut the reward to **0.35** and **0.2 TON** would change the page overnight. The ceiling is that there is none: TON has no maximum supply, and beyond the mint there is **1.26B TON** in an escrow running to **Oct 2028**, **112.42M** in a treasury wallet that is actively selling, and **1,081.39M** unfreezing on **Feb 21 2027**.

---

*MrNasdog Pressure Framework analysis of TON, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 6 2026.*
