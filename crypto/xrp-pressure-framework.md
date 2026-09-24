---
title: "XRP Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description: "XRP mints nothing, yet supply grows +1.29% net over 90 days: Ripple's wallets paid 813M XRP into the market while the fee burn removed only 32,954 XRP."
canonical_url: "https://mrnasdog.com/research/xrp/inflation"
tags: ["crypto", "xrp", "ripple", "escrow"]
published: true
---

Originally published at [https://mrnasdog.com/research/xrp/inflation](https://mrnasdog.com/research/xrp/inflation) by MrNasdog.

# XRP Inflation Analysis · September 2026 · Supply growing, projected to keep growing

XRP, the native coin of the XRP Ledger, is never minted — all 100B XRP were created when the ledger started — yet XRP supply on the market still grows, because Ripple pays coins out of its own wallets. Over the last 90 days Ripple's escrow released **3.0B XRP**, Ripple locked **2.1B** straight back, and Ripple's wallets paid **813M XRP** into the market, against only **32,954 XRP** destroyed by the transaction-fee burn. The MrNasdog Pressure Framework therefore reads XRP at **+1.29% net** over 90 days against a supply-monitor reading of **+1.16%**, a gap of **0.13 percentage points**. XRP is capped at 100B, but **31.70B XRP** still sits in escrow waiting to be released.

## The verdict, in one paragraph

For the 90-day window ending **Sep 24 2026**, the Pressure Framework reads **XRP at +1.29% net**: the sell side added **813.02M XRP** to the circulating float, all of it paid out by Ripple, and the buy side removed **32,954 XRP** through the fee burn. The independent supply monitor reads the realised 90-day change at **+1.16%**. The gap is **0.13 percentage points**, inside the framework's half-point tolerance, so XRP ships with **no data-conflict flag**. The forward column also reads **+1.29%**, because Ripple's payout pace has held steady and three more XRP escrow releases fall inside the next 90 days. The label for XRP is **inflationary by company distribution**: a fixed-supply coin whose float grows as its issuer releases its own treasury, not because the protocol mints anything.

## Sell pressure: where new XRP comes from

Sell #1, protocol inflation, is **zero**. The XRP Ledger has no block reward and no staking payout; validators earn nothing in XRP, and no transaction type can create a new coin. That was read rather than assumed: the ledger's own supply count fell from **99,985,643,219 XRP** to **99,985,610,265 XRP** across the window, on three separate public servers, and rose at no point. Since the ledger started, about **14.39M XRP** has been destroyed this way and none created.

Sell #2, vesting unlocks, is where the XRP escrow lives, and it books **zero** for a reason that matters. Ripple's escrow is readable on the ledger. It held **32.60B XRP** at the start of the window and **31.70B XRP** at the end. In between, three monthly releases on **Jul 1**, **Aug 1** and **Sep 1 2026** freed **3.0B XRP**, and Ripple locked **2.1B** of it straight back into new escrows — **700M** each month. The other **900M XRP** moved into Ripple's own wallets. Those wallets are not counted as circulating, so an escrow release that stops there has not reached the market yet. The framework counts each XRP once, at the moment it enters the float.

That moment is Sell #3, foundation and unscheduled unlocks, at **813.02M XRP**. Reading every Ripple wallet with a public label at both ends of the window, the combined balance of those wallets plus the escrow fell by **813.02M XRP**. A full sweep of their transactions gives the same answer: **816M XRP** paid out to outside accounts and **3M** taken back, nearly all from one operating wallet that pays out almost every day — **352M** in July, **259M** in August and **173M** in the first 24 days of September. Ripple's own published count of distributed XRP rose at the same pace, about **9M XRP** a day. Sell #4, long-term locked or bankruptcy supply, is **zero**: no estate or trustee is releasing XRP, and the listed companies and funds that hold XRP took coins that were already in the float.

## Buy pressure: where new XRP goes

The XRP buy side has one working row. Buy #2, the protocol fee burn, removed **32,954 XRP** over the window, about **366 XRP** a day. Every XRP Ledger transaction pays a tiny fee in XRP, and the ledger destroys that fee instead of paying it to anyone, so there is no burn address to read — the ledger's supply count falling is the burn itself. The fee is kept very small on purpose, to stop spam rather than to earn money, so the XRP burn stays small even with the ledger busy. Against Ripple's **813M XRP** of payouts it cancels about one coin in every **25,000**.

Buy #1, programmatic buyback, is **zero**: Ripple has no programme that buys XRP on the market. Buy #3, foundation buying, is **zero**: Ripple's wallets took in only **3M XRP** from outside accounts this window, and nothing shows XRP being bought. Buy #4, new long-term locks, is also **zero**, and this is the second place where the escrow could be misread. The **2.1B XRP** Ripple locked back into escrow never left Ripple's hands, so locking it takes nothing off the market. Booking it as a buy would invent 2.1B of buying and, next to it, 3.0B of selling that never reached anyone. The XRP Ledger also has no staking, so no supply is tied up securing the chain.

## Foundation and overhang

Ripple is the whole XRP overhang, and it has two parts. The first is the escrow: **31.70B XRP**, split into monthly lots of up to **1B** that run until May 2029. The ledger itself enforces the dates, so Ripple cannot release more than the schedule allows, but it can re-lock as much as it likes, and it has been re-locking 700M a month. The second is Ripple's own wallets outside escrow: **3.65B XRP** in wallets that carry a public label, plus roughly **1.5B XRP** more that is also kept out of the circulating count. Adding escrow, labelled wallets and that remainder reproduces the gap between total and circulating XRP. All of it is read from the ledger on every refresh. The 900M that moved from escrow into those wallets this window sits among them now. If any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How XRP compares to other payment and Layer-1 chains

Most proof-of-stake Layer-1s grow their supply by minting new coins for stakers every block, and they rely on a fee burn to offset part of it. XRP works the other way round. Its protocol mints nothing and burns every fee, so on the protocol side alone the XRP supply can only fall. The growth comes entirely from outside the protocol: a company that was given most of the supply at the start, and pays it out over time. That makes the XRP sell side a question about Ripple's decisions, not about code. A proof-of-work coin with a hard cap sits in between — it also has a fixed ceiling, but its new coins go to miners by a fixed rule, not to one issuer by choice.

Against other chains whose supply was created up front and handed out by a founding organisation, the XRP difference is the on-ledger escrow. The monthly XRP release is public and enforced by the ledger, so anyone can see what Ripple could release and what it actually did. The trade-off is plain: the escrow caps the pace, but Ripple chooses how much of each month to keep, and this window it kept 70% and paid out a steady amount. The fee side stays small by design — about **$195,000** a year of fees against a market value near **$91.6B** — so the XRP burn will not offset the payouts at any realistic level of activity. What moves the XRP reading is how much Ripple sends out.

## What to watch in the next 90 days

First, the XRP escrow releases on **Oct 1**, **Nov 1** and **Dec 1 2026**, each up to **1B XRP**: the forward reading assumes Ripple keeps re-locking most of each one, and a month that re-locks less would add to Ripple's wallets and, later, to the market. Second, the pace of Ripple's operating wallet: the forward column holds the trailing **813M XRP** per 90 days, and a sustained move above or below roughly **270M** a month would move the reading. Third, the Batch amendment, set to switch on around **Sep 29 2026** if validator support holds, which lets several transactions settle together but does not create or burn XRP. Fourth, Evernorth's shareholder vote on **Sep 30 2026**: the XRP Ripple put into it moved in October 2025, so the listing adds no new XRP to the float.

## Summary

The MrNasdog Pressure Framework reads XRP at **+1.29% net** over the trailing 90 days and **+1.29%** over the next 90. The XRP protocol mints nothing and burns every fee, but Ripple paid **813M XRP** from its own wallets into the market over the window, while the fee burn removed only **32,954 XRP**. The key risk is that the XRP sell side is a company decision: Ripple re-locked 70% of each monthly escrow release this window and could keep less. The ceiling is fixed at 100B XRP, but **31.70B XRP** remains in escrow and about **5.1B** more sits in Ripple's wallets, so there is plenty left to release.

*MrNasdog Pressure Framework analysis of XRP, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 24 2026.*
