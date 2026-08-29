---
title:         "LDO Inflation Analysis · August 2026 · Supply shrinking, projected to keep shrinking"
description:   "LDO mints nothing and burns nothing: supply held at exactly 1B all window while a DAO treasury buyback pulled 14.84M LDO off the market. Framework −1.79%, monitor −1.77%."
canonical_url: "https://mrnasdog.com/research/ldo/inflation"
tags:          ["crypto", "ldo", "lido", "defi"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/ldo/inflation](https://mrnasdog.com/research/ldo/inflation)*

# LDO Inflation Analysis · August 2026 · Supply shrinking · projected to keep shrinking

Lido DAO's governance token LDO has the rarest sell ledger in the framework: all four sell rows read **0**, and that is a measurement rather than a claim. The LDO supply was read on-chain at both ends of the quarter and at two much older heights and returned exactly **1B** every time; the Lido vesting contract holds nothing; and the Lido DAO treasury sent out **zero** LDO across the whole window. Against that empty sell side, a token-holder-approved buyback moved **~14.84M LDO** into the DAO treasury in four dated transfers, plus **~0.06M** more from two smaller inflows. Net supply change is **−1.79%** over 90 days against **−1.77%** on the inflation monitor — a gap of **0.02** percentage points. The constraint is that the buyback budget is finite: about **7,680** staked ETH of the approved **10,000** is still unspent, and nothing continues past it without a new vote.

## The verdict, in one paragraph

The framework reads Lido DAO at **−1.79%** net supply change over the trailing 90 days and **−1.33%** for the next 90. The inflation monitor reads **−1.77%** over the same window, a gap of **0.02** percentage points — comfortably inside tolerance, so no data-conflict chip is raised on the LDO overview. The two readings are unusually independent for a match this tight: the framework counts LDO arriving at the Lido DAO treasury address, while the monitor counts LDO leaving the classified float, and the treasury absorbed **14,900,633** LDO while the float fell by **14,993,777** — the same event read from opposite ends. On mechanism, LDO is a **fixed-supply governance token that is deflationary purely by treasury buyback**: no issuance, no burn, no unlock calendar, and a float that only moves when Lido DAO votes to move it.

## Sell pressure: where new LDO comes from

It does not come from anywhere, and this is the load-bearing fact about LDO. Sell #1, protocol inflation, is **0**: LDO is an Aragon MiniMe token whose supply has stood at exactly one billion since the 2020 genesis, confirmed on-chain at four separate heights this session. New LDO would require a token-holder vote through the Aragon Token Manager, and none has been proposed. Sell #2, vesting unlocks, is **0** because the original allocation ran a one-year lock followed by a year of linear vesting and released its last tranche on **Dec 16 2022**; the Lido vesting contract was read this session and holds no LDO at all, which is a stronger proof than a published calendar. Sell #3, Foundation and unscheduled unlocks, is **0** as a measured result, not an assumption: every LDO transfer touching the Lido DAO Aragon Agent across the window was pulled from the chain, and there were **six** inbound transfers and **zero** outbound ones. Sell #4 is **0** because no bankruptcy estate, trustee or court-ordered distribution is attached to LDO.

## Buy pressure: where new LDO goes

Buy #1, the programmatic buyback, carries the entire page at **~14.84M LDO**. Lido DAO token holders approved spending up to **10,000** staked ETH of treasury reserves on open-market LDO, released in batches that a growth committee executes under a published price cap and that holders can veto before each batch settles. Four transfers landed inside this window — **4.50M** on **Jun 1 2026**, **1.72M** on **Jun 11 2026**, **6.47M** on **Jul 8 2026** and **2.15M** on **Aug 25 2026** — and the committee's own published batch figures match the chain to the unit. The destination matters more than the size: bought LDO is **not burned**, it goes to the Lido DAO treasury, which sits outside the counted float, so it leaves the market without leaving existence. Buy #2, protocol fee burn, is **0**, verified on both surfaces — the unspendable address held the same **5.2** LDO throughout and the headline supply never moved. Buy #3 is **0**: there is no separate foundation bid beside the DAO. Buy #4 is **0** because LDO still has no staking product, vote-lock or lockup contract. A fifth row tracks Lido's new automatic buyback, activated by on-chain vote on **Aug 14 2026**, which routes surplus staking revenue into LDO and sends it straight to the treasury — it has bought **0** so far, because revenue has not cleared its trigger level once since launch. A sixth row carries **~0.06M** of treasury re-absorption from two smaller non-programme inflows.

## Foundation and overhang

The dominant Lido DAO overhang is the Aragon Agent treasury itself, which held **~116.9M LDO** at the window close, up from **~102.0M** at the open — and the buyback is making it bigger every batch. That is the honest tension in this reading: the same mechanism that shrinks the float grows the largest single pile of LDO under one governance key. Nine early-allocation safes are enumerated alongside it and every one held an identical balance at both ends of the window — two at **50M**, plus **45.8M**, **45M**, **31.1M**, **10M** and three at **5M**, some **246.9M** in total, none of it under any remaining lock. The wallet that executes the buyback is tracked too: it ended the window holding no LDO and **682** staked ETH of undeployed budget. Exchange custodial wallets are excluded from this list because they belong to depositors, not to Lido DAO. Every one of these balances is refreshed by chain read on each rebuild, and the rule is simple: if any of them falls between refreshes, that outflow enters Sell #3 at the next refresh.

## How LDO compares to other DAO-governance tokens

Against uncapped proof-of-stake layer-1s, LDO is a different animal entirely. A staking chain issues new units every epoch whether anyone wants them or not, so its buy side has to run just to stand still; LDO has no issuance to outrun, which is why an empty sell ledger and one modest buyback produce a deflationary read that most large-cap chains cannot reach at any burn rate.

Against exchange tokens with quarterly buy-and-burn programmes, the mechanism difference is destination, not size. Those programmes send bought tokens to an unspendable address, so the reduction is permanent and visible in total supply. Lido DAO sends bought LDO to its own treasury, so the reduction is real for the float but reversible by a future vote — the tokens still exist and still belong to the DAO. The framework counts it as buy pressure because the float is what the market prices, but it is a weaker form of removal than a burn, and the overview says so.

Against governance tokens with live fee-sharing, LDO is still the version without a demand sink attached. Lido's new automatic buyback is designed to be that sink — a fee-linked bid that runs without a vote each time — but it has not fired yet. Until it does, LDO's deflation is discretionary spending from a finite pot rather than a structural claim on protocol revenue, and those two things deserve very different confidence levels.

## What to watch in the next 90 days

The dated item is the buyback's Batch 3 residual: **680** staked ETH remain from that batch under a published execution window closing **Sep 29 2026**, worth roughly **4.5M LDO** at the last realised rate, and unspent residual returns to the Lido DAO treasury rather than rolling forward. Second, watch the price cap itself — the committee moved it from 0.000163 down to 0.000151 and back to 0.000153 across this window, and Batch 3 only filled **320** of its **1,000** staked ETH because of it, which is exactly why the forward column is projected below the trailing figure. Third, watch whether Lido's automatic buyback fires at all: it needs surplus staking revenue above its trigger level, and revenue has been under it since activation on **Aug 14 2026**. Fourth, a holder push to raise the cap and to roll unspent batch budgets forward was live on the Lido governance forum through late **Aug 2026**; if it reaches a vote and passes, the forward buyback figure rises. Fifth, watch the treasury address for any first outbound LDO transfer — there were none this quarter, and one would flip Sell #3 off zero immediately.

## Summary

Lido DAO's LDO is a fixed-supply governance token with a genuinely empty sell ledger — no issuance, no unlocks since **Dec 2022**, and not one LDO leaving the DAO treasury across the quarter — set against **~14.9M** of buy-side absorption, for a net reading of **−1.79%** that the inflation monitor independently confirms at **−1.77%**. The structural mechanism is a token-holder-approved treasury buyback that removes LDO from the float without burning it, which makes the deflation real but reversible by a future Lido DAO vote. The key risk is that the mechanism is a budget rather than a pipe: about **7,680** of **10,000** approved staked ETH remain, the committee's price cap has already slowed execution to a third of a batch, and Lido's fee-linked automatic buyback — the thing that would make this structural — has yet to buy a single token. The ceiling is hard and known: supply cannot exceed **1B** without a vote, and it has not moved in six years.

---

*MrNasdog Pressure Framework analysis of LDO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 30 2026.*
