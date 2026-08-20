---
title:         "ETC Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description:   "Ethereum Classic mined 1.11M ETC in 90 days with no buyback and no burn. Framework net +0.70%, monitor +0.78%, gap 0.08pp. The 20% reward cut fired Jul 22 2026."
canonical_url: "https://mrnasdog.com/research/etc/inflation"
tags:          ["crypto", "etc", "ethereumclassic", "mining"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/etc/inflation](https://mrnasdog.com/research/etc/inflation)*

# ETC Inflation Analysis · August 2026 · Supply growing · projected to keep growing

Ethereum Classic is a pure proof-of-work chain whose entire supply story is one number: the block reward. Over the last 90 days the Ethereum Classic chain issued **1.11M ETC** from **574,370** blocks, against a buy ledger that is empty in all four rows — no buyback, no burn, no foundation bid, no lock. That is **+0.70%** of circulating supply reaching the market, against **+0.78%** on the inflation monitor, a gap of **0.08** percentage points. The important event already happened: on **Jul 22 2026** the ECIP-1017 schedule cut the ETC block reward 20% to **1.6384** ETC, so the forward read drops to **+0.60%** even though nothing else about Ethereum Classic changed.

## The verdict, in one paragraph

The framework reads Ethereum Classic at **+0.70%** net supply growth over the trailing 90 days and **+0.60%** for the next 90. The inflation monitor reads **+0.78%** over the same window, leaving a gap of **0.08** percentage points — inside tolerance, so no data-conflict chip is raised on the ETC overview. That agreement is worth less than it looks, because both sides are trying to measure the same single thing and only one of them counts coinbase output directly; the classified supply feed spent **59** days of this window frozen on one value before catching up in a single step on **Jul 17 2026**. On mechanism, ETC is a **capped, halving-model proof-of-work chain with a permanently empty buy side**: the reward schedule is the only lever, and it only ever moves one way.

## Sell pressure: where new ETC comes from

Sell #1, protocol inflation, is the whole ledger. The Ethereum Classic chain produced **574,370** blocks between the two window edges, and three separate details decide what that is worth. First, the pace: the measured interval was **13.54** seconds a block, not the **13** seconds the schedule targets — reading the target instead of the chain would have over-claimed issuance by about **4%**. Second, the reward itself changed mid-window: ECIP-1017 cuts the ETC block reward 20% every five million blocks, and block **25,000,000** was mined on **Jul 22 2026**, taking the subsidy from **2.048** to **1.6384** ETC. The trailing quarter is therefore a blend of a retired reward and the live one, which is why the framework projects forward from the post-cut rate rather than the trailing average.

Third, uncles. Ethereum Classic still pays ommer rewards: under ECIP-1017 the miner of an uncle block receives **1/32** of the era reward and the miner who includes it receives another **1/32**, so every uncle quietly adds a sixteenth of a block reward to supply. Rather than sample, this build counted every uncle in every one of the **574,370** blocks: **24,234** uncles, a rate of **4.22%**, worth **2,902** ETC or **0.26%** on top of the base subsidy. Base and uncle together give the **1.11M ETC** the overview shows, and the same arithmetic run from genesis reproduces the chain's own supply counter to within the uncle payments it has made across ten years.

The other three sell rows are zero, each for a different structural reason. Sell #2, vesting unlocks, is zero because Ethereum Classic has no vesting schedule and no lock contract at all — it inherited its ledger from Ethereum at the **2016** split, by which point the original public sale had fully released, so there is no ETC team tranche or investor cliff in existence. Sell #3, foundation and unscheduled unlocks, is zero because no foundation reserve, protocol treasury or DAO allocation holds ETC; the full block reward goes to the miner and the supporting non-profit is donation-funded, with no published wallet and no protocol share. Sell #4, long-term locked or bankruptcy, is zero because there is no bankruptcy estate: a listed US trust holds **10,850,163** ETC as of **Jun 30 2026**, shrinking only by its in-kind sponsor fee, with no creations, no redemptions and no redemption program — coins already inside circulating supply that cannot become new supply.

## Buy pressure: where new ETC goes

Nowhere, and on Ethereum Classic that is measured rather than assumed. Buy #2, protocol fee burn, is the row people expect to be non-zero because Ethereum burns its base fee — Ethereum Classic does not have one. Block headers read at the window open, at the reward cut and at the head all come back with no base-fee field whatsoever: the fee market was deliberately excluded from the 2022 upgrade and was not added in 2024, so **100%** of gas paid on Ethereum Classic goes to the miner. The two null addresses on the chain took in **1.1** ETC in total across the entire quarter, in two dust transfers on **Aug 5 2026**, and even that ether is still counted in supply because the chain's supply counter is genesis plus rewards. There is no burn to find.

Buy #1, programmatic buyback, is zero because Ethereum Classic collects no protocol revenue and holds no treasury — there is nothing to buy with. Buy #3, foundation buy, is zero for the same reason one step further out: no endowment, no DAO balance sheet, no announced corporate reserve programme for this coin. Buy #4, new long-term lock, is zero because proof-of-work offers no staking, no bonding and no lockup, so a holder has no protocol-level way to remove ETC from the tradable float. The practical consequence is that the framework's ETC reading can never turn negative while the reward is still paying. Its floor is the halving schedule.

## Foundation and overhang

Ethereum Classic has no team-controlled overhang to enumerate, which is unusual enough to state plainly. There is no premine reserve, no foundation multisig, no DAO treasury and no buyback accumulation wallet; circulating supply sits just **466** ETC below the chain's total supply, which is what a chain with no non-circulating bucket looks like. The twenty largest ETC balances on chain are exchange-shaped — deposit wallets and labelled custodial addresses — which the framework excludes by definition, since those coins belong to depositors rather than to a coordinated group.

Two things are watched rather than counted. The first is the proposed fee-market upgrade, which would introduce a base fee on Ethereum Classic but route it into a new on-chain treasury instead of destroying it — that would create a future Sell #3, not a Buy #2, and it remains a draft with no activation block named. The second is the listed US trust holding **10.85M** ETC, recorded here for completeness and excluded from the overhang enumeration because it is a fund holding on behalf of shareholders with no redemption path. If either balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How ETC compares to other halving-model proof-of-work chains

Ethereum Classic belongs to the same structural family as Bitcoin, Bitcoin Cash and Dash: a hard ceiling, a scheduled reward reduction, and no mechanism that removes supply. Where it differs is the shape of the schedule. Bitcoin halves — a 50% cut every four years — so its issuance falls in violent steps and then sits flat for a long time. Ethereum Classic cuts **20%** every five million blocks, roughly every two years, which produces a gentler and far more frequent glide path toward its stated ceiling of **~210.7M** ETC. Around **75%** of that ceiling is already issued, so the remaining supply arrives slowly and predictably rather than in cliffs.

The comparison that matters most is with Ethereum itself, because the two chains share an ancestor and almost nothing else. Ethereum moved to proof-of-stake and burns its base fee, so its net supply swings with network activity and can turn negative. Ethereum Classic kept proof-of-work, kept the miner as the sole recipient of every unit of gas, and never adopted the burn — which is exactly why its reading is a small positive number every single quarter rather than a variable one. Against uncapped continuous-emission chains the contrast runs the other way: those set a target inflation rate that governance can revisit, whereas Ethereum Classic's issuance is fixed in code and its next change is already dated. Ethereum Classic also still pays uncle rewards, a mechanism Ethereum retired at the merge, and that is the one part of ETC issuance that is not fully deterministic — it moves with how contested block production is.

## What to watch in the next 90 days

There is no scheduled protocol event inside the forward window, which closes around **Nov 18 2026** — the next ECIP-1017 reduction sits at block **30,000,000**, roughly **756** days out at the current pace and due around **Sep 2028**, when the reward falls to 1.31072 ETC. Watch the block interval instead: it is the only free variable in this ledger, and a sustained shift in Ethereum Classic hashrate moves the forward figure directly. Watch the uncle rate for the same reason, since at **4.22%** it adds a quarter of a percent to issuance and rises when block production gets contested. Watch the fee-market proposal for an activation block, because the moment a base fee exists the buy ledger stops being empty by design — though as drafted it would fund a treasury rather than burn. And watch the listed trust's next quarterly disclosure for any change to its no-redemption stance.

## Summary

Ethereum Classic runs the simplest supply mechanism in the framework and the emptiest buy side: **1.11M ETC** mined over the trailing 90 days, nothing bought back, nothing burned, nothing locked, for a net **+0.70%** that eases to **+0.60%** now the reward cut of **Jul 22 2026** covers the whole forward quarter. The structural mechanism is ECIP-1017's 20%-every-five-million-blocks reduction, which makes ETC issuance both fixed and knowably falling against a ceiling of **~210.7M** ETC. The key risk is not a supply shock but the absence of any offset: with no burn and no buyback, Ethereum Classic can never post a negative quarter, so its best possible reading is a small positive number that only the schedule can shrink. The next time it shrinks is block **30,000,000**, around **Sep 2028**.

---

*MrNasdog Pressure Framework analysis of ETC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 20 2026.*
