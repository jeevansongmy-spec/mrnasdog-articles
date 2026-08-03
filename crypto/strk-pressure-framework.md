---
title:         "STRK Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description:   "Starknet adds about 916M STRK per 90 days from live monthly vesting cliffs, with zero buyback and zero burn. Framework reads +13.45% net now and +10.07% forward; the monitor reads +15.53%, a 2.08pp denominator gap."
canonical_url: "https://mrnasdog.com/research/strk/inflation"
tags:          ["crypto", "strk", "starknet", "layer2"]
published:     true
---

*Originally published at [mrnasdog.com/research/strk/inflation](https://mrnasdog.com/research/strk/inflation)*

Starknet's STRK reads **+13.45%** net new supply over the 90 days to **Aug 3 2026** on the MrNasdog Pressure Framework, and projects **+10.07%** over the next 90 — strongly inflationary in both directions. The driver is structural vesting: a published **127M STRK** unlock every month to early contributors and investors that runs until **Mar 15 2027**, with other genesis pools releasing on the same calendar, so circulating supply grew about **916M STRK** in the window. There is **no buyback** and **no STRK fee burn** to offset it, and staking minting is tiny. Our supply monitor reads **+15.53%** — a **2.08 percentage-point** gap that is the denominator convention, so a data-conflict flag ships with the page.

## The verdict, in one paragraph

For the 90-day window from **May 5 2026** to **Aug 3 2026**, the framework reads **STRK at +13.45% net**: sell pressure of about **916M STRK** against buy pressure of **zero**, on a circulating base of **6.81B STRK**. Our supply monitor reads **+15.53%** for the same period, a gap of **2.08 percentage points** that clears the framework's half-point tolerance, so a monitor-gap chip ships on the STRK overview page. That gap is not a disagreement about how much supply grew — both readings agree Starknet added roughly **915.8M STRK** — it is purely the denominator convention: the monitor divides that growth by the supply 90 days ago (**5.90B**, giving +15.53%) while the framework divides by today's larger circulating base (**6.81B**, giving +13.45%). The label for STRK is a **structurally inflationary token with a live monthly unlock and no offsetting sink**.

## Sell pressure: where new STRK comes from

Almost all of it is vesting. **Vesting unlocks** are the engine, at about **381M STRK** over the window. Starknet's published schedule releases **127M STRK every month on the 15th** to early contributors and investors, in a phase that began **Apr 15 2025** and runs until **Mar 15 2027**; three of those cliffs fall inside every 90-day window, so about 381M STRK unlocks to insiders each period. These are not theoretical calendar entries — they were seen reaching circulating on-chain month by month across the window, with the supply series stepping up in **May**, **June** and **July** rather than in any single spike.

**Foundation and unscheduled unlocks** add about **530M STRK**. The Foundation strategic reserves and treasury, grants, community pools and the StarkWare allocation also vest on the tokenomics calendar, and were observed reaching circulating on-chain alongside the insider cliffs every month across the window. The monthly circulating steps ran above the insider quantum each month, and that residual above insider vesting plus staking is booked here.

**Protocol inflation** is small at about **5M STRK**. New STRK is minted only to pay staking rewards, on a governance-set curve capped at **1.6%** a year and running near **0.3%** today, so issuance is tiny next to the vesting unlocks. No block reward is issued while a single operator runs the sequencer. **Long-term locked or bankruptcy** is **zero** — no estate, trustee schedule or court order touches STRK.

## Buy pressure: where new STRK goes

Nowhere — every buy row is **zero**, which is what makes STRK read as one-way. **Programmatic buyback** is zero: there is no open-market STRK buyback, so nothing bids against the monthly unlocks on exchanges. **Protocol fee burn** is zero: Starknet does not burn STRK, because network fees pay the sequencer and settle in ETH, so there is no per-block STRK burn the way an EIP-1559 chain removes its own gas token. **Foundation buy** is zero: no disclosed open-market STRK accumulation, and no wallet shows a position being built from exchanges. **New long-term lock** is zero: staking holds over **1B STRK** and does take some float off the market, but staked STRK is still counted as circulating and can be unstaked, so the framework treats it as a mitigant rather than a supply removal, and no new multi-year lock or escrow was announced in the window. With the entire buy ledger empty, the roughly **916M STRK** of new supply reaches the market unopposed.

## Foundation and overhang

The standing overhang on STRK is large and known. Of the **10B STRK** genesis supply, about **6.81B** is circulating (68.1%), which leaves roughly **3.19B STRK** still non-circulating. That balance is not a discretionary treasury sitting idle — it is scheduled vesting across the same buckets already releasing: the early-contributor and investor tranche unlocking **127M** a month to **Mar 2027**, plus the Foundation strategic reserves and treasury, grants, the community provisions and rebates pools, and the StarkWare allocation, all of which continue releasing on the tokenomics calendar that runs into **2031**. We read circulating supply on-chain on every rebuild, so if these pools' balances fall between refreshes, that outflow enters the Foundation-and-unscheduled row at the next refresh — which is exactly what the framework observed happening month by month this window. The overhang is the story: STRK is only two-thirds distributed, and the remaining third is contractually scheduled to keep arriving.

## How STRK compares to other uncapped-emission tokens

The right peer group for STRK is not a hard-capped, halving chain — it is a large genesis allocation still working through a multi-year vesting calendar. Against a halving-model chain with a fixed cap, STRK is the opposite shape: a halving chain's new supply shrinks on a schedule and its float is largely already free, while STRK's new supply is delivered by unlock cliffs and its float is still climbing from two-thirds toward full distribution. The dilution here comes from the vesting calendar, not from block rewards.

The more useful comparison is with other recent layer-two and layer-one tokens that launched with heavy investor and team allocations on multi-year cliffs — the same structural pattern of a low initial float followed by years of scheduled unlocks. Against that class STRK is a fairly pure example: a documented monthly cliff, a transparent published schedule, and — crucially — no counter-mechanism. Many peers in this class have at least a fee burn that scales with usage or a revenue-funded buyback that removes supply in steps; STRK has neither, so its unlocks are not partially offset the way a burn-and-unlock token's are. The distinction that matters is exactly that: a chain that burns a share of fees can grow usage into a lower net issuance, whereas STRK's net supply change is governed almost entirely by the unlock calendar until that calendar ends in 2027.

The honest summary of the comparison is that STRK today behaves like a mid-distribution token whose supply curve is dominated by a known, dated unlock schedule with nothing pulling the other way. It is not hidden or surprising dilution — it is on the calendar — but it is real, it is monthly, and it is unopposed.

## What to watch in the next 90 days

First, the monthly vesting cliffs on **Aug 15 2026**, **Sep 15 2026** and **Oct 15 2026**, each releasing about **127M STRK** to contributors and investors — the single most predictable supply event, and the reason the next-90-day read stays strongly inflationary at **+10.07%**. Second, the governance forum proposal to **reduce STRK maximum supply to 1B** by burning unused treasury and future allocations: it is discussion only today, not voted and not executed, but a passed-and-executed version would be the first real deflationary lever this token has ever had, and would move the ledger materially. Third, the staking participation rate — Starknet has over **1B STRK** staked and growing, and rising participation both locks more float and nudges the minting curve toward its **1.6%** ceiling. Fourth, any first-time STRK buyback or fee-burn mechanism, which would be the first entry in an otherwise empty buy ledger. Fifth, the end of the current vesting phase in **March 2027**, after which the dominant 127M monthly cliff stops.

## Summary

The MrNasdog Pressure Framework reads STRK at **+13.45%** net new supply over the last 90 days and projects **+10.07%** over the next 90 — strongly inflationary and rising, with our supply monitor reading **+15.53%** and a **2.08 percentage-point** gap that is purely the denominator convention. The mechanism is a published **127M STRK** monthly vesting unlock to contributors and investors that runs until **March 2027**, with other genesis pools releasing on the same calendar, growing circulating supply about **916M STRK** in the window. The key risk is that this dilution has **no offset** — no buyback and no STRK fee burn — so new supply reaches the market unopposed, and roughly **3.19B STRK** is still non-circulating and scheduled to keep arriving into 2031. The one thing that could change the picture is a governance vote to burn treasury and cut the **10B** supply, which is being discussed but has not happened.

---

*MrNasdog Pressure Framework analysis of STRK, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 3 2026.*
