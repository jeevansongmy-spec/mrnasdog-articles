---
title:         "ETH Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description:   "Mixed flows, supply roughly steady: Ethereum created about 259K ETH for validators and burned only 3.4K over 90 days, so ETH supply grows 0.21% net with no cap."
canonical_url: "https://mrnasdog.com/research/eth/inflation"
tags:          ["crypto", "eth", "ethereum", "staking"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/eth/inflation](https://mrnasdog.com/research/eth/inflation)*

# ETH Inflation Analysis · September 2026 · Mixed flows, supply roughly steady

**ETH, the gas coin of Ethereum, has no supply cap and no vesting: Ethereum pays its validators in newly created ETH, and the amount rises with the square root of how much ETH is staked. Over the 90 days to Sep 13 2026, Ethereum issuance created about 259K ETH on a stake that grew to 43.18M ETH, and Ethereum Foundation payouts sent another 5,775 ETH to recipients, while the EIP-1559 base-fee burn and the blob-fee burn destroyed only 3,421.5 ETH. The MrNasdog Pressure Framework therefore reads ETH at +0.21% net over the last 90 days and +0.21% over the next 90, against a supply-monitor reading of +1.14% — a gap of 0.93 percentage points that traces to a one-day jump in the monitor's upstream supply field, not to new ETH. ETH supply grows slowly, with nothing on the buy side large enough to offset issuance.**

## The verdict, in one paragraph

For the 90-day window ending **Sep 13 2026**, the Pressure Framework reads **ETH at +0.21% net**: **264,775 ETH** reached the market through Ethereum validator issuance and Ethereum Foundation outflows, against **3,422 ETH** removed by the fee burn, on a circulating supply of **122.04M ETH**. The independent supply monitor reads the same window at **+1.14%**, a gap of **0.93 percentage points**, which is over the framework's half-point tolerance, so ETH ships with a **data-conflict flag**. A five-source walk found the cause: the monitor's supply series sat near **120.68M** from June through **Sep 2 2026** and then jumped **1,327,331 ETH** in one day on **Sep 3 2026**, while the chain itself added roughly **2.9K ETH** that day. The forward column reads **+0.21%** as well, so the Inflation score is **2 of 5**. The label for ETH is **mildly inflationary by staking issuance**: a chain whose supply rises with its stake, and whose fee burn has become too small to matter.

## Sell pressure: where new ETH comes from

Sell #1, protocol inflation, is **259K ETH**, and it is nearly the whole Ethereum sell side. Ethereum proof-of-stake pays each epoch's rewards out of new ETH, and the protocol sizes that reward to the square root of the total staked balance, so more stake means more issuance but less per staker. The staked balance was read straight from the beacon chain registry rather than from a dashboard: **43,176,622 ETH** of active balance across **911,512** validators at the end of the window, against about **39.7M ETH** when it opened. Integrating the issuance curve across the **20,250** epochs between those two points, at the participation rate measured today, gives **259K ETH** over 90 days. Rewards are paid per epoch rather than per block, so the handful of empty slots changes nothing. The forward figure keeps that trailing pace, and it is a floor: **1.84M ETH** is still waiting in the deposit queue to join the Ethereum stake, and no validator is scheduled to leave.

Sell #2, vesting unlocks, is **zero**. Ethereum has no vesting contract; the 2014 ETH sale and the founding allocations were distributed years ago, and no unlock tracker carries a remaining ETH release. Sell #3, foundation and unscheduled unlocks, is **5,775 ETH**, and it is measured rather than estimated. The Ethereum Foundation's nine wallets were read at both ends of the window, and every wallet's inflows, outflows and fees close against its balance change. Only ETH that left the group is counted: **3,305 ETH** paid out by two disbursing wallets to grant and expense recipients, and one **2,469 ETH** grant tranche that unlocked on **Jul 1 2026** and was claimed four days later. Sell #4, long-term locked or bankruptcy supply, is **zero**: no estate or trustee schedule distributes ETH in kind, and companies holding ETH treasuries bought on the open market, so those coins were already in the float.

## Buy pressure: where new ETH goes

Buy #2, the protocol fee burn, is the only thing on the Ethereum buy side, and it is small: **3,421.5 ETH** over 90 days. Since EIP-1559 the base fee of every Ethereum transaction is destroyed, and since the blob upgrades the fee rollups pay for blob space is destroyed too. Every one of the **645,608** blocks in the window was swept, and the burn came to about **38 ETH** a day, of which blob fees contributed just **4.5 ETH** in total. Priority tips go to validators and are not burned. The rate held steady across the window — the second half burned barely more than the first — so the forward figure holds it flat. That burn offsets roughly one ETH for every **76** that issuance creates.

Buy #1, programmatic buyback, is **zero**: Ethereum has no protocol treasury and buys nothing back. Buy #3, foundation buying, is **zero**: the Ethereum Foundation spends its ETH and no purchase appears in any of its wallets this window. Buy #4, new long-term locks, is **zero**: ETH staking is slashable but has no stated lock size and no cap, and staked ETH remains inside circulating supply, so a growing Ethereum stake removes nothing from the float — it shows up on the sell side instead, as higher issuance.

## Foundation and overhang

The one team-controlled ETH overhang is the Ethereum Foundation treasury. Its largest safe holds about **68K ETH**, and **69.6K ETH** more is staked through **34** Foundation validators whose rewards sweep back into that safe. A DeFi multisig holds about **20.2K ETH** plus ETH lent and staked inside DeFi positions, and the older main wallet holds about **6.8K ETH**. Two disbursing safes refill two payout wallets in round tranches, which is why grant payments reach the market steadily rather than in lumps. One further Foundation grant tranche of **2,469 ETH** sits in a time-locked contract until **Jul 1 2027** and is watched as a scheduled release. Every wallet is re-read on each refresh; if any Foundation balance falls between refreshes and the ETH lands outside the group, the outflow enters Sell #3 at the next refresh.

## How ETH compares to other large smart-contract chains

ETH belongs to the uncapped proof-of-stake chains, and its structural difference from a hard-capped proof-of-work chain is direction and timing. A capped chain issues a fixed subsidy that halves on a calendar until it reaches a ceiling, so its supply growth is known years ahead. Ethereum issuance is set by participation instead: the more ETH is staked, the more ETH is created, with no ceiling and no calendar. That makes Ethereum's issuance a live response to staking demand, and it is currently rising as the deposit queue clears.

Against other uncapped proof-of-stake chains, Ethereum stands out on the burn. Most staking chains either burn nothing or burn a fixed slice of fees; Ethereum burns the entire base fee, which once made ETH supply fall outright. That burn now offsets barely more than one percent of issuance, because most Ethereum activity has moved onto rollups that settle on cheap blob space. Against zero-issuance chains that pay validators from fees and add a scheduled burn, ETH is the mirror image: those chains shrink toward a floor, while ETH grows by a fraction of a percent each quarter. The honest trade-off is that Ethereum issuance buys security from a stake worth more than a third of ETH supply, and the price is steady dilution for anyone who does not stake.

## What to watch in the next 90 days

First, the Ethereum deposit queue: **1.84M ETH** is waiting to activate, and as it clears the issuance rate rises above the **259K ETH** the forward column holds. Second, the Glamsterdam upgrade, scheduled for the Sepolia test network on **Oct 6 2026** with mainnet later: it changes block building and capacity, not the ETH issuance curve or the burn rule, but more L1 activity would lift the fee burn. Third, EIP-8363, a draft proposal published **Aug 4 2026** that would burn a rising share of staking rewards; it has no upgrade slot, and it would reshape Sell #1 only if it is scheduled. Fourth, the Ethereum Foundation's disbursing wallets, which paid **3,305 ETH** to recipients this window and set the forward Sell #3 figure.

## Summary

The MrNasdog Pressure Framework reads ETH at **+0.21% net** over the trailing 90 days and **+0.21%** over the next 90, giving an Inflation score of **2 of 5**. The structural mechanism is Ethereum proof-of-stake issuance of about **259K ETH** a quarter, sized by a **43.18M ETH** stake, plus **5,775 ETH** of Ethereum Foundation payouts, against an EIP-1559 and blob-fee burn of only **3,421.5 ETH**. The key risk is that issuance keeps climbing with the stake while the burn stays small, so dilution edges higher unless Ethereum L1 fee demand returns. There is no supply cap: the only ceiling on ETH issuance is the square-root curve itself, and it can be changed only by a hard fork.

*MrNasdog Pressure Framework analysis of ETH, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 13 2026.*
