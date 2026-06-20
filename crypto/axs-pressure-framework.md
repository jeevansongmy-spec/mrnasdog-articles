---
title:         "AXS Inflation Analysis · June 2026 · Supply growing, but the growth is fading fast"
description:   "Axie Infinity's AXS: vesting concluded, no buyback or burn, a staking tail shrinking 5% every 9 days adds ~1.53M AXS / 90D. Net +0.9%, decelerating."
canonical_url: "https://mrnasdog.com/research/axs/inflation"
tags:          ["crypto", "axs", "axie-infinity", "gaming"]
published:     true
---

*Originally published at [mrnasdog.com/research/axs/inflation](https://mrnasdog.com/research/axs/inflation)*

# AXS Inflation Analysis · June 2026 · Supply growing, but the growth is fading fast

Axie Infinity's **AXS** is a capped game token whose 65-month vesting schedule has finished, leaving only the tail of a staking-reward allocation as new supply. That tail shrinks **5% every 9 days**, so the framework projects about **1.53M AXS** into the float over the next 90 days — roughly **+0.88% net** on **~173.89M** circulating, with no buyback and no burn on the other side. Our supply monitor reads the trailing 90 days at **+2.68%**, a **1.80 percentage-point** gap, so the page carries a monitor-gap flag.

## The verdict, in one paragraph

For the 90-day window from June 20 2026, the MrNasdog Pressure Framework reads **AXS at about +0.88% net** — supply still growing, but only from the fading tail of Axie Infinity's staking-reward emission. Our supply monitor reads the realized last-90-day change at **+2.68%**, a gap of **1.80 percentage points**, so the page ships a **monitor-gap flag**. The gap is a mechanism artefact rather than a conflict: the trailing window captured a heavier staking-reward tail — roughly **4.54M AXS** added — and that emission is decelerating **5% every 9 days**, so the framework projects the decayed forward rate of about **1.53M AXS**, not the front-loaded one. AXS is best characterised as a **capped play-to-earn token in the last stretch of its emission** — mildly inflationary on the active float today, but on a curve that bends toward flat as the staking allocation runs out.

## Sell pressure: where new AXS comes from

Almost all of AXS's new supply now comes from one place. Sell #1 — protocol inflation — is the tail of Axie Infinity's **staking-reward allocation**, a 78.3M-token bucket that is about **95%** distributed. The reward curve was revamped to decline **5% every 9 days**, so the trailing window's roughly **4.54M AXS** of fresh supply is decelerating toward about **1.53M AXS** projected over the next 90 days. There is no fixed emission rate and no mint function above the **270M** hard cap, so this tail is the entire engine of new supply. Sell #2 — vesting unlocks — is zero: the original **65-month** unlock schedule from the Q4 2020 public sale has reached its end, the published per-cliff calendar ran through late 2025, and vesting aggregators now show AXS as fully unlocked, so no cliff falls inside the window.

Sell #3 — Foundation and unscheduled unlocks — is zero in the window. The roughly **23M AXS** Community Treasury, run by the **Axie Infinity Foundation** and deployed only through quarterly governance votes, plus the **Sky Mavis** and Ecosystem Fund allocations inside the roughly **96M** gap between circulating and the 270M cap, are the standing team-controlled overhangs. None has a deployment dated inside these 90 days, and treasury AXS moves only when governance votes to deploy it. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court distribution applies to AXS.

## Buy pressure: where new AXS goes

The buy side of AXS is empty, and that is the key structural fact. Buy #1 — programmatic buyback — is zero: Axie Infinity runs **no AXS buyback** programme; protocol revenue flows to the Community Treasury for governance to allocate, not to an automated open-market buy. Buy #2 — protocol fee burn — is also zero: **AXS has no burn mechanism** at all. The token that gets destroyed in the game economy is **SLP**, a separate reward token consumed by breeding sinks; AXS itself is never burned, so nothing removes it from supply. Buy #3 — Foundation buy — is zero: the Foundation holds and deploys treasury AXS rather than buying more from the market. Buy #4 — new long-term lock — is zero as a booked offset, but it is the one place AXS does come off the float: **bonded AXS (bAXS)**, backed one-to-one and non-transferable, holds AXS for breeding and staking, and more than **60%** of supply now sits in staking plus bonding contracts. That is standing bonding rather than a new disclosed lockup fired inside the window, so it is tracked as scope, not booked as a buy-side offset.

## Foundation and overhang

AXS carries a large structural overhang, all of it governance-gated rather than scheduled. The **Community Treasury** — about **23M AXS** alongside ETH, RON and stablecoins — is controlled by the **Axie Infinity Foundation** and can be deployed only by quarterly governance vote, not on a calendar. Beyond it, the roughly **96M AXS** between the ~173.89M circulating and the 270M cap holds the **Sky Mavis** (21%) and Ecosystem Fund (8%) allocations plus the undistributed staking remainder. None of these has a release dated inside this window. The framework re-checks the Axie Infinity governance forum, the Foundation's treasury disclosures and the staking-emission curve on a roughly bi-weekly walk; none books a discretionary sell value today, and each is tracked as scope. If the Community Treasury or any Sky Mavis allocation deploys AXS between refreshes, the outflow enters Sell #3 at the next refresh.

## How AXS compares to other capped game and emission tokens

AXS belongs to the class of **capped tokens running off the end of a fixed emission schedule**. Unlike an uncapped continuous-emission proof-of-stake Layer-1 that mints fresh tokens forever to pay validators, Axie Infinity has a **270M hard cap** and a staking allocation that is nearly spent, so its supply growth is headed toward zero rather than continuing indefinitely. Unlike a halving-model coin whose emission steps down on fixed block intervals, AXS uses a smoother **5%-every-9-days** decay on its remaining staking rewards — a continuous taper rather than a cliff.

The sharper contrast is with **exchange tokens and fee-burn Layer-1s** that actively shrink supply. Those tokens pair issuance against a buyback or an **EIP-1559-style burn**, so their net can turn deflationary. AXS has neither — no buyback and no AXS burn — so even a small emission tail still reads as net positive, because there is nothing on the buy side to offset it. Its only supply sink is **bonded AXS**, which locks tokens off the float but does not destroy them; if bonding ever unwinds, that supply returns. The result is that AXS is **mildly inflationary by structure** until the staking tail fully exhausts, at which point the cap, not a burn, becomes the ceiling.

## What to watch in the next 90 days

Watch the running **staking-reward emission** — this is the only live driver of the reading, and because it declines 5% every 9 days, each refresh should show a smaller forward number than the last. Watch the **Axie Infinity Foundation** and its quarterly governance votes: the Community Treasury holds about 23M AXS, and a vote to deploy any of it would add a dated Sell #3 quantum. Watch **bonded AXS (bAXS)** balances, since rising bonding pulls more AXS off the float and falling bonding returns it. Watch for any governance proposal to introduce an **AXS buyback or burn**, which would be the first buy-side mechanism the token has ever had and would flip the net toward flat or negative. And watch the broader **Sky Mavis** ecosystem disclosures for any reclassification of the roughly 96M AXS held against the cap.

## Summary

AXS is a capped Axie Infinity game token in the final stretch of its emission: the 65-month vesting schedule has concluded, and the only new supply is the tail of a staking-reward allocation that is about 95% spent and shrinks 5% every 9 days. With no buyback and no AXS burn on the other side, the framework reads about +0.88% net over the next 90 days — roughly 1.53M AXS into a ~173.89M float — while the supply monitor reads +2.68% over the trailing window, 1.80 percentage points higher because the staking tail was heavier before it decelerated; the page carries a monitor-gap flag. The key risk ahead is the governance-gated Community Treasury and Sky Mavis overhang of roughly 96M AXS against the 270M cap; the structural backstop is that cap itself, which no mint can exceed.

---

*MrNasdog Pressure Framework analysis of Axie Infinity (AXS), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 20 2026.*
