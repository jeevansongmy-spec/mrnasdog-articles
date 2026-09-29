---
title: "FLR Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description: "FLR supply is growing: 640.5M FLR of staking rewards and 295.7M of vested rFLR against 34.9M burned or parked gives +1.04% in 90 days, about the same next."
canonical_url: "https://mrnasdog.com/research/flr/inflation"
tags: ["crypto", "flr", "flare", "oracles"]
published: true
---

Originally published at [FLR Inflation Analysis · September 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/flr/inflation).

# FLR Inflation Analysis · September 2026 · Supply growing · projected to keep growing

FLR supply is growing and is projected to keep growing. Over the 90 days to **Sep 29 2026**, Flare paid **640.5M FLR** of new staking and data rewards to holders and released another **295.7M FLR** of vested ecosystem rewards, while fee burns, one holder's monthly burns and the new FIRE buyback fund took out only **34.9M FLR**. Net, supply grew **+1.04%** on an 86.96B FLR float, and the next 90 days project **+1.03%**; the monitor reads **+0.60%**.

## The verdict, in one paragraph

The MrNasdog Pressure Framework reads FLR at **+1.04%** net inflation over the last 90 days and **+1.03%** for the next 90. The monitor, which divides market value by price every day, reads **+0.60%**. The gap is **0.44 percentage points**, inside the 0.5-point tolerance, so no warning chip is shown. The monitor's float count moves less than the chain's own supply contract, and the two agree on the direction. Flare is **inflationary by design on the active float**: new rewards arrive every day, and the burn side is a small fraction of them.

## Sell pressure: where new FLR comes from

Protocol inflation is the biggest source at **640.5M FLR**. Flare mints new FLR at 3% a year on its spendable supply — the rate the FIP.16 governance vote cut from 5% in April 2026, with a yearly ceiling of 3B FLR. That inflation pays validators, P-chain stakers, delegators to data providers, and the FTSO price-feed and FDC data-connector networks. Validators claimed **209.9M FLR** and delegators and data providers claimed **430.6M FLR** this window. The chain authorized 667.2M FLR of new inflation in the same 90 days, so the claims track the mint closely. Rewards that nobody claims in time are burned inside the reward pools — **66.6M FLR** this window — and because those coins never reached a holder, Flare counts them on neither side of the ledger.

Vesting unlocks add **295.7M FLR**. Flare's ecosystem incentives are paid as rFLR, which vests over 12 months inside a personal account; a holder who leaves early gets half of the locked part and the other half is burned. Holders took **306.6M FLR** out of those accounts this window, of which **11.4M FLR** was burned as the early-exit penalty, leaving **295.2M FLR** that reached wallets. The old token-sale escrow is fully vested and released only **0.53M FLR** more.

Foundation and unscheduled unlocks are **0**: no Foundation-controlled wallet paid coins straight into the market this window. Long-term locked or bankruptcy releases are also **0** — Flare has no estate or trustee, the early-backer distribution finished in the first quarter of 2026, and the FlareDrop airdrop ended on **Jan 30 2026**.

## Buy pressure: where new FLR goes

The programmatic buyback row is the new FIRE fund, the Flare Income Reinvestment Entity that FIP.16 created to buy FLR and burn it. It has not bought or burned any FLR yet. What it has done is collect fees: from **Aug 18 2026** its data-request fee wallet started filling and now holds **3.1M FLR**, which the chain's supply contract excludes from circulation. Across the Foundation-listed wallets, **3.2M FLR** left the float this window, and at the pace since Aug 18 the fund would collect about **6.7M FLR** in the next 90 days.

The protocol fee burn destroys every transaction fee. The Granite hard fork on **Jul 14 2026** raised the minimum base fee twentyfold, from 25 to 500 gwei, but network usage is small, so the burn is too: **6.0M FLR** over the whole window and **5.5M FLR** in the 75 days after the fork, about 74K FLR a day. The next 90 days use that post-fork pace, **6.66M FLR**.

One more buy row sits outside the canonical four. A single large staker's multisig wallet collects its rewards every few days and sends a lump to the burn address about once a month — 13 burns since **Jul 9 2025**. This window it burned **25.7M FLR** (8.7M on Jul 7, 12.0M on Aug 14 and 5.0M on Sep 9 2026), the largest single offset on the page. Foundation buying is **0**, and new long-term locks are **0**: staking grew from about 16B FLR in July to about 21.5B by late August, but staked FLR still counts as circulating.

## Foundation and overhang

The largest overhang is the incentive treasury, which held **17,306M FLR** at the end of the window, down 440.0M as it funded new rFLR grants. Those grants sit first in the RNat reward pool, which holds **763.2M FLR**, and then in personal vesting accounts; the framework counts them only when a holder takes them out, so moving money between these reserves adds nothing. The fully vested sale escrow still holds **204.0M FLR** nobody has claimed, and the seven Foundation-listed wallets hold **3.2M FLR**, almost all of it FIRE fee revenue. Every one of these balances is read from the chain at each rebuild. If any of them falls between refreshes by more than the vesting and reward flows already counted, the extra outflow enters Sell #3 at the next refresh.

## How FLR compares to other staking-reward Layer 1s

Flare belongs with the uncapped staking chains that pay security from continuous issuance, but it has two features most of them lack. First, it runs a second supply stream: a large pre-minted incentive treasury that keeps releasing coins through 12-month vesting, adding **295.7M FLR** a quarter on top of the **640.5M FLR** of inflation. A chain whose genesis allocations have finished vesting has only the first stream. Second, Flare's inflation is a percentage of the spendable balance with a yearly ceiling, not a fixed per-block reward, so it scales with the float rather than shrinking on a halving schedule the way a proof-of-work coin does.

On the burn side, Flare now has both a fee burn and a buyback fund, like chains that pair an EIP-1559-style burn with a treasury buyback. The difference is scale. On a busy smart-contract chain the fee burn can offset a meaningful slice of issuance; on Flare this quarter it offset **less than 1%** of the new supply, and the buyback fund has so far only collected fees. The biggest offset came from one holder's voluntary burns, which no protocol rule guarantees.

Flare also burns rewards that go unclaimed and half of every early rFLR exit. Those burns are real, but they destroy coins before any holder could trade them, so they cut future additions rather than taking tradable FLR off the market. That is why FLR's large burn-address growth — 109.8M FLR this window — shrinks to a much smaller offset in this framework.

## What to watch in the next 90 days

Watch whether the FIRE fund makes its first open-market purchase and burn; until it does, its fee wallet is a parked balance, not a buyback. Watch the monthly inflation slots through **Dec 28 2026** — the current slot recognizes about 218.6M FLR per 30 days. Watch the rFLR withdrawal pace and early-exit burns, since that stream is the second-largest source of new supply. Watch the large staker's monthly burn: if it stops, the forward buy side loses about two-thirds of its size. And watch transaction volume after the fee rise, because the fee burn only grows if usage does.

## Summary

FLR supply grew **+1.04%** in the 90 days to Sep 29 2026 and is projected at **+1.03%** for the next 90, against a monitor reading of **+0.60%**. Staking and data rewards (**640.5M FLR**) and vested ecosystem rewards (**295.7M FLR**) far outweigh fee burns, one holder's monthly burns and the new buyback fund combined (**34.9M FLR**). The key risk is that the 17.3B FLR incentive treasury keeps feeding vesting releases while usage-driven burns stay small. Flare's 3% rate and 3B FLR yearly ceiling limit the pace of new supply, but there is no fixed lifetime cap.

*MrNasdog Pressure Framework analysis of FLR, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*
