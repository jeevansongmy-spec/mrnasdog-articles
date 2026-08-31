---
title:         "TRX Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description:   "TRON minted 352.4M TRX and burned 237.0M in fees over 90 days. The framework reads +0.12% net — barely inflationary, with the burn covering ~67% of issuance."
canonical_url: "https://mrnasdog.com/research/trx/inflation"
tags:          ["crypto", "trx", "tron", "layer1"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/trx/inflation](https://mrnasdog.com/research/trx/inflation)*

# TRX Inflation Analysis · September 2026 · Mixed flows, supply roughly steady

TRON mints and burns TRX at the same time, and the burn hands back most — not all — of what the chain issues. Over the 90 days to **Sep 1 2026**, TRON block rewards minted **352.4M TRX** while the transaction-fee burn destroyed **237.0M TRX**, leaving **+0.12% net** supply growth against a supply monitor reading **+0.11%**. TRX has no cap, so the ceiling on TRON inflation is behavioural, not coded: TRX stays near flat only while fee burning keeps pace with a fixed **136 TRX** per block, and the burn now covers about **67%** of issuance — down from roughly **80%** at the start of the year.

## The verdict, in one paragraph

For the 90-day window ending **Sep 1 2026**, the MrNasdog Pressure Framework reads TRX at **+0.12% net** supply growth and projects **+0.12%** forward. Total sell pressure on TRON was **352.4M TRX** of block-reward issuance and nothing else. Total buy pressure was **237.0M TRX** of protocol fee burn, and every other row on both ledgers is zero. The supply monitor reads the same window at **+0.11%** — a gap of about **0.01 percentage points**, far inside the half-point tolerance, so no monitor-gap chip ships on the TRX overview. The two readings agree because TRON is effectively fully circulating: TRX circulating supply and TRON total supply differ by **0.3M TRX** out of **94.93B**, leaving no reserve bucket for them to disagree about. The cite-able label for TRX is a **stablecoin settlement chain whose fee burn returns about two-thirds of its block rewards** — inflationary by a hair, and widening slowly.

## Sell pressure: where new TRX comes from

Sell #1, protocol inflation, is the only live sell row on TRON, and it is pure protocol arithmetic. Every TRON block pays **8 TRX** to the Super Representative that produced it and **128 TRX** in vote rewards spread across the 127 Super Representatives and their voters — **136 TRX** per block, fixed, with no halving and no decay curve. Because TRON block times drift a fraction above the nominal three seconds, this build counted blocks rather than assuming them: the chain moved from block **83,258,604** to block **85,846,905** across the window, **2,588,301** blocks at an average of **3.0010** seconds, which normalises to **2,591,136** blocks over a full 90 days. That gives **352.4M TRX** of gross issuance, or about **3.92M TRX** a day. TRON governance cut this pay rate once, on **Jun 13 2025**, from **176 TRX** per block; nothing has touched it since, so the trailing rate is also the forward rate.

The figure was cross-checked against TRON's own quarterly disclosures before shipping. TRON reported **352.3M TRX** minted in Q1 2026 and **356.3M TRX** in Q2 2026 — a 91-day quarter, which is **352.4M** on a 90-day basis. Both land within **0.1%** of the block-counted number, which is the behaviour you expect from an emission that is indexed to blocks rather than to time and that no protocol constant re-scales.

Sell #2, vesting unlocks, is zero. TRON's founding allocations finished releasing on **Jan 1 2020** and no TRON team, investor or escrow cliff remains to fire. Sell #3, foundation and unscheduled unlocks, is also zero, and on TRON that zero is close to unarguable: circulating supply is **99.9997%** of total supply, so there is no off-float reserve a transfer could push into the market. Sell #4, long-term locked or bankruptcy, is zero because no estate holds TRX on a trustee schedule — the **Mar 31 2026** and **Jul 31 2026** bankruptcy distributions were paid in cash.

## Buy pressure: where new TRX goes

Buy #2, the protocol fee burn, is the load-bearing number on this page. TRON destroys resource fees rather than paying them to producers: when a sender holds no staked bandwidth or energy, the network burns TRX to cover the gap, and no fee pool routes any of it back. The chain keeps its own burn counter, which stood at **16.35B TRX** destroyed since genesis when this build read it — and because TRON total supply falls by the same amount, this is a real burn, not a transfer to an unspendable address that leaves supply untouched. Across the window the fee burn came to **237.0M TRX**, about **2.63M TRX** a day, of which roughly **80%** is energy consumed by contract calls — overwhelmingly stablecoin transfers.

The burn is falling, and that is the whole story of TRX inflation right now. TRON burned **281.8M TRX** in Q1 2026 and **269.5M TRX** in Q2 2026 against near-identical issuance, and the current window sits lower again. The cause is not weaker usage — TRON settled **$2.08T** of stablecoin volume in Q2 2026 on an **$89B** stablecoin float — but a shift in how users pay for it. Staking TRX for energy, or renting energy from someone who has staked it, is now far cheaper than burning TRX for the same resource, and **48.2%** of all TRX is staked. Every user who rents instead of burning removes a burn without removing a block reward.

Buy #1, programmatic buyback, is zero: TRON runs no protocol or treasury repurchase of TRX, and its own Q1 and Q2 2026 reports describe a mint-and-burn model with no repurchase leg. Buy #3, foundation buy, is zero — no foundation or reserve open-market buying was evidenced in the window. Buy #4, new long-term lock, is zero, because TRON staking is a standing mechanism that unwinds in fourteen days and is already counted as float; nothing new was announced with a stated size. The row that looks like it should count, and does not, is the Nasdaq-listed treasury taking delivery of about **$50,000** of TRX per day — **13.7M TRX** across the window, taking its stack to **711.9M TRX** on **Aug 30 2026**. Its own filing describes a single prepaid **$18.0M** stablecoin payment to a related counterparty that then delivers TRX to the treasury wallet each day for 360 days from **Jan 22 2026**. That is a transfer between two holders who both already sit inside circulating supply, not a bid that absorbs float, so the framework leaves it out of the buy ledger and carries the balance as an overhang instead.

## Foundation and overhang

TRON's overhang question is unusually small, because almost every large TRX holder is an exchange holding customer coins, and customer deposits are not a team-controlled overhang. Stripping those and the unidentified addresses out leaves two things worth watching. The first is that same Nasdaq-listed treasury: **711.9M TRX** on **Aug 30 2026**, disclosed in company filings, growing by roughly **150,000 TRX** a day and over **90%** committed to a staking position rather than held liquid — which is why it currently reads as absorption rather than overhang. The second is the TRX leg of the reserve backing TRON's network stablecoin, which is known through the issuer's own disclosure rather than a published address, and which has moved without a vote before. Neither sold TRX inside this window.

If either balance falls between refreshes, the outflow enters Sell #3 at the next refresh. The treasury is checkable against company filings; the reserve is checkable only against the issuer's disclosures, which is the weaker of the two and is carried as such.

## How TRX compares to other fee-burn chains

TRON belongs to the small class of chains that pair a fixed, uncapped block subsidy with a fee burn — the same shape as Ethereum after EIP-1559, and the opposite of Bitcoin, whose supply is capped and whose fees are paid to miners rather than destroyed. What separates TRON inside that class is how well funded its burn is relative to its size. TRON collected **$722M** of fee revenue in Q2 2026, an annualised run rate near **$2.9B** against a market capitalisation of roughly **$31.6B** — close to **9%** of market cap in fees each year, which puts TRON at the top of the field rather than the bottom. Most large layer-1 chains sit in the low single digits on that ratio; TRON is not short of fees.

TRON's problem is the routing, not the revenue. On Ethereum, the base fee is burned whether the payer is a whale or a bot, so revenue and burn move together. On TRON, a user can stake TRX and pay in staked energy instead, and that fee never touches the burn — which is exactly why TRON revenue grew **18%** quarter over quarter in Q2 2026 while the burn fell. Against exchange tokens that run scheduled buy-and-burn programmes, TRON has no discretionary lever at all: no repurchase, no quarterly burn announcement, no committee. TRX is either burned by usage or it is not burned, and the framework reads that as a cleaner mechanism than a discretionary buyback but a slower-moving one.

## What to watch in the next 90 days

The TRON Q3 2026 quarterly report, due around **Oct 2026**, is the single most informative item: it publishes mint, burn and net issuance on the same basis used above, and a third consecutive quarter of falling burn against flat issuance would push the next-90-day reading further above **+0.12%**. A Super Representative vote changing the energy price or the per-block pay rate is the only thing that can move either leg fast — neither has moved since **Aug 29 2025** and **Jun 13 2025** respectively, and proposal 107, which activated on **Aug 28 2026**, only enabled new smart-contract opcodes and touched no fee or reward parameter. Watch the staked share of supply, currently **48.2%**: every point it rises is a point of fee flow diverted away from the burn. Watch whether the Nasdaq treasury's delivery agreement is ever replaced by open-market buying, which would turn it into a real buy row. And watch the TRX leg of the stablecoin reserve, which is the only sizeable identified balance that could turn Sell #3 non-zero.

## Summary

The MrNasdog Pressure Framework reads TRX at **+0.12% net** supply growth over the 90 days to **Sep 1 2026** and projects the same forward, against a supply monitor reading **+0.11%**. The structure is two independent engines: a fixed **136 TRX** per block that mints **352.4M TRX** a quarter regardless of activity, and a usage-driven fee burn that destroyed **237.0M TRX** and is shrinking as users move from burning TRX to staking and renting it. The key risk is that this drift continues quietly — nothing announces it, and each quarter of it widens net issuance while the headline stays under a tenth of a percent. There is no cap and no buyback to catch it: on TRON, the only thing that holds supply flat is people paying fees the expensive way.

---

*MrNasdog Pressure Framework analysis of TRX, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 1 2026.*
