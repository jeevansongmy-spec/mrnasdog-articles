---
title: "CFG Inflation Analysis · August 2026 · Supply was growing, trend cooling"
description: "A MrNasdog Pressure Framework read of Centrifuge (CFG): the treasury released ~15.7M CFG in 90 days for +4.13% net, but distribution has stopped and the forward read is +0.45%. The monitor's −33.92% is a counting change, not a sell."
canonical_url: "https://mrnasdog.com/research/cfg/inflation"
tags: ["crypto", "cfg", "centrifuge", "rwa"]
published: true
---

> Originally published at **[mrnasdog.com/research/cfg/inflation](https://mrnasdog.com/research/cfg/inflation)** by MrNasdog.

# CFG Inflation Analysis · August 2026 · Supply was growing, trend cooling

Centrifuge's CFG is now a single Ethereum token whose treasury holds most of the supply, spent hard around the June migration, and has since gone quiet. The Pressure Framework reads **+4.13% net** supply growth over the last 90 days — about **15.7M CFG** sent out of the Centrifuge treasury's distribution wallet against a tradable base of **380.38M** — but projects only **+0.45%** forward as the distribution stops, with **zero** buy pressure of any kind. Our monitor reads **−33.92%** for the same window, a gap of about **38 percentage points** that is a counting change rather than a sell, so a ⚠ chip ships.

## The verdict, in one paragraph

For the 90 days to **Aug 3 2026** the framework reads CFG at **+4.13%** net supply growth, driven entirely by treasury distribution, and projects **+0.45%** for the next 90 days as that distribution decelerates to near zero. Our monitor reads **−33.92%**, a gap of about **38 percentage points**, which triggers the ⚠ chip. The deep walk settles it without ambiguity: the monitor's own daily series drops from **577.5M** tracked supply on **Jun 8 2026** to **379.3M** on **Jun 9 2026** — a one-day step of roughly 198M tokens while the CFG price moved less than a cent. No burn of that size exists. On-chain, total CFG supply actually *rose* to about **700.3M** by **Aug 3 2026**. The tracked count was simply re-based onto Centrifuge's own released-supply definition of 54.6%. CFG is inflationary on the active float, but the inflation is delivered by discretionary treasury spending — which has just paused — rather than by the mint.

## Sell pressure: where new CFG comes from

**Protocol inflation** books at **zero** to market, and the reason matters. Centrifuge mints roughly **3%** of total CFG supply a year, but under CP149 that inflation accrues entirely to the Centrifuge DAO treasury rather than to holders — the EVM chain has no collators to pay, so the mint simply lands in a project wallet. The chain shows exactly that: total supply climbed to about **700.3M**, and a fresh read of the distribution wallet shows it absorbing the newest mint without passing it on. Because Centrifuge's circulating figure is defined as the released bucket, a mint into the treasury changes nothing about the tradable float; counting it here as well as counting the treasury's spending would double-count the same coins.

**Vesting unlocks** also book at **zero**. There is a real vesting stream — the **100M** CP149 incentive allocation minted in 2025 vests linearly to **April 2029** — but it vests into the Centrifuge Network Foundation's own wallets, not onto the market, and no verifiable public unlock calendar exists to date its market release. Under the framework's released-beats-scheduled rule, the realised on-chain outflow from those foundation wallets governs, and that outflow is the next row.

**Foundation and unscheduled unlocks** carries the entire CFG sell ledger at about **15.7M CFG** over the window — roughly **4.1%** of tradable CFG. That figure is real but front-loaded and non-recurring: the Centrifuge distribution wallet released around **6.5M** in May and **7.8M** in June as the CP149 migration closed out, then only about **1.3M** in early July and essentially nothing from mid-July into August. A fresh on-chain read confirms the wallet has since been absorbing the ongoing mint with zero net outflow to third parties — the spending has stopped for now. **Long-term locked or bankruptcy** is zero: Centrifuge has no bankruptcy estate and no trustee distributing CFG.

## Buy pressure: where new CFG goes

Every buy row on CFG is zero, and the buy side is the structural weakness of the token. **Programmatic buyback** is zero: Centrifuge has implemented a fee switch charging 25–50 basis points on assets under management to build "buyback readiness," but the buyback proposal itself failed to reach its voting quorum and nothing is live. A separate restructuring vote named CFG the protocol's single value-accrual mechanism and handed treasury execution to the Centrifuge Network Foundation, but it specified no buyback, no staking and no burn — it is an intent statement, not a mechanism. **Protocol fee burn** is zero: Centrifuge charges its fees in the assets and in ETH, and none of that destroys CFG. Only a tiny amount of CFG has ever been burned, by a single unlabelled contract with no published mechanism, so the framework discloses rather than counts it.

**Foundation buy** is zero — a treasury funded by minting new CFG has no reason to buy CFG, and no market purchase was observed. **New long-term lock** is zero for the same evidentiary discipline: the **16.88M** sitting untouched in a contract since **Jun 5 2026** may well be a vesting or escrow contract, but nothing published names it one, so crediting it as supply removed from the market would be an invention. It is tracked as an overhang instead.

## Foundation and overhang

The overhang is the dominant fact about CFG. Total supply is about **700.3M** and only **380.38M** counts as tradable, leaving well over **300M CFG** — roughly 45% of everything — in Centrifuge-controlled or unreleased buckets. Three pools are individually tracked from fresh on-chain reads. The Centrifuge reserve wallet holds **143.07M CFG**, unchanged since the previous check; it has never sent tokens anywhere except to the distribution wallet. The distribution wallet itself holds about **7.19M CFG** — up as it absorbs the fresh mint — and is the pipe through which everything reaches the market. The unlabelled contract holds **16.88M CFG** and has made zero outgoing transfers since it was funded. Behind all three sit the documented allocations: the team at 12%, the CP149 incentive pool of 100M vesting to April 2029, ecosystem at 14.3%, and other stakeholders. If any of these balances falls between refreshes, that outflow enters the Foundation and unscheduled unlocks row at the next refresh.

## How CFG compares to other RWA and governance tokens

CFG belongs to the governance-token class whose protocol succeeds without the token being needed. Centrifuge's real-world-asset business is genuinely working — the Janus Henderson JAAA AAA CLO fund runs on it, Kraken Custody added JAAA as its first tokenized RWA in **Jun 2026**, and New York Life Investment Management signed on in **Jul 2026** — but none of that activity requires anyone to buy CFG, and none of the fee revenue reaches it yet. That is the opposite of an exchange token with a quarterly buyback, where revenue mechanically retires supply, and it is a weaker position than a fee-burn chain like Ethereum, where usage destroys the asset by protocol rule.

Against capped proof-of-work assets the contrast is sharper still. A halving-model coin has a fixed, falling issuance schedule that no committee can change; CFG has uncapped 3% annual inflation controlled by governance, with the mint directed to a treasury that then decides discretionary release timing. That combination — uncapped emission plus a large discretionary reserve plus no live structural demand — puts CFG at the inflationary end of its own class. Its closest structural analogues are other post-migration governance tokens where a foundation holds a majority of supply and the release calendar is a decision rather than a rule.

The one genuine mitigant is that the mint itself is off-market. Unlike a proof-of-stake chain that pays inflation directly to stakers who can sell it the same day, CFG's new supply enters a treasury first, which means the framework can watch the treasury wallets and see the pressure coming before it lands — and right now those wallets are holding, not spending.

## What to watch in the next 90 days

Watch the Centrifuge reserve wallet balance, currently **143.07M CFG** — any fall is direct evidence of the next distribution round, and it is the single most informative number on this token. Watch whether the distribution wallet, which has been quietly absorbing the mint since mid-July, resumes the May and June release pace near **8M** a month, which is the difference between the projected **+0.45%** and something several times larger. Watch the 16.88M contract funded on **Jun 5 2026** for its first outgoing transfer, which would convert a tracked overhang into realised sell pressure. Watch Centrifuge governance for any return of the buyback proposal that failed quorum, since it is the only thing that would put a non-zero figure on the buy side. And watch whether the Foundation publishes a treasury balance and release schedule, which would close the vesting row's current opacity.

## Summary

The MrNasdog Pressure Framework reads Centrifuge's CFG at **+4.13%** net supply growth over the 90 days to **Aug 3 2026** but only **+0.45%** projected forward — the last window was inflationary, but the trend is cooling as the migration-driven distribution stops, and there is no buyback, no fee burn and no offsetting demand anywhere in the ledger. The mechanism is unusual and worth stating precisely: CFG's 3% annual mint goes to the Centrifuge treasury rather than to the market, so the pressure arrives only when the treasury spends — and it has just stopped spending. The key risk is the roughly **300M+ CFG** — about 45% of all supply — held outside the tradable float on a discretionary release schedule, of which **143.07M** sits in one reserve wallet. There is no supply ceiling to constrain any of it; emission is uncapped and governance-controlled, which makes the treasury's own conduct the entire supply story for CFG.

*MrNasdog Pressure Framework analysis of CFG, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 3 2026.*
