---
title:         "LUNC Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "LUNC supply roughly steady: no minting, and a 1.5% transfer tax burned 6.23B LUNC in 90 days. Net −0.32% over 90 days, and about −0.19% projected next."
canonical_url: "https://mrnasdog.com/research/lunc/inflation"
tags:          ["crypto", "lunc", "terraclassic", "tokenomics"]
published:     true
---

Originally published at [LUNC Inflation Analysis · September 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/lunc/inflation).

# LUNC Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

The MrNasdog Pressure Framework reads Terra Luna Classic (LUNC) at **−0.32% net** over the trailing 90 days and **−0.19%** over the next 90: supply is shrinking, but slowly. Terra Classic mints no new LUNC at all, and **18.16B LUNC** left the circulating count in 90 days — a **6.23B** transfer-tax burn, a **1.21B** exchange buy-and-burn, **9.60B** of new staking and **1.11B** into the community pool — against only **291.7M** paid back out by vote. With **5.51 trillion LUNC** circulating, even billions of burned coins move the total by only a fraction of a percent.

## The verdict, in one paragraph

LUNC supply fell **0.32%** over the 90 days from Jul 1 to Sep 29 2026, and the framework projects a **0.19%** fall over the next 90 days. The independent monitor reads **−0.29%** for the same stretch, a gap of just **0.04 percentage points**, well inside the 0.5-point limit, so no data-conflict flag is shown. The forward figure is smaller than the trailing one because the trailing window includes **9.60B LUNC** of fresh staking, which has no set programme and is not projected forward. Terra Classic is a **zero-issuance chain with a transfer-tax burn**: nothing new comes in, and every taxed transfer destroys a little.

## Sell pressure: where new LUNC comes from

Protocol inflation is **0**. The Terra Classic mint rate is set to zero, the old market swap that once created LUNC is switched off, and total LUNC supply fell on every one of the 90 days in the window, from **6.455 trillion** to **6.448 trillion**. Staking rewards on Terra Classic are paid from a reward pool of coins that already exist, topped up by the transfer tax, so they add nothing new. Because a governance vote could switch minting back on, the row is checked at every rebuild rather than marked as fixed forever.

Vesting unlocks are **0**. LUNC has no team, investor or foundation allocation left to vest, and no unlock tracker lists any release.

Foundation and unscheduled unlocks come to **291.7M LUNC**. Terra Classic has no foundation; its treasury is the community pool, which sits outside the circulating count. Two voted payouts put coins back on the market: **9.87M LUNC** on Jul 1 2026 for bridge work to Solana and **281.85M LUNC** on Sep 4 2026 to keep the chain's cross-chain links running. Payouts are sporadic, so the next 90 days carry 0 unless a new spending vote passes.

Long-term locked or bankruptcy supply is **0**. Terraform Labs is being wound down, and its last eight wallets hold about **302.7M LUNC** that did not move in the window. The court order requires those coins to be burned or their keys destroyed, and they are already counted as circulating, so they add nothing new either way.

## Buy pressure: where new LUNC goes

There is no programmatic buyback by the protocol, so that row is **0**. The biggest steady buyer is the burn.

The protocol fee burn removed **6.23B LUNC**. Most LUNC transfers on Terra Classic pay an on-chain tax, and 80% of that tax is destroyed on the spot, with 10% going to the community pool and 10% to the staking-reward pool. On Aug 2 2026 a governance vote raised the tax from **0.5%** to **1.5%**. The burn went from about **33M LUNC a day** before the change to about **89M a day** after it — 2.7 times more on a tax three times higher, which means somewhat less LUNC is being moved on-chain. A handful of very large transfers on Sep 14 and 15 2026, together more than 58B LUNC, paid about 700M of that burn on their own. The next 90 days use the post-change rate: about **8.05B LUNC**.

Foundation buying is **0**: there is no foundation, and no vote this window spent community funds on buying LUNC.

New long-term locks came to **9.60B LUNC**. Staked LUNC sits outside the circulating count, and the staked total rose from **904.38B** to **913.98B** in the window, most of it in September after a dip to 900.5B on Sep 5 2026. Staking follows holders' choices rather than a set plan, and it has run the other way in earlier windows, so the next 90 days carry 0 for this row.

Two extra rows complete the Terra Classic buy side. The first is an **exchange buy-and-burn**: one large exchange burns LUNC from its trading fees on the first day of each month, and in the window it sent **604.28M** on Jul 1, **275.65M** on Aug 1 and **334.88M** on Sep 1 2026 to the burn address — **1.21B LUNC** in all. Three more burns are due on Oct 1, Nov 1 and Dec 1 2026, about **1.00B** at the latest size. The second is **community pool intake**: the pool's tenth of the tax took **1.11B LUNC** off the market in 90 days, and about **1.52B** is expected over the next 90 at the higher tax.

## Foundation and overhang

Terra Classic has no foundation, team treasury or buyback wallet. The balances we track are all on-chain and read at every rebuild. The **community pool** holds **9.15B LUNC** outside the circulating count and pays only by a governance vote; a **1.60B LUNC** payout for a security audit is in a vote that ends Oct 1 2026. The **staked pool** holds **913.98B LUNC**, also outside the count; unstaking takes 21 days, and **38.80B** is already on its way out and already counted as circulating. The **staking-reward pool** holds **36.55B LUNC** and pays stakers from coins that are already counted. The eight remaining **Terraform Labs wallets** hold about **302.7M LUNC**. A fixed **14.95B LUNC** is also left out of the circulating count and did not change all window. If any of these balances falls between rebuilds and the coins reach the market, the outflow enters the foundation and unscheduled row at the next rebuild.

## How LUNC compares to other burn-driven Layer 1s

Most proof-of-stake Layer 1 chains pay validators in newly created coins and then try to offset it with a fee burn. Ethereum is the clearest example: it creates new ETH every block and burns part of each fee, and the burn usually loses. Terra Classic is built the other way round. LUNC has **no issuance at all**, so every burned coin is a net reduction, and the tax taxes the movement of the coin itself rather than the use of blockspace.

The closest structural analogue is BNB, which also mixes a protocol burn with a large exchange-driven burn. The difference is scale: BNB's burns remove a visible share of a small, capped supply every quarter, while LUNC's **18.16B** of buy-side flow in 90 days is about a third of one percent of a **5.51 trillion** float. Meme-style coins such as SHIB rely on voluntary community burns with no protocol tax, which keeps their burn tiny; Terra Classic's tax makes the burn automatic, but the size of the supply left behind by the 2022 collapse means it works very slowly.

Terra Classic also counts staked coins outside its circulating supply, unlike Ethereum or Cardano. That makes LUNC's net figure sensitive to staking swings: a few billion coins moving into or out of staking can outweigh a month of burning.

## What to watch in the next 90 days

**Oct 1 2026:** the vote on proposal 12228 closes; if the 1.60B LUNC audit payout passes, those coins leave the community pool and enter the market.

**Oct 1, Nov 1 and Dec 1 2026:** the exchange's monthly LUNC burns, about 335M each at the latest size.

**A rival audit plan:** a second community pool request of about US$74,000 in LUNC is being discussed on the forum and could reach a vote in the window.

**Tax and staking:** any vote to change the 1.5% tax or its 80/10/10 split resets the burn forecast, and a large move into or out of staking can swing the net by more than the burn itself.

## Summary

LUNC supply is shrinking slowly: **−0.32%** over the last 90 days and a projected **−0.19%** over the next 90, in line with the monitor's **−0.29%**. Terra Classic creates no new coins, and a **1.5%** transfer tax, raised from 0.5% on Aug 2 2026, burns about **89M LUNC a day**, with an exchange adding a monthly burn on top. The main risks to the reading are a community pool payout passing by vote and a large exit from staking, both of which put coins back on the market. With **5.51 trillion LUNC** circulating, the burn cuts supply by well under one percent a quarter.

---

*MrNasdog Pressure Framework analysis of LUNC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*
