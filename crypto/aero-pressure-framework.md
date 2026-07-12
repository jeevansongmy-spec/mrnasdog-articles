---
title: "AERO Inflation Analysis · July 2026 · Structurally inflationary on ve(3,3) gauge emission, with no buyback to offset"
description: "A MrNasdog Pressure Framework read of Aerodrome (AERO): ~52.3M/90d of ve(3,3) gauge emission to the float vs ~13.1M new veAERO locks, no buyback and no burn. Framework +4.1% net; monitor +4.76%."
canonical_url: "https://mrnasdog.com/research/aero/inflation"
tags: ["crypto", "aero", "aerodrome", "base"]
published: true
---

> Originally published at **[mrnasdog.com/research/aero/inflation](https://mrnasdog.com/research/aero/inflation)** by MrNasdog.

Aerodrome (AERO) is an **uncapped ve(3,3) DEX token** on Base: new AERO is minted every weekly epoch straight to liquidity gauges. At the current Aero Fed tail rate that is about **4.07M AERO an epoch**, or roughly **52.3M** reaching the float over 90 days. There is **no buyback and no burn** — 100% of trading fees go to veAERO voters — so the only offset is holders locking about **13.1M AERO** into vote-escrow. The framework nets that to about **+4.1%** supply growth; our supply monitor reads the trailing 90 days at **+4.76%**. AERO is inflationary today and projected to keep growing.

## The verdict, in one paragraph

For the window opening Jul 13 2026, the MrNasdog Pressure Framework reads **AERO at about +4.1% net** supply growth over the next 90 days — roughly **52.3M AERO** of weekly gauge emission against about **13.1M** of new veAERO locks. Our supply monitor reads the realized last-90-day change at **+4.76%**, a gap of about **0.7 percentage points** that ships a **⚠ monitor-gap chip**. That gap is structural: the framework books the on-chain gauge emission net of on-chain vote-escrow locks and uses the current circulating base, while the monitor reads net circulating growth on a 90-day-ago base and counts some vote-locked and team AERO the framework holds as locked or non-selling. AERO is a **structurally inflationary ve(3,3) DEX token on Base** — the emission is the entire engine of new supply, and no buyback or burn stands against it.

## Sell pressure: where new AERO comes from

Sell #1 — protocol inflation — is the dominant and defining force, at about **52.3M AERO** over 90 days. Aerodrome mints new AERO every weekly epoch straight to its liquidity gauges, where veAERO voters direct it to the pools they back. The protocol has passed its take-off and cruise phases and now sits in the **Aero Fed tail**: the weekly emission is fixed at about **0.21% of total supply** per epoch, which on-chain is roughly **4.07M AERO an epoch**. Across the 13 epochs in a 90-day window that is about 52.3M AERO handed to liquidity providers — new, liquid supply that can be sold. On-chain, total AERO supply rose from **1.876B** to **1.936B** over the last 90 days, a gross mint of about **60M** once the veAERO rebase and team allocation are added on top of the gauge emission.

Sell #2 — vesting unlocks — is **zero** inside the window: there is no third-party investor or seed cliff. AERO's launch allocations — the airdrop to veVELO lockers, the team and ecosystem shares — were distributed as vote-locked veAERO and are already inside total supply, so on-chain supply rises smoothly with the emission and shows no cliff step. Sell #3 — Foundation and unscheduled unlocks — is also **zero** in booked value: the standing overhang is the vote-escrow lock of roughly **1.04B AERO** plus a small team allocation of about **0.16M** an epoch that mints to the team wallet and has not been seen selling, and the pending Aerodrome–Velodrome merger, which has no confirmed on-chain firing yet. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate applies to AERO.

## Buy pressure: where new AERO goes

The defining fact of AERO's buy side is that there is almost none. Buy #1 — programmatic buyback — is **zero**: in the ve(3,3) design, 100% of trading fees are routed to veAERO voters, so the protocol never buys AERO back off the market. Buy #2 — protocol fee burn — is **zero** for the same reason: fees are paid to voters, not sent to a burn address, so no AERO is destroyed on each trade. Buy #3 — Foundation buy — is **zero**, with no discretionary open-market buying observed. The only real offset is Buy #4 — new long-term lock — at about **13.1M AERO**. Holders keep locking AERO into 4-year-max vote-escrow to vote and earn: on-chain, the veAERO locked balance rose about **19M** over the last 90 days, and stripping out the roughly **5.9M** weekly rebase that is minted already-locked leaves about 13.1M of AERO that holders pulled off the float. That lock absorbs part of the gauge emission, but it does not reverse it.

## Foundation and overhang

AERO's team-controlled overhang is dominated by the **vote-escrow lock**: roughly **1.04B AERO** — more than half of total supply — sits locked as veAERO, and the weekly rebase mints fresh AERO straight to those lockers. Alongside it, the team allocation accrues at about **0.16M** an epoch (~2.1M over 90 days) to the team wallet, and the largest latent catalyst is the **Aerodrome–Velodrome merger** into Aero, which would issue new AERO to VELO holders — about 5.5% of the merged supply, mostly as locked veAERO — but has not yet hit the chain and carries no confirmed date. None of these has a dated market release inside the window, so the framework books no discretionary sell from them; they are surfaced as watched overhang and re-checked on a roughly bi-weekly walk. If any of these balances falls between refreshes through a real market sale, that outflow enters Sell #3 at the next refresh.

## How AERO compares to other ve(3,3) DEX tokens

AERO belongs to the class of **uncapped, continuous-emission ve(3,3) DEX tokens** — the Solidly lineage that includes its own sibling Velodrome on Optimism. Where a hard-capped token simply cannot dilute, a ve(3,3) token mints new supply to liquidity every epoch and returns 100% of fees to lockers rather than to the protocol. That makes AERO structurally closer to an inflationary proof-of-stake chain than to a fee-burning exchange token: the emission is a live variable, and the vote-escrow lock is what keeps a large share of supply off the float. Aerodrome's Aero Fed refinement lets veAERO voters nudge the emission rate, but at the tail it is still fixed near 0.21% of supply an epoch, so the dilution does not stop on its own.

The sharper contrast is with exchange tokens that run quarterly buy-and-burns and with revenue-burning DeFi tokens: those destroy supply outright and can read as clean deflation, because the protocol takes fees as its own revenue and spends them buying the token back. Aerodrome deliberately does the opposite — it gives every fee to veAERO voters, which is excellent for lockers but means **nothing on the protocol side is buying AERO back**. So while a capped fee-burn token can offset or reverse its issuance, AERO's only counterweight is voluntary vote-escrow locking. That is why AERO reads inflationary even though it is one of the most productive fee-generating DEXs in DeFi: the fees never touch the token's supply.

## What to watch in the next 90 days

The single biggest item is the **Aerodrome–Velodrome merger into Aero**, expected around Q3 2026: it would issue new AERO to VELO holders worth about 5.5% of the merged supply, and although most is expected to arrive as locked veAERO, the exact liquid share and date are unconfirmed — this is the event most likely to move the reading. Watch the **Aero Fed emission votes**, since veAERO voters can raise or cut the weekly rate by 0.01% of supply an epoch. Watch the **veAERO lock ratio** — currently over half of supply — because a falling lock rate would push more emission onto the float. Watch the **predictive-allocation upgrade** Aerodrome flagged for July 2026, which changes how emissions are directed. And expect the framework to keep reading below our supply monitor while vote-locked and team AERO sit in the monitor's circulating base.

## Summary

AERO is an uncapped ve(3,3) DEX token on Base that mints roughly 52.3M new AERO to liquidity gauges over 90 days, about 4.07M an epoch at the Aero Fed tail rate. There is no buyback and no burn — 100% of trading fees go to veAERO voters — so the only offset is holders locking about 13.1M AERO into vote-escrow, leaving the framework at about +4.1% net supply growth. Our supply monitor reads +4.76% over the trailing 90 days, the extra coming mostly from base convention and vote-locked or team AERO in the monitor's circulating base. AERO is structurally inflationary and projected to keep growing, with the pending Aero merger the one catalyst that could reshape its supply.

---

*MrNasdog Pressure Framework analysis of Aerodrome (AERO), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 13, 2026.*
