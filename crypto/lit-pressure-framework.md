---
title: "HEI Inflation Analysis · June 2026 · A capped token finishing its unlock"
description: "A MrNasdog Pressure Framework read of Heima (HEI, formerly LIT): a hard-capped 100M token with a ~1M/90d vesting tail, no buyback, and a pending 16.5M burn vote. +1.0% net."
canonical_url: "https://mrnasdog.com/research/lit/inflation"
tags: ["crypto", "hei", "heima", "litentry"]
published: true
---

> Originally published at **[mrnasdog.com/research/lit/inflation](https://mrnasdog.com/research/lit/inflation)** by MrNasdog.

Heima's HEI is capped at **100M** with roughly **97.76M circulating**, so the only new supply is the last of its vesting unlock — about **1M HEI** over the next 90 days. There is no protocol minting, no buyback and no quantified burn, so the Pressure Framework reads about **+1.0%** net to market. Our supply monitor has no clean read for HEI yet — the Litentry-to-Heima contract migration broke the 90-day series — so that end-check is deferred and primary is kept.

## The verdict, in one paragraph

For the 90-day window ending June 16 2026, the MrNasdog Pressure Framework reads **HEI at about +1.0% net** on the forward view, driven entirely by the tail of its vesting unlock with nothing on the buy side to offset it. The supply monitor coverage is **absent** for HEI — the migration from the old LIT contract to the new HEI contracts broke the supply history, so there is no realized 90-day delta to compare against and no monitor-gap chip; the end-check is deferred to the next refresh and the primary read stands. HEI is a **capped token in the final stretch of its unlock**: mildly inflationary today, but with a hard ceiling close above the current float.

## Sell pressure: where new HEI comes from

Sell #1 — protocol inflation — is **zero**. HEI is hard-capped at **100M** and has no staking emission or block reward; gas on Heima is sponsored by intent fillers rather than charged and minted, so the protocol never creates new coins. That makes HEI structurally unlike an inflationary proof-of-stake chain — there is no perpetual issuance, only a finite distribution being released.

Sell #2 — vesting unlocks — is the entire sell story, at about **1M HEI** over the next 90 days. The original plan moved circulating supply from **66.45M** toward the **100M** ceiling over 20 months; with circulating now near **97.76M**, only about **2.2M** of headroom is left, and recent unlock steps have shrunk to tiny **~40K-coin** events. The post-migration schedule is not published cleanly, so the framework estimates the remaining tail by date as a small continuous unlock rather than a single cliff. Sell #3 — Foundation and unscheduled unlocks — is zero as a discrete flow, because the ecosystem wallet's remaining release is already inside that vesting tail and there is no dated discretionary unlock pending. Sell #4 — long-term locked or bankruptcy — is zero, with no estate or court distribution attached to HEI.

## Buy pressure: where new HEI goes

The buy side is empty today. Buy #1 — programmatic buyback — is **zero**: Heima runs no buyback contract and does not repurchase HEI on a published schedule. Buy #2 — protocol fee burn — is also zero, because gas is abstracted and sponsored rather than paid in HEI, so there is no quantified on-chain fee burn to count. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no disclosed open-market buying or new escrow. The one mechanism worth flagging is a **governance burn proposal**: a community vote to permanently burn **16.5M HEI** from the ecosystem allocation — reserves originally set aside for Polkadot parachain auctions and now deemed unnecessary — opened in early June 2026 with the Heima Foundation voting in favor. Because execution is not confirmed within this window, the framework carries it at zero rather than crediting an unconfirmed burn; if it executes, it would cut supply by roughly a sixth and flip the net reading sharply deflationary.

## Foundation and overhang

HEI's only meaningful overhang is the **ecosystem allocation** still finishing its unlock — about **2.2M HEI** of headroom between current circulating and the 100M cap, plus the **16.5M HEI** reserve that the burn proposal targets. The first is the vesting tail already counted in Sell #2; the second is the candidate for removal under the pending vote, not a release. There is no team, treasury or partner stockpile beyond the capped allocation, because the total can never exceed 100M. The framework re-checks the unlock schedule and the governance outcome on a roughly bi-weekly walk; if the ecosystem balance falls between refreshes for any reason other than the scheduled unlock, that outflow enters Sell #3 at the next refresh.

## How HEI compares to other capped utility tokens

HEI belongs to the class of **hard-capped utility tokens released through a finite vesting schedule** — closer to a fixed-supply app token than to an uncapped, continuously-minting proof-of-stake chain. Unlike a chain that pays staking rewards out of fresh issuance, HEI has no emission curve at all: once the unlock completes, gross new supply is structurally zero, and the only future supply move is a burn. That puts its inflation profile on a one-way path toward flat.

The contrast worth drawing is with tokens that pair a cap with an active buyback or fee burn. Those can go net-deflationary while still distributing; HEI, for now, has neither a buyback nor a quantified burn, so during these final unlock months it reads mildly inflationary purely from the vesting tail. The pending 16.5M burn is the swing factor: if it passes and executes, HEI moves from this group into the small set of capped tokens that actively shrink supply — a sharp, one-time deflation rather than a steady drip.

## What to watch in the next 90 days

Watch the **16.5M HEI burn vote** — its approval and on-chain execution is by far the most important supply event, and it would turn the net reading deeply deflationary if completed. Watch the unlock tail finish, since circulating is already near the **100M** cap and the remaining vesting is small and shrinking toward zero. Watch for the supply monitor to regain coverage once the new HEI contracts accumulate a clean 90-day history, which would let the framework restore its realized end-check. And note that with no buyback or burn live yet, nothing currently pulls supply back — so the reading stays mildly positive until the unlock completes or the burn executes.

## Summary

HEI is the capped utility token of Heima, the rebranded Litentry network, swapped 1:1 from LIT. It has no protocol minting; supply grows only from the last of a vesting unlock, about 1M HEI over 90 days toward a 100M ceiling that circulating (~97.76M) is already close to. With no buyback and no quantified burn live, the framework reads about +1.0% net to market, and the supply monitor's end-check is deferred because the contract migration broke its history. The key risk and key upside are the same event: a pending community vote to burn 16.5M HEI, which would flip the token from mildly inflationary to sharply deflationary if it executes.

---

*MrNasdog Pressure Framework analysis of HEI (Heima, formerly LIT), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 16, 2026.*
