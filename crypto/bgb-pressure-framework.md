---
title: "BGB Inflation Analysis · August 2026 · Mixed flows, supply roughly steady"
description: "Bitget burned 3.01M BGB for Q2 2026 — from a non-circulating reserve the float excludes. The MrNasdog Pressure Framework reads BGB at 0.00% net on 699.99M tradable — flat."
canonical_url: "https://mrnasdog.com/research/bgb/inflation"
tags: ["crypto", "bgb", "bitget", "exchange-token"]
published: true
---

> Originally published at **[mrnasdog.com/research/bgb/inflation](https://mrnasdog.com/research/bgb/inflation)** by MrNasdog.

Bitget burned **3,010,400 BGB** for the Q2 2026 window, announced **Jul 15 2026**, and yet the MrNasdog Pressure Framework reads BGB at **0.00%** net supply over the last 90 days — flat, not deflationary. The reason is where the burned BGB came from: a non-circulating Morph Foundation reserve of about **210.93M BGB** that the tradable count already excludes. Sell pressure was **zero** — Bitget Token has no mint function — buy pressure on the float was **zero**, and the tradable supply of **699.99M BGB** held steady near 700M through the burn. Our supply monitor reads **−0.54%**, a gap of **0.54 percentage points** that is derivation drift around a flat float, not a real shrink. BGB is a **fixed-supply exchange token whose burn shrinks the ceiling rather than the float**.

## The verdict, in one paragraph

For the 90-day window from **May 5 2026** to **Aug 3 2026**, the framework reads **BGB at 0.00% net**: sell pressure of **zero** against buy pressure of **zero** on a tradable base of **699.99M BGB**. Our supply monitor reads **−0.54%** for the same period, a gap of **0.54 percentage points**, just past the framework's half-point tolerance, so the page ships with a data-conflict flag. That gap is not a disagreement about Bitget Token's supply — it is measurement noise. The monitor's own supply reading bounced between **698M** and **702M** across the window with no downward trend — **701.9M** on **Jun 9 2026**, **698.1M** on **Aug 3 2026** — which is a flat float plus rounding, not a real reduction. The one genuine supply event, the **3.01M BGB** burn, was funded from the reserve and never touched the tradable market. BGB is best labelled a **reserve-funded burn: permanently deflationary in total supply, flat in tradable supply**.

## Sell pressure: where new BGB comes from

Sell #1 — protocol inflation — is **zero**, and unlike most tokens in this framework that is a hard structural zero. Bitget Token has no mint function: there is no chain paying validators in BGB, no staking curve that issues new BGB, and no inflation rule anywhere in its design. The token was distributed from a fixed allocation, originally capped at **2,000,000,000**, and every BGB that will ever exist already exists.

Sell #2 — vesting unlocks — is **zero** on realised flow. Bitget Token's allocation table does vest on paper into **2029**, but this framework measures supply that actually reaches the market, and the tradable float did not rise — it held near **700M** all window while the scheduled portions stayed inside Foundation and reserve wallets, unclaimed and untradable. Aggregators themselves report no scheduled unlock in the next 90 days. Sell #3 — Foundation and unscheduled unlocks — is **zero** on observed behaviour, with two overhangs enumerated below. Sell #4 — long-term locked or bankruptcy — is **zero**: Bitget is a going concern.

## Buy pressure: where new BGB goes

Buy #2 — protocol fee burn — is the mechanism BGB is famous for, and it reads **zero on the float**, which needs explaining because the burn is completely real. Bitget runs a quarterly burn whose size is now tied to on-chain gas usage, and the Q2 2026 burn retired **3,010,400 BGB**, announced **Jul 15 2026**. The catch is the funding source: the burned BGB was pulled from the non-circulating Morph Foundation reserve, not bought off the market. So when the burn fires, total supply falls — from around **910.92M** — and the reserve falls by the identical amount, while the tradable float does not change. Booking a 3.01M burn as absorbed float would have printed a **−0.43%** reading no BGB holder experienced.

Buy #1 — programmatic buyback — is **zero** for a related reason: the current mechanism is a reserve burn, not an open-market buyback. There is no disclosed or observable purchase of BGB off the market this window, and no Bitget address shows a position building. Buy #3 — Foundation buy — is **zero**. Buy #4 — new long-term lock — is **zero**: Bitget's earn and staking products pay out of existing pools, and no new lockup was created.

## Foundation and overhang

Bitget Token carries two identified overhangs, both read on-chain. The first is the Morph Foundation reserve, holding about **210.93M BGB** — the gap between the **910.92M** total supply and the **699.99M** tradable float — the wallet the quarterly burn eats. Press reporting puts the amount already destroyed at around **220M BGB**, with a stated long-term goal of grinding total supply down to **100M**. The reserve sits outside the counted market, and its only outflow goes into the burn address. The second overhang matters more: a Bitget corporate wallet holding about **227.6M BGB** that sits **inside** the counted float already — it needs no unlock, no vote and no announcement to reach the market. This window it showed only an internal routing hop, not a distribution. If either balance falls toward the open market between refreshes, the outflow enters Sell #3 at the next refresh, and on the corporate wallet that would be the largest single supply event this ledger could record.

## How BGB compares to other exchange tokens

The peer group is exchange tokens with quarterly burn programmes, and structurally BGB sits at the more conservative end. The classic exchange-token burn is revenue-funded end to end — the venue takes a slice of profit, buys the token on the open market, and destroys what it bought — so the burn is simultaneously a bid and a supply cut, and both halves land on the tradable float. Bitget's realised burn is reserve-funded: the tokens are already in the Foundation's hands, so there is a total-supply cut but no verifiable market bid. That makes BGB's burn genuine in accounting terms and inert in market terms, which is why a token that destroys millions every quarter still reads flat rather than deflationary here.

That places BGB alongside the other exchange tokens whose burns eat an excluded allocation rather than the market, and away from the fee-burn chains where every burned unit comes out of a circulating balance and the float genuinely shrinks. BGB also has no live issuance at all — no consensus rewards, no emission curve — so unlike an uncapped L1 it cannot dilute holders even slightly. So Bitget Token is neither a deflation story on the tradable float nor an inflation risk: a fixed-supply token with a large, real, off-market burn.

## What to watch in the next 90 days

First, the **Q3 2026** quarterly burn, expected around **mid-Oct 2026** — the number to check is not the size but the funding wallet, because a burn paid from anywhere other than the Foundation reserve would turn Buy #2 non-zero immediately. Second, that reserve's remaining **210.93M BGB** and the pace toward the stated **100M** total-supply target. Third, the Bitget corporate wallet holding **227.6M BGB** inside the float, which needs no unlock to sell. Fourth, any change to the burn formula, now tied to Bitget Wallet gas usage. Fifth, any sign that a paper vesting tranche from the **2029** schedule actually reaches the float.

## Summary

The MrNasdog Pressure Framework reads Bitget's BGB at **0.00%** net supply change over the last 90 days and projects the same for the next 90 — flat, not deflationary. BGB has no mint function and had no realised unlock this window, so sell pressure is a hard zero; and while the quarterly burn is genuine — **3,010,400 BGB** retired for Q2 2026 — it is drawn from a non-circulating Morph Foundation reserve, so total supply falls while the tradable float holds near **700M**. The key thing to watch is not inflation, which is absent, but a Bitget corporate wallet holding **227.6M BGB** already inside the counted float — it needs no unlock to sell, and it, not the burn, is where BGB's real supply risk sits.

*MrNasdog Pressure Framework analysis of BGB, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 3 2026.*
