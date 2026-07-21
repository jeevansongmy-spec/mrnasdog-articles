---
title: "CFG Inflation Analysis · July 2026 · Supply growing, projected to keep growing"
description: "A MrNasdog Pressure Framework read of Centrifuge (CFG): the treasury released 18.59M CFG in 90 days for +4.89% net, with zero buyback or burn. The monitor's −34.06% is a counting change, not a sell."
canonical_url: "https://mrnasdog.com/research/cfg/inflation"
tags: ["crypto", "cfg", "centrifuge", "rwa"]
published: true
---

> Originally published at **[mrnasdog.com/research/cfg/inflation](https://mrnasdog.com/research/cfg/inflation)** by MrNasdog.

# CFG Inflation Analysis · July 2026 · Supply growing, projected to keep growing

Centrifuge's CFG is now a single Ethereum token whose treasury holds most of the supply and has begun releasing it. The Pressure Framework reads **+4.89% net** supply growth over the last 90 days — **18.59M CFG** sent out of the Centrifuge treasury's distribution wallet against a tradable base of **380.38M** — with **zero** buy pressure of any kind. Our monitor reads **−34.06%** for the same window, a **38.95 percentage point** gap that is a counting change rather than a sell, so a ⚠ chip ships.

## The verdict, in one paragraph

For the 90 days to **Jul 21 2026** the framework reads CFG at **+4.89%** net supply growth, driven entirely by treasury distribution, and projects **+1.51%** for the next 90 days on the slower July release rate. Our monitor reads **−34.06%**, a gap of **38.95 percentage points**, which triggers the ⚠ chip. The deep walk settles it without ambiguity: the monitor's own daily series drops from **577.5M** tracked supply on **Jun 8 2026** to **379.3M** on **Jun 9 2026** — a one-day step of roughly 198M tokens while the CFG price moved less than a cent. No burn of that size exists. On-chain, total CFG supply *rose* from **631.19M** to **697.16M** across the same window, and just **115.7K CFG** were destroyed in total. The tracked count was re-based onto Centrifuge's own released-supply definition of 54.6%. CFG is structurally inflationary on the active float, with the inflation delivered by treasury spending rather than by the mint.

## Sell pressure: where new CFG comes from

**Protocol inflation** books at **zero** to market, and the reason matters. Centrifuge mints roughly **3%** of total CFG supply a year, but every newly minted token is paid into the Centrifuge treasury rather than to holders. The chain shows exactly that: 1,401 mint events over the window totalling **66.09M CFG**, of which two batch mints on **Jun 4 2026** — 59.81M and 5.12M — accounted for almost all of it, and both landed in Centrifuge-controlled wallets. That mint closed out the CP149 token migration to its 675M target and swept up the accrued treasury inflation on top. Because Centrifuge's circulating figure is defined as the released bucket, a mint into the treasury changes nothing about the tradable float; counting it here as well as counting the treasury's spending would double-count the same coins.

**Vesting unlocks** also book at **zero**, but for an evidence reason rather than a structural one. No verifiable dated unlock calendar for CFG exists in public today: one unlock tracker still serves a frozen legacy Centrifuge cap table that stopped updating in September 2025, and another quotes an unlock amount that contradicts its own stated percentage and paywalls the schedule. One unusable source is not two, so the row stays opaque — and the framework's released-beats-scheduled rule means the realised on-chain outflow governs anyway.

**Foundation and unscheduled unlocks** carries the entire CFG sell ledger at **18.59M CFG**. Centrifuge's distribution wallet sent **35.46M CFG** out across 81 transfers to 20 distinct addresses over the window. Of that, **16.88M** moved on **Jun 5 2026** into a contract that has never sent a single token out and still holds the full balance, so those coins are excluded as not-yet-market supply. The remaining **18.59M** reached outside parties — about **4.89%** of tradable CFG. The releases were lumpy and front-loaded around the migration close-out: 0.91M in late April, **8.52M** in May, **7.82M** in June, then only **1.34M** in the first 21 days of July. **Long-term locked or bankruptcy** is zero — Centrifuge has no bankruptcy estate and no trustee distributing CFG.

## Buy pressure: where new CFG goes

Every buy row on CFG is zero, and the buy side is the structural weakness of the token. **Programmatic buyback** is zero: the Centrifuge proposal that would have routed Anemoy fund fee revenue into CFG was voted down in **Sep 2025** for failing its quorum, and nothing has replaced it. A later restructuring vote in **Nov 2025** named CFG the protocol's single value-accrual mechanism and handed treasury execution to the Centrifuge Network Foundation, but it specified no buyback, no staking and no burn — it is an intent statement, not a mechanism. **Protocol fee burn** is zero: Centrifuge charges its fees in the assets and in ETH, and none of that destroys CFG. About **115.7K CFG** were burned over the window, all from a single unlabelled contract, but no published mechanism explains them and a second confirming angle does not exist, so the framework discloses rather than counts them.

**Foundation buy** is zero — a treasury funded by minting new CFG has no reason to buy CFG, and no market purchase was observed. **New long-term lock** is zero for the same evidentiary discipline that kept it out of the sell side: the 16.88M sitting untouched since **Jun 5 2026** may well be a vesting or escrow contract, but nothing published names it one, so crediting it as supply removed from the market would be an invention. It is tracked as an overhang instead.

## Foundation and overhang

The overhang is the dominant fact about CFG. Total supply is **697.16M** and only **380.38M** counts as tradable, leaving **316.78M CFG** — roughly 45% of everything — in Centrifuge-controlled or unreleased buckets. Three pools are individually tracked. The Centrifuge reserve wallet holds **143.07M CFG** as of **Jul 21 2026**, up from 103.26M at the start of the window after the **59.81M** mint on **Jun 4 2026**; it has never sent tokens anywhere except to the distribution wallet. The distribution wallet itself holds **4.02M CFG** and is the pipe through which everything reaches the market. The unlabelled contract holds **16.88M CFG** and has made zero outgoing transfers since it was funded. Behind all three sit the documented allocations: team at 12% vesting to May 2030, the CP149 incentive pool of 100M vesting into the treasury to April 2029, ecosystem at 14.3%, and other stakeholders to March 2028. If any of these balances falls between refreshes, that outflow enters the Foundation and unscheduled unlocks row at the next refresh.

## How CFG compares to other RWA and governance tokens

CFG belongs to the governance-token class whose protocol succeeds without the token being needed. Centrifuge's real-world-asset business is genuinely working — the Janus Henderson JAAA AAA CLO fund runs on it, Kraken Custody added JAAA as its first tokenized RWA in **Jun 2026**, and New York Life Investment Management signed on in **Jul 2026** — but none of that activity requires anyone to buy CFG, and none of the fee revenue reaches it. That is the opposite of an exchange token with a quarterly buyback, where revenue mechanically retires supply, and it is a weaker position than a fee-burn chain like Ethereum, where usage destroys the asset by protocol rule.

Against capped proof-of-work assets the contrast is sharper still. A halving-model coin has a fixed, falling issuance schedule that no committee can change; CFG has uncapped 3% annual inflation controlled by governance, with the mint directed to a treasury that then decides discretionary release timing. That combination — uncapped emission plus a large discretionary reserve plus zero structural demand — puts CFG at the inflationary end of its own class. Its closest structural analogues are other post-migration governance tokens where a foundation holds a majority of supply and the release calendar is a decision rather than a rule.

The one genuine mitigant is that the mint itself is off-market. Unlike a proof-of-stake chain that pays inflation directly to stakers who can sell it the same day, CFG's new supply enters a treasury first, which means the framework can watch the treasury wallets and see the pressure coming before it lands.

## What to watch in the next 90 days

Watch the Centrifuge reserve wallet balance, currently **143.07M CFG** — any fall is direct evidence of the next distribution round, and it is the single most informative number on this token. Watch whether the July release rate of roughly **1.9M CFG** a month holds or reverts to the May and June pace near 8M a month, which is the difference between the projected **+1.51%** and something three times larger. Watch the 16.88M contract funded on **Jun 5 2026** for its first outgoing transfer, which would convert a tracked overhang into realised sell pressure. Watch Centrifuge governance for any return of the fee-switch or buyback proposal that failed quorum in **Sep 2025**, since it is the only thing that would put a non-zero figure on the buy side. And watch whether the quarterly earnings calls promised under the Foundation restructuring publish a treasury balance and release schedule, which would close the vesting row's current opacity.

## Summary

The MrNasdog Pressure Framework reads Centrifuge's CFG at **+4.89%** net supply growth over the 90 days to **Jul 21 2026** and **+1.51%** projected forward — inflationary on both windows, with no buyback, no fee burn and no offsetting demand anywhere in the ledger. The mechanism is unusual and worth stating precisely: CFG's 3% annual mint goes to the Centrifuge treasury rather than to the market, so the pressure arrives when the treasury spends, and it spent **18.59M CFG** this window. The key risk is the **316.78M CFG** — about 45% of all supply — held outside the tradable float on a discretionary release schedule, of which **143.07M** sits in one reserve wallet. There is no supply ceiling to constrain any of it; emission is uncapped and governance-controlled, which makes the treasury's own conduct the entire supply story for CFG.

---

*MrNasdog Pressure Framework analysis of CFG, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 21 2026.*
