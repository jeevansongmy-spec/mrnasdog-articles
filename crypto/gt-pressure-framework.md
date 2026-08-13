---
title: "GT Inflation Analysis · August 2026 · Mixed flows, supply roughly steady"
description: "Gate burned 189.9M GT — 63% of supply — yet the MrNasdog Pressure Framework reads GT at +0.09% net on a 106.591M float, because every burn is funded from a frozen reserve the circulating count already excludes."
canonical_url: "https://mrnasdog.com/research/gt/inflation"
tags: ["crypto", "gt", "gate", "exchange-token"]
published: true
---

> Originally published at **[mrnasdog.com/research/gt/inflation](https://mrnasdog.com/research/gt/inflation)** by MrNasdog.

Gate has destroyed **189.9M GT** — about **63%** of GateToken's original 300M genesis supply — and the burn is entirely real, most recently **2,570,063 GT** on **Jul 4 2026**. It is also, for pricing purposes, invisible: every GT burned comes out of a frozen Gate reserve wallet whose balance equals the entire non-circulating bucket, so total supply falls while the tradable float does not move. GateChain, meanwhile, is not fixed-supply at all — it issues roughly **0.10M** new GT every 90 days as consensus-node rewards. The MrNasdog Pressure Framework therefore reads GT at **+0.09%** net supply growth per 90 days, not deflation.

## The verdict, in one paragraph

Across the 90 days to **Aug 13 2026**, the framework books **0.10M GT** of sell pressure and **zero** buy pressure against a circulating float of **106.591M GT**, giving net supply growth of **+0.09%**. The inflation monitor reads **+0.71%** over the same window, a gap of **0.61 percentage points** — above the framework's 0.5pp tolerance, so a **⚠ monitor gap** chip ships on the GT overview page. The deep walk traced the difference to the monitor's 90-day base date landing on **May 15 2026**, a single-day 604,517 GT dip below the surrounding level; measured median-to-median across the window, the tradable count drifted just **127,547 GT**. Both readings agree on direction. GateToken is a **quietly inflating exchange token wearing a deflationary headline** — the burn shrinks the reserve, not the float.

## Sell pressure: where new GT comes from

Only one row on the GT ledger carries a number. **Protocol inflation** books **0.10M GT** per 90 days, and it exists because GateToken lives on two chains with two different supply rules. On Ethereum, the 2019 GT contract has minted exactly **300,000,000** tokens and has no mint function — that half of GT genuinely is fixed. GateChain, the proof-of-stake Layer 1 Gate operates, pays its consensus nodes in newly issued GT drawn from a **30M** reward allocation. Of that allocation, **8.75M GT** has been mined and **21.25M** remains unmined. At the published **0.99%** annualised consensus yield applied to the **40.31M GT** delegated across GateChain's validator set, issuance runs at roughly 0.399M GT a year, or 0.10M per 90 days. It is a small number, but it is the only mechanism on this page that adds GT, and it is why describing GateToken as fixed-supply is wrong.

The other three sell rows are zero for structural reasons. **Vesting unlocks** is zero because GT's full 300M was issued at genesis in 2019 and the Ethereum contract supply has not changed since; the vesting tracker shows no unlock round before **Aug 26 2030**, far outside any 90-day window. **Foundation and unscheduled unlocks** is zero because none of the three identified Gate wallets sent GT to a trading venue during the window — the reserve's only outflow is the burn itself. **Long-term locked or bankruptcy** is zero because Gate is an operating exchange with no estate, trustee schedule or creditor distribution releasing GT.

## Buy pressure: where new GT goes

The buy side is where GateToken's reputation and its arithmetic part company. **Programmatic buyback** books **zero** — not because the burn is fake, but because it does not consume market supply. Gate publishes a quarterly buyback-and-burn and the quanta are verifiable: **2,570,063 GT** reached the burn address on **Jul 4 2026**, following **2,557,729 GT** on **Apr 26 2026**, against a cumulative **189,947,219 GT** destroyed since 2019. Every hop of the July burn is readable on-chain, and it is a straight line: the GT left Gate's frozen reserve wallet, passed through the burn executor, and landed in the burn address on the same day, with no open-market purchase anywhere in the path. That reserve holds **12,251,232 GT**, a figure that matches the entire non-circulating bucket to within 49 tokens. Burning from it lowers GateToken's total supply and leaves the tradable float exactly where it was — which is precisely what the supply series shows, with no step across **Jul 4 2026** and a flat 106.4M–106.7M band for the whole window.

**Protocol fee burn** is zero: GateChain has no base-fee burn in the Ethereum sense, gas is paid to validators rather than destroyed, and GateChain fees are near-zero by design, so ordinary network use removes no GT. **Foundation buy** is zero, because no open-market GT purchase by Gate was disclosed or observed outside the burn programme, and that programme is reserve-funded. **New long-term lock** is zero, because no fresh lockup, escrow or staking-cap programme was announced in the window; GateChain's seven-day unbonding period is a withdrawal delay, not a supply lock.

## Foundation and overhang

Three Gate-controlled wallets are enumerated and refreshed on every rebuild. The **frozen burn reserve** holds **12.25M GT** and is the single most important address on this page: it funds every quarterly burn, it sits outside the circulating count, and at roughly 2.57M GT a quarter it has about **four to five quarters** of runway left. The **burn executor** holds **12.62M GT** and has historically forwarded only to the burn address. The **consolidated cold wallet** holds **52.40M GT**, was topped up in January 2026, and — unlike the other two — is counted inside the circulating float, which makes it the largest genuine overhang in GateToken's supply picture at roughly half the tradable count. None of the three moved GT to a trading venue in the window. If any of their balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How GT compares to other exchange tokens

Exchange tokens are usually sorted by whether the burn is revenue-linked, and by that test GateToken looks conventional: a fixed slice of Gate's trading profit funds a quarterly repurchase and burn, the same shape used across the sector. The mechanism-level distinction the framework cares about is different, and it splits the class in two. An exchange token whose burn buys tokens on the open market and then destroys them removes supply that traders actually hold — the float shrinks and the deflation is economically real. An exchange token that burns from an internal reserve already excluded from the circulating count destroys an accounting line, not a market position. GateToken sits firmly in the second group, and the on-chain funding path makes that unambiguous rather than a matter of interpretation.

The second difference is that GateToken carries an issuance side most exchange tokens do not. A pure exchange token has one supply lever — the burn. GateToken has two, because GateChain is a working proof-of-stake Layer 1 that must pay validators, and it pays them in new GT. That places GateToken structurally closer to an uncapped continuous-emission Layer 1 than to a burn-only exchange token, with the burn acting as an offset against issuance rather than as a one-way removal. The result is a token whose 63% cumulative burn is genuine, whose deflationary reputation is well earned in total-supply terms, and whose tradable supply nonetheless drifts slowly upward.

## What to watch in the next 90 days

The **Q3 2026 GateToken burn** is the main dated event, expected around **Oct 2026** on the roughly quarterly cadence of Jan 8, Apr 26 and Jul 4 2026; the number to check is not the quantum but the funding wallet. The **frozen reserve balance** matters more than the burn itself — once it empties, Gate must either fund burns from the open market, which would make them genuinely float-shrinking, or stop, and either outcome moves this page materially. The **consolidated cold wallet** holding 52.40M GT is worth watching for any first outflow, because it already sits inside the circulating count. On the issuance side, the **21.25M unmined consensus allocation** and the delegated-stake total set the pace of new GT, and a rise in either lifts the sell row. Finally, any Gate announcement revising the burn formula or its funding source would change the structural reading rather than just the numbers.

## Summary

The MrNasdog Pressure Framework reads Gate (GT) at **+0.09%** net supply growth per 90 days — mixed flows, supply roughly steady. GateToken's headline is one of the strongest in crypto, with **189.9M** of an original 300M supply permanently destroyed, but the burn is funded from a frozen reserve wallet the circulating count already excludes, so it lowers total supply without shrinking the tradable float. The genuine supply movement is in the other direction: GateChain issues about **0.10M** new GT every 90 days to its consensus nodes out of a 21.25M unmined allocation. The key risk is concentration rather than issuance — a single Gate-controlled cold wallet holds **52.40M GT** inside the float, roughly half of it. The ceiling that matters is the reserve: at roughly 2.57M GT a quarter, its **12.25M** balance funds about four to five more burns before the mechanism has to start touching supply that counts.

---

*MrNasdog Pressure Framework analysis of GT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 13 2026.*
