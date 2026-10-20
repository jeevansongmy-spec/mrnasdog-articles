---
title:         "QNT Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "QNT supply is roughly steady: no new QNT since 2018, no unlocks, no burn. A reserve wallet released 12,002 QNT, net +0.08% in 90 days, 0.00% next."
canonical_url: "https://mrnasdog.com/research/qnt/inflation"
tags:          ["crypto", "qnt", "quant", "interoperability"]
published:     true
---
*Originally published at [https://mrnasdog.com/research/qnt/inflation](https://mrnasdog.com/research/qnt/inflation)*

<!-- main-page -->
Looking for the buy-or-sell answer? It is on the QNT coin page, with demand and price drivers: [mrnasdog.com/research/qnt](https://mrnasdog.com/research/qnt)

# QNT Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

QNT supply is roughly steady. Quant has made **no new QNT** since June 2018, nothing vests, and nothing buys back or burns QNT. In the 90 days to Oct 13 2026 the one real flow was a reserve wallet, kept outside the circulating count, that released **12,002 QNT** in October, against only **7.36 QNT** lost for good. Net, the QNT float grew **+0.08%**, and nothing is scheduled for the next 90 days.

## The verdict, in one paragraph

Over the 90 days from Jul 15 2026 to Oct 13 2026, our ledger reads QNT net supply at **+0.08%** of the **14.56M QNT** in circulation, and **0.00%** for the next 90 days. The monitor, which follows the circulating count day by day, reads **+0.02%**, a gap of **0.06 percentage points**, well inside our 0.5-point tolerance, so no warning chip ships. Most of the small difference is timing: the monitor's last reading came before the larger of the two October releases was counted. QNT is a closed-supply Ethereum token: quiet by design, with one small reserve that has started to move.

## Sell pressure: where new QNT comes from

Protocol inflation is **0**. QNT is an ERC-20 token on Ethereum, not a chain of its own, so there are no block rewards, no staking pay and no emission curve. Every QNT that exists was made in June 2018, when the 2018 sale contract handed out **24.43M QNT** in 608 transfers. That figure closes exactly against the sale contract's own counters. The token's printed total of 45.47M is a fixed number written into the code; it never changes and says nothing about real supply.

Vesting unlocks are **0**. QNT has no vesting calendar: team, sale buyers and Quant itself all received their coins in one go in 2018, and no unlock tracker shows anything left to release.

Foundation and unscheduled unlocks are **12,002 QNT**, the only non-zero sell row. One wallet that had held **42,378 QNT** without ever sending a transaction moved 2,001 QNT on Oct 6 2026 and 10,001 QNT on Oct 10 2026, all to one new wallet that still holds them. That wallet sat inside the small group of coins kept outside the circulating count, so these coins entered the float for the first time. The owner is not public. With no schedule behind the two moves, we project **0** for the next 90 days and watch the **30,376 QNT** still left in it.

Long-term locked or bankruptcy supply is **0**. No estate, trustee or long lock holds QNT on a release schedule.

## Buy pressure: where new QNT goes

The programmatic buyback is **0**. Quant does not buy QNT back. Business users pay for Overledger licences, and the QNT behind a licence is set aside for its term, but Quant publishes no amounts, and the public treasury contracts it lists for this held **0 QNT** at both ends of the window.

The protocol fee burn is **0**. The QNT contract has no burn function and no fee that is destroyed; the standard dead address gained only dust. Foundation buying is also **0**: nothing public shows Quant buying QNT in the window.

New long-term locks are **0**. QNT set aside for licences, and QNT moved to Solana through a bridge in early October, stay inside the circulating count, so neither takes coins out of the float.

One small extra row is real: coins lost in the token contract, **7.36 QNT** in 90 days. People sometimes send QNT to the token's own address by mistake, and the code has no way to send them back. The address now holds **9.55M QNT**, almost all from 2018; this window added 23 small transfers. We count it as a steady trickle out of supply.

## Foundation and overhang

The largest overhang is the 2018 sale contract. Its owner wallet can still switch it back on: it could record up to 6.47M QNT of presale buys by itself, and up to 21.04M more if it reopened the public sale, a total of **27.50M QNT**, almost twice today's float. That owner wallet has sent no transaction since 2019 and none in this window, so we read it on-chain at every rebuild rather than guess.

The second overhang is the group of coins kept outside the circulating count, now about **56,315 QNT**, including the **30,376 QNT** left in the wallet that moved in October. The rest of that group has no published address. Three large wallets, two of them about **600,000 QNT** each and one linked by public reports to Quant's founder, moved coins on Sep 29 and Sep 30 2026; because they were already counted as circulating, those moves add no new supply. If any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How QNT compares to other enterprise and fixed-supply tokens

QNT sits with the fixed-supply tokens, not with the inflationary Layer 1s. A proof-of-stake chain such as Ethereum or Hedera's HBAR network pays new coins to validators or releases treasury coins on a timetable, so its float grows every quarter by design. QNT has no validators to pay and no release timetable, so its float only moves when an existing holder outside the count lets coins go, as happened this October.

Against oracle and data tokens such as Chainlink's LINK, which still releases coins from team and reserve wallets in large blocks, QNT's outside-the-count group is tiny: about **0.4%** of circulating supply versus far larger reserves elsewhere. The catch is different: QNT's printed supply is not truly locked, because the old sale contract was never shut off. Most fixed-supply tokens end minting in code; QNT relies on one wallet staying quiet.

Unlike exchange tokens with a quarterly burn, or fee tokens with a buyback, QNT has no buyer built into the token. Licence demand sets coins aside rather than destroying them, so any lift from bank use shows up as holding, not as a shrinking supply.

## What to watch in the next 90 days

First, the reserve wallet that released 12,002 QNT on Oct 6 and Oct 10 2026: it still holds 30,376 QNT, and a third move would enter the ledger at the next refresh.

Second, the 2018 sale contract's owner wallet: any transaction from it would be the first since 2019 and could mean new QNT.

Third, Quant's bank work: The Clearing House picked Quant on Sep 24 2026 for a tokenized deposit network planned for the first half of 2027, and Quant speaks at a tokenised markets conference in London on Oct 19 2026. Watch for any word on how much QNT bank licences lock up.

Fourth, the large wallets that moved on Sep 29 and Sep 30 2026, including the founder-linked one: they cannot add supply, but further sales would add selling pressure from coins already in the float.

## Summary

QNT is a closed-supply Ethereum token: no new QNT since June 2018, no vesting, no burn and no buyback. In the 90 days to Oct 13 2026 its float grew **+0.08%**, all from a reserve wallet that released **12,002 QNT**, and nothing is scheduled for the next 90 days. The key risk is the old sale contract, which could still create up to **27.50M QNT** if its long-silent owner acted. The ceiling on everyday supply growth is small: only about **56,315 QNT** sit outside the circulating count.


---

*MrNasDog Pressure Framework analysis of QNT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 13 2026.*
