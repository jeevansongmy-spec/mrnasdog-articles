---
title: "LEO Inflation Analysis · July 2026 · Mixed flows, supply roughly steady"
description: "A MrNasdog Pressure Framework read of UNUS SED LEO: no mint, no vesting, only a revenue-funded buyback-and-burn. Framework −0.07% net; the supply monitor agrees at −0.05%."
canonical_url: "https://mrnasdog.com/research/leo/inflation"
tags: ["crypto", "leo", "bitfinex", "exchange-token"]
published: true
---

> Originally published at **[mrnasdog.com/research/leo/inflation](https://mrnasdog.com/research/leo/inflation)** by MrNasdog.

UNUS SED LEO, the Bitfinex exchange token issued by iFinex, has no mint function, no vesting calendar and exactly one supply mechanism: a buyback-and-burn funded by a share of exchange revenue. Over the 90 days to **Jul 27 2026** that mechanism retired **638,310 LEO** against **zero** new issuance, so the MrNasdog Pressure Framework reads LEO at **−0.07% net** on a **920.1M** float. Our independent supply monitor reads **−0.05%** across the same window — a gap of **0.02 percentage points**, which is agreement, not conflict.

## The verdict, in one paragraph

For the 90-day window ending **Jul 27 2026**, the Pressure Framework reads LEO at **−0.07% net**: every sell row in the LEO ledger is zero, and the only live buy row is the iFinex buyback-and-burn, which removed **638,310 LEO** from the circulating float. Our supply monitor reads the realised change at **−0.05%** over the same window, and the gap between the two readings is **0.02 percentage points** — far inside the framework's half-point tolerance, so LEO ships with **no monitor-gap flag**. The label for LEO is **deflationary by contract, but slowly**: the supply can only ever fall, and at the current pace it falls by roughly a quarter of a percent a year. The burn is real, verifiable on-chain, and small.

## Sell pressure: where new LEO comes from

It does not come from anywhere, and that is the single most important fact about LEO. Sell #1, protocol inflation, is **zero**. LEO is not a blockchain — it is a token issued by an exchange operator, so there are no block rewards, no staking emissions and no security budget denominated in LEO. The Ethereum-side supply has read exactly **660,000,000** since the 2019 issuance, unchanged at both ends of this window, and the Vaulta-side supply has only ever moved downward. Sell #2, vesting unlocks, is **zero** for an equally structural reason: the May 2019 private sale sold all **1,000,000,000** LEO in ten days and delivered every token immediately, with no cliff, no linear release and no team or seed allocation held back. There is no unlock calendar for LEO because one was never written.

Sell #3, Foundation and unscheduled unlocks, is **zero** as a flow, but it is the row that carries LEO's real long-run risk and it deserves the detail below. Sell #4, long-term locked or bankruptcy, is **zero**: no bankruptcy estate holds LEO, and the court-approved restitution flowing from the 2016 Bitfinex security breach returns **94,643** bitcoin to iFinex — not LEO — so no estate distribution can ever land in this ledger. Four sell rows, four zeros, and none of them depends on a judgement call.

## Buy pressure: where new LEO goes

Buy #1, programmatic buyback, is the whole story. iFinex committed at launch to spend no less than **27%** of its consolidated gross monthly revenue — across Bitfinex trading, lending and its other products — repurchasing LEO on the open market and retiring it, and to keep doing so until no LEO remains in commercial circulation. Unusually for a corporate buyback, this one is fully readable on-chain. It executes as a single transfer a day from the iFinex operating account into the LEO issuer account on Vaulta, tagged with the memo **burn**, and the issuer account's balance is excluded from the circulating float. Across the window there were **86** such transfers totalling **638,310 LEO**, ranging from **7,286** to **8,667** a day and averaging about **7,400**. At the prevailing price that is roughly **$6.2M** of LEO retired per quarter.

Buy #2, protocol fee burn, is **zero**: LEO is not the gas token of Ethereum or of Vaulta, so no transaction fee is ever paid or burned in LEO. Buy #3, Foundation buy, is **zero** — and this is the row to watch. iFinex has also committed to spend **80%** of net proceeds from the recovered 2016 breach bitcoin on repurchasing and burning LEO within roughly eighteen months, and the first restitution transfers landed in **April 2026**. That commitment is armed but it has not fired: the on-chain burn stream shows no acceleration whatsoever across the window — **241,400** LEO in April, **219,766** in May, **226,360** in June — so the framework books it at zero rather than crediting an announcement. Buy #4, new long-term lock, is **zero**: repurchased LEO is retired outright, not escrowed, so there is nothing to double-count.

## Foundation and overhang

LEO carries the largest single company-controlled holding of any coin in this catalogue, and it is important to state it plainly. An Ethereum cold-storage safe holds **648,000,000 LEO** — **98%** of the entire Ethereum-side supply, and counted inside the 920.1M circulating denominator this page divides by. It was funded in 2020 and topped up in 2023, and it has never sent a single LEO out. The second holding is the Vaulta issuer account, the burn sink itself, which held **46,907,358 LEO** at the open of this window and **47,545,668 LEO** at its close; it has no outgoing transfers in its entire indexed history, which is what makes the burn count trustworthy. The third is the operating account that funds the retirements, holding **2,313,141 LEO** and draining only into the burn sink.

None of the three has ever shown an outflow, so each stays at value zero in the ledger under the framework's evidence rules — capacity is not a schedule. But the enumeration is the point: the 648M safe is roughly a thousand times larger than a quarter of burning, and if its balance ever fell between refreshes, that outflow would enter Sell #3 at the next refresh and would dominate every other number on this page.

## How LEO compares to other exchange tokens

LEO belongs to the class of **exchange tokens with a revenue-funded buyback-and-burn**, and inside that class it sits at the conservative end on mechanism and at the transparent end on verification. The classic model — a quarterly buyback whose size is announced by the exchange and executed in batches — hands the reader a press release and asks for trust. LEO's version runs continuously, one small increment a day, into an account whose balance any reader can query, and the arithmetic ties out exactly: the Ethereum supply plus the Vaulta supply minus the issuer balance equals the published circulating figure to the decimal. That is a materially stronger verification story than most exchange tokens offer.

The trade-off is size. A peer that has removed the ability to mint or burn at all reads a flat 0.00% and is fixed rather than falling; LEO reads **−0.07%** and is genuinely falling, which is better, but only just. Against uncapped Layer 1s that fund security through perpetual staking issuance and print persistently positive inflation, LEO's ledger looks unambiguously favourable — there is simply no sell side. Against gas tokens with a base-fee burn, the mechanism differs in what drives it: a fee burn scales with on-chain usage, whereas LEO's burn scales with iFinex's revenue, which is neither constant nor disclosed in real time. That is why this page treats the burn as a measured quantity rather than a modelled rate.

## What to watch in the next 90 days

First and most important, watch whether the restitution-funded buyback actually starts: the commitment to spend 80% of net recovery proceeds on retiring LEO is the one event that could move this page from −0.07% to something an order of magnitude larger, and the tell will be the size of the burn transfer that lands each day, not a headline. Second, watch the monthly burn totals themselves — they have drifted down from **295,775** in March 2026 to about **223,000** a month since, which reads as softer exchange revenue after Bitfinex removed spot trading fees on **Dec 17 2025**. Third, watch the 648M Ethereum cold-storage safe for any outgoing transfer, which would immediately become the largest sell-side event LEO has ever had. Fourth, watch for any disclosure quantifying iFinex consolidated revenue, since the 27% floor is only as informative as the base it applies to. Fifth, expect the framework and the supply monitor to keep agreeing near flat, both hovering within a tenth of a percent of zero.

## Summary

UNUS SED LEO is a fixed-supply exchange token whose supply can only fall: no mint function exists, the 2019 sale left no vesting calendar behind, and the sole supply mechanism is a buyback-and-burn funded by at least 27% of iFinex gross revenue. Over the 90 days to **Jul 27 2026** it retired **638,310 LEO** for a net of **−0.07%**, matched by the supply monitor at **−0.05%**. The structural strength is that the burn is verifiable on-chain rather than merely disclosed; the structural risk is a **648,000,000 LEO** company-controlled safe that has never moved but is counted as circulating. The ceiling on the good news is arithmetic: at the current pace, a quarter of burning removes less than a tenth of one percent of the float.

---

*MrNasdog Pressure Framework analysis of LEO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 27 2026.*
