---
title:         "MON Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description:   "Monad mints 18 MON a block; 134.5M reaches its thin float against a 23.2M fee burn and nothing vests until Nov 24 2026 — framework reads +0.94% next 90 days."
canonical_url: "https://mrnasdog.com/research/monad/inflation"
tags:          ["crypto", "mon", "monad", "layer1"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/monad/inflation](https://mrnasdog.com/research/monad/inflation)*

# MON Inflation Analysis · August 2026 · Supply growing, projected to keep growing

Monad grew its tradable MON float by **+0.97%** over the last 90 days and the Pressure Framework projects **+0.94%** for the next 90. The Monad protocol mints a fixed **18 MON** block reward on every block of its parallel-EVM Layer-1 — **465.2M MON** minted last quarter — but most of that emission accrues to the Monad Foundation's own delegated stake, so only **135.2M MON** reached the **11.8B** float, against a measured base-fee burn of **20.9M MON**. Our monitor reads **−0.07%** for the same window, a **1.03 percentage point** gap, so a ⚠ chip ships. Nothing vests until the **Nov 24 2026** cliff, when roughly **16.6B MON** — more than the entire float — begins unlocking.

## The verdict, in one paragraph

For the 90 days to **Aug 17 2026** the Pressure Framework reads MON at **+0.97%** net supply growth and projects **+0.94%** for the next 90 days. Our monitor reads **−0.07%** for the historical window, a gap of **1.03 percentage points**, which is over tolerance and triggers the ⚠ chip. The disagreement is structural rather than factual. The counted circulating figure for MON tracks Monad's published unlock ledger — its value on **Aug 17 2026** matches the trackers' cumulative unlocked total to the unit — and because no vesting cliff opens before **Nov 24 2026**, that figure reads flat. The Monad chain, meanwhile, never stops minting: the staking contract's balance rises by exactly **18 MON** every block, and MON total supply has already passed its **100B** genesis. The framework books the part of that mint which actually lands with holders outside the Foundation's delegation programme. MON is best labelled a **thin-float, continuous-emission Layer-1** whose near-term dilution is modest and whose real supply event is one quarter away.

## Sell pressure: where new MON comes from

Sell #1, protocol inflation, is the only live sell row in the Monad ledger and it reads **135.2M MON** for the last 90 days and **134.5M MON** for the next. MON is uncapped: the Monad protocol mints a fixed block reward to the validator producing each block and to everyone delegating to it, with no halving and no ceiling. We read that reward directly off the staking contract rather than trusting the published figure — the balance grows by exactly **18 MON** per block, not the **25 MON** the project's own tokenomics post and the staking aggregators still quote. The MIP-12 hard fork activated on Monad mainnet on **Jul 23 2026**, cutting block time from **400ms** to **300ms** and the per-block reward proportionally, so issuance per second barely moved: **465.2M MON** minted over the trailing window and **463.0M MON** projected forward. The gap between that gross mint and the **135.2M** we book is the Monad Foundation's Validator Delegation Program: of the **15.4B MON** staked across **196** validators, roughly **10.9B** sits in fixed Foundation delegation tiers whose rewards flow back into the ecosystem allocation and never become tradable float.

Sell #2, vesting unlocks, is **zero** — and that is the most important zero on this page. Monad locked **50.6%** of supply at its **Nov 24 2025** mainnet launch, and the team, investor and treasury allocations are all still **0%** released. Their one-year cliff opens on **Nov 24 2026**, eight days after this forward window closes. Sell #3, Foundation and unscheduled unlocks, is also **zero**: no discretionary outflow was observed, though the enumerated overhang is enormous. Sell #4 is **zero** and permanent — there is no Monad bankruptcy estate, no trustee and no court-supervised seller.

## Buy pressure: where new MON goes

Buy #2, the protocol fee burn, is the only working counter-flow and it reads **20.9M MON** for the last 90 days and **23.2M MON** forward. Monad burns the base component of every transaction fee, the same shape as an EIP-1559 burn, so every unit of network activity destroys MON permanently. We measured it from blocks sampled evenly across the window rather than assuming it away, and it offsets about a sixth of the emission reaching the float — small against the mint, but real, and rising as Monad's faster blocks carry more transactions.

Buy #1, programmatic buyback, is **zero**. Category Labs disclosed in **Jan 2026** that it might repurchase up to **$30M** of MON on the open market, and widened the authorisation to **$80M** in **Apr 2026**, but the programme is explicitly discretionary, no destination wallet was ever published, and no purchased quantity has ever been confirmed. An authorisation is not a purchase, so the row stays at zero until a disclosure lands. Buy #3, Foundation buy, is **zero** — the Monad Foundation is a distributor of supply, not a buyer of it. Buy #4, new long-term lock, is **zero** because Monad undelegation clears in a single epoch of roughly five and a half hours, which makes staked MON effectively liquid rather than a lock.

## Foundation and overhang

About **88.9B MON** — roughly **88%** of everything that exists — sits outside the tradable float, and it is the defining fact of the Monad supply picture. The largest single overhang is the **38.5B** Ecosystem Development allocation, unlocked at genesis and spent at Monad Foundation discretion with no published schedule; about **10.9B** of it is visibly delegated to validators in fixed programme tiers, which we re-read on each refresh. Behind it sit the **27B** team allocation, the **19.7B** investor allocation and the **3.95B** Category Labs treasury, all cliff-locked to **Nov 24 2026** and all opaque at the wallet level. The **$80M** repurchase authorisation is a fifth watched item with no disclosed address, so anything bought under it is invisible until Category Labs says so. Each of these is watched, not projected: if any of these balances falls between refreshes, that outflow enters Sell #3 at the next refresh.

## How MON compares to other Layer-1 chains

Against a hard-capped, halving-model chain, Monad is the opposite structure. MON has no maximum supply and no scheduled emission decay, so its block reward is a permanent charge on holders rather than a diminishing one; the only brake is the base-fee burn, and that brake is presently about a sixth of the mint. Against Ethereum, the mechanism rhymes but the balance does not — both pay stakers and burn a base fee, yet Ethereum burns against a fully distributed float, while Monad burns against a float that is barely **11.8%** of supply, so the same burn buys far less relief per token outstanding.

The sharper comparison is to other young uncapped Layer-1 chains that launched with a majority of supply locked. There, the emission line is almost never the story; the unlock calendar is. Monad follows that pattern exactly: a **+0.94%** quarterly drift from block rewards is unremarkable, while a single **16.6B MON** cliff on **Nov 24 2026** is larger than the entire circulating supply today. Chains that pair a small float with a big cliff tend to price the cliff long before it lands, which is why the quiet reading on this page should be read as a countdown rather than a verdict.

## What to watch in the next 90 days

First, **Nov 24 2026** — the Monad one-year cliff, when the team, investor and Category Labs treasury allocations begin releasing together, roughly **16.6B MON**. It sits eight days past this window and dominates the next rebuild. Second, the Monad Foundation's Validator Delegation Program: the delegation tiers were already cut once in **Jan 2026** and re-set in **Apr 2026**, and any further reduction changes how much emission reaches the float without any change in the block reward. Third, any confirmation that the **$80M** repurchase authorisation has actually been used — a disclosed amount or wallet would move Buy #1 off zero for the first time. Fourth, a further MIP protocol change to block time or block reward; the **Jul 23 2026** fork kept issuance per second flat, but a future one need not. Fifth, Monad network activity: the fee burn scales directly with usage, and a step change in transactions is the only way the buy side grows on its own.

## Summary

The MrNasdog Pressure Framework reads Monad as mildly and continuously inflationary today: **+0.97%** net supply growth over the last 90 days and **+0.94%** projected for the next, from a fixed **18 MON** block reward whose float-reaching share is **135.2M MON** a quarter against a measured **20.9M MON** base-fee burn. The structural mechanism is an uncapped block reward paid mostly into the Monad Foundation's own delegated stake, which is why the mint looks large on chain and small at the float. The key risk is not the emission but the calendar: **88%** of MON sits outside the float, and the **Nov 24 2026** cliff releases more MON than exists in circulation today. There is no supply ceiling to fall back on — MON has no maximum supply, so the only structural limit on dilution is how much of the fee burn network activity can generate.

---

*MrNasdog Pressure Framework analysis of MON, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 18 2026.*
