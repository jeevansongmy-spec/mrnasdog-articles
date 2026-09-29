---
title:         "QNT Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "QNT supply is flat: 0 QNT minted, unlocked or burned in 90 days, 0.00% net on 14.54M circulating. No emission, no vesting, but a parked 2018 mint switch."
canonical_url: "https://mrnasdog.com/research/qnt/inflation"
tags:          ["crypto", "qnt", "quant", "interoperability"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/qnt/inflation](https://mrnasdog.com/research/qnt/inflation)*

# QNT Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

Quant (QNT) had a completely still supply over the last 90 days: **0 QNT** of new supply against **0 QNT** removed, for a net of **0.00%** on a circulating base of **14.54M QNT**. QNT is a fixed-issue ERC-20 token on Ethereum with no block reward, no vesting left and no burn programme. The one thing that could change it is a parked mint switch in the 2018 sale contract, which did nothing this window.

## The verdict, in one paragraph

The MrNasdog Pressure Framework reads QNT at **0.00%** net supply change over the last 90 days (Jul 1 to Sep 29 2026) and **0.00%** for the next 90 days. Our supply monitor, which infers supply from market data, reads **+0.20%** over the same stretch. The gap is **0.20 percentage points**, inside our 0.5-point tolerance, so no warning chip is shown. The monitor moves a little because it divides market value by price, and during a week when the QNT price tripled, that ratio wobbles; nothing on-chain moved. In one line: QNT is a frozen-supply token — nothing is minted, nothing is burned, and the float stays where it was.

## Sell pressure: where new QNT comes from

Protocol inflation is **0 QNT**. Quant has no chain of its own, so there are no validators or miners to pay. The only way new QNT can be created is the mint function in the QNT token contract, and only the 2018 sale contract may call it. Every mint on record — **608 of them, 24.43M QNT in total** — happened on Jun 25 2018. None has happened since, and the wallet that controls the sale contract did not send a single transaction in the window, so no mint could have fired. That switch is parked, not removed: the sale code still lets its owner record and mint up to about **6.47M QNT**. We read it at every check.

Vesting unlocks are **0 QNT**. There is no vesting contract. The whole 2018 allocation — about 68% to sale buyers and the rest to the company, the founders and advisors — was handed out when the tokens were minted, and no unlock tracker lists any QNT calendar today.

Foundation and unscheduled unlocks are **0 QNT**. Only about **68.3K QNT** sits outside the circulating count, which leaves very little room for a company release to add new coins to the market. Long-term locked or bankruptcy supply is also **0 QNT**: there is no estate, trustee or time lock holding QNT for later.

## Buy pressure: where new QNT goes

The programmatic buyback is **0 QNT**. Quant sells Overledger licences and platform access to banks and other institutions, but no contract or treasury uses that revenue to buy QNT back from the market.

The protocol fee burn is **0 QNT**. QNT has no fee burn. The token contract itself works as a dead end: coins sent to it can never move again, and it holds the **9.55M QNT** that Quant burned in 2018 when it cut the planned supply. In this window people sent it another **5.2 QNT** by mistake — gone for good, but too small to change the totals, so the row stays at zero.

The foundation buy is **0 QNT**: no announcement or on-chain flow shows Quant buying QNT. The new long-term lock is also **0 QNT**. Node staking on Quant's Fusion network went live on Jun 2 2026, before this window, but no staking contract on Ethereum holds QNT yet, and coins staked or locked for licences stay inside the circulating count. Staking may tie up QNT, but by our measure it does not shrink the float.

## Foundation and overhang

Three overhangs are tracked. The first and largest is the parked sale switch: about **6.47M QNT** the sale owner could still record and mint directly, plus a larger regular-sale allowance that would need the sale reopened and buyers paying in. Its owner wallet has been silent since 2018; we read it on-chain at every check. The second is three large dormant wallets holding **1.86M QNT** between them, unchanged across the window. Each is far larger than the 68.3K QNT outside the circulating count, so their coins are already counted as circulating — if they sell, coins change hands but no new QNT reaches the market. The third is the small **68.3K QNT** bucket the circulating count leaves out; its wallets are not published. Quant's Overledger treasury contracts held **0 QNT** at both ends. If any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How QNT compares to other enterprise and fixed-supply tokens

Most Layer-1 coins pay for security with new issuance: stakers or miners receive fresh coins every block, so supply grows by a steady fraction of a percent to several percent a year whether or not the network is used. QNT sits on the other side of that line. It is a utility token on Ethereum, Ethereum's own validators secure it, and so there is no issuance to pay out. Against a proof-of-stake chain with 2–5% yearly emission, QNT's zero sell side is a structural difference, not a quiet quarter.

Among fixed-supply tokens, QNT also stands apart from the ones that shrink. Exchange tokens with quarterly burns and DeFi tokens that route fees into buybacks take coins off the market on a schedule; QNT has no such buyer, so its supply is flat rather than falling. Its closest match is an older ERC-20 whose sale finished years ago: full float, no vesting overhang, no burn. The difference that matters for QNT is the sale contract that was never switched off — a token whose supply stays fixed by choice, not by code.

## What to watch in the next 90 days

First, the sale owner wallet: any transaction from it is the one signal that could move QNT's supply, and we read its nonce at every check. Second, staking on the Fusion network: if Quant moves staking onto an Ethereum contract that the circulating count starts to leave out, it becomes a new long-term lock. Third, The Clearing House network Quant was picked for on Sep 24 2026, due to open to banks in the first half of 2027; any rule that banks must hold or lock QNT would show up here first. Fourth, the 68.3K QNT outside the circulating count, which would enter Sell #3 if it moved. No dated supply event is scheduled before Dec 28 2026.

## Summary

QNT's supply did not change over the last 90 days: **0 QNT** minted, **0 QNT** unlocked and **0 QNT** burned, for a net of **0.00%** on **14.54M QNT** circulating, with our monitor at **+0.20%**. The structure is a fixed-issue Ethereum token with its whole allocation out since 2018, no emission and no buyer. The key risk is the parked 2018 sale switch, which could still mint about 6.47M QNT if its owner chose to. Until that wallet moves, QNT's supply is capped in practice at its current level.

*MrNasdog Pressure Framework analysis of QNT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*
