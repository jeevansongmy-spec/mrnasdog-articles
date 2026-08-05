---
title:         "WLD Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description:   "All 10B WLD were pre-minted, so World's only inflation is a daily unlock — ~245.8M WLD last 90 days, cut 43% on Jul 24 2026. Framework reads +6.87% net, monitor +7.48%, easing to +5.45%."
canonical_url: "https://mrnasdog.com/research/wld/inflation"
tags:          ["crypto", "wld", "world", "tokenomics"]
published:     true
---

> Originally published at **[mrnasdog.com/research/wld/inflation](https://mrnasdog.com/research/wld/inflation)** by MrNasdog.

# WLD Inflation Analysis · August 2026 · Supply growing, projected to keep growing

World is the heaviest unlocker in our coverage, and the unusual part is that its contract **cannot mint a single new token**. WLD is hard-capped at **10 billion**, all pre-minted at launch, so every bit of supply pressure is the daily linear unlock of tokens that already exist. Over the last 90 days about **246M WLD** reached the market — roughly **163.8M** of team and investor vesting plus **82M** of community grants that verified users actually claimed. There is **no buyback and no burn** to offset it. The framework reads **+6.87% net** against a supply monitor at **+7.48%**, a **0.61-point** gap that is purely a denominator difference. The aggregate unlock rate was cut **43%** on **Jul 24 2026**, easing the forward reading to **+5.45%**.

## The verdict, in one paragraph

For the 90-day window ending **Aug 5 2026**, the Pressure Framework reads **WLD at +6.87% net**. Sell pressure is **245.8M WLD**, buy pressure is **zero**, against a circulating base of **3.58B WLD**. Our supply monitor reads **+7.48%**, so a monitor-gap note ships on the WLD overview — and the deep walk explains it cleanly. Both readings agree on the numerator: about **246M WLD** reached the market this window. The difference is the base each divides by. The monitor divides that flow by the smaller float of **May 7 2026** — around **3.33B** — while the framework divides by today's larger **3.58B**. On-chain total supply is a fixed **10B** and did not move, so this is not a disagreement about how much unlocked, only about the denominator. World is best characterised as **structurally inflationary by scheduled unlock, with nothing on the buy side to slow it**.

## Sell pressure: where new WLD comes from

Sell #1, protocol inflation, is **zero** — and this is the defining feature of WLD. All **10 billion** tokens were minted at genesis on **Jul 24 2023**, and the contract has no live mint function and no per-block issuance. Governance cannot create any new supply until the **15-year** mark on **Jul 24 2038**, and even then only up to **1.5%** a year. Everything the market feels as inflation is not new minting; it is the release of pre-minted tokens onto the float.

Sell #2, vesting unlocks, is **163.8M WLD** and is the hard, predictable core of the sell side. Team and early-investor tokens unlock daily on a fixed linear schedule — a 12-month cliff that ended in July 2024, then roughly **20%** over 24 months and **80%** over 48 months, concluding around **July 2028**. These tokens are distributed to their wallets and are tradable the moment they unlock. On **Jul 24 2026** this slice was cut from **1.9M** to **1.3M WLD** a day, a 32% reduction, so the window is a blend and the forward figure re-bases on the lower rate: the next 90 days project **117.0M WLD**.

Sell #5, community grants claimed, is **82M WLD** — a coin-specific row, because World's largest allocation reaches the market in an unusual way. The **75%** community allocation unlocks on schedule into a grant pool, but those tokens only become circulating when a **verified human claims them**; unclaimed grants sit idle. World's own circulating-supply methodology makes this explicit — as of **Apr 10 2026**, **4.9B** WLD were unlocked but only **3.3B** were in circulation, a **1.6B** unclaimed backlog. So the framework books realised claims, not the calendar. Across roughly **18 million** verified humans, and with the recurring grant shrinking to about **1.36 WLD** a month from **3.22** a year earlier, claims ran near **82M** this window. Because claims draw on the backlog rather than the daily unlock, the July cut barely touches them, so the next 90 days project about **78M**.

The remaining sell rows are **zero**. Sell #3, foundation and unscheduled unlocks, is zero because no discretionary open-market sale by the World Foundation was observed — the large team-controlled overhang is watched, not sold. Sell #4, long-term locked or bankruptcy, is zero because World has no estate, no trustee and no court-ordered distribution.

## Buy pressure: where new WLD goes

Every buy row is **zero**, and that is the second defining feature of WLD. Buy #1, programmatic buyback, is zero because the design has no buyback mechanism at all — no protocol revenue is routed into open-market WLD purchases. Buy #2, protocol fee burn, is zero because the token cannot burn: WLD is a fixed-cap ERC-20 with no burn function, and World Chain charges gas in **ETH**, not WLD, so ordinary network usage removes no supply. Buy #3, foundation buy, is zero because no open-market purchase by the World Foundation was disclosed in the window. Buy #4, new long-term lock, is zero because no new lock-up contract or staking cap with a committed quantum was announced — the July unlock cut slows the release but locks nothing new. With the buy side empty, the daily unlock has nothing working against it.

## Foundation and overhang

The team-controlled overhang for WLD is enormous, but most of it is watched rather than sold. The biggest piece is the **community grant pool**: roughly **1.6B WLD** that is unlocked on paper but still unclaimed as of **Apr 10 2026**, held under the World Foundation and entering circulation only as users claim it — a flow already captured in Sell #5. Beyond that sit the small **TFH Reserve** — about **0.3%** of supply, itself on a lockup-plus-linear release — and the still-locked remainder of the team and investor allocation, which unlocks linearly through **July 2028** and shows up in Sell #2 as it releases. These balances are re-checked at every rebuild. If the Foundation were to move any of this pool onto the market outside the claim mechanism, that outflow would enter Sell #3 at the next refresh; through this window, none did.

## How WLD compares to other pre-minted unlock tokens

The natural comparison class for WLD is hard-capped tokens whose supply is fully pre-minted and released on a vesting schedule — the opposite of a chain that mints new coins each block. Against that class, WLD is unusual in two ways. First, its unlock is exceptionally heavy and long: a **75%** community allocation plus multi-year team and investor vesting means the float roughly doubled in size over the past year, which is why it reads as the heaviest unlocker we track even with a **fixed cap**. Second, the community portion is claim-gated, so the gross schedule badly overstates real supply-to-market — a distinction most unlock trackers miss, which is why aggregate "unlock" figures for WLD run well above what actually circulates.

Against uncapped proof-of-stake Layer 1s, the contrast is instructive. Those chains mint new supply forever but often at a modest **3–5%** a year, partly offset by fee burns; WLD mints **nothing**, yet its scheduled unlock pushes net supply growth above **6%** for the window with no burn to soften it. A capped token can still be more inflationary in practice than an uncapped one when the pre-mint is this large and the release this fast.

Against tokens with structural buybacks or fee burns, WLD has no offset at all. Exchange tokens and revenue-burn chains remove supply as they earn; WLD earns no protocol revenue for the token and destroys nothing. The only thing that slows WLD is the unlock schedule itself stepping down — which is exactly what the **Jul 24 2026** cut did.

## What to watch in the next 90 days

Watch the unlock schedule first: the **43%** aggregate cut on **Jul 24 2026** — team and investor from **1.9M** to **1.3M** a day, community from **3.2M** to **1.6M** a day — is the assumption behind the **+5.45%** forward reading, and it holds at that rate through this window with no further step due. Watch the claim rate: the recurring grant keeps shrinking toward **1.36 WLD** a month, and any change to grant amounts or verified-human growth moves Sell #5 directly. Watch for any World Foundation transparency post or on-chain movement from the community pool outside the claim mechanism, which would open Sell #3. And watch for a buy-side mechanism appearing — there is none today, so any announced buyback or lock would be the first offset WLD has ever had.

## Summary

The MrNasdog Pressure Framework reads World at **+6.87%** net supply growth over the last 90 days and **+5.45%** projected for the next 90, against a supply monitor at **+7.48%**. The structural mechanism is unusual: WLD cannot mint or burn, so all pressure is the linear unlock of a pre-minted **10B** supply — about **163.8M** of team and investor vesting plus **82M** of claimed community grants this window — with **no buyback and no burn** to offset it. The **Jul 24 2026** cut eased the rate by **43%** but did not reverse it. The lasting risk is simple: a fixed cap is not the same as low inflation, and with a huge unlocked-but-unclaimed backlog and years of vesting still to run, WLD keeps adding supply for the foreseeable future.

---

*MrNasdog Pressure Framework analysis of World (WLD), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 5 2026.*
