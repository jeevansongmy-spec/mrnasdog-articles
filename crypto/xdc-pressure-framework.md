---
title:         "XDC Inflation Analysis · July 2026 · An uncapped trade-finance chain that barely inflates"
description:   "XDC's 108 masternodes mint ~21.4M XDC/90d at 5.5 per block, with no buyback and a sub-cent fee burn. Framework reads +0.11% (monitor -0.03%)."
canonical_url: "https://mrnasdog.com/research/xdc/inflation"
tags:          ["crypto", "xdc", "xdc-network", "layer1"]
published:     true
---

*Originally published at [mrnasdog.com/research/xdc/inflation](https://mrnasdog.com/research/xdc/inflation)*

XDC Network is an **uncapped** delegated proof-of-stake Layer-1 whose **108 masternodes** mint **5.5 XDC per block** at roughly 2-second blocks — about **21.4M XDC** over 90 days, the only real new supply. There is **no buyback** and the live fee burn is negligible at sub-cent fees, and no vesting cliff falls inside the window — the next unlock is **Feb 5 2027**. The framework reads XDC at **+0.11%** net supply, a slow drift up. Our supply monitor reads **-0.03%**, a gap of about **0.14 percentage points** that stays within tolerance, so no monitor-gap flag is raised.

## The verdict, in one paragraph

For the 90-day window beginning July 13 2026, the MrNasdog Pressure Framework reads **XDC at about +0.11% net supply growth** — roughly **21.4M XDC** minted as masternode block rewards, with **almost nothing on the buy side** to offset it. Our supply monitor reads the realized last-90-day change at **-0.03%**, essentially flat, a gap of about **0.14 percentage points** that **does not raise a monitor-gap chip** because it sits inside the framework's half-point tolerance. The two readings agree on the shape: the monitor's circulating-supply figure barely moves over the quarter, while the framework books the small block-reward emission. XDC is best read as an **uncapped chain that is only mildly inflationary**, because its one new-supply force — a fixed 5.5 XDC per block — is small against a nearly 20-billion-XDC float.

## Sell pressure: where new XDC comes from

Sell #1 — protocol inflation — is the whole story, about **21.4M XDC** over the next 90 days. XDC Network is secured by **108 masternodes** running the XDPoS 2.0 delegated proof-of-stake consensus, and the protocol **mints 5.5 XDC every block** at roughly 2-second blocks as their reward. That is about **86.7M XDC a year**, or roughly **0.43%** of the circulating float — real new supply, since the block reward increases total supply, which has grown from about 37.5B at the 2019 genesis to about 38.1B today. It is paid to masternode operators as a liquid reward, so it reaches the market.

The other three sell rows are **zero** in this window. Sell #2 — vesting unlocks — is zero because XDC's large non-circulating reserve is released on **cliff vesting** on an annual Feb 5 cadence; the last unlock was Feb 5 2026 and the next is **Feb 5 2027**, outside the window, so no cliff adds supply now. Sell #3 — Foundation and unscheduled unlocks — is zero because no discretionary release was observed, though the roughly **18.1B XDC** still held in reserve is a real overhang, covered below. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate applies to XDC.

## Buy pressure: where new XDC goes

There is almost no buy pressure — every buy row is effectively **zero**. Buy #1 — programmatic buyback — is zero: XDC Network runs no token buyback and no protocol revenue is used to purchase XDC. Buy #2 — protocol fee burn — is the interesting one: a burn IS live. The **January 2026 Cancun upgrade** added an **EIP-1559 base-fee burn**, on top of the legacy rule that burns **20% of smart-contract transaction fees**. But XDC fees are sub-cent, so the amount burned over 90 days is **negligible** against the 21.4M emission and rounds to zero — a genuine but tiny counter-force. The XDCDAO governs the burn rate and can raise it as enterprise usage grows, which is the lever that could one day tip XDC toward flat or deflationary. Buy #3 — Foundation buy — is zero, with no open-market buying observed. Buy #4 — new long-term lock — is zero: the 108 masternodes each lock **10M XDC** — about **1.08B** in collateral — but that stake is static and pre-existing, so no new lock was created in the window.

## Foundation and overhang

The overhang is large. About **18.1B XDC** — the gap between the roughly 19.9B circulating and the 38.1B total — sits in **non-circulating reserve**, spread across the **Founder/Advisors/Team** allocation (near 28.6% of the genesis distribution), **Ecosystem Development** (near 26.0%) and **Contingency** (near 9.0%). These pools are released on cliff vesting, and because the schedule is annual on Feb 5, none of them fires inside this window — the next unlock is **Feb 5 2027**. It is monitored on that schedule and via on-chain balances. The trigger is simple: if any of these reserve balances falls between refreshes — an early or larger release than the schedule implies — that outflow enters Sell #3 at the next refresh.

## How XDC compares to other uncapped Layer-1 chains

XDC looks scarce for an uncapped chain. Unlike **Bitcoin**, which has a hard 21M cap and a fixed halving schedule, XDC has **no maximum supply** — the protocol can keep minting 5.5 XDC per block indefinitely. But the emission is small: about **0.43% a year**, far below the double-digit staking inflation of an uncapped chain like **Cosmos Hub** (ATOM), and gentler than many delegated proof-of-stake networks. In practice XDC's inflation reads more like a hard-capped chain than its uncapped label suggests, because the per-block reward is fixed and the float is already large.

The sharper contrast is on the burn side. Post-Merge **Ethereum** pairs issuance with a heavy **EIP-1559 base-fee burn** that can tip it deflationary when usage is high. XDC added the same EIP-1559 mechanic in its **Cancun upgrade**, plus a 20% smart-contract fee burn — but its fees are sub-cent, so the burn cannot yet offset the block reward the way Ethereum's can. That is the key mechanism difference: XDC has the deflationary plumbing in place, but it only bites once enterprise trade-finance volume drives real fees. Until then, the fixed masternode reward wins, and XDC drifts slowly up.

## What to watch in the next 90 days

Watch the **on-chain fee-burn rate** — the single variable that could turn XDC flat or deflationary. Enterprise and real-world-asset volume has been climbing (tokenized assets on XDC surpassed **$1.1B** on Jul 1 2026), and a step-change in smart-contract activity would make Buy #2 material. Watch **XDCDAO governance** for any vote to raise the burn percentage, which the DAO controls directly. Watch the masternode set — steady at **108** validators each staking 10M XDC — since the block reward and collateral are tied to it. And keep the **Feb 5 2027** cliff on the calendar: the next scheduled reserve unlock is the biggest dated supply event ahead, and while it is outside this window, it is the one to prepare for.

## Summary

XDC is an uncapped delegated proof-of-stake token whose supply grows only through a fixed masternode block reward — 5.5 XDC per block, about 21.4M over 90 days, or roughly +0.11% net. There is no buyback, and while an EIP-1559 fee burn and a 20% smart-contract fee burn are both live, sub-cent fees make them negligible today, so nothing meaningful offsets the emission. Our supply monitor reads -0.03%, essentially flat and about 0.14 points below the framework, but that stays within tolerance and both agree XDC is barely inflating. The key point is structural: an uncapped chain with a small fixed reward and a burn that only bites at high usage sits close to flat, and the fee burn is the lever that could tip it deflationary as trade-finance volume grows.

---

*MrNasdog Pressure Framework analysis of XDC Network (XDC), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 13 2026.*
