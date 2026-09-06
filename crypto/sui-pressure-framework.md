---
title: "SUI Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description: "Sui released 67.34M SUI in 90 days (39.94M unlocks + 27.40M subsidy) against 137.58K of non-refundable storage fees. Framework +1.64% net; monitor +1.73%."
canonical_url: "https://mrnasdog.com/research/sui/inflation"
tags: ["crypto", "sui", "layer1", "vesting"]
published: true
---

*Originally published at [mrnasdog.com/research/sui/inflation](https://mrnasdog.com/research/sui/inflation)*

# SUI Inflation Analysis · September 2026 · Supply growing, projected to keep growing

Sui released **67.34M SUI** in 90 days — **27.40M** from the Sui staking subsidy, **39.94M** from the Sui Foundation's monthly calendar — against a buy side of **137.58K SUI**, the part of a Sui storage deposit that is never refunded. The MrNasdog Pressure Framework reads SUI at **+1.64% net** trailing and **+1.54%** forward, against a supply monitor at **+1.73%** — a **0.09 percentage point** gap, which is agreement. SUI is capped at **10B** and no function can raise it, but only **41%** circulates: the unlock calendar, not a mint, is the whole story.

## The verdict, in one paragraph

For the 90 days ending **Sep 6 2026** the framework reads **SUI at +1.64% net**: **67.34M SUI** of new float against **137.58K** of offset, on a base of **4,096.5M SUI**. The supply monitor reads **+1.73%** — a **0.09 percentage point** gap, far inside tolerance, so this build ships **no data-conflict flag**. They agree structurally: the Sui Foundation publishes its own monthly circulating-supply series and the framework books that series rather than inferring one. The forward column reads **+1.54%**, softer because the Sui staking subsidy is cut again on **Oct 14 2026**. SUI is **structurally inflationary on the active float**.

## Sell pressure: where new SUI comes from

Sell #2, vesting unlocks, is the largest row at **39.94M SUI** trailing and **38.76M** forward. Sui does not release in annual cliffs; the Sui Foundation steps circulating supply up on the 1st of each month, on a calendar running to **May 2030**, drawing from the Sui community reserve, the Mysten Labs treasury and the early-contributor allocation. Three firings land inside the window at full quantum: **Jul 1 2026** at **23.14M SUI**, **Aug 1** at **22.20M**, **Sep 1** at **22.01M**. Dated reporting splits the August unlock **4M** community reserve, **7.65M** early contributors, **2.07M** Mysten treasury. The calendar is decaying: the Series B vest ended **May 1 2026** and the step fell from **52.03M** to **23.78M**, sliding to **20.60M** due **Dec 1 2026**.

Sell #1, protocol inflation, is the Sui staking subsidy — a finite escrow, not an open-ended mint. Read from the Sui mainnet system state, the network pays **282,429.54 SUI** an epoch, and a Sui epoch is one day. The escrow is readable at both window ends: **266.11M SUI** ninety epochs ago, **239.50M** now, and summing the ninety distributions one by one gives the identical **26.61M SUI** — log and balance closing to **zero**. The three monthly steps inside the window carried **27.40M** of that subsidy, and that is the row. The rate is cut **10%** every 90 epochs on a rule no vote reverses: it stepped **Jul 16 2026** from **313,810.60**, and steps again **Oct 14 2026** to **254,186.58**.

One trap would double the Sui sell side: the monthly step is not pure vesting, and the project says so — subsidy releases are incorporated into the SUI emission schedule. The framework books the steps **net** of that share and lets Sell #1 carry the subsidy alone, so the two rows add to exactly the **67.34M SUI** released. Sell #3 is **zero** — nothing left an identified Sui team wallet off-calendar. Sell #4 is **zero** by construction: no estate, no trustee schedule, no court-ordered release.

## Buy pressure: where new SUI goes

Buy #1, the programmatic buyback, is real, published, and for supply purposes **zero**. The Sui Foundation converts stablecoin-reserve yield into open-market SUI purchases and publishes every session: **601,800 SUI** for about **$435,100** across **72** sessions between **Jun 22 2026** and **Sep 4 2026**. The destination decides the row. Bought SUI is neither burned nor held — the Sui Foundation states it reinvests the coins into the ecosystem rather than removing supply, handing them to lending and trading partners, validators and grant programmes. Bought and passed straight back out is a redistribution loop, not a sink.

Buy #2, protocol fee burn, is **zero** because Sui destroys nothing, tested two ways: total SUI supply read exactly **10B** at both window ends, and Sui has no dead-address sink. The recycling is provable — across **90** epochs Sui stake rewards came to **26.82M SUI**, the subsidy inside them to **26.61M** and Sui computation charges to **210.32K**, reconciling within **3.95 SUI**. Buy #3 is zero beyond the buyback. Buy #4 is zero, and Sui makes the reason clear: total stake is **6,976.43M SUI**, more than circulating supply itself because locked SUI can be staked before it vests — and it **fell** from **7,252.92M** across the window.

That leaves one genuine removal, Buy #5. Every object on Sui carries a storage deposit; the refundable part returns on deletion, but a share never does, and the Sui Foundation itself calls those coins permanently removed from circulation. The Sui storage fund grew **167.82K SUI**, read from state at both ends and matched to its inflow and outflow legs within **3.95 SUI** — but only the **137.58K** that can never be refunded is counted.

## Foundation and overhang

The overhang is the largest single fact about SUI supply: **5,903.46M SUI**, about **59%** of the Sui cap, sits outside the circulating count, and most of it has no calendar. The published series ends in **May 2030** at **4,782.79M SUI**, leaving **5,217.21M** with no release date and the Sui Foundation deciding when it moves; another **686.26M** is queued between now and then. The Sui staking escrow holds **239.50M SUI** and the Sui storage fund **2.77M**. The buyback destination is the one opaque item — no wallet address is published. Exchange custody and unidentified holders are excluded. If any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How SUI compares to other capped Layer 1 chains

SUI belongs to a class that is routinely misread: the **hard-capped, fully-premined Layer 1**. Total SUI supply is fixed at **10B** and every coin was minted at genesis — the Sui network's own supply record reports a fixed future because the authority that could mint more no longer exists. That sounds deflationary and is not. What a holder feels is the tradable float, and the Sui float is **41%** of the cap with the rest arriving on a calendar. A halving-model chain issues slowly but carries almost no locked overhang; Sui has no issuance in the strict sense yet carries a **5,903.46M SUI** overhang that behaves like issuance.

Against an uncapped Layer 1 with a fee burn the contrast is sharper. Those chains mint continuously but destroy a share of every fee, so heavy usage can push net supply negative. Sui has the opposite shape — no mint and no burn — so Sui activity cannot reduce SUI supply however high it goes, and the fee base could not matter if the design changed: **210.32K SUI** of computation charges in a window where the subsidy alone paid **26.61M**. Against a peer whose unlock schedule is still accelerating, though, the Sui monthly step is in decline and the subsidy shrinks **10%** every 90 epochs. SUI inflation is high today and committed to falling.

## What to watch in the next 90 days

Four dated items would move this reading. The Sui monthly steps on **Oct 1 2026**, **Nov 1 2026** and **Dec 1 2026** add **21.73M**, **20.77M** and **20.60M SUI** — any landing above its published figure means the Sui Foundation changed the schedule. The Sui staking subsidy steps down on **Oct 14 2026** to **254,186.58 SUI** an epoch. The Sui Foundation buyback ledger runs near **8,400 SUI** a session; a change in where those coins go, not how many are bought, is what would give this page a real buy row. And any disclosure touching the post-2030 tranche: releasing part of that **5,217.21M SUI** early would change the SUI profile rather than nudge it.

## Summary

The MrNasdog Pressure Framework reads Sui (SUI) as **structurally inflationary on the active float**: **+1.64%** net supply growth over the last 90 days and **+1.54%** projected for the next, against a supply monitor reading of **+1.73%** — a **0.09 percentage point** gap needing no reconciliation. The mechanism is a published monthly Sui unlock calendar plus a finite, escrowed staking subsidy, with a stablecoin-funded buyback that recycles rather than removes. The risk is the overhang: **5,903.46M SUI**, most of it post-2030 with no calendar, and no burn anywhere in the Sui design. The comfort is the ceiling: SUI is capped at **10B** and every coin already exists.

---

*MrNasdog Pressure Framework analysis of SUI, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 6 2026.*
