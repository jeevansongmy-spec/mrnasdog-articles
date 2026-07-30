---
title:         "OP Inflation Analysis · July 2026 · Supply growing, projected to keep growing"
description:   "Optimism is a fixed-cap token still running inflationary: ~135.7M OP vested last quarter vs a 4.7M buyback, net +5.73% (monitor +6.31%), with a 116M unlock due Sep 21 2026."
canonical_url: "https://mrnasdog.com/research/optimism/inflation"
tags:          ["crypto", "op", "optimism", "layer2"]
published:     true
---

*Originally published at [mrnasdog.com/research/optimism/inflation](https://mrnasdog.com/research/optimism/inflation).*

**TL;DR.** Optimism is a fixed-cap token that is still inflationary by its vesting. OP can never exceed **4,294,967,296** and has **no protocol mint**, yet over the last 90 days about **135.7M OP** vested out of the original allocation and into the **2.29B** circulating float — most of it in a single mid-July cliff. A real revenue buyback absorbs only about **4.7M OP** a quarter, so the framework reads **+5.73% net** against a supply monitor at **+6.31%**. With a **116M OP** unlock scheduled for Sep 21 2026, the next quarter looks just as inflationary.

## The verdict, in one paragraph

For the 90-day window ending Jul 31 2026, the Pressure Framework reads **OP at +5.73% net**. Sell pressure totals **135.7M OP** of vesting and buy pressure totals **4.7M OP** of buyback, against a circulating base of **2.29B OP**. Our supply monitor reads the realised change at **+6.31%**, a gap of about **0.58 percentage points**, which is just over tolerance and ships a monitor-gap chip on the OP overview. The gap is by mechanism, not error: the buyback buys OP off the open market and parks it in a treasury wallet the monitor still counts as circulating, so the framework nets out roughly **4.7M OP** the monitor does not, and the small remainder is the denominator base convention. OP is best characterised as **inflationary on a fixed cap** — capped in the long run, but heavily front-loaded with vesting the market is still absorbing.

## Sell pressure: where new OP comes from

Sell #1, protocol inflation, is **0**, and it always will be. Optimism does not mint OP to secure the chain — the L2 is settled and paid for in ETH, and the OP token supply is fixed at **4.29B**. So unlike an uncapped proof-of-stake L1, there is no ongoing issuance. Every unit of supply growth comes from Sell #2, vesting unlocks, which is **135.7M OP** for the window. This is the original token allocation — core contributors at 19%, investors at 17%, and the Foundation-run seed, partner, governance and ecosystem funds, plus user airdrops and RetroPGF — vesting out of lockup and into the tradable float. The proof is on-chain: circulating supply sat flat near **2.15B** from late April through Jul 6, then stepped up by roughly **121M OP** into mid-July, then went flat again at **2.29B**. OP does not drip; it releases in lumps.

Sell #3, Foundation and unscheduled unlocks, is **0** as a firing, but it is the largest overhang on the page: about **2.01B OP** — nearly half the cap — is still non-circulating across the ecosystem, partner, governance and seed funds and the Foundation treasury. That supply is released on the published vesting schedule already captured in Sell #2, and no separate off-schedule sale was observed, so it is monitored rather than booked. Sell #4, long-term locked or bankruptcy, is **0**: Optimism has no estate, trustee or court-ordered distribution.

## Buy pressure: where new OP goes

The buy side has one genuine mechanism. Buy #1, programmatic buyback, is **4.7M OP** for the quarter. In January 2026 the Optimism Collective voted, with **84.4%** in favor, to direct **50%** of net Superchain sequencer revenue into recurring OP buybacks — a 12-month pilot that has executed monthly since February, buying roughly **1.575M OP** a month through over-the-counter vendors to limit market impact. Crucially, the repurchased OP is **held in a treasury wallet, not burned**: on-chain that wallet holds about **9.45M OP** as of Jul 31 2026, and governance will later decide whether those tokens are burned, staked, or redeployed. So the buyback removes float today but is not yet a permanent sink.

The other three buy rows are zero. Buy #2, protocol fee burn, is **0** because OP Mainnet charges gas in ETH and the base-fee burn destroys ETH, never OP — network usage does not remove OP the way it removes the gas token on some chains. Buy #3, Foundation buy, is **0** beyond the revenue buyback already counted. Buy #4, new long-term lock, is **0**: OP has no protocol staking and no new lockup contract was deployed. The result is a lopsided ledger — **135.7M OP** of vesting against **4.7M OP** of buyback, a roughly 29-to-1 imbalance.

## Foundation and overhang

Two team-controlled overhangs sit behind the float. The first is the **non-circulating allocation**: about **2.01B OP**, the gap between the **4.29B** cap and the **2.29B** circulating, spread across the ecosystem, partner, governance and seed funds and the Foundation treasury, released on a vesting schedule that extends into 2029. The second is the **buyback treasury wallet** at 0x36c4E68d…, which holds about **9.45M OP** of repurchased tokens whose fate governance has not yet decided. Both are re-read on every rebuild. If the buyback wallet's balance falls between refreshes — a governance decision to redeploy the held OP — that outflow enters Sell #3 at the next refresh; and any off-schedule Foundation sale would land there too.

## How OP compares to other capped rollup tokens

The cleanest comparison is another capped rollup governance token like Arbitrum's ARB. Both share the same structure: a hard-capped supply, no protocol mint, and a multi-year vesting schedule that keeps releasing team, investor and ecosystem allocations into the float long after launch. For both, the headline "fixed cap" understates the near-term inflation, because the market is still absorbing the difference between circulating and fully diluted supply. OP's circulating is only about **53%** of its cap, so roughly **2.01B OP** of scheduled dilution is still ahead — the token behaves inflationary despite the ceiling.

Where OP differs is the buyback. Most L2 governance tokens have no revenue-to-token pipe at all; OP is unusual in routing **50%** of Superchain sequencer revenue into OP purchases. But the scale gap is the point: sequencer revenue funds only about **4.7M OP** of buying a quarter, while vesting adds **135.7M OP**. Against an uncapped proof-of-stake L1 that mints continuously, OP at least has a finite ceiling and a shrinking release runway; against a deflationary fee-burn token, OP is the opposite — its supply is still expanding, and its one buy mechanism holds rather than burns. That makes OP a **front-loaded, cap-bounded inflation** story rather than a scarcity one.

## What to watch in the next 90 days

First, the **Sep 21 2026** unlock of about **116M OP** — roughly **6.89%** of circulating — the single largest cliff in the forward schedule and the main reason the next-90-day reading stays inflationary. Second, whether the buyback pilot is renewed or expanded when its 12-month term ends, and whether governance votes to **burn** the roughly 9.45M OP already held, which would turn Buy #1 from a temporary hold into a permanent sink. Third, the monthly buyback execution reports, since a higher OP price or higher Superchain revenue would grow the quarterly buy above **4.7M OP**. Fourth, any Foundation transparency post signalling an off-schedule ecosystem-fund deployment. Fifth, smaller seed-fund unlocks around Oct 11 2026 that add to the drip.

## Summary

Optimism is a fixed-cap token that still reads inflationary: OP cannot exceed 4.29B and has no protocol mint, but about 135.7M OP vested into the float over the last 90 days — largely one mid-July cliff — against only 4.7M OP of revenue buyback, for a net of +5.73% versus a monitor at +6.31%. The structural fact is that circulating is only about 53% of the cap, leaving roughly 2.01B OP of scheduled dilution ahead, with a 116M OP unlock due Sep 21 2026. The key risk is that the one offsetting mechanism, the Superchain-revenue buyback, holds its OP in treasury rather than burning it, so unlike a deflationary token OP's supply keeps expanding while the vesting schedule runs.

*MrNasdog Pressure Framework analysis of Optimism (OP), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 31 2026.*
