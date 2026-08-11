---
title:         "STRK Inflation Analysis · August 2026 · A cliff every month, and nothing on the other side"
description:   "Starknet releases about 128M STRK on the 15th of every month until Mar 15 2027 and mints more on top through staking, against a buy ledger of four zeros. Framework reads +6.13% net now and +6.18% forward; the monitor reads +15.43%, a 9.30pp gap."
canonical_url: "https://mrnasdog.com/research/strk/inflation"
tags:          ["crypto", "strk", "starknet", "layer2"]
published:     true
---

*Originally published at [mrnasdog.com/research/strk/inflation](https://mrnasdog.com/research/strk/inflation)*

Starknet releases about **128M STRK** on the 15th of every month until **Mar 15 2027**, and its staking system mints new STRK on top of that — the token supply on Ethereum rose from **10,113.1M** to **10,149.5M** over the 90 days to **Aug 11 2026**. Against that, the buy ledger is four zeros: no buyback, no burn, no Foundation bid, no new lock. The MrNasdog Pressure Framework reads **+6.13%** net over the last 90 days and **+6.18%** over the next, on a circulating supply of **6.81B STRK**. Our supply monitor reads **+15.43%**, a gap of **9.30 percentage points**, because it also frees the **5.42B STRK** of genesis pools that carry no release dates. STRK is an unlock-driven token with a mint attached and nothing at all on the other side.

## The verdict, in one paragraph

For the 90-day window ending **Aug 11 2026** the framework reads **STRK at +6.13% net**, and projects **+6.18%** for the 90 days ahead. Two rows carry the whole ledger: the Starknet staking mint at **36.4M STRK**, and the published monthly unlock at **384.7M STRK** across the three cliffs on **Aug 15 2026**, **Sep 15 2026** and **Oct 15 2026**. Our supply monitor reads the realised change in circulating STRK at **+15.43%**, so the gap is **9.30 percentage points** and a **data-conflict chip ships** with the page. That gap is not an error on either side — the monitor's float releases every genesis pool as its designated wallets drain, while the framework books only what a published calendar or a chain read can defend. The label for STRK is precise: **an unlock-driven layer two with a live mint and an empty buy side**.

## Sell pressure: where new STRK comes from

Sell #1, protocol inflation, is **36.4M STRK**, and unusually for a layer two it is a real, measurable mint. Starknet pays its validators in newly created STRK under the minting curve the community approved, which scales issuance with the share of STRK staked and caps it at **4%** a year. Reading the Starknet token contract on Ethereum at both ends of the window gives the answer directly: **10,113.1M STRK** on **May 13 2026** and **10,149.5M STRK** on **Aug 11 2026**. Intermediate reads across the window show a smooth run rate of about **0.40M** new STRK a day with no step in it, which is why the framework carries the same figure forward. Annualised, that is roughly **1.4%** — near the bottom of the band, because only about an eighth of the supply is staked. The two angles agree: the measured mint and the approved curve land within 1% of each other.

Sell #2, vesting unlocks, is **384.7M STRK** and is the dominant number on the page. Starknet allocated **20.04%** of supply to early contributors and **18.17%** to investors, and both groups unlock monthly in two phases — the second running from April 2025 to **Mar 15 2027** and releasing **3.048B STRK** in twenty-four equal steps of **127M**. Three of those steps fall inside every 90-day window. The next one, on **Aug 15 2026**, carries about **128.2M STRK** across both groups, and both are still only around **73%** released. This is the mechanism most STRK holders are actually exposed to: not a mint, but a handover.

Sell #3, Foundation and unscheduled unlocks, is **zero**, and the reason matters more than the number. Starknet's remaining genesis pools — StarkWare's own **10.76%**, grants and development partners **12.93%**, strategic reserves **10.00%**, foundation treasury **8.10%**, community rebates **9.00%** and donations **2.00%** — publish no release dates whatsoever, about **5.42B STRK** in total. The framework reads the wallets instead. Two identified project addresses held **1,001.3M** and **1,150.0M STRK** on **Aug 11 2026**, and the only large move inside the window, **100M STRK** on **Jul 28 2026**, went to another project-controlled address rather than to the market. Capacity is not a release, so the row stays at zero and the pools are tracked instead. Sell #4, long-term locked or bankruptcy, is **zero**: STRK has no estate, no trustee and no court-ordered distribution anywhere in its history.

## Two corrections to the previous read

This rebuild overturns two things the earlier version of this page said, and both are worth stating plainly.

The first is a claim that has circulated about Starknet more than once: that the on-chain vesting lock drew its whole remaining calendar in a single **April 2026** transfer and has released nothing since. It is refuted by this session's reads. The readable escrow is a family of **167** individual lock contracts holding **774.7M STRK** in grants over their lifetime, and its aggregate balance fell from **485.129M** to **469.107M STRK** inside this window — a realised release of **16.0M**. The **1,500M** move that prompted the claim was an internal transfer from a project safe to a project hot wallet, and it happened before this window opened. The locks are still draining, month by month, and so is the float.

The second correction is about method. The prior build sized its third sell row at roughly **916M STRK** by inferring it from the observed rise in circulating supply. That is exactly the back-derivation the framework bans, because the float series it was sized from *is* the monitor's own circulating-supply series — the number would have been the monitor's answer wearing the framework's clothes. Re-derived from primaries only, the defensible ledger is **417.4M** for the trailing window, and Sell #3 is set to **0**, since those genesis pools publish no dates. The consequence is visible on the page: the gap to the monitor widened rather than narrowed, and the framework carries it openly instead of closing it with a plug.

## Buy pressure: where new STRK goes

Nowhere. Buy #1, programmatic buyback, is **zero** — Starknet operates no buyback contract and has announced no buyback programme, so network growth never becomes a bid for STRK. Buy #2, protocol fee burn, is **zero**, and this one is the common misreading. Transaction fees on Starknet can only be paid in STRK since **Sep 1 2025**, and the late-June 2026 network upgrade made gas pricing dynamic and STRK-denominated, which sounds like an Ethereum-style burn. It is not. Those fees are paid onward to sequencers and stakers; nothing is destroyed, and the Starknet token supply on Ethereum has only ever risen.

Buy #3, Foundation buy, is **zero**: neither StarkWare nor the Starknet Foundation has disclosed or been observed buying STRK on the open market, and their wallets have only ever moved tokens outward. Buy #4, new long-term lock, is **zero**: over **1.3B STRK** is staked, which sounds like a lock, but the exit delay is short and the liquid staking protocol launched in 2026 hands stakers a tradable receipt — so staked STRK never leaves the tradable float. Four buy rows, four zeros. Everything the Starknet network does with STRK adds supply or moves it; nothing removes it.

## Foundation and overhang

The overhang on STRK is one of the largest in the framework by share of supply. Against **6.81B** circulating, roughly **5.42B STRK** of genesis allocation carries no published release date. Three pieces of it are readable on chain and the framework tracks all three. A project safe held **1,001.3M STRK** at both ends of the window — unchanged. A second project wallet fell from **1,250.0M** to **1,150.0M STRK**, the **100M** going to another project address on **Jul 28 2026**. And the family of **167** lock contracts fell from **485.1M** to **469.1M STRK** across the same window.

The tracking rule is simple: if any of these balances falls to a destination outside the Starknet project between refreshes, that outflow enters Sell #3 at the next refresh as genuine new market supply. On today's float, the untracked pools alone could add roughly **80%** to the circulating supply of STRK — which is why this row is watched rather than dismissed.

## How STRK compares to other Ethereum layer-two tokens

STRK sits in the hardest structural class the framework covers: **layer-two tokens that unlock on a calendar and burn nothing**. Its closest analogues are the other 2024-vintage rollup tokens that launched with a large genesis supply, a small initial float and multi-year investor and contributor schedules. Against Ethereum itself the contrast is total. Ethereum burns its base fee, so heavy usage pushes net supply toward zero or below and the token captures the network's success directly. Starknet charges its fees in STRK and forwards every one of them, so a busier Starknet moves more STRK through more hands without removing a single token. Usage and scarcity are simply not connected here.

Against the other rollup tokens, STRK carries the extra weight of a live mint. Most layer-two tokens have no issuance at all — their inflation is purely the release calendar. Starknet added a staking system with a minting curve, which is defensible security spending but makes STRK the rarer case where the unlock schedule and a real mint run at the same time. The mint is small, at roughly **1.4%** a year against an unlock stream worth about **5.6%** of the float per quarter, but it means STRK cannot rely on the usual layer-two consolation that the supply ceiling is fixed. It is not: the chain read is already **10,149.5M STRK** against a genesis of **10B**.

The third comparison is with exchange tokens and revenue-burning chains, and it explains the entire verdict. Those assets convert business performance into a shrinking supply through a quarterly buyback or a burn, so a good quarter is visible in the ledger as a negative number. Starknet has real usage and a real fee token and converts none of it. Until a governance decision routes some part of sequencer revenue into a buyback or a burn, the buy side of the STRK ledger will stay at four zeros no matter how well the network performs.

## What to watch in the next 90 days

**Aug 15 2026**, **Sep 15 2026** and **Oct 15 2026** are the three scheduled cliffs, about **128.2M STRK** each to early contributors and investors. Watch whether the market absorbs them the way it has absorbed the previous ones, and count down to **Mar 15 2027**, when this stream finishes and the largest single source of STRK supply pressure ends for good.

Watch the staking rate. The Starknet minting curve rises with the share of STRK staked, and the Foundation can move the constant that scales it within a **1.0%** to **4.0%** band — so a rise in staking or a decision to raise that constant would lift the mint above today's **36.4M** a quarter. Watch the two identified project wallets, at **1,001.3M** and **1,150.0M STRK**, and the **469.1M** still sitting in the lock contracts; a move from any of them to an exchange or a market maker is the event that would push Sell #3 off zero. Finally, watch Starknet governance for any proposal that turns sequencer fees into a burn or a buyback — that is the single change that would move this verdict.

## Summary

The framework reads STRK at **+6.13%** net over the 90 days to **Aug 11 2026** and **+6.18%** for the quarter ahead, against a supply monitor reading of **+15.43%** — a **9.30 percentage point** gap that the page carries openly, because the monitor frees genesis pools the framework will not book without a date or a chain read behind them. The mechanism is a published monthly cliff of about **128M STRK** running to **Mar 15 2027**, plus a staking mint of **36.4M** a quarter, set against a buy ledger of four zeros. The key risk is the **5.42B STRK** of genesis allocation with no release dates at all — nearly as much again as the entire circulating supply. And there is no ceiling to fall back on: Starknet's supply already reads **10,149.5M** against a **10B** genesis, and the minting curve is capped only in rate, never in total.

---

*MrNasdog Pressure Framework analysis of STRK, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 11 2026.*
