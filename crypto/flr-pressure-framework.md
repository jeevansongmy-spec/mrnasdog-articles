---
title: "FLR Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description: "A MrNasdog Pressure Framework read of Flare (FLR): 1,003.8M FLR/90D reaching the market vs 127.5M taken off it. Framework +1.01% net; monitor +1.56% (gap 0.55pp, flagged)."
canonical_url: "https://mrnasdog.com/research/flr/inflation"
tags: ["crypto", "flr", "flare", "oracles"]
published: true
---

# FLR Inflation Analysis · September 2026 · Supply growing, projected to keep growing

> Originally published at **[mrnasdog.com/research/flr/inflation](https://mrnasdog.com/research/flr/inflation)** by MrNasdog.

Flare put **1,003.8M FLR** onto the market over the last 90 days and took **127.5M FLR** back off it — a net of **+1.01%** trailing and **+1.01%** projected. Only **666.3M** of that supply is newly issued FLR; the other **337.5M** is FLR created at genesis in 2022 that had simply never been counted, draining out of Flare's twelve protocol reserve pools. Our supply monitor reads **+1.56%** for the same window, a gap of **0.55 percentage points**, so the FLR overview carries a **⚠ monitor gap** chip. Flare is an uncapped chain whose headline 3% inflation rate describes barely two-thirds of the FLR that actually arrives.

## The verdict, in one paragraph

For the 90-day window ending **Sep 4 2026**, the MrNasdog Pressure Framework reads **FLR at +1.01% net**, with **+1.01%** projected over the next 90 days. Our supply monitor reads **+1.56%** for the trailing window, a gap of **0.55 percentage points**, which is over the framework's half-point tolerance and therefore ships a **⚠ monitor gap** chip on the FLR overview. The gap is not a disagreement about Flare — it is an artefact of where the monitor's 90-day base landed. Its supply series fell **958.8M** in a single day on **Jun 6 2026** and jumped back **1,058.6M** on **Jun 19 2026**, and the base snapshot sits inside that trough. Read directly on-chain instead, Flare's own circulating-supply function moved **+875.5M FLR** across the window, and the framework's ledger predicts **+876.3M** from independently measured parts — a residual of **800,709 FLR** on a base of 86.8 billion. Flare is **structurally inflationary on two taps, not one**: a 3% protocol inflation mint the network advertises, and a genesis incentive reserve it does not.

## Sell pressure: where new FLR comes from

Sell #1 — protocol inflation — is **666.3M FLR** over the last 90 days and **666.3M FLR** projected over the next. Flare issues FLR to pay four reward streams: FTSO oracle reward offers, FLR staking and validator rewards, the Flare Data Connector, and fast-update incentives. Governance proposal **FIP.16**, accepted **Apr 24 2026** with **98.06%** in favour, cut the annual inflation rate from **5%** to **3%** and lowered the hard issuance cap from **5B FLR** to **3B FLR** a year. This analysis does not take that 3% on trust. Flare's Supply contract keeps a running total of authorised inflation, and reading it at both ends of the window gives the realised number directly: **10,040,035,384 FLR** on **Jun 7 2026** and **10,706,364,670 FLR** on **Sep 4 2026**. That is **7.4M FLR** a day, or **2.98%** a year against Flare's inflatable balance — the 3% rate, measured rather than quoted. The cut is visible in the run rate too: **12.4M FLR** a day before it landed in mid-May 2026, **7.5M FLR** a day after, and the whole measured window sits on the far side of that step, so nothing here blends an old rate with a new one.

Sell #2 — vesting unlocks — is **0**, and it is zero on both the calendar and the chain. Flare's **FlareDrop** programme distributed roughly 24 billion FLR in 36 monthly instalments and made its final payment on **Jan 30 2026**, 128 days before this window opened. The distribution treasury and the distributor contract that ran it both hold nothing at both window edges, and their pool rows read a change of exactly zero. The early-backer escrow, which holds the residual of a vesting extension that ran to the first quarter of 2026, held **204.5M FLR** on **Jun 7 2026** and **204.5M FLR** on **Sep 4 2026** — it released nothing. Scheduled zero, realised zero.

Sell #3 — Foundation and unscheduled unlocks — is **337.5M FLR**, and it is the tap almost no FLR inflation figure includes. Flare's Supply contract tracks twelve reserve pools, each reporting how much it holds locked, how much inflation it has been authorised, and how much has been claimed out of it. Sum the undistributed balances of all twelve at both window edges and they fall **337.5M FLR** — genesis-era FLR that existed but had never been counted as circulating, quietly becoming counted. Nearly all of it is a genesis incentive reserve feeding Flare's locked reward programme, which still holds **17,427.4M FLR** with no published release date, plus a legacy oracle reward-claim backlog of **62.0M FLR**. This flow leaves no transaction on the block explorer: Flare's chain daemon settles it directly in state, so it is invisible unless you read the reserve pools themselves at both ends of the window.

Sell #4 — long-term locked or bankruptcy — is **0**. No estate, trustee or court-administered pool holds FLR. Enumerating every reserve the Flare protocol itself tracks returns twelve contracts, all of them reward or distribution machinery; none is a bankruptcy claim.

## Buy pressure: where new FLR goes

Buy #1 — programmatic buyback — is **0**. FIP.16 created the **Flare Income Reinvestment Entity**, a revenue pool whose stated primary mandate is to reduce FLR supply by buying and burning, funded by Flare Data Connector attestation fees, FAssets minting and redemption fees, Smart Account fees and captured MEV. It has been collecting since **May 2026**, but cumulative collections stood at roughly **$31,438** on **Sep 4 2026** across those four streams. No purchase has been executed or disclosed, so the row is zero and the mandate is monitored.

Buy #2 — protocol fee burn — is **125.6M FLR**, and its composition is the opposite of what the name suggests. The Flare burn address held **4,099,926,603 FLR** at the window open and **4,225,498,740 FLR** at the close, and Flare's Supply contract subtracts that balance from circulating directly. Almost none of the rise is the gas burn Flare is known for. FIP.16 raised the base gas fee twentyfold, from 25 gwei to 500 gwei, on the **Jul 14 2026** hard fork, and that lifted the per-block burn about **43** times over — yet it still amounts to only about **1.5M FLR** across the quarter, rising to a projected **2.5M FLR** for the next one now that the whole window sits after the fork. The remaining **124.1M FLR** arrives as discrete transfers whose senders resolve to Flare's locked reward accounts: cash out an rNat reward account before its lock expires and half the balance is burned on the spot. That is a real, protocol-encoded destruction of supply, but it is a penalty on early exit, not a fee on network use.

Buy #3 — Foundation buy — is **1.9M FLR**. The seven wallets the Flare protocol itself tags as foundation-controlled held **45,000 FLR** on **Jun 7 2026** and **2.0M FLR** on **Sep 4 2026**, and the chain's own supply meter treats that balance as outside the tradable float. It is accumulation into those wallets rather than a disclosed open-market purchase, and at 0.002% of supply it decides nothing on its own — it is booked because it is measured, not because it matters.

Buy #4 — new long-term lock — is **0**, and the reasoning matters more than the number. About **20B FLR** is bonded to Flare validators, up from roughly 11B when FIP.16 was proposed, and **43,746.4M FLR** is wrapped as WFLR. Neither is a lock for framework purposes: wrapped FLR is a freely transferable receipt that unwraps on demand, and bonded FLR sits inside the counted float rather than outside it. Separately, **918.4M FLR** genuinely did move into Flare's locked reward pools this window — but that locking is already netted inside the Sell #3 figure, so booking it here as well would count the same flow twice.

## Foundation and overhang

FLR's team-controlled overhang is large, enumerable and almost entirely unscheduled. The biggest single item is the genesis incentive reserve behind Sell #3, which held **17,427.4M FLR** on **Sep 4 2026**, down from **17,870.4M FLR** at the window open — it is draining steadily at roughly 4.9M FLR a day with no published end date and no published schedule. Behind it sit **710.4M FLR** in locked rNat reward accounts, up from 514.5M across the window as the reward programme funds itself; **204.5M FLR** of untouched early-backer escrow; and **2.0M FLR** across the seven foundation-tagged wallets. Flare's buyback destination is unstated — the Flare Income Reinvestment Entity has published no wallet address and no executed quantum — so it is tracked through official disclosure and re-checked at each rebuild rather than read on-chain.

Every one of those balances is read from the Flare C-chain at each rebuild, and the rule is the same for all of them: if any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh. The reserve is the one to watch, because it is the only overhang currently moving, and it is moving in one direction.

## How FLR compares to other uncapped smart-contract layer-1s

Against chains with a hard cap, Flare is structurally the opposite animal. A halving-model chain issues on a schedule written into the protocol and cannot exceed its cap no matter what governance decides; Flare has no maximum supply at all, only an annual issuance ceiling of 3B FLR that governance itself set and governance itself can move. The practical difference is that Flare's inflation is a policy variable, not a constant — it has already been changed once this year, from 5% to 3%, by a single vote in April 2026.

Against other uncapped continuous-emission layer-1s, the interesting distinction is not the rate but the second tap. Most staking chains have one supply source: a mint that pays validators. Flare has that mint, at a measured 2.98% a year, and it also has roughly **19,687.8M FLR** of already-created supply parked in reserve pools that pays out on its own logic. A reader who compares Flare's 3% to another chain's 3% is comparing two different quantities, because on Flare the reserve drain adds another half again on top — **337.5M FLR** against **666.3M FLR** this quarter.

Against fee-burn chains, Flare's burn is real but structurally small relative to issuance. An EIP-1559-style chain with heavy block space demand can burn more than it mints; Flare's gas burn is about **1.5M FLR** a quarter against **666.3M FLR** of issuance, even after a twentyfold fee increase, because the burn scales with transaction demand and Flare's demand is still small. What actually offsets Flare's issuance is not a fee burn at all but an early-exit penalty on locked rewards — a mechanism most comparable chains do not have, and one that shrinks as reward locks mature rather than growing with usage.

## What to watch in the next 90 days

First, whether the Flare Income Reinvestment Entity executes its first buyback. Its collections nearly doubled in the last two weeks of **Aug 2026** and its Data Connector fee stream only began that month, but at roughly **$31,438** cumulative it is still four orders of magnitude away from mattering to this ledger. A published wallet address would move Buy #1 off zero for the first time.

Second, whether the MEV capture stage of FIP.16 goes live. It is the largest of FIRE's four intended revenue sources and the only one with the scale to make the buyback row material; it is on a staged roadmap with no announced date.

Third, the genesis incentive reserve's drain rate. It fell **443.0M FLR** across this window and still holds **17,427.4M FLR**. A step down in that rate would cut Sell #3 directly; a step up would push FLR's net past 1.5%.

Fourth, the early-exit penalty burn. It carried **124.1M FLR** of this quarter's buy side, and it depends on how many holders cash locked reward accounts out early — a behavioural quantity, not a scheduled one, and the least predictable line in this ledger.

Fifth, whether any proposal past **FIP.16** reaches a vote. Flare's governance index carried nothing newer as of **Sep 5 2026**, and FIP.16 showed that a single vote can move Flare's issuance by 40% in one step.

## Summary

The MrNasdog Pressure Framework reads **FLR at +1.01% net** over the 90 days to **Sep 4 2026** and **+1.01%** projected — supply growing, projected to keep growing. Flare is structurally inflationary on two taps: a measured 3% protocol mint worth **666.3M FLR** a quarter, and a genesis reserve drain worth another **337.5M FLR** that appears in no published inflation figure and leaves no trace on the block explorer. Against them, **125.6M FLR** was destroyed, but only about **1.5M** of that is the twentyfold gas burn FIP.16 is famous for; the rest is the half of a locked reward account burned when a holder exits early. The key risk is that Flare has no maximum supply — only a 3B-a-year issuance ceiling that a single governance vote already moved once this year — and the ceiling on any deflationary turn is that the buyback entity built to shrink supply has collected about **$31,438** and has never bought anything.

*MrNasdog Pressure Framework analysis of FLR, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 5 2026.*
