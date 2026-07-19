---
title:         "ZEC Inflation Analysis · July 2026 · Supply growing, projected to keep growing"
description:   "Zcash minted 141.9K ZEC over 90 days at 1.375 per block, with 12% of every subsidy deferred to a lockbox. Framework +0.84% net vs monitor +0.65%."
canonical_url: "https://mrnasdog.com/research/zec/inflation"
tags:          ["crypto", "zec", "zcash", "privacy"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/zec/inflation](https://mrnasdog.com/research/zec/inflation)*

# ZEC Inflation Analysis · July 2026 · Supply growing, projected to keep growing

Zcash mints new ZEC only through mining, and each block actually pays out **1.375 ZEC** — not the headline **1.5625 ZEC** block subsidy, because **12%** of every subsidy is deferred into a development fund lockbox and never issued as coins at all. Over the last 90 days the Zcash chain produced **103,185 blocks** and minted **141.9K ZEC**, against zero buyback and zero fee burn. The MrNasdog Pressure Framework reads **+0.84%** net for the window and **+0.85%** for the next 90 days, against our supply monitor at **+0.65%** — a gap of **0.19 percentage points**, inside tolerance, so no data flag ships.

## The verdict, in one paragraph

For the 90-day window ending Jul 19 2026, the MrNasdog Pressure Framework reads **ZEC at +0.84% net**, with the forward view at **+0.85%**. Every unit of that comes from the Zcash block subsidy; nothing on the buy side offsets it, because Zcash has no buyback contract and no fee burn. Our supply monitor reads the realised last-90-day change at **+0.65%**, so the gap is **0.19 percentage points** — comfortably inside the framework's tolerance, and no monitor-gap flag is warranted. The reconciliation is direct rather than inferred: a block explorer read at both ends of the window shows the chain moved from block **3,314,455** to block **3,417,640**, and the coinbase at both heights pays exactly **137,500,000 zatoshi**, or **1.375 ZEC**. Multiplying observed blocks by observed reward gives the mint directly, with no assumption about block cadence. Zcash is **mildly inflationary on a hard-capped halving schedule**: a fixed subsidy that halves roughly every four years, against a **21 million** ceiling that is already about **80%** mined.

## Sell pressure: where new ZEC comes from

Sell #1, protocol inflation, is **141.9K ZEC** and it is the only non-zero row in the entire ZEC ledger. Zcash is proof-of-work, so mining is the sole mint: no staking rewards, no treasury emission, no bridge issuance. The important detail is the split. The full block subsidy is **1.5625 ZEC**, but under the Zcash development fund rules only **88%** of it is actually paid out as coins — **80%** to miners, which is **129.0K ZEC** over the window, and **8%** to the Zcash Community Grants committee, which is **12.9K ZEC**. Both of those reach the market, so both belong in Sell #1. The remaining **12%** creates no transaction output whatsoever; it is booked by the protocol as a deferred balance in a lockbox. Those coins are not new circulating supply, and counting them as sell pressure would overstate the Zcash mint by roughly a sixth.

Sell #2, vesting unlocks, is **zero** and structurally so. Zcash never ran a token sale with investor vesting; the original Founders' Reward was a block-subsidy carve-out that ran from launch in 2016 until the first halving in **Nov 2020**, at which point it expired permanently. There is no schedule left to unlock. Sell #3, foundation and unscheduled unlocks, is **zero** for the window because nothing was released, though two real overhangs sit behind that zero and are covered below. Sell #4, long-term locked or bankruptcy, is **zero**: Zcash has no bankruptcy estate and no identified long-term locked seller distributing coins into the market.

## Buy pressure: where new ZEC goes

Every buy row on the Zcash ledger is **zero**, and that is the honest reading rather than a gap in coverage. Buy #1, programmatic buyback, is zero because Zcash has no protocol mechanism that acquires ZEC from the market — there is no revenue stream to fund one and no contract that would execute it. Buy #2, protocol fee burn, is zero because Zcash transaction fees are paid to miners rather than destroyed; a fee-burn ZIP has been discussed in the Zcash governance process but has not been adopted, so it changes nothing today.

Buy #3, foundation buy, is zero because the Zcash Community Grants committee is funded straight out of the block subsidy rather than by buying ZEC on an exchange — its funding is a sell-side mint, not a buy-side bid. Buy #4, new long-term lock, is zero, and this row deserves the clarification. It would be tempting to book the **12%** lockbox here, since those coins are demonstrably not going to market. But the lockbox is not supply being taken off the market; it is supply that was never issued in the first place. Booking it as a buy would inflate both sides of the ledger by **19.3K ZEC** while leaving the net identical, and it would misdescribe the mechanism. The lockbox belongs in the overhang discussion, not the buy column.

## Foundation and overhang

Two team-controlled pools are tracked for Zcash. The first is the **Deferred Development Fund Lockbox**, which holds **129,041 ZEC** as of Jul 19 2026 and grows by **0.1875 ZEC** every block — about **216 ZEC** a day, or **19.3K ZEC** per 90-day window. It has never disbursed anything, and the arithmetic proves it: the balance divides by the per-block accrual into **688,220** whole blocks exactly, which could not be true if any partial amount had ever left. Critically, the lockbox is a consensus-level balance with no spending path — releasing it requires a network upgrade that encodes a disbursement, and the proposal to do that, which would send **787,500 ZEC** to a multisig held by the Zcash Foundation, Electric Coin Company and Shielded Labs, remains at proposal status and has not been adopted. Refresh is a governance walk plus the continuous chain read.

The second is the **Zcash Community Grants treasury**, holding about **79,949 ZEC**. Unlike the lockbox, this is already-circulating supply held by an identified entity, funded by the **8%** subsidy leg that is already counted inside Sell #1. Its balance is disbursed to ecosystem projects on the committee's own cadence. For both pools the trigger is the same: if either balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How ZEC compares to other hard-capped proof-of-work chains

Zcash belongs to the Bitcoin structural family: proof-of-work, a fixed **21 million** cap, and a block subsidy that halves on a fixed block-height schedule rather than drifting with usage. Against Bitcoin itself, the differences that matter for inflation are cadence and carve-out. Zcash targets **75-second** blocks against Bitcoin's ten minutes, so it produces roughly eight times as many blocks per day, and its third halving lands at block **4,406,400**, projected for around **Nov 2028**. More importantly, Bitcoin pays **100%** of its subsidy to miners, while Zcash routes **20%** away from them — **8%** to grants and **12%** to the lockbox. That carve-out makes Zcash's effective circulating mint lower than its nominal subsidy, an unusual property for a halving-model chain.

Against uncapped continuous-emission chains, the contrast is sharper. A proof-of-stake L1 that pays validators a percentage-of-stake yield has an emission rate that responds to participation and can be changed by governance parameter, with no terminal ceiling. Zcash's issuance is a step function written into consensus: it cannot be tuned upward, it declines by half on schedule, and it terminates. Against other privacy coins the divergence is structural rather than cosmetic — chains that ship a permanent tail emission accept a small perpetual inflation floor in exchange for a permanent security budget, whereas Zcash accepts the Bitcoin trade-off of a hard cap and an eventual fee-only security model.

Against exchange tokens and fee-burn L1s, Zcash sits at the opposite pole. Those assets generate revenue and route it into quarterly buybacks or a base-fee burn, which can push net supply negative in a busy quarter. Zcash has neither mechanism, so its net supply change is simply its mint. That makes the reading unusually predictable — nothing can surprise the ledger except a governance decision on the lockbox — but it also means the framework will never score ZEC as deflationary while the subsidy is running.

## What to watch in the next 90 days

First, the **Ironwood** network upgrade, with activation height set at block **3,428,143** and targeted for **Jul 28 2026**. It retires the existing shielded pool in favour of a new one and moves funds across a turnstile that verifies the circulating ZEC supply has not been secretly inflated — a supply-integrity event rather than an emission change, so the ledger should not move, but the turnstile output is worth reading as independent confirmation of the mint figure. Second, any coinholder vote that authorises a lockbox disbursement: a grant requires a **420,000 ZEC** quorum and a simple majority, and a successful disbursement would move a large block from overhang into Sell #3 in one step. Third, the status of the one-time disbursement proposal, which would release **787,500 ZEC** and is by far the largest single supply event available to Zcash governance. Fourth, the Zcash Community Grants treasury balance, currently **79,949 ZEC**, which draws down as grants are paid. Fifth, the third halving at block **4,406,400** around **Nov 2028** — far outside this window, but it is the only scheduled event that changes the mint rate itself.

## Summary

The MrNasdog Pressure Framework reads Zcash at **+0.84%** net over the last 90 days and **+0.85%** forward, against a supply monitor at **+0.65%** — a **0.19 percentage point** gap that needs no flag. The structural mechanism is a hard-capped proof-of-work block subsidy of **1.5625 ZEC**, of which only **1.375 ZEC** is actually issued because **12%** is deferred into a lockbox that has never paid out, with no buyback and no fee burn anywhere on the buy side. The key risk is governance rather than emission: the **129,041 ZEC** lockbox is a single coinholder vote away from becoming the largest sell event in Zcash's history, and the framework would reclassify it the moment a disbursement lands. The ceiling is the constraint that bounds everything else — **21 million** ZEC, about **80%** already mined, halving again around **Nov 2028**.

---

*MrNasdog Pressure Framework analysis of ZEC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 19 2026.*
