---
title: "TIA Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description: "Celestia adds ~37.7M TIA over 90 days (31.0M unlock + 6.6M mint) with no buyback and no burn. Framework +3.96% net; monitor +4.25% — no data conflict."
canonical_url: "https://mrnasdog.com/research/tia/inflation"
tags: ["crypto", "tia", "celestia", "data-availability"]
published: true
---

*Originally published at [mrnasdog.com/research/tia/inflation](https://mrnasdog.com/research/tia/inflation)*

Celestia adds about **37.7M TIA** to circulation over the next 90 days — roughly **31.0M** from a smooth genesis unlock and **6.6M** from the staking mint — and nothing buys any of it back, because Celestia runs no buyback and burns nothing today. The MrNasdog Pressure Framework reads **+3.96% net** forward, essentially matching the **+3.96%** of the last 90 days, on a circulating base of **950.46M TIA**. TIA is uncapped, but the story is the unlock calendar, not the mint: the mint was already cut to about **2.29%** a year, while the daily unlock still dominates.

## The verdict, in one paragraph

Over the last 90 days the MrNasdog Pressure Framework reads Celestia at **+3.96% net**: about **37.7M TIA** of new float against a zero buy-side offset, on a circulating base of **950.46M TIA**. Our supply monitor reads the same trailing window at **+4.25%**, a gap of about **0.28 percentage points** — inside tolerance, so this build ships **no monitor-gap chip** and needs no reconciliation walk. The small residual is the ordinary difference between booking the published unlock schedule and measuring realised circulating change, not a data conflict. Looking forward, the framework again reads **+3.96%** for the next 90 days. Celestia is **structurally inflationary** — an uncapped chain whose supply cannot shrink, releasing a steady daily tranche of previously locked coins on top of a small, disinflating staking mint.

## Sell pressure: where new TIA comes from

Sell #2 — vesting unlocks — is the larger of Celestia's two supply forces, at about **31.0M TIA** over both the last 90 days and the next. Celestia does not release locked supply in lumpy annual cliffs; its genesis allocations to the Foundation's R&D and ecosystem pool, the initial core contributors and the inflation allocation vest linearly, adding roughly **344,924 TIA** to the float every day. Public unlock trackers bucket that continuous flow into a monthly figure of about **10.7M TIA**, but the underlying release is per-block and smooth. Because the vest is linear rather than a cliff into a lock contract, tokens become liquid continuously and there is no on-chain escrow backlog — what the calendar schedules is what actually reaches the market, so realised and scheduled unlock agree. The full genesis schedule runs to about **Sep 30 2027**.

Sell #1 — protocol inflation — is the staking mint, and on Celestia it has already been cut hard. The chain's x/mint query for the inflation rate itself returns "not implemented," but its annual-provisions figure reads about **26.87M TIA** a year, which is about **73,603 TIA** a day and works out to roughly **6.6M TIA** over 90 days. That is an annual rate of about **2.29%** — the level set by CIP-41, which reduced issuance to 2.5% in November 2025 and keeps it disinflating about 6.7% a year toward a 1.5% floor. The rate steps once a year on the genesis anniversary, so it held constant across this window; the next step lands around **Oct 31 2026**. The mint is now the smaller force on Celestia supply, and it is shrinking.

Sell #3 — foundation and unscheduled unlocks — is **zero** on this build, though the overhang behind it is real. About **223.7M TIA** remains outside circulation; roughly **102.5M** of that is still on the linear schedule already counted in Sell #2, and about **126.1M** is unscheduled — the Celestia Foundation's R&D and ecosystem balance, the community pool and unclaimed genesis. The framework books nothing here because no off-schedule Foundation distribution was observed in the window. Sell #4 — long-term locked or bankruptcy — is **zero** and structurally so: there is no bankruptcy estate, no trustee distribution and no court-ordered release affecting TIA.

## Buy pressure: where new TIA goes

Every buy-side row on Celestia is **zero**, and that is a structural property of the network today rather than a gap in the research. Buy #1 — programmatic buyback — is zero because Celestia operates no buyback of any kind; neither the protocol nor the Foundation runs a TIA repurchase programme. Buy #2 — protocol fee burn — is zero because Celestia does not burn. Data-availability fees, paid by rollups to post blob data, and ordinary transaction fees are distributed to stakers and the community pool under the standard Cosmos model; none is destroyed. That is the single most important asymmetry on Celestia: supply is continuously added by both the mint and the unlock, and nothing on the protocol takes any of it back out.

Buy #3 — foundation buy — is zero: the Celestia Foundation discloses no open-market TIA accumulation. Buy #4 — new long-term lock — is zero as well. Most TIA is staked, but staking on Celestia is holder-driven yield seeking with a short unbonding exit, so staked TIA remains part of the circulating float rather than an announced lock of a fixed size, and no new lockup was created in the window. The one change on the horizon is the Matcha upgrade and its Proof-of-Governance model, which would burn transaction fees and MEV and cut the mint toward about 0.25%; but Matcha is not live — the chain still reads a 2.29% mint and the standard fee-distribution module — so it opens no buy-side row yet.

## Foundation and overhang

The team-controlled overhang on Celestia is about **223.7M TIA**, the whole of the non-circulating supply, and it splits cleanly in two. Roughly **102.5M TIA** is still on the linear genesis schedule — the tail of the R&D and ecosystem, core-contributor and inflation allocations that keeps releasing at about **344,924 TIA** a day through to about **Sep 30 2027**. The other **126.1M TIA** is unscheduled: the Celestia Foundation's discretionary R&D and ecosystem balance, the community pool and unclaimed genesis holdings, with no fixed release calendar.

The scheduled portion is watched against Celestia's published unlock calendar, re-fetched each rebuild and compared step by step; the unscheduled portion is watched for any off-calendar Foundation outflow on-chain. Both are booked at zero in Sell #3 today because nothing fired outside the linear schedule. If any of these balances falls between refreshes faster than the published schedule allows, the excess outflow enters Sell #3 at the next refresh rather than being absorbed silently into the vesting row.

## How TIA compares to other uncapped continuous-emission chains

Celestia belongs to the uncapped, venture-funded Cosmos-SDK class of layer-1, where two independent supply forces run at once: a protocol mint and a multi-year genesis unlock. Against a halving-model chain like Bitcoin, where a hard cap and a fixed emission schedule are the same fact and the float converges on the cap, TIA has no cap at all — supply simply grows, and the near-term rate is set far more by the unlock calendar than by the mint. In that respect TIA reads much like Sui or Aptos: the dominant supply variable is a vesting schedule the team can see years out, not a block subsidy.

Against its closest structural sibling, Cosmos Hub's ATOM, the contrast is instructive. ATOM is also uncapped, but its genesis vesting is long finished, so its inflation is almost entirely a staking mint pinned near its ceiling. Celestia is at the opposite point of that lifecycle: its mint has been deliberately cut to about **2.29%**, well below ATOM's realised rate, yet its overall supply growth is higher because roughly **31.0M** of its **37.7M** forward supply comes from the unlock rather than the mint. As Celestia's genesis schedule drains toward late 2027, that unlock force fades and the disinflating mint becomes the whole story — which is the structural case for TIA supply growth easing over time.

The sharpest contrast is with fee-burn chains. Ethereum can post negative net issuance when base-fee burn exceeds validator rewards; BNB retires supply on a quarterly schedule. Celestia has neither lever today — fees are distributed, not destroyed — so TIA net supply cannot mathematically fall on this build. The proposed Matcha upgrade would change exactly that by burning fees and MEV and slashing the mint, which is why it is the single most important thing to watch for TIA's long-run inflation profile.

## What to watch in the next 90 days

Watch the continuing daily unlock: two roughly **10.5M TIA** monthly tranches land across **Aug 31 2026** and **Sep 30 2026**, and any divergence between realised circulating supply and the published schedule would mean the calendar has changed. Watch the annual disinflation step around **Oct 31 2026**, when the mint rate falls another 6.7% on the genesis anniversary. Watch the end of the core-contributor tranche, also near **Oct 2026**, which begins to thin the daily unlock rate. Above all, watch the **Matcha / Proof-of-Governance** upgrade: if it activates, it would introduce a fee-and-MEV burn and cut the mint toward 0.25%, the first mechanism that could ever push TIA net issuance toward zero.

## Summary

The MrNasdog Pressure Framework reads TIA as **structurally inflationary** at **+3.96% net** over the next 90 days, essentially flat against **+3.96%** over the last 90. The mechanism is two-sided on the sell ledger and empty on the buy ledger: about **31.0M TIA** of linear genesis unlock plus about **6.6M TIA** of a disinflating **2.29%** staking mint, against a buy side that is zero on every row because Celestia neither buys back nor burns. The key risk is the **126.1M TIA** of unscheduled Foundation and unclaimed supply that sits outside the schedule. The ceiling is equally clear: with no burn and no buyback live today, TIA supply can only slow as the genesis unlock drains — it cannot shrink until an upgrade like Matcha gives the protocol a way to take supply back.

*MrNasdog Pressure Framework analysis of TIA, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 2 2026.*
