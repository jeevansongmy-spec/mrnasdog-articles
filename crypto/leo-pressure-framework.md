---
title: "LEO Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description: "A MrNasdog Pressure Framework read of UNUS SED LEO: nothing minted, no vesting, and a buyback that parked 521,595 LEO in the issuer's own account. −0.06% net over 90 days."
canonical_url: "https://mrnasdog.com/research/leo/inflation"
tags: ["crypto", "leo", "bitfinex", "exchange-token"]
published: true
---

> Originally published at **[mrnasdog.com/research/leo/inflation](https://mrnasdog.com/research/leo/inflation)** by MrNasdog.

# LEO Inflation Analysis · September 2026 · Mixed flows, supply roughly steady

UNUS SED LEO, the exchange token issued by iFinex, the parent of Bitfinex, mints nothing and has no vesting schedule — every LEO was delivered in the 2019 sale. The only LEO supply flow is a revenue-funded LEO buyback: over the last 90 days it bought **521,595 LEO** and moved it into the issuer's own account, where it is **parked, not destroyed**. That is **zero** added against **0.52M LEO** removed from the float, so the MrNasdog Pressure Framework reads LEO at **−0.06% net** against a supply-monitor reading of **−0.53%** — a gap of **0.47 percentage points**, inside tolerance. LEO supply is shrinking slowly, and reversibly: both LEO mint paths are still live.

## The verdict, in one paragraph

For the 90-day window ending **Sep 14 2026**, the Pressure Framework reads **LEO at −0.06% net**: nothing on the sell side adds a single LEO, while the LEO buyback took **521,595 LEO** off a circulating supply of **919.86M**. The independent supply monitor reads the realised 90-day change at **−0.53%**, a gap of **0.47 percentage points**. That sits inside the framework's half-point tolerance, so LEO ships with **no data-conflict flag** — and the monitor's wider reading comes from a single rounded price print on its opening day, not from any LEO flow: a day earlier it read **−0.06%**, the same as the ledger. The forward column also reads **−0.06%**, holding the measured LEO buyback pace. The label for LEO is **slowly deflationary by parked buyback**: a corporate token with no issuance whose float falls a little every day, into an account its issuer still controls.

## Sell pressure: where new LEO comes from

Nowhere, this window — but not because it cannot. Sell #1, protocol inflation, is **zero**: LEO is a token living on two host chains, Ethereum and Vaulta (formerly EOS), so no block reward or staking stream pays out new LEO. The two LEO contracts do still carry working mint paths. On Ethereum, a controller contract owned by a single Bitfinex key can create or destroy LEO, and the LEO supply figure sits in live storage that a mint would rewrite. On Vaulta, the LEO contract exposes issue and retire actions under a two-of-three Bitfinex multisig, under a one-billion cap that leaves about 692.35M LEO unissued on that chain. Neither path fired: Ethereum LEO held at **660M** and Vaulta LEO at **307.65M** across the whole window, and a full sweep of issue and retire actions on two independent history nodes found none. Because the switch is on, the framework tags this row checked rather than permanent. Sell #2, vesting unlocks, is **zero**: LEO never had a team or investor vesting schedule, since the entire supply was sold and delivered in the **May 2019** private sale.

Sell #3, foundation and unscheduled unlocks, is **zero**, and it covers the largest balances in LEO. Almost the whole LEO float sits in Bitfinex-labelled wallets: an Ethereum wallet holding **648M LEO**, untouched since **Jun 25 2023**, and a Vaulta cold account holding **257.79M LEO**, untouched since **Sep 15 2025**. Both may hold depositors' LEO rather than the company's own, and the framework tracks them regardless. Neither moved a coin this window. Sell #4, long-term locked or bankruptcy supply, is **zero**: no estate or trustee holds LEO. The 2016 Bitfinex hack recovery is bitcoin, not LEO, so if it returns it feeds the LEO buy side rather than this row.

## Buy pressure: where new LEO goes

Buy #1, the programmatic LEO buyback, is the only non-zero line on the page at **0.52M LEO**. iFinex committed in the 2019 LEO whitepaper to spend at least **27%** of its consolidated gross monthly revenue buying LEO off the market. The bought LEO then moves on-chain, once a day, from a Bitfinex funding account into **bitfinexleo1** — the LEO contract's own issuer account on Vaulta — with the memo burn. The framework measured that flow four ways and all four agree exactly: the issuer account rose by **521,595 LEO** between its two balance readings, **72** transfers summed to the same figure on two separate history nodes, the funding account fell by the same amount, and iFinex's own published LEO supply figure fell by it too.

The word burn is where LEO needs care. On a Vaulta token, sending coins to the issuer account does not reduce supply; only a retire action does, and none happened. The LEO is **parked, not destroyed**. The framework still counts it as bought back, for three reasons: the coins were paid for out of revenue and left the tradable float; the parking account has never sent a coin out across **7,460** recorded inbound moves; and the circulating figure the whole market reads already excludes it. It is booked once, as accumulation, and never as a burn — so Buy #2, the protocol fee burn, is **zero**: no LEO reached a dead address and neither chain's supply fell. One timing detail: no on-chain move has fired since **Sep 1 2026**, while iFinex reports about **87.8K LEO** bought and waiting. Past pauses all caught up, but the framework books only what reached the chain. Buy #3, foundation buying, is **zero**, and Buy #4, new long-term locks, is **zero**: LEO has no staking contract and no lockup programme.

## Foundation and overhang

Four Bitfinex-controlled LEO balances are enumerated and re-read from the chain on every refresh. The LEO buyback parking account holds **47.80M LEO**, about **5.2%** of circulating LEO, and it is the overhang that matters most, because its coins are counted as gone while its keyholders could still send them back to market. The Vaulta cold account holds **257.79M LEO**; the Ethereum wallet holds **648M LEO**; the funding account that pays into the buyback holds **2.06M LEO** and received nothing on-chain this window. There is no DAO treasury and no bankruptcy residual. If any of these balances falls between refreshes and the LEO does not land in the parking account, the outflow enters Sell #3 at the next refresh; if the parking account itself ever sends LEO out, that outflow is booked as new sell pressure the same day it is read.

## How LEO compares to other exchange-linked tokens

LEO belongs to the small group of exchange-linked tokens whose supply falls through issuer action rather than rising on an emission curve, and the useful comparison is where the removed coins end up. A token like BNB sends its quarterly burn to a dead address, so the coins are gone for good and the supply figure falls with them. LEO sends its buyback to the issuer's own live account. The float effect today is the same — both leave the tradable count — but only a destroyed coin is a one-way trip. A parked coin is a promise backed by an unbroken record, not by code.

The second contrast is the mint. A chain token with no block reward and a renounced or absent mint cannot add supply at all. LEO can: both LEO contracts keep a live issuing path in Bitfinex's hands, so the zero on the LEO sell side is an observed zero, re-checked each time, rather than a built-in one. The third contrast is scale. At **0.06%** a quarter, the LEO buyback is modest next to some reserve-funded burns that clear a percent or more in a single event, and it is sized by one company's revenue rather than by a public rule. What could change that is not the everyday stream but the 2016 hack recovery: iFinex has committed at least **80%** of net recovered bitcoin to LEO repurchases within **18 months** of recovery, and the seized wallet still holds about **94.64K BTC**.

## What to watch in the next 90 days

First, the seized bitcoin wallet: it has never spent a coin, and the first transfer out toward Bitfinex would start the **18-month** clock on iFinex's biggest standing LEO buyback commitment. Second, the on-chain LEO buyback pause that began after **Sep 1 2026**: a catch-up transfer near the **87.8K LEO** backlog would confirm the everyday flow, while a pause that runs for months would pull the forward figure down. Third, the parking account at **47.80M LEO**: any outflow at all reverses the logic of the buy row and enters the sell side. Fourth, the funding account at **2.06M LEO**, which drains by roughly the buyback pace and will need refilling within a year. Fifth, any issue or retire action on either LEO contract — a retire would turn parked LEO into destroyed LEO, and an issue would open Sell #1.

## Summary

The MrNasdog Pressure Framework reads UNUS SED LEO at **−0.06% net** over the trailing 90 days and **−0.06%** over the next 90, with zero on all four sell rows. The mechanism is a corporate LEO token with no issuance and no vesting, whose only flow is a revenue-funded LEO buyback that moved **521,595 LEO** into the issuer's own account. The key risk is that nothing is destroyed and nothing is locked in code: the **47.80M LEO** parking account and the live mint paths on both chains are held by the issuer. The upside lever sits off-chain, in a seized bitcoin wallet whose return would fund LEO repurchases many times the size of today's everyday flow.

*MrNasdog Pressure Framework analysis of LEO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 14 2026.*
