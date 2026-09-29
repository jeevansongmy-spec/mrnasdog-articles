---
title: "LEO Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description: "LEO supply is roughly steady: no new coins, and the iFinex buyback parked 421,293 LEO in 90 days, −0.05% net, with about −0.06% expected over the next 90 days."
canonical_url: "https://mrnasdog.com/research/leo/inflation"
tags: ["crypto", "leo", "bitfinex", "exchange-token"]
published: true
---

> Originally published at **[mrnasdog.com/research/leo/inflation](https://mrnasdog.com/research/leo/inflation)** by MrNasdog.

# LEO Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

UNUS SED LEO is roughly steady, with a slow lean toward less supply. Over the last 90 days **0 LEO** entered the market and the iFinex buyback took **421,293 LEO** out of the circulating count, a net change of **−0.05%**; at today's price the next 90 days take out about **592,632 LEO**, or **−0.06%**. The coins are parked in the token's own issuer account, not destroyed, and the one thing that could shrink LEO fast — a buyback funded by bitcoin recovered from the 2016 Bitfinex hack — still has no date.

## The verdict, in one paragraph

The framework reads LEO's net supply change at **−0.05%** over the last 90 days and **−0.06%** over the next 90. The inflation monitor reads **+0.02%** for the same stretch, a gap of **0.07 percentage points** — well inside the 0.5-point tolerance, so no ⚠ monitor gap chip is shown. The monitor's tiny rise is noise around a supply line that only ever steps down. In one line: LEO is a **zero-issuance exchange token with a slow, revenue-funded buyback** — nothing new is ever added, and a little is removed most days.

## Sell pressure: where new LEO comes from

Protocol inflation is **0 LEO**. LEO has no miners, no validators and no emission schedule. Its supply lives on two chains, and both read exactly the same at the start and the end of the window: **660M LEO** on the Ethereum token and **307.65M LEO** on the Vaulta token (the chain formerly called EOS). That does not mean new LEO can never appear. The Ethereum contract can still create tokens through its controller, and the Vaulta contract can still issue up to **692.35M LEO** more under its one-billion cap, signed by a 2-of-3 Bitfinex multisig. Neither was used, and nothing in the record suggests they will be, but the doors exist.

Vesting unlocks are **0 LEO**. iFinex sold the whole supply in a private sale in May 2019 to cover the money it lost when a payment processor's funds were seized. There was no team allocation and no investor cliff, so there is nothing left to unlock, and no unlock tracker follows LEO at all.

Foundation and unscheduled unlocks are **0 LEO**. Bitfinex controls very large LEO balances, but only one of them sits outside the circulating count, and that one has never sold: the issuer account covered below. The rest are already counted as circulating, so even if they moved they would add nothing new.

Long-term locked or bankruptcy supply is **0 LEO**. No estate, trustee or lock-up releases LEO. The 2016 hack is a bitcoin story, not a LEO one: if the stolen bitcoin ever comes back to Bitfinex, it would fund buying, not new supply.

## Buy pressure: where new LEO goes

The programmatic buyback is the only moving part. iFinex, the company behind Bitfinex, spends at least 27% of its revenue buying LEO back. Each day the bought coins travel on Vaulta from a Bitfinex account to the token's issuer account with the note "burn". Over the window that came to **421,293 LEO**, and the count checks out five separate ways: the issuer account's balance rose from **47.37M** to **47.80M LEO**, two independent chain-history nodes list the same 59 transfers, the paying account fell by the same amount, and iFinex's own supply figure dropped by exactly that much.

Two details matter. First, these coins are **parked, not destroyed**: the issuer account is a Bitfinex multisig that could send them out again. They leave the circulating count all the same, which is why they count here. Second, the moves are lumpy. They ran at about 7,100 LEO a day, then stopped after **Sep 1 2026**, while buying carried on: **144,153 LEO** bought since then is still waiting to be moved. Past pauses ended with one large catch-up transfer. The buyback is set in dollars, so the forward figure takes the last 90 days' spend of about **$5.35M** at today's price of about $9.02: roughly **592,632 LEO** over the next 90 days. The waiting backlog is not added on top, because no date is set for it.

Protocol fee burn is **0 LEO**. Nothing is destroyed: supply on both chains stayed flat, no coins went to a dead address, and the Vaulta contract's retire function was not used. Foundation buy is **0 LEO**: iFinex has promised to spend at least 80% of any money recovered from the 2016 hack on buying LEO back, but that bitcoin is still held by the US government while a court works through competing claims. New long-term lock is **0 LEO**: LEO has no staking, and the fee discounts for holding it leave the coins in holders' own wallets.

## Foundation and overhang

The one team balance outside the circulating count is the Vaulta issuer account, holding **47.80M LEO** — every coin the buyback has parked. Not one coin has left it since at least March 2023. Three more Bitfinex balances are large but already inside the circulating count: an Ethereum multisig with **648M LEO**, unmoved across the window; a Vaulta cold account with **257.79M LEO**, untouched since Sep 15 2025; and the account that pays for the buyback, down to **2.06M LEO** after sending 421,293 this window. We read all four on chain at each rebuild. If the issuer account's balance ever falls between rebuilds, those coins return to the market and enter the foundation row at the next rebuild; a move by the other three changes nothing unless it reaches the issuer account.

## How LEO compares to other exchange tokens

Exchange tokens usually shrink by buying coins back with exchange profits. The difference is where the coins end up. BNB, the best-known case, destroys its coins in a scheduled quarterly burn and burns part of every gas fee on its chain, so its supply figure on chain actually falls. LEO's bought coins sit in an account its issuer controls, so its on-chain supply never changes and the shrink shows only in the circulating count. For a holder the effect today is the same — fewer coins trade — but a parked coin can come back, and a destroyed one cannot.

LEO also differs in size and pace. Its buyback is tied to iFinex revenue rather than a set rule based on price or blocks, and at about $5.35M a quarter it removes only around **0.05%** of supply every 90 days. Unlike most exchange tokens, LEO also carries a large, unusual option: a court decision returning the hack bitcoin could fund buying worth many years of the normal programme. That is a buyer waiting on a judge, not a schedule — so we leave it at zero until a date exists.

## What to watch in the next 90 days

First, the paused moves: if the **144,153 LEO** backlog lands in the issuer account in one catch-up, the next 90 days take out more than the forward figure. Second, the court process over the **94,643 BTC** seized after the 2016 hack — any ruling that returns it to Bitfinex would start the recovery buyback. Third, the buyback's paying account is down to **2.06M LEO**; how it is refilled, and from which wallet, is worth watching. Fourth, any outflow from the issuer account's **47.80M LEO** would turn parked coins back into supply. No dated supply event is scheduled between Sep 29 2026 and Dec 28 2026.

## Summary

UNUS SED LEO adds no new coins: there is no emission, no vesting and no unlock, and supply on its Ethereum and Vaulta tokens did not change in 90 days. The iFinex buyback removed **421,293 LEO** from the circulating count, a net **−0.05%**, and about **592,632 LEO** (**−0.06%**) is expected next. The key risk is that those coins are parked in an issuer account rather than destroyed, and both token contracts can still create more. The big upside lever — a buyback funded by recovered hack bitcoin — waits on a court, with no date.

*MrNasdog Pressure Framework analysis of LEO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*
