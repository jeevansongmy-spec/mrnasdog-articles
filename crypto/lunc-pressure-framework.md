---
title:         "LUNC Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "LUNC supply roughly steady: no minting, and a 1.5% transfer tax burned 6.62B LUNC in 90 days. Net −0.16% over 90 days, and about −0.18% projected next."
canonical_url: "https://mrnasdog.com/research/lunc/inflation"
tags:          ["crypto", "lunc", "terraclassic", "tokenomics"]
published:     true
---
Originally published at [LUNC Inflation Analysis · October 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/lunc/inflation).

# LUNC Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

<!-- main-page -->
This is the long supply read. For the signal, the price drivers and the questions people ask about Terra Luna Classic, see [mrnasdog.com/research/lunc](https://mrnasdog.com/research/lunc).

**LUNC supply is roughly steady and leaning down.** Terra Classic mints no new LUNC, so the only coins that reached the market were **281.85M LUNC** paid out of the community pool by vote, while the transfer-tax burn, a monthly exchange burn, net staking and the pool's tax share took **9.33B LUNC** off it. Net, supply fell **0.16%** over 90 days and is projected to fall about **0.18%** in the next 90; the monitor reads **−0.17%**. The burn is real but small next to a **5.52T** float, so a 1.5% tax moves the supply by tenths of a percent, not by whole percents.

## The verdict, in one paragraph

Over the 90 days to Oct 9 2026, our ledger puts LUNC's net supply change at **−0.16%** of the circulating count (sell **281.85M**, buy **9.33B**). The inflation monitor reads **−0.17%** for the same 90 days, a gap of just **0.01 percentage points**, well inside the 0.5-point line, so no warning chip is needed. For the next 90 days the Terra Classic ledger projects **−0.18%**: buy **10.20B** against sell **253.07M**. The plain label for LUNC today: a **no-mint chain with a slow, tax-driven burn**.

## Sell pressure: where new LUNC comes from

**Protocol inflation is 0.** The Terra Classic mint module is set to a 0% rate with 0 annual provisions, the old market swap that once created LUNC from UST is shut, and total supply fell from **6,454.35B** to **6,446.77B LUNC** across the window. Validators and stakers are paid from fees and an oracle reward pool, not from fresh coins.

**Vesting unlocks are 0.** The 2019 LUNC allocations finished long ago and no team, investor or token-sale schedule is left on the chain, so no cliff or monthly tranche can land.

**Foundation and unscheduled unlocks: 281.85M LUNC.** Terra Classic has no foundation; the one shared treasury is the community pool, which sits outside the circulating count. A vote on Sep 4 2026 paid **281.85M LUNC** from it to keep the chain's IBC relayers running, and that is the only LUNC that crossed into the market in these 90 days. For the next 90 days we book **253.07M LUNC**: a payment for the finished Hyperlane bridge, with 94% yes votes and the vote closing on Oct 15 2026. A larger 1.60B LUNC security-audit request was rejected on Oct 1 2026.

**Long-term locked or bankruptcy: 0.** Eight wallets left by the wound-down Terraform Labs still hold about **302.2M LUNC**, but they moved by only 0.44M in the window and are already part of the circulating count, so they add nothing new. No trustee is paying LUNC out.

## Buy pressure: where new LUNC goes

**Programmatic buyback: 0.** The Terra Classic protocol itself buys nothing back.

**Protocol fee burn: 6.62B LUNC.** Every on-chain LUNC transfer pays a tax, and 80% of it is destroyed in the same block; 10% goes to the community pool and 10% to the oracle reward pool. A governance vote raised the tax from 0.5% to **1.5%** on Aug 2 2026, and the burn rose from about **33M** to about **86M LUNC** a day. Because that change landed inside the window, the next 90 days use the new rate only: about **7.78B LUNC**.

**Foundation buy: 0.** No foundation or treasury buys LUNC on the market.

**New long-term lock: 555.97M LUNC.** Staked LUNC is left out of the circulating count, so a bigger stake takes coins off the market. The bonded stake rose from **902.15B** to **902.71B LUNC**, but it swings both ways (it touched 914.91B on Oct 1 2026), so we project no change for the next 90 days. Another 51.05B LUNC is in its 21-day unstaking wait and already counts as circulating.

**Exchange buy-and-burn: 966.42M LUNC.** A large exchange burns LUNC on the 1st of each month from its trading fees: **275.65M** on Aug 1, **334.88M** on Sep 1 and **355.89M** on Oct 1 2026, each sent to the chain's burn address and gone in the same block. Three more burns fall in the next 90 days, booked at the recent average of about 322M each.

**Community pool intake: 1.19B LUNC.** The pool's 10% tax share leaves the circulating count until a vote spends it. It took in 1.19B LUNC in 90 days, about 16M a day since the tax rise, and about **1.45B** is projected for the next 90 days.

## Foundation and overhang

The biggest pile that could reach the market is the **staked LUNC: 902.71B**, about one coin in seven. Any holder can unstake, and the coins become liquid after 21 days; we read the bonded pool on-chain at every rebuild. The **community pool holds 9.27B LUNC** and pays out only by vote, with one 253.07M payment now likely. The **oracle reward pool (36.10B)** pays stakers a little every block and is already counted as circulating. The **Terraform Labs wallets (about 302.2M)** are dormant and already counted. A further fixed set of about 14.97B LUNC is left out of the circulating count without a public label; it did not move. If any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How LUNC compares to other proof-of-stake chains

Most proof-of-stake chains pay validators in new coins: Cosmos Hub, Polkadot and Ethereum all issue fresh supply every day, and a fee burn, where it exists, only trims that issuance. Terra Classic is unusual because issuance is switched off entirely, so the burn is not fighting new coins; every LUNC destroyed shrinks the total. That puts LUNC closer to a fixed-supply coin with a slow drain than to a typical staking chain.

The drain is the catch. A transfer tax only burns what moves on-chain, and most LUNC trading happens on exchanges, where no tax is paid. At about 86M LUNC a day the burn removes roughly **0.6% of the float a year** before the exchange burn, so even at three times the old tax the supply curve bends slowly. Chains with a base-fee burn, like Ethereum, burn in proportion to block space demand; LUNC burns in proportion to on-chain transfer volume, which a higher tax can also push away.

LUNC also differs in what counts as circulating: staked coins and the community pool are left out. That makes staking a real lock on the float and an unstaking wave a real source of sell pressure — a risk most chains that count staked coins as circulating do not show in their supply numbers.

## What to watch in the next 90 days

**Oct 15 2026** — the vote to pay 253.07M LUNC from the community pool for the Hyperlane bridge closes; if it fails, Sell #3 drops to 0.

**Nov 1 2026, Dec 1 2026 and Jan 1 2027** — the monthly exchange burns; a smaller fee month means a smaller burn.

**The burn tax itself** — any new proposal to change the 1.5% rate or the 80/10/10 split would change the burn and the pool intake at once.

**The staked pool** — a large unstaking wave would turn the lock into sell pressure 21 days later; the signal proposal on dropping the "Classic" name (deposit period to Oct 19 2026) changes no supply rule by itself.

## Summary

Terra Luna Classic (LUNC) mints no new coins, so its supply only falls: a 1.5% transfer-tax burn, a monthly exchange burn and the community pool's tax share took **9.33B LUNC** off the market in 90 days, against **281.85M** paid out by vote, for a net change of **−0.16%**, with **−0.18%** projected next. The monitor agrees within 0.01 points. The burn is steady but small next to a 5.52T float, and the key risk is the 902.71B LUNC staked pool, which could return to the market on a 21-day delay.

*MrNasdog Pressure Framework analysis of LUNC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 9 2026.*
