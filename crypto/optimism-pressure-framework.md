---
title:         "OP Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "OP supply grows 1.06% over 90 days as Foundation grants release 24.4M tokens while nothing is minted. See the full Pressure Framework ledger and risks."
canonical_url: "https://mrnasdog.com/research/optimism/inflation"
tags:          ["crypto", "op", "optimism", "layer2"]
published:     true
---

Originally published at [OP Inflation Analysis · September 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/optimism/inflation).

# OP Inflation Analysis · September 2026 · Supply growing · projected to keep growing

Supply is growing and is projected to keep growing. Optimism mints no new OP, but the Optimism Foundation's grant wallets released **24.39M OP** into circulation over the last 90 days, while the buyback bought nothing and burns removed less than one OP. The Pressure Framework reads OP at **+1.06%** for the trailing 90 days and **+1.47%** for the next 90, against a monitor reading of **+6.55%**. The OP token contract can still mint up to 2% a year, but the Collective's policy keeps that at 0%.

## The verdict, in one paragraph

On a circulating base of **2,299.6M OP**, the framework books **24.39M OP** of sell pressure and effectively **0** of buy pressure over the trailing 90 days, a net of **+1.06%**, and projects **+1.47%** for the next 90 days. The inflation monitor reads **+6.55%** for the same window, a gap of **5.49 percentage points**, which is above the framework's 0.5-point tolerance, so the OP overview carries a monitor-gap warning. The gap has one clear cause. On **Jul 16 2026** the Optimism Foundation's own circulating count jumped by about **122M OP** when it caught up on investor and early-team slices that had already unlocked between February and **May 31 2026**, before this window opened. That late recount alone is **5.51 points**. OP is best described as a non-minting governance token whose float now grows mainly through Foundation grant spending.

## Sell pressure: where new OP comes from

Sell #1, protocol inflation, is **0**. The OP token on OP Mainnet held **4,294.96M OP** at both ends of the window, and the figure actually fell by a quarter of a coin through small burns, so the supply field is live and no mint happened. The OP token is owned by a MintManager contract that allows one mint of up to **2%** of supply every 365 days, which is about **85.9M OP** today. That clock was started by a zero-sized mint on **Oct 28 2025**, so a real mint becomes possible again after **Oct 28 2026**, inside the forecast window. The Optimism Collective has kept inflation at 0% since launch and no proposal to change it exists, so the row stays at 0 and is watched.

Sell #2, vesting unlocks, is **0** for the window. The four-year investor lock and the original early-team lock both paid their last monthly slices on **May 31 2026**. The Foundation's tracker now shows investors at **735.9M OP**, 100% of their allocation, and early core contributors at **686.9M OP**, unchanged between Aug 6 and Sep 4 2026. A smaller team tail remains: the Foundation's Year 5 outlook expects about **35.2M OP** more from early contributors by Apr 30 2027, which the framework spreads to about **9.5M OP** for the next 90 days. Several unlock calendars still show a monthly slice of about 31M OP; the Foundation's own figures show that schedule has ended.

Sell #3, Foundation and unscheduled unlocks, is the whole story at **24.39M OP**. The Optimism Foundation pays grants from the Governance Fund and the Ecosystem Fund through a small set of wallets. Their combined balance fell from **1,790.9M OP** to **1,766.5M OP** across the window, and every coin of that drop left through outgoing grant payments, mostly monthly batches from one payout wallet. On Aug 7 2026 the budget safe moved **142M OP** into a new Year 5 safe; both are Foundation wallets outside the circulating count, so that move added nothing. As a cross-check, the Foundation's own count added **11.63M OP** of grants between Aug 6 and Sep 4 2026, while the wallets paid out **10.79M OP** over the same days. Sell #4, long-term locked or bankruptcy, is **0**: OP has no bankruptcy estate and no court-ordered release.

## Buy pressure: where new OP goes

Buy #1, programmatic buyback, is **0**. Optimism governance approved a buyback in January 2026 that directs half of Superchain revenue into monthly OP purchases. It bought **9.45M OP** in total, and the last batch landed on **May 1 2026**. Nothing was bought in this window. Base, which had produced almost all of the revenue, announced in February 2026 that it would leave the Superchain, and Collective revenue now runs at roughly 20 ETH a month. The bought OP sits unspent in a single wallet and is still counted as circulating, so even when the buyback runs it moves OP within the float rather than removing it.

Buy #2, protocol fee burn, is effectively **0**. OP has no fee burn. Both burn surfaces were read at both window ends: the supply count fell by **0.25 OP** and the dead address gained **0.01 OP**. Buy #3, Foundation buy, is **0**: no OP flowed back into the Foundation wallets from outside, and the Foundation made no market purchase. Buy #4, new long-term lock, is **0**, because OP has no staking and no new lockup launched.

## Foundation and overhang

The overhang on OP is large and almost all of it belongs to the Optimism Foundation. The main treasury safe holds **1,294.0M OP** and did not move once in the window; it is roughly the size of the unspent airdrop and Retro Funding reserves. The budget safe holds **318.5M OP**, the new Year 5 safe **131.4M OP**, and an older grants safe **21.4M OP**. In August 2026 governance approved moving the **546.9M OP** of unspent airdrop tokens into a new Strategic Ecosystem Fund for OP Mainnet and OP Enterprise deals. That vote released nothing by itself, but it gives a large idle pool a spending mandate. About **123.4M OP** of early-contributor tokens are still unvested and held in custody locks that cannot be read on chain. The buyback wallet, at **9.45M OP**, is tracked too. All of these balances are refreshed at every rebuild, and if any Foundation wallet falls by more than its grant payouts explain, that outflow enters Sell #3 at the next refresh.

## How OP compares to other L2 governance tokens

OP belongs to the class of layer-2 governance tokens that launched with a fixed genesis supply and a large foundation treasury. Compared with a proof-of-work coin such as Bitcoin, OP has no block reward at all: its supply count has not grown since 2022. The mint switch exists, but it is a governance choice, capped at 2% a year and never used. On the pure issuance axis, OP is stricter than proof-of-stake chains that pay stakers with new coins every epoch.

What moves OP is spending, not minting. With the investor and early-team vests finished, the float now grows through Foundation grants, partner deals and the remaining team tail. That puts OP closer to a treasury-funded token than to a vesting-driven one: the pace depends on budget decisions, and the Foundation's Year 5 plan points to about **210M OP** from the Governance and Ecosystem funds over twelve months, about twice the pace seen on chain this quarter.

Compared with exchange tokens that burn a share of revenue, OP's buyback holds rather than burns, and its revenue base shrank sharply after Base left. For the buy side to matter, the buyback would need to take in several million OP a month and park it outside circulation, and neither is happening today.

## What to watch in the next 90 days

First, **Oct 28 2026**: after this date the MintManager allows a mint of up to **85.9M OP**; any governance proposal to use it would move Sell #1 from 0. Second, the payout wallet and the new Year 5 safe, now at **131.4M OP**: a faster grant pace would lift Sell #3 above its current **24.39M OP** per 90 days. Third, the new Strategic Ecosystem Fund of **546.9M OP**: its first deals will show how fast it spends. Fourth, the buyback thread: a restart would add OP to a wallet that stays in circulation. Fifth, the early-team tail of about **9.5M OP**, which should show up in the Foundation's weekly tracker.

## Summary

The MrNasdog Pressure Framework reads OP at **+1.06%** over the trailing 90 days and **+1.47%** projected forward: supply growing, projected to keep growing. Optimism mints nothing and burns almost nothing; the float grows because the Optimism Foundation pays out grants, **24.39M OP** this window, with a small early-team tail still to come. The key risk is the Foundation's treasury of more than **1,700M OP** and the 2% mint that becomes possible again after **Oct 28 2026**. The fixed supply of **4,294.96M OP** holds only as long as governance keeps inflation at 0%.

MrNasdog Pressure Framework analysis of OP, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.
