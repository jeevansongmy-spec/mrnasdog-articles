---
title: "TIA Inflation Analysis · August 2026 · Supply growing on genesis unlocks"
description: "Celestia adds ~38.2M TIA over 90 days (31.0M genesis unlock + 7.2M mint) with no buyback and no burn. Framework +4.01% net; monitor +4.23% — no data conflict."
canonical_url: "https://mrnasdog.com/research/tia/inflation"
tags: ["crypto", "tia", "celestia", "data-availability"]
published: true
---

*Originally published at [mrnasdog.com/research/tia/inflation](https://mrnasdog.com/research/tia/inflation)*

Celestia cut its staking mint to about **2.5%** a year, but that is not the story: a linear genesis unlock releasing roughly **344,924 TIA** a day — about **31.0M** over the trailing 90 days — is more than four times the **~7.2M** mint. There is nothing on the other side — no buyback, no fee burn, no lockup — so the MrNasdog Pressure Framework reads **+4.01% net** new supply on a circulating base of **952.96M TIA**, and our supply monitor agrees at **+4.23%**, a gap of just **0.22 percentage points** that ships no data-conflict chip. TIA inflates on an uncapped supply with no counterweight.

## The verdict, in one paragraph

For the 90-day window to **Aug 9 2026**, the MrNasdog Pressure Framework reads **TIA at +4.01% net** for the trailing window and **+3.92%** for the forward window — the staking mint and the daily unlock both reach the market in full, with nothing to offset them. Our supply monitor reads **+4.23%** for the trailing window, a gap of only **0.22 percentage points**, well inside the framework's 0.5-point tolerance, so no monitor-gap chip appears on the TIA overview and no reconciliation walk is needed. The two agree because both capture the same reality: a small staking mint stacked on a large linear vesting unlock, on a supply with no hard cap. TIA is best characterised as **a persistently inflationary uncapped Layer 1 whose vesting unlock dwarfs its already-reduced mint**.

## Sell pressure: where new TIA comes from

Sell #1 — protocol inflation — is about **7.2M TIA** over 90 days, and it is the smaller of Celestia's two supply forces. TIA launched with an **8%** annual staking mint, but governance upgrades cut it hard: the v4 "Lotus" upgrade in mid-2025 and the v6 upgrade in November 2025 drove the rate down to about **2.5%** a year, and it continues decaying toward a **1.5%** floor. On a total supply near **1,174.5M**, that is roughly 7.2M TIA minted to stakers over the window, with 2% of every block reward routed to an on-chain community pool.

Sell #2 — vesting unlocks — is the force that makes TIA inflate, at about **31.0M TIA** over 90 days, more than four times the mint. Celestia's genesis allocations to Series A&B and seed investors, initial core contributors and the ecosystem reserve vest on a straight-line schedule that runs until **October 2027**. The live release rate is about **344,924 TIA a day**, which holds near **9.7M a month** through October 2026 before stepping down to about **5.1M a month** — so the next 90 days release roughly **30.2M**. This is the single dominant input to the reading: it is the difference between TIA being a mildly inflationary chain and one running near the top of its class.

Sell #3 — foundation and unscheduled unlocks — is **zero** this window; the community pool and the Celestia Foundation reserve are tracked but neither made an off-schedule distribution to the market. Sell #4 — long-term locked or bankruptcy — is **zero** and structurally so: no bankruptcy estate, trustee distribution or court-ordered release touches TIA.

## Buy pressure: where new TIA goes

Buy #1 — programmatic buyback — is **zero**. Celestia has never deployed a buyback: the protocol does not use revenue to repurchase TIA, so there is no structural demand pulling supply back in against the mint and the daily unlock. Buy #2 — protocol fee burn — is also **zero**: Celestia has no EIP-1559-style base-fee destruction, and blob and transaction fees are paid to stakers rather than burned. A future upgrade that would burn fees is discussed but not live.

Buy #3 — foundation buy — is **zero**: no discretionary open-market TIA buying by the Celestia Foundation or any treasury was disclosed this window. Buy #4 — new long-term lock — is **zero** as well; no new multi-year TIA lock or escrow contract was announced, and the network's **21-day** unbonding period is a withdrawal delay, not a supply lock. With every buy-side row at zero, the full mint and the full unlock reach the market, and the net reading is simply their sum divided by the float.

## Foundation and overhang

Two team-controlled overhangs sit behind TIA. The first is the still-locked vesting bucket: about **95.6M TIA** remains locked and draining at the daily rate above, the tail of the genesis allocations to investors, core contributors and the ecosystem reserve. That drain is already booked in the vesting row, so it is a scheduled release rather than a discretionary one. The second is the Celestia Foundation ecosystem and R&D reserve together with the on-chain community pool, which is fed by the **2%** tax skimmed off every block reward and can be drawn only by a passing governance vote.

The vesting bucket is watched by its published daily schedule, re-fetched each rebuild; the Foundation reserve and community pool are watched independently for any off-calendar move. Both are booked at zero in Sell #3 today because nothing fired outside the linear schedule. If either the Foundation reserve or the community pool makes a large TIA-denominated distribution to the market between refreshes, that outflow enters Sell #3 at the next refresh rather than being absorbed silently into the vesting row.

## How TIA compares to other uncapped Layer 1 chains

TIA belongs to the **2023-vintage, VC-backed, uncapped Layer 1** class — chains like Celestia, Sui and Sei that launched with a large private allocation on a multi-year linear vest, layered on top of a continuous staking mint with no hard cap. Within that group, TIA is defined by how lopsided its ledger is: the mint has been cut to about **2.5%**, but the genesis unlock is still the dominant force, so the supply story is almost entirely a vesting story rather than an emission story. That is the opposite balance to a chain like Cosmos Hub (ATOM), whose vesting finished years ago and whose entire inflation is now the **staking mint** alone.

The sharper contrast is with chains that have a burn. A fee-burning Layer 1 leans on transaction volume to claw supply back, and an exchange or DeFi token with a revenue-funded buyback can push net supply flat or negative. Celestia has neither — no burn, no buyback, no lockup — so its buy side is simply zero and its net reading equals its gross mint plus its unlock. Against a hard-capped, halving-model asset the gap is starker still: that asset issues on a fixed, shrinking schedule toward a ceiling, while TIA issues on a floating rate with no ceiling and simultaneously releases a large pre-minted allocation into the float.

The offsetting hope for TIA holders is structural and dated, not mechanical. The vesting unlock steps down from about **9.7M** to about **5.1M** a month in November 2026 and ends entirely in October 2027, and the mint keeps decaying toward its **1.5%** floor. Once the unlock is gone, TIA's inflation collapses toward the mint rate alone — but until then, it inflates near the top of its class.

## What to watch in the next 90 days

Watch the daily unlock rate near **344,924 TIA** a day: it is the single biggest input to the reading, and it steps down to about **5.1M a month** on **Nov 1 2026**, which will start to cool the net figure. Watch the staking mint near **2.5%**, which keeps decaying toward its 1.5% floor and would fall faster under any further governance cut. Watch Celestia governance for the discussed fee-burn and deeper-mint-cut upgrade, which is not yet live but would add the first buy-side force TIA has ever had. And watch the Foundation reserve and community pool near their published balances for any large TIA-denominated distribution, which would register as a discrete Sell #3 release on top of the scheduled vest.

## Summary

Celestia is a persistently inflationary uncapped Layer 1. Its staking mint has been cut to about **2.5%** a year — roughly **7.2M TIA** over 90 days — but a linear genesis unlock releasing about **344,924 TIA** a day, some **31.0M** over the window, is the dominant force. With no buyback, no fee burn and no lockup anywhere in the design, the buy side is zero and the full mint and unlock reach the market. The framework reads **+4.01% net** and our monitor **+4.23%**, a **0.22-point** gap inside tolerance. The path to lower inflation is dated: the unlock steps down in November 2026 and ends in October 2027, after which only the shrinking mint remains.

*MrNasdog Pressure Framework analysis of Celestia (TIA), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated August 9, 2026.*
