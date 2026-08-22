---
title:         "APT Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description:   "Supply growing, projected to keep growing: APT reads +4.47% net per 90 days, as a 33.93M vesting calendar dwarfs a 4.90M staking mint and a 0.49M gas burn."
canonical_url: "https://mrnasdog.com/research/apt/inflation"
tags:          ["crypto", "apt", "aptos", "layer1"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/apt/inflation](https://mrnasdog.com/research/apt/inflation)*

# APT Inflation Analysis · August 2026 · Supply growing, projected to keep growing

Aptos has done nearly everything a chain can do to slow its own supply — a protocol hard cap of **2.10B APT**, a staking reward rate cut to its **2.60%** floor, and **100%** of gas fees burned — and APT supply still grows, because the growth was never coming from the Aptos protocol. The staking mint realised only **4.90M APT** over the last 90 days while the 2022 vesting calendar released **33.93M APT** and the gas burn took back **0.49M APT**, so the MrNasdog Pressure Framework reads **+4.47% net** for the trailing window and **+3.67%** forward. Our supply monitor reads **+4.55%** — a gap of **0.085 percentage points**, inside tolerance. The constraint worth knowing is a date: **Oct 12 2026** is the final core-contributor and investor tranche of the four-year Aptos vest, and it retires about 60% of the recurring monthly unlock.

## The verdict, in one paragraph

Over the last 90 days the MrNasdog Pressure Framework reads Aptos at **+4.47% net**: about **38.83M APT** of supply reaching the market against **0.49M APT** destroyed, on a circulating base of **857.8M APT**. Our supply monitor reads the same window at **+4.55%**, a gap of **0.085 percentage points**, comfortably inside the framework's half-point tolerance, so this build ships no data-conflict flag. Projected forward the framework reads **+3.67%**, and the whole of that improvement comes from the vesting calendar rather than from anything the Aptos protocol does differently. APT is **structurally inflationary on the calendar, not on the mint** — the cleanest label for the reading, and the reason the 2.1B hard cap does much less work than its headline suggests.

## Sell pressure: where new APT comes from

Sell #1, protocol inflation, is the smaller of the two taps and it is the one everyone quotes. Aptos mints staking rewards once per epoch against the balance actually staked, multiplied by each validator's proposal success ratio, which makes the published **2.60%** annual rate a ceiling rather than a measurement. This build measured all three inputs instead of assuming them. The chain ran **1,084** epochs across the window, not the **1,080** its two-hour epoch interval implies, because Aptos governance resolutions force an early reconfiguration and each of those pays a full epoch of rewards. The staked base averaged **764.6M APT** and validator performance averaged **99.601%**. Together that is **4.90M APT** of genuinely new supply, or **99.97%** of the scheduled ceiling — the performance drag and the extra epochs almost exactly cancel, which is only knowable after measuring both. One trap is worth naming: the legacy Aptos staking-config field still returns a **7.00%** rate and is no longer the live parameter.

Sell #2, vesting unlocks, is the tap that actually sets the reading. The Aptos genesis allocation releases on the 12th of every month across four buckets — core contributors **3.96M**, community **3.21M**, investors **2.81M**, foundation **1.33M** — for **11.31M APT** a month, and three tranches fell inside the window for **33.93M APT**. That is roughly seven times the Aptos mint. The published unlock tracker places the final core-contributor and investor tranche on Nov 12 2026; the supply arithmetic says otherwise, and the arithmetic wins. Documented cumulative unlocks plus realised mint fall short of circulating APT by **6,766,310** — the core-contributor plus investor monthly quantum to within **5 APT** — so those two buckets have already paid one tranche more than the tracker shows and their last one lands **Oct 12 2026**.

Sell #3, foundation and unscheduled unlocks, is **0**, and unusually for a large layer-1 that zero is provable rather than assumed. Aptos has **349.75M APT** minted but not circulating, and the four published vesting buckets account for **349,749,982** of it against a measured **349,749,944** — a difference of **38 APT**. There is no unscheduled pool hiding behind the calendar. Sell #4, long-term locked or bankruptcy, is **0** because no bankruptcy estate or trustee distribution has ever touched APT.

## Buy pressure: where new APT goes

Buy #2, the protocol fee burn, is the only live counter-force, and Aptos runs the strict version of it: **100%** of gas fees are burned, with no share redirected to validators, and the Apr 2026 overhaul raised gas roughly tenfold. Measured against two exact chain reads at both window ends — gross mint **4,900,589 APT** minus a net supply change of **4,414,031 APT** — the burn is **0.49M APT** over 90 days. Sampling **4,000** consecutive Aptos transactions directly gives **0.55M**, agreeing within **12%**. It offsets about one APT in every ten minted. It is also a useful reminder that a documented burn rate is marketing until it is measured: the new fully on-chain perpetuals venue on Aptos is projected to burn **32M APT** a year, and the entire chain is currently burning at about **1.97M** a year.

The other three buy rows are **0**. Buy #1, programmatic buyback, is empty because the Aptos Foundation has only said it will explore one funded from licensing revenue; nothing has been proposed on-chain, and the ten Aptos governance proposals created inside this window were framework upgrades, a per-block gas limit, transaction limits and two feature flags — none of them supply-affecting. Buy #3, foundation buy, is empty because no open-market purchase has been disclosed. Buy #4, new long-term lock, is empty because the Aptos Foundation's permanent stake of **210.0M APT** executed in **Apr 2026**, before this window opened.

## Foundation and overhang

Every team-controlled APT overhang sits on the published Aptos calendar, which is rarer than it sounds. The community bucket holds **237.55M APT** still to release at **3.21M** a month into the 2030s; the Aptos Foundation bucket holds **98.67M APT** at **1.33M** a month; core contributors hold **7.92M APT** and investors **5.62M APT**, each with exactly two tranches left. Separately, the Aptos Foundation has permanently staked **210.0M APT** and committed to funding operations from the staking rewards rather than selling the principal — that position carries no release schedule of any kind, and it is the single biggest reason the foundation is not a discretionary seller. The supply leg is re-read from chain state on every rebuild, and the calendar leg from a fresh walk of the schedule. If any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How APT compares to other capped proof-of-stake layer-1s

Against uncapped continuous-emission layer-1s, Aptos now looks structurally tighter on the mint and structurally looser on the calendar. Chains that never fixed a ceiling carry an issuance tap that cannot be switched off, but many of them launched without a large private allocation, so once the mint is measured the whole supply story is measured. Aptos is the reverse: its mint is small and shrinking — the staking rate has hit its floor and cannot decay further — while a four-year private vest signed in 2022 keeps releasing seven times as much APT as the protocol creates. A hard cap constrains the mint. It does nothing at all to a calendar of already-minted coins, which is why the 2.1B ceiling has not moved this reading.

Against fee-burn chains, the comparison is about scale rather than design. Aptos burns 100% of gas fees, which is the strictest burn policy available, but Aptos fees are deliberately sub-cent and the burn lands at **0.49M APT** a quarter. A chain whose burn actually offsets its issuance is one where blockspace is scarce and expensive; Aptos is optimised for the opposite. That is a product choice, not a flaw, but it means the deflation case for APT depends on transaction volume growing by an order of magnitude rather than on the burn mechanism itself.

Against other 2021–2022 vintage layer-1s working through their own four-year vests, Aptos is late in the cycle rather than early, and that is the constructive part of this reading. The heaviest buckets retire first: after **Oct 12 2026** the recurring monthly release drops from **11.31M APT** to **4.54M APT**, and what remains is community and foundation issuance stretched over years rather than concentrated insider unlocks.

## What to watch in the next 90 days

The **Sep 12 2026** unlock releases a full **11.31M APT** across all four Aptos buckets and is the last routine one. The **Oct 12 2026** unlock is the date that matters: it is the final core-contributor and investor tranche of the four-year Aptos vest, and if the schedule holds, the recurring release drops by **6.77M APT** a month from there. The **Nov 12 2026** unlock is the confirmation — it should print at about **4.54M APT**, community and foundation only, and a full-size print instead would mean the vest runs a month longer than this build reads. Watch the Aptos staked balance too: it drifted from **778.1M APT** mid-window to **751.9M APT**, and because rewards are struck on staked APT rather than on all APT, a further fall shrinks the mint again. Finally, watch the Aptos Foundation buyback: it is currently only an intention, and a governance proposal turning it into a programmatic buy would be the first genuine buy-side row this ledger has ever carried.

## Summary

The MrNasdog Pressure Framework reads Aptos at **+4.47%** net supply growth over the last 90 days and **+3.67%** forward, against a supply monitor reading of **+4.55%**. The structural mechanism is that APT inflation is a vesting calendar, not an emission curve: the Aptos staking mint realised **4.90M APT** while the 2022 allocation schedule released **33.93M APT**, and a 100% gas-fee burn took back only **0.49M APT**. The key risk is that the counter-force is far too small to matter — the burn would need to grow roughly tenfold before it offsets even the mint, let alone the unlocks. The ceiling is real but distant: Aptos is capped at **2.10B APT** with **1.21B** minted, and the constraint that actually binds inside the next year is the **Oct 12 2026** expiry of the core-contributor and investor vest.

---

*MrNasdog Pressure Framework analysis of APT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 22 2026.*
