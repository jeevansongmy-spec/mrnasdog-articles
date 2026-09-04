---
title: "CAKE Inflation Analysis · September 2026 · Supply shrinking, projected to keep shrinking"
description: "PancakeSwap destroys more than 3x the CAKE that reaches the market: 1.96M emitted against 7.04M burned per 90 days. Framework -1.58% net, monitor -1.88%."
canonical_url: "https://mrnasdog.com/research/cake/inflation"
tags: ["crypto", "cake", "pancakeswap", "defi"]
published: true
---

> Originally published at **[mrnasdog.com/research/cake/inflation](https://mrnasdog.com/research/cake/inflation)** by MrNasdog.

# CAKE Inflation Analysis · September 2026 · Supply shrinking, projected to keep shrinking

PancakeSwap destroyed **7.04M CAKE** over the last 90 days and paid out only **1.96M** — a net **−1.58%** against **−1.88%** from our supply monitor, a gap of **0.30 percentage points** and no warning chip. CAKE is **deflationary by revenue**: the burn is funded by trading fees rather than by a schedule, and PancakeSwap was fair-launched with no premine, so the sell side of the ledger has no vesting row at all. The **400M** ceiling, cut from 450M in **January 2026**, is an accounting promise rather than a line of code.

## The verdict, in one paragraph

For the 90-day window ending **Sep 4 2026**, the MrNasdog Pressure Framework reads **CAKE at −1.58% net**, with **−1.37%** projected over the next 90 days. Our supply monitor reads **−1.88%** for the same trailing window — a gap of **0.30 percentage points**, comfortably inside the framework's half-point tolerance, so no **⚠ monitor gap** chip is attached to the CAKE overview page. Getting to that number took an unusual amount of care, because PancakeSwap's raw on-chain figures are a trap. The CAKE supply number only ever rises, and it rose **767M** inside this window alone, while the burn address took in **772M** over exactly the same period. Neither figure is the ledger. PancakeSwap's farm contract still mints at its original **40 CAKE** a block and destroys **99.72%** of it in the same step, so almost all of that traffic is a wash that never touches a holder. Strip it out and the real flows are small, clean and firmly one-way. CAKE is **deflationary by structural buyback**.

## Sell pressure: where new CAKE comes from

Sell #1 — protocol inflation — is **1.96M CAKE**, and it is the only place new PancakeSwap supply reaches a holder. The rate is set on-chain and was read at both ends of the window without moving: the farm contract pays **0.1133 CAKE** a block to farms, syrup pools, position-manager vaults and ecosystem grants, which across the **17,270,731** blocks BNB Chain actually produced in this window works out to **21,740 CAKE** a day. PancakeSwap's own monthly burn reports use the same stated method and give between **21,676** and **22,477** a day across April, May and June 2026 — independent agreement to within a few tenths of a percent. Counting the blocks matters more than it sounds: BNB Chain ran at **0.4502 seconds** a block over this window, so assuming a nominal block time instead of counting would have understated PancakeSwap's emission badly.

Sell #2 — vesting unlocks — is **zero**, and it is zero by construction rather than quiet this quarter. PancakeSwap was fair-launched in **September 2020** with no presale, no venture round and no team premine; there is no vesting contract anywhere in the CAKE design, so no cliff can land in this window or any future one. Very few tokens in this catalogue can say that. Sell #4 — long-term locked or bankruptcy — is also **zero**: no estate, trustee or court-administered pool holds CAKE, and none has ever been created.

Sell #3 — foundation and unscheduled unlocks — books **zero** because there is no team-held CAKE allocation to release and no treasury outflow was observed inside the window. The row still carries the scope, and the scope is not empty. PancakeSwap retired its vote-escrow lock on **Apr 23 2025** and closed redemption on **Oct 23 2025**, but the contract is not empty: it held **5.92M CAKE** at the start of this window and **5.25M** at the end, while the retired staking pool moved from **13.48M** to **13.44M**. Together they released **703,853 CAKE** back into liquid hands. We read those balances at five points across the window and re-read them on a second independent node, and we do not book them as sell pressure — unlocking a coin that already exists is a reclassification, not new supply, and over the same window the counted supply fell further than the chain supply did, which is the opposite of what a release of previously-uncounted CAKE would produce.

## Buy pressure: where new CAKE goes

Buy #1 — programmatic buyback — is the engine, at **6.34M CAKE**. PancakeSwap routes between **15%** and **23%** of spot trading fees and **20%** of perpetual trading profits into CAKE bought on the open market, and every repurchased coin goes straight to the burn address rather than into a treasury. There is no accumulation wallet to watch, which is unusual and, for a holder, better: the buyback cannot quietly become an overhang. Because it is funded by real volume rather than by a schedule, it rises and falls with trading — this is the whole reason CAKE's deflation is a revenue story rather than a tokenomics story.

Buy #2 — protocol fee burn — adds **0.70M CAKE**, about a tenth of the total destroyed. Prediction, lottery, NFT market, profile, domain and launchpad fees are paid in CAKE and burned directly, with no market purchase in between. That leg is being retired: a governance vote that closed **Jun 21 2026** with **99.57%** support redirects every side-product fee stream to the PancakeSwap treasury instead of the burn, leaving the AMM buyback engine untouched. Our forward column therefore drops Buy #2 to zero, which is why the projection softens from **−1.58%** to **−1.37%**. Buy #3 — foundation buy — is **zero**, because no separate entity buys CAKE on a published timetable outside the burn engine. Buy #4 — new long-term lock — is **zero** as well: term locking was retired in April 2025 and nothing replaced it, so no CAKE can be newly locked at all.

The two buy rows together total **7.04M CAKE**, and that figure is measured rather than quoted. It closes exactly against the chain: emission of **1,956,642** minus a burn of **7,041,180** equals the **−5,084,538** move we measured in the real CAKE supply between the two ends of the window, to the unit. PancakeSwap's own published monthly burns — **2,751,901** for April 2026, **2,632,830** for May and **2,402,150** for June — imply about **7.0M** a quarter on the same trend, within one percent of the measurement.

## Foundation and overhang

Three overhangs are tracked on CAKE and all three are small or shrinking. The first is room under the ceiling: PancakeSwap holds no reserve wallet, but the token's mint function is live and uncapped, and the **400M** ceiling is a governance commitment rather than a contract check — **67.55M CAKE** of headroom sits above today's **332.45M** total. That is the honest way to state CAKE's supply risk, and it is also why no row on the CAKE overview page carries a permanent tag. The second and third are the retired vote-escrow contract at **5.25M CAKE** and the legacy staking pool at **13.44M**, both of which are unwinding rather than filling; we re-read both every rebuild. If either of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh — and if the buyback ever stopped sending its purchases to the burn address, that destination would become a fourth overhang the same day.

## How CAKE compares to other exchange tokens

CAKE belongs to the class of exchange tokens that buy their own supply back with trading revenue, and the useful comparison is mechanical rather than about price. Against a centralised exchange token running a quarterly auto-burn, CAKE burns continuously and in public: every purchase is a market order on PancakeSwap itself, so the demand is verifiable on-chain rather than announced after the fact. The trade-off is volatility — a quarterly burn based on profit is smoothed, while CAKE's burn tracks weekly trading volume and can swing by a third from one week to the next.

Against a fee-burn chain — the base-fee model where every transaction destroys a slice of the native asset — CAKE is closer in spirit than it looks, but the burn is funded by an application's revenue rather than by block space, so it scales with PancakeSwap's market share instead of with the underlying chain's. And against the more common decentralised-exchange token, the difference is stark: most of them still emit far more than they retire, and most carry a vesting calendar that CAKE simply does not have. PancakeSwap's emission has been cut repeatedly — from roughly **40,000** CAKE a day under the old model to about **21,740** today — and the ceiling has been cut once, from **450M** to **400M** in January 2026. The result is a token whose supply has now fallen for **34** consecutive months.

## What to watch in the next 90 days

First, whether the side-product fee redirect approved on **Jun 21 2026** is actually implemented — the vote authorises it but does not schedule it, and the July and August burn reports are the place it will show. Second, the monthly CAKE burn report, published in the first week of each month; a print materially below **2.3M CAKE** would mean trading revenue, not policy, is softening. Third, any further treasury proposal on the PancakeSwap governance space: the June vote moved a small stream, but it established that burn revenue can be redirected, and a larger redirect would change this page's verdict. Fourth, the vote-escrow contract balance — it released **670,882 CAKE** in this window, more than half of it in the last two weeks, so the drain is accelerating rather than fading. Fifth, the **400M** ceiling itself, which governance has already shown it is willing to move.

## Summary

PancakeSwap's CAKE is one of the few tokens in this catalogue whose supply genuinely shrinks, and it shrinks for a structural reason: **7.04M CAKE** destroyed in 90 days against **1.96M** emitted, a net of **−1.58%**, with **−1.37%** projected. The mechanism is a revenue-funded open-market buyback that sends every coin it buys to the burn address, backed by a fair-launched token with no vesting, no premine and no investor cliff to absorb. The key risk is not dilution but dependence: the burn is funded by trading volume, so a quiet quarter shrinks it directly, and the **400M** ceiling that caps the downside is a governance promise rather than a contract constraint — the mint function is live, uncapped and owned by the farm contract. Watch revenue and watch the governance space; the emission side has been settled for years.

---

*MrNasdog Pressure Framework analysis of CAKE, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 5 2026.*
