---
title:         "ALGO Inflation Analysis · August 2026 · Capped, fully minted — and the reserve tap just opened wider"
description:   "Algorand mints nothing under its 10B hard cap, yet 106.7M ALGO per 90 days reaches the market from a block bonus and a sharply accelerating Foundation reserve. Framework +1.18% net measured and forward; monitor +1.30%."
canonical_url: "https://mrnasdog.com/research/algo/inflation"
tags:          ["crypto", "algo", "algorand", "layer1"]
published:     true
---

> Originally published at **[mrnasdog.com/research/algo/inflation](https://mrnasdog.com/research/algo/inflation)** by MrNasdog.

# ALGO Inflation Analysis · August 2026 · Capped, fully minted — and the reserve tap just opened wider

Algorand is hard-capped at **10 billion ALGO**, all of it minted at the 2019 genesis, and the protocol has no mint function at all — yet the tradable float still grew **+1.18%** over the last 90 days. Every unit of that growth is already-minted ALGO leaving Algorand Foundation custody through two taps: a block-production bonus worth **19.1M ALGO** to non-Foundation validators, and **87.6M ALGO** of discretionary Foundation reserve deployment. Nothing offsets it — no buyback, no burn, and liquid staking that locks nothing away — so the framework reads **+1.18%** against a supply monitor at **+1.30%**, a gap of just **0.12 percentage points**.

## The verdict, in one paragraph

Over the 90 days to **Aug 11 2026**, the Pressure Framework books **106.7M ALGO** of sell pressure and **zero** buy pressure against a circulating base of **9.02B ALGO** — a net of **+1.18%**. The independent supply monitor reads **+1.30%** for the same window, a gap of **0.12 percentage points**, comfortably inside the framework's 0.5-point tolerance, so no data-conflict flag is raised. Both readings describe the same thing from opposite ends: the monitor watches the float rise, the framework watches the Foundation reserve fall. The forward reading is essentially identical at **+1.18%**. The cite-able label for Algorand is **a hard-capped chain that is still structurally inflationary on the active float** — the cap constrains the total, not the release, and the release is one entity's decision.

## Sell pressure: where new ALGO comes from

Nothing on Algorand is newly minted. The **10 billion** ALGO cap was fully issued at genesis, and the mainnet ledger confirms it — the participating-supply figure reads **9.76B ALGO**, the remainder sitting in the protocol's fee sink and rewards pool. What the market experiences as Algorand inflation is redistribution, not issuance.

**Sell #1, protocol inflation, is 19.1M ALGO.** Algorand's consensus incentive is a block-production bonus: every block header carries a bonus field, paid from the fee sink to whichever validator proposed that block. That bonus is **8.429426 ALGO** per block at the head of the chain, having stepped down from **8.600578** and then **8.514572** earlier in the window. The decay is protocol-encoded and exact — one percent at every millionth round, applied as integer arithmetic — which puts the gross bonus at **24.1M ALGO** across the window. That gross figure is not the number the market feels. Roughly a fifth of every block bonus is earned by Foundation-operated validators and lands straight back in Foundation wallets, so the market-reaching share was measured rather than assumed: an exhaustive walk of **1,038,475** fee-sink payments over the last six weeks put it at **79.448%**. That gives **19.1M ALGO** of real sell pressure for the last 90 days and **18.6M** projected for the next 90 as the bonus decays through three more steps — and a second, independent angle against the prior quarter's published reward outflow lands within **1.1%** of it.

**Sell #2, vesting unlocks, is zero.** Every genesis allocation — public sale, node-running grants, early backers, team and investors — finished vesting by 2024, and the early-backer accelerated vesting programme physically exhausted its pool back in October 2021. There is no unlock calendar left to draw against, which is why this row is marked permanent rather than merely checked.

**Sell #3, Foundation and unscheduled unlocks, is 87.6M ALGO — and it is the whole story.** The Foundation publishes its own custody wallet list, and across those 74 addresses it held **945.7M ALGO** on **Aug 11 2026**, down from a reported **1,035.6M** at the end of June.

The window splits into two segments measured on different evidence. The first, from mid-May to **Jun 30 2026**, is taken from the Foundation's own quarterly reconciliation, which books **43.3M ALGO** of total release for the second quarter of 2026 — **10.6M** of structured and OTC selling, **20.1M** of staking rewards, and the balance in ecosystem support, xGov, grants, investments, business development, communities, marketing, R&D and operations. Stripping out the reward line and pro-rating the rest across the 48 days inside the window gives **12.2M ALGO**.

The second segment, **Jul 1 2026** to **Aug 11 2026**, was measured on-chain instead of projected — and it is materially hotter. **83.9M ALGO** left the published wallet set across those 42 days with **nothing** flowing back. Netting out the fee-sink bonus already booked in Sell #1 leaves **75.4M ALGO** of fresh reserve deployment, for a total of **87.6M**. Inside that walk: a **30M** transfer on **Jul 18 2026** into a wallet created three days earlier and absent from the custody list, which has since passed **25M** onward and still holds **5M**; two **10M** top-ups of the structured-selling wallet on **Jul 18 2026** and **Aug 5 2026**; and **27M** pushed onward from that wallet to an exchange-style deposit address in six tranches.

That is the headline of this rebuild. Structured selling ran at **24M** in the first quarter of 2026 and **10.6M** in the second; the six weeks to **Aug 11 2026** alone moved **83.9M** out of custody. The **3.8×** step-up was triple-confirmed before it was booked: by the payment walk itself, by the published wallet list's balance falling **1,035.6M → 945.7M**, and by the derived supply series rising **+86.7M** over the same 42 days. Three independent angles, one answer. This is a genuinely variable tap that has to be re-derived every cycle rather than carried forward on faith.

**Sell #4, long-term locked or bankruptcy, is zero.** No bankruptcy estate holds ALGO and there is no trustee distribution schedule pointed at the asset, so there is no forced-seller overhang of the kind that dominates some other large-cap ledgers.

## Buy pressure: where new ALGO goes

The Algorand buy ledger is empty on all four rows, and that is the single most important structural fact about ALGO.

**Buy #1, programmatic buyback, is zero** — there is no buyback programme of any kind, and the Foundation's dedicated market-operations wallets are configured for selling, not buying.

**Buy #2, protocol fee burn, is zero**, and this is the detail most often misread. Algorand fees are not destroyed. Half of every block's collected fees is paid immediately to the block proposer, and the remainder settles into the fee sink — the very same pool the block bonus is paid out of. The sink held **13.1M ALGO** at the head of the chain and functions as a recycling account, not a burn address. Network activity does not retire supply here.

**Buy #3, Foundation buy, is zero.** There is no evidence of Foundation purchases in the window; every flow observed across its published wallets ran outward. **Buy #4, new long-term lock, is also zero**, because Algorand staking is liquid by design — no lock-up, no unbonding period, no slashing. Over **2.02B ALGO** participates in consensus, but every unit of it remains sellable within a single block, so staking removes nothing from the tradable float. A chain whose staking genuinely locked that much supply would read very differently in this framework; Algorand's does not.

## Foundation and overhang

The Foundation is the only team-controlled overhang that matters here, and it is unusually well documented. Its published treasury wallets held **931.5M ALGO** at the head of the chain, with a further **13.1M** in the fee sink that funds the block bonus, **1.0M** staged in the market-operations wallets used for structured selling, and negligible residue in the legacy governance and community reward pools — **945.7M ALGO** in total, or roughly one tenth of the entire cap, with no published release schedule attached to any of it. A fourth overhang sits just outside that list: the wallet created on **Jul 15 2026** that still holds **5M ALGO** and is not captured by the Foundation's own balance reporting at all.

The custody is verifiable on-chain at any time and the reconciliation is published each quarter, so the tracking is real rather than nominal. If the balance across those wallets falls between refreshes, the outflow enters Sell #3 at the next refresh — which is exactly what happened this cycle, and exactly why the reading came in hotter than the prior quarter's published rate would have suggested.

## How ALGO compares to other hard-capped chains

Algorand belongs to the small class of chains with a genuine, protocol-enforced hard cap — the same structural family as Bitcoin — but it arrives there by the opposite route. Bitcoin's 21 million cap is approached asymptotically through a halving subsidy, so its float rises only as miners are paid newly created coins. Algorand's 10 billion were all created at once in 2019, so the cap has already been reached and the protocol will never mint again. The consequence is counter-intuitive: a chain with zero issuance can still be more inflationary on the active float than a chain that mints every block, because releasing a pre-minted reserve is a governance decision rather than an emission schedule.

Against uncapped continuous-emission Layer 1s — the staking-mint chains, or fan-token chains running a decaying per-block mint — Algorand looks structurally superior on the sell side and materially worse on the buy side. Those chains dilute holders mechanically, but many pair the mint with a fee burn or a revenue-funded buyback that gives supply a genuine sink. Algorand has neither: no burn, no buyback, and fees recycled straight back to producers. The result is a one-way ledger where the only variable is how quickly the Foundation chooses to spend down its reserve.

The closest structural analogues are therefore not other Layer 1s at all but foundation-led ecosystems whose supply is dominated by treasury release rather than protocol issuance. For those assets, and for ALGO, the number that matters is not the emission curve but the transparency report — and Algorand deserves credit for publishing one detailed enough to reconcile against on-chain wallet balances line by line.

## What to watch in the next 90 days

First, the block bonus steps down one percent at each millionth round, and three of those steps fall inside the window: to **8.345131 ALGO** per block around **Aug 12 2026**, to **8.261679** around **Sep 13 2026**, and to **8.179062** around **Oct 15 2026**. That trims Sell #1 from **19.1M** to **18.6M** — real, but small next to the reserve.

Second, the Q3 2026 transparency report, due after the quarter closes, will confirm or contradict the sharply elevated July and August release measured on-chain here. It is the single most important scheduled disclosure for this ledger. Third, the monthly ecosystem supply posts run on a much shorter cycle and will show whether the structured-selling wallet keeps drawing down after its **Aug 5 2026** top-up.

Fourth, the Foundation's rework of Algorand's fee and incentive economics is now circulating with its advisory council, and the Foundation has committed to funding the bonus for a further year to **January 2028**; any change it proposes to fee handling or reward funding would be the first thing in years capable of putting a number on the buy side of this ledger. Fifth, watch the unlisted wallet created on **Jul 15 2026**, and whether it is ever added to the published custody list.

## Summary

Algorand is hard-capped at **10 billion ALGO**, fully minted at genesis and incapable of minting again, and it is still structurally inflationary on the float at roughly **+1.18%** per 90 days. The mechanism is not issuance but release: a decaying block-production bonus contributes **19.1M ALGO** and discretionary Foundation reserve deployment contributes **87.6M ALGO**, against a buy ledger that is empty on every row because there is no buyback, no burn and no staking lock-up. The framework's **+1.18%** sits **0.12 percentage points** below the supply monitor's **+1.30%**, well inside tolerance.

The key risk is that the reserve tap is discretionary and demonstrably variable — structured selling ran at **24M** in the first quarter of 2026, **10.6M** in the second, and visibly faster again through July and August, with **83.9M** leaving custody in six weeks. The ceiling, and the genuine consolation, is that the overhang is finite and shrinking: **945.7M ALGO** remain in published Foundation custody, and when that reserve is spent, a coin with no mint function has nothing left to inflate with.

---

*MrNasdog Pressure Framework analysis of Algorand (ALGO), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 11 2026.*
