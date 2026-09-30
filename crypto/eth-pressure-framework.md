---
title:         "ETH Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "ETH is mildly inflationary: 262K ETH of validator issuance against a 4.07K fee burn gives +0.21% net over 90 days, the same next. No vesting, no unlock, no cap."
canonical_url: "https://mrnasdog.com/research/eth/inflation"
tags:          ["crypto", "eth", "ethereum", "staking"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/eth/inflation](https://mrnasdog.com/research/eth/inflation)*

# ETH Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

ETH supply is growing slowly and steadily. Over the 90 days to Sep 30 2026, Ethereum paid its validators **262,002 ETH** of brand-new coins, while the EIP-1559 fee burn destroyed **4,073 ETH**, so net supply rose **+0.21%**, and the next 90 days project the same **+0.21%**. There is no vesting, no unlock and no buyback: ETH supply is set by two protocol rules, validator issuance in and the fee burn out, and ETH has no supply cap.

## The verdict, in one paragraph

The MrNasdog Pressure Framework reads Ethereum at **+0.21%** net new supply over the last 90 days and **+0.21%** for the next 90. The inflation monitor reads **+1.15%**, a gap of **+0.94 percentage points**, which is above the 0.5-point line, so the ETH page carries a ⚠ monitor-gap note. We walked the gap back to its source: the supply figure the monitor reads sat near 120.68M ETH for months, then jumped **1.33M ETH** in a single day on Sep 3 2026 to catch up with the chain. That jump was a recount of ETH that already existed, not new ETH, and the chain itself shows no such step. Our number stays. In one line: ETH is a **mildly inflationary proof-of-stake coin** whose issuance is roughly 64 times its fee burn.

## Sell pressure: where new ETH comes from

All new ETH comes from protocol inflation. Ethereum creates **262,002 ETH** in 90 days to pay its validators, about **2,911 ETH a day**, or roughly 0.87% of supply a year before the burn. The ETH reward is not a fixed amount per block. Each epoch, the Ethereum protocol pays a reward that grows with the square root of all staked ETH, so a bigger stake means more new ETH in total, even though each validator earns a lower rate. That stake is still rising. At the end of the window **43.74M ETH** was active across 882,608 validators, about 36% of all ETH; **3.90M ETH** was deposited to stake during the 90 days; and another **1.58M ETH** is still waiting in the entry queue.

We measured ETH issuance two ways. Ethereum supply read at both ends of the window, with the burned ETH added back, gives 262,002 ETH. Ethereum's own reward rule, applied to the stake at the start and end of the window, gives about 265,900 ETH at perfect validator performance; the measured figure is 98.5% of that, which is what normal participation looks like. The two readings sit 1.5% apart.

The other three sell rows are zero. Vesting unlocks are **0**: the 2014 ETH sale and the founder allocations could move from the first block in 2015, unlock trackers list Ethereum as fully unlocked, and circulating ETH equals total ETH. Foundation and unscheduled unlocks are **0**: the Ethereum Foundation does hold and sell ETH, but every one of those coins is already counted as circulating, so a sale moves ETH from one holder to another without adding supply. Long-term locks and bankruptcy releases are **0**: no estate, trustee or lock contract is paying ETH out.

## Buy pressure: where new ETH goes

The only thing that removes ETH is the protocol fee burn. Under EIP-1559 the base fee on every Ethereum transaction is destroyed, and since the blob upgrade the blob fee that rollups pay is destroyed too. Summed block by block over all 645,464 blocks in the window, the burn came to **4,073 ETH**, about 45 ETH a day. Blob fees were a tiny part of it, just 5.6 ETH. The burn picked up sharply at the end of September: **1,237 ETH** burned in the last ten days alone, as busier blocks pushed the base fee up. No Ethereum upgrade or fee rule changed, so the ETH forecast keeps the 90-day rate, but a burn that stays at the late-September pace would cut net supply growth noticeably.

The other buy rows are zero. There is no programmatic buyback: no Ethereum contract or treasury buys ETH off the market. There is no Foundation buy: the Ethereum Foundation spends and stakes its ETH, and nothing this window shows it buying. New long-term locks are **0** as well. Staking is real, slashable and growing, but staked ETH still counts as circulating supply, so a larger stake takes nothing out of the float. In fact it works the other way: more staked ETH raises ETH issuance.

## Foundation and overhang

The one team-held pile of ETH we track is the Ethereum Foundation's. Its four known wallets hold about **94,170 ETH**: 68,084 ETH in its main Safe, 20,176 ETH in a multisig, 5,774 ETH in its oldest wallet and 134 ETH in another. On top of that, the Foundation has about **70,000 ETH** staked in its own validators, with the rewards flowing back to its treasury. This window its oldest wallet paid out 4,000 ETH and its main Safe gained 444 ETH of staking rewards. There is no DAO treasury, no unscheduled unlock pool and no buyback wallet. Funds and listed companies hold far more ETH than the Foundation (the largest company reports about 6.0M ETH), but they bought it on the market, so it was already part of the float.

We re-read these Foundation wallets on every rebuild. Because ETH's circulating supply equals its total supply, no ETH wallet sits outside the float today, so a Foundation sale moves coins between holders rather than adding new ones. If a balance outside the circulating count ever appears and then falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How ETH compares to other smart-contract Layer 1s

ETH vs BTC: Bitcoin has a hard cap of 21M coins and a fixed issuance schedule that halves about every four years, with no fee burn at all. Ethereum has no cap, and its issuance is set by how much ETH is staked, not by a calendar. Bitcoin's new supply falls on a timetable no matter what users do; Ethereum's new supply rises when more ETH is staked and is partly cancelled when more people pay fees. Right now both grow at a similar yearly pace, a little under 1%, but for different reasons, and only Ethereum can in principle shrink.

ETH vs other proof-of-stake chains: many Layer 1s pay stakers from a preset inflation schedule that starts high and steps down year by year, and most burn little or nothing. Ethereum's design is different on both counts. Its issuance follows the size of the stake instead of a timetable, and it destroys the base fee of every transaction. That burn once outpaced ETH issuance for long stretches. Today, with most activity moved to cheaper rollups built on top of Ethereum, the burn is small, and the mechanism that decides ETH's supply is the stake.

ETH vs exchange tokens and buyback coins: those coins shrink supply on purpose, with a company buying back and destroying coins from its profits. Ethereum has no owner and no buyback. Its only offset to issuance is the fee burn, which depends on how busy Ethereum blocks are, not on anyone's decision to spend.

## What to watch in the next 90 days

**Oct 6 2026**: the Glamsterdam upgrade goes live on the Sepolia test network. It changes gas costs and paves the way for bigger blocks, but it does not change ETH issuance or the burn rule, and its Ethereum mainnet date is not yet set.

**The staking queue**: 1.58M ETH is waiting to start validating. As it joins, the stake grows and ETH issuance rises a little above the trailing rate this page projects.

**The burn**: if the late-September pace of about 124 ETH a day holds, the burn would roughly triple from its 90-day average, still far below issuance but a real change in ETH's net supply.

**Issuance policy**: EIP-8363, a proposal to burn part of validator rewards, was declined for the next upgrade on Sep 7 2026. Developers said issuance needs its own process, so any change to how ETH is paid out would come later and be announced well ahead.

**Dec 2 2026**: around then the monitor's 90-day window moves past the Sep 3 2026 recount, and its reading should drop back close to ours.

## Summary

The MrNasdog Pressure Framework reads ETH at **+0.21% net** over the last 90 days and **+0.21%** over the next 90: **262,002 ETH** of validator issuance against a **4,073 ETH** EIP-1559 fee burn, with no vesting, no unlocks and no buyback. Ethereum's supply is driven by staking: the more ETH is staked, the more new ETH the protocol pays out, and the stake is still growing with 1.58M ETH in the entry queue. The key risk to this reading is that issuance keeps rising with the stake while the burn stays small; the upside case is a busier chain that burns more. ETH has no supply cap, so supply keeps growing until the burn catches up or Ethereum changes how validators are paid.

---

*MrNasdog Pressure Framework analysis of ETH, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 30 2026.*
