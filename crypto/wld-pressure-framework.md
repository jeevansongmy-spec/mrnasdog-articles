---
title:         "WLD Inflation Analysis · July 2026 · Supply growing, projected to keep growing"
description:   "All 10B WLD were pre-minted, so World's only inflation is a daily unlock — ~450M WLD last 90 days, cut 43% on Jul 24 2026. Framework reads +11.98% net, easing to +6.95%."
canonical_url: "https://mrnasdog.com/research/wld/inflation"
tags:          ["crypto", "wld", "world", "tokenomics"]
published:     true
---

*Originally published at [mrnasdog.com/research/wld/inflation](https://mrnasdog.com/research/wld/inflation)*

# WLD Inflation Analysis · July 2026 · Supply growing, projected to keep growing

World is the purest unlock story in our coverage: all **10 billion WLD** were minted once at genesis on **Jul 24 2023**, and the contract can never mint or burn again, so the entire inflation reading is a daily linear **unlock** of locked coins. Over the 90 days to **Jul 28 2026** that unlock added about **450.2M WLD** to the market — **281.6M** in community grants and **168.6M** in team-and-investor vesting — against **zero** buyback and **zero** burn. The Pressure Framework reads **+11.98% net** for the last 90 days. On **Jul 24 2026** World cut the daily unlock rate by **43%**, which drops the forward reading to **+6.95%** — lower, but still firmly inflationary.

## The verdict, in one paragraph

For the 90-day window ending **Jul 28 2026**, the Pressure Framework reads **WLD at +11.98% net**. Sell pressure totals **450.2M WLD**, buy pressure is **zero**, against a circulating base of **3,756.47M WLD**. Our supply monitor reads the realised change at **+13.76%**, which looks like a **1.78 percentage-point** gap — but it resolves completely on inspection and ships no monitor-gap chip. The monitor divides the same unlock flow by the supply as it stood 90 days ago (**3,300.89M**); the framework divides by today's larger circulating base. That base convention accounts for **1.66pp** of the gap, and a sub-one-percent difference between the scheduled unlock (**450.2M**) and the realised circulating delta (**454.1M**) accounts for the rest. Both readings agree the same way: World released roughly **450 to 454 million WLD** into the market this quarter. WLD is best characterised as **a fixed-cap coin whose only inflation is a scheduled unlock, with no offsetting sink on the buy side**.

## Sell pressure: where new WLD comes from

Sell #1, protocol inflation, is **zero**, and that is the structural fact everything else hangs on. World does not mint. Every one of the **10 billion WLD** was created at launch, the ERC-20 contract on Ethereum has no mint function, and there is no staking reward or block subsidy. So unlike a proof-of-stake chain, none of World's supply pressure is newly created coin — it is entirely the release of coins that already exist but were locked.

Sell #2, vesting unlocks, is **168.6M WLD**. The team and early-investor allocations — the Tools for Humanity investor and team tranches, about **24%** of total supply between them — unlock a fixed amount every day with no cliffs. That rate ran at **1.9M WLD** a day for most of the window and was cut to **1.3M** a day on **Jul 24 2026**, which is how the 90-day total lands at **168.6M**. Because the cut is now fully live, the framework projects the forward leg entirely at the lower rate — about **117.0M WLD** over the next 90 days.

Sell #3, Foundation and unscheduled unlocks, is the largest single row at **281.6M WLD**. This is the **75%** World Community allocation — grants distributed to Orb-verified people plus the ecosystem fund — released on the same daily linear schedule and controlled by the World Foundation. It ran at **3.2M WLD** a day and was halved to **1.6M** a day on **Jul 24 2026**. The framework books it here rather than under classic vesting because it is a Foundation-run grant program, but the evidence is the same published schedule, and the on-chain circulating delta confirms it: this community stream is bigger than the team and investor unlocks combined, and it is why the 43% cut, though real, still leaves supply growing. Sell #4, long-term locked or bankruptcy, is **zero** — there is no World bankruptcy estate, no trustee and no court-ordered distribution.

## Buy pressure: where new WLD goes

Every buy row is **zero**, and that is the other half of why WLD reads so inflationary. Buy #1, programmatic buyback, is zero because World runs none — no protocol mechanism and no Foundation wallet is buying WLD on the open market. Buy #2, protocol fee burn, is zero and is structurally impossible: World Chain is an OP-stack Ethereum layer-2 whose gas is paid in **ETH** — currently subsidised for users by Tools for Humanity — so network activity destroys no WLD, and the WLD contract has no burn function to call in the first place. Buy #3, Foundation buy, is zero, with no disclosed open-market purchase by the World Foundation or the developer company. Buy #4, new long-term lock, is zero — supply is moving the other way this window, out of locks and into the float, and staking WLD is not a lock because it can be withdrawn. With no minting on the sell side and no sink on the buy side, WLD's inflation is exactly the unlock schedule, nothing more and nothing less.

## Foundation and overhang

The overhang is enormous but unusually legible. About **6.24 billion WLD** — the gap between the **10 billion** minted and the **3,756.47M** circulating — is still locked, and every coin of it is on the published daily schedule with no cliffs and no discretionary releases. The community share of that overhang drains at the new **1.6M WLD** a day, and the team-and-investor share at **1.3M** a day, all the way to the final tranche **15 years** after launch, in **2038**. There is no separate treasury wallet firing outside the calendar and no bankruptcy residual to track. Both streams are re-read on every rebuild from the official schedule and the on-chain circulating supply; if either balance moves faster than the schedule between refreshes, the excess enters Sell #3 at the next refresh. The key point for a holder is that the overhang is more than **60%** of all WLD, and it is contractually committed to keep arriving — the only variable the project controls is the rate, which it just lowered.

## How WLD compares to other fixed-cap unlock tokens

WLD sits in the same structural class as large pre-minted, hard-capped tokens whose supply curve is a vesting calendar rather than a mint — the pattern common to venture-backed layer-1s and app-tokens launched with a fixed genesis supply. Against a proof-of-work coin like Bitcoin, the contrast is total: Bitcoin's inflation is a shrinking block subsidy on a halving schedule and its float is already most of its cap, whereas WLD mints nothing yet still reads double-digit quarterly inflation because more than half its supply is waiting to unlock. Against an uncapped proof-of-stake chain, WLD actually looks cleaner in one respect — there is a hard **10 billion** ceiling that can never be raised — but far heavier in another, because the distance between circulating and total supply is **6.24 billion** coins rather than a thin non-circulating sliver.

The sharpest comparison is against tokens that pair unlocks with a sink. Exchange tokens with quarterly buybacks, or fee-burning smart-contract chains, offset some or all of their new supply; WLD offsets none. It has no burn, because gas is paid in ETH, and no buyback, because none has been funded. That is the single biggest difference between WLD and a coin like BNB or a base-fee-burning L1: those can run net-flat or net-deflationary in a busy quarter, while WLD is mechanically pinned to positive net supply until either the schedule runs down or the project introduces a sink it does not have today. The **43%** cut narrows the gap versus its peers but does not change the category — WLD is still an unlock token with an empty buy side.

## What to watch in the next 90 days

First, whether the post-cut rate holds: the framework's forward reading of **+6.95%** assumes the full window runs at **2.9M WLD** a day, and any further schedule change would move it. Second, whether World ever introduces a buy-side sink — a WLD-denominated fee, a burn, or a funded buyback — since that is the only thing that could pull the net reading toward neutral before the schedule itself winds down years from now. Third, the pace of realised grant claims: community grants only pressure the market when Orb-verified users actually claim and move them, so a widening or narrowing gap between the scheduled unlock and the on-chain circulating delta is worth tracking each rebuild. Fourth, any move to pay World Chain gas in WLD instead of subsidised ETH, which would create the first genuine demand sink for the token. Fifth, governance or Foundation announcements around the remaining **6.24B** locked coins, which stay on the calendar through **2038** unless the project changes it again.

## Summary

World is a fixed-cap token whose entire inflation is a scheduled unlock: all 10 billion WLD were pre-minted, the contract cannot mint or burn, and over the 90 days to Jul 28 2026 the daily unlock released about 450.2M WLD — 281.6M in community grants and 168.6M in team-and-investor vesting — against no buyback and no burn, for a net reading of +11.98%. The Jul 24 2026 cut lowered the daily rate by 43% and drops the forward reading to +6.95%, but the direction does not change, because there is nothing on the buy side to offset the release. The key structural fact is the 6.24 billion WLD still locked — more than 60% of all supply, committed to keep arriving on a no-cliff schedule through 2038 — and the key risk is that WLD has no sink at all, so its net supply stays positive until the schedule winds down or the project builds a demand mechanism it does not yet have.

---

*MrNasdog Pressure Framework analysis of World (WLD), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 28 2026.*
