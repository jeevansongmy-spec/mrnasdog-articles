---
title:         "SKY Inflation Analysis · July 2026 · Mixed flows, supply roughly steady"
description:   "Sky Token Rewards mint ~419M SKY/90d; the Smart Burn Engine buys and burns ~324M. Framework reads +0.41% net, roughly steady, in line with the monitor."
canonical_url: "https://mrnasdog.com/research/sky/inflation"
tags:          ["crypto", "sky", "makerdao", "defi"]
published:     true
---

*Originally published at [mrnasdog.com/research/sky/inflation](https://mrnasdog.com/research/sky/inflation)*

Sky Protocol's SKY token runs two supply engines against each other. Sky Token Rewards mint about **419M SKY** over 90 days to stakers and USDS holders, while the Smart Burn Engine buys and permanently burns about **324M SKY** with protocol surplus. The two nearly cancel, so the Pressure Framework reads about **+0.41%** net — close to our supply monitor's **+0.76%**, a gap of roughly **0.35 percentage points**, inside tolerance and needing no chip.

## The verdict, in one paragraph

For the 90-day window opening July 13 2026, the MrNasdog Pressure Framework reads **SKY at +0.41% net** on the forward view. Sky Token Rewards add roughly **419M SKY** of new supply, and the Smart Burn Engine removes roughly **324M SKY** through an on-chain buyback-and-burn, so the ledger is a near tie with a slight lean toward growth. Our supply monitor reads the realized last-90-day change at **+0.76%**, so the gap is about **0.35 percentage points** and **no monitor-gap chip** is needed. The small extra growth the monitor sees is consistent with legacy MKR-to-SKY conversions still adding to the SKY count — a value-neutral reclassification the framework deliberately excludes. SKY is best characterised as a **token where an active buyback almost fully offsets reward emissions**, leaving supply roughly steady rather than clearly inflationary or deflationary.

## Sell pressure: where new SKY comes from

Sell #1 — protocol inflation — is the only real source of new SKY, at about **419M SKY** over 90 days. Sky pays Sky Token Rewards in freshly issued SKY to two groups: users who stake SKY, and users who hold the USDS stablecoin and activate rewards. A governance vote that passed on **Feb 27 2026** and executed on **Mar 2 2026** normalised this reward rate down to about **838M SKY** over 180 days — a cut of roughly 162M versus the prior schedule — which is where the ~419M-per-90-day figure comes from. This is the number that makes SKY inflationary before any offset.

The other sell rows are zero. Sell #2 — vesting unlocks — is zero because SKY inherited MakerDAO's tokenomics, which never had a venture, team or investor vesting allocation, so there are no unlock cliffs. Sell #3 — Foundation and unscheduled unlocks — is zero because Sky does not sell SKY from a treasury; its protocol surplus is instead spent on the burn engine, making the surplus a buy-side tool rather than a sell-side overhang. Sell #4 — long-term locked or bankruptcy — is zero, with no estate or court distribution. There is one extra tracked line, the MKR-to-SKY conversion, which the framework carries at zero: swapping MKR for SKY at 24,000 to 1 lifts the SKY count but is value-neutral, since the same holder keeps the same value and no new seller is created.

## Buy pressure: where new SKY goes

The buy side is carried entirely by Buy #1 — the programmatic buyback — at about **324M SKY** over 90 days. Sky's Smart Burn Engine takes protocol surplus, denominated in USDS, and uses it to buy SKY on the open market and permanently burn it, removing roughly **3.6M SKY** a day. Cumulatively the engine has already destroyed about **1.83B SKY** for roughly $114.5M spent, so this is a genuine, continuous reduction in supply — not a marketing promise. Because the bought-back SKY goes to a burn address, it leaves no accumulation overhang; the tokens are gone.

The remaining buy rows are zero and would double-count if filled. Buy #2 — protocol fee burn — is zero because Sky has no separate fee burn; the surplus burn already runs through the Smart Burn Engine in Buy #1. Buy #3 — Foundation buy — is zero, with no discretionary open-market buying beyond the programmatic engine. Buy #4 — new long-term lock — is zero because staking SKY to earn rewards keeps the coins liquid and withdrawable, so it never removes supply from the float. The net effect: the ~324M burn cancels most of the ~419M reward emission, leaving about 95M of net new SKY.

## Foundation and overhang

SKY has no conventional team or foundation overhang to watch, which is unusual for a token of its size. There is no VC unlock schedule and no treasury wallet dripping coins into the market. The one balance-sheet lever that matters is the **surplus buffer** — the protocol's accumulated profit — but it points the other way: rather than being a pile of SKY that could be sold, it is the USDS surplus that funds the buyback. The genuine long-term variable is the **MKR-to-SKY conversion**: about 176K MKR remains unconverted, equal to roughly 4.2B SKY at the 24,000-to-1 ratio, and it converts slowly with no deadline. If those conversions accelerate, the SKY count rises faster than the framework's formula shows, because the framework treats the swap as a value-neutral reclassification rather than new pressure. If that conversion pace or the buyback balance shifts between refreshes, the change enters the ledger at the next roughly bi-weekly walk.

## How SKY compares to other buyback-and-burn tokens

SKY belongs to the class of **revenue-funded buyback-and-burn tokens**, and it sits at an interesting midpoint within that class. Compared with an exchange token like BNB, which burns on a quarterly schedule and has no ongoing reward emission, SKY burns continuously but also emits continuously — so its net reading is a race between the two rather than a one-way burn. Compared with Ethereum, where a base-fee burn can push net supply negative during busy periods with no reward inflation on the token itself, SKY's reward stream is large enough that the burn only offsets it rather than overwhelming it.

The contrast that matters is **emission versus buyback**. On a pure-mint layer-1, inflation is set by an issuance curve the holder cannot influence; on SKY, inflation is the difference between two governance-tuned dials — the reward rate and the surplus routed to the burn engine. That makes SKY's inflation a governance signal: the Feb 2026 vote that cut rewards, combined with rising protocol revenue feeding the burn, is exactly what has pulled the net reading down toward flat. If revenue keeps growing and rewards stay capped, SKY could tip net deflationary; if rewards are raised again, it drifts back up. For an inflation lens, SKY today reads as **roughly steady** — mildly inflationary, but with an unusually strong structural offset.

## What to watch in the next 90 days

Watch the Sky governance forum for any change to the Sky Token Rewards rate — the **Feb 2026** cut is the single reason the net reading is near flat, and another adjustment in either direction would move Sell #1 directly. Watch the Smart Burn Engine's daily buyback size, since it scales with protocol revenue; a sustained rise above the recent ~3.6M-SKY-per-day pace would push the net reading toward deflationary. Watch the surplus buffer and Sky Savings Rate settings, because a lower savings rate leaves more surplus for the burn. And track the MKR-to-SKY conversion pace directly — it is the quiet variable that lifts the SKY count without showing up as pressure in the framework's formula.

## Summary

SKY is the governance token of Sky Protocol, and its supply is governed by two engines pulling in opposite directions: Sky Token Rewards mint about 419M SKY over 90 days, while the Smart Burn Engine buys and burns about 324M with protocol surplus. The two nearly cancel, leaving the framework at about +0.41% net — close to our supply monitor's +0.76%, a gap inside tolerance that needs no chip. The key variable is governance: the reward rate and the share of surplus routed to the burn set whether SKY tips inflationary or deflationary. Today it reads roughly steady, with an active, continuous buyback offsetting most of a reward stream that a February 2026 vote already trimmed.

*MrNasdog Pressure Framework analysis of Sky (SKY), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 13, 2026.*
