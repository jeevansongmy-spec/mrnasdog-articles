---
title:         "GRASS Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description:   "Grass mints nothing, yet ~45.4M GRASS left its vaults in 90 days against zero buyback or burn. Framework reads +6.93% net supply growth; monitor +11.49%."
canonical_url: "https://mrnasdog.com/research/grass/inflation"
tags:          ["crypto", "grass", "solana", "depin"]
published:     true
---

*Originally published at [mrnasdog.com/research/grass/inflation](https://mrnasdog.com/research/grass/inflation)*

# GRASS Inflation Analysis · August 2026 · Supply growing, projected to keep growing

Grass mints no new GRASS at all — the full **1,000,000,000 GRASS** was created at launch and the on-chain supply sits flat below the cap — yet GRASS is one of the more dilutive tokens the MrNasdog Pressure Framework tracks, because pre-minted coins keep leaving their vaults. About **45.4M GRASS** reached the market over the trailing 90 days through reward emissions, vesting locks and one Foundation deployment, against a buy side of **0**. That puts the framework at **+6.93%** net for the trailing window and **+4.89%** forward. Our supply monitor reads a higher **+11.49%**, a gap that traces to the difference between vested-on-paper and actually-released supply.

## The verdict, in one paragraph

For the 90-day window opening **Aug 2 2026**, the MrNasdog Pressure Framework reads **GRASS at +4.89% net** forward, below the **+6.93%** it measured over the trailing 90 days because a one-off treasury deployment sits inside the trailing figure and carries none of it forward. Our supply monitor reads **+11.49%** for the trailing window, a gap of **4.56 percentage points** that ships a monitor-gap chip on the GRASS overview. The deep walk reconciled it: read straight off the chain, the Foundation vault paid a reward stream three times plus one deployment, and three lock vaults each released exactly **1.95M GRASS** on May 28, June 28 and July 28 — about **45.4M** actually left the locks — while the published unlock calendar for the same window is **94.8M** because it counts coins as released the moment they vest on paper even while they stay inside the vault. The monitor follows that entitlement; the framework follows custody. GRASS is best characterised as **a zero-mint token that is persistently inflationary on its active float until its vesting calendar empties**.

## Sell pressure: where new GRASS comes from

Sell #1 — protocol inflation — is about **14.5M GRASS** per 90 days, and the mechanism is unusual. Grass mints nothing: all **1,000,000,000 GRASS** already exist, and the on-chain supply reads flat below the cap. What functions as emission is a reserve-funded reward stream — the Grass Foundation treasury vault paid out about **4.8M GRASS** to the network three times over the window, roughly **14.5M** in total, all from coins that already existed rather than freshly printed ones. Grass earns its real revenue by selling bandwidth and web data to AI customers off-chain, so no GRASS is created to pay for the network; the reward is drawn from the reserve.

Sell #2 — vesting unlocks — is about **17.5M GRASS**, and this is where the framework departs sharply from the aggregators. Grass's locked investor and contributor coins sit in on-chain escrow, and three lock vaults each released exactly **1,948,333.333 GRASS** on the 28th of May, June and July 2026 — **17.535M** reaching the market, read directly from the vaults. The published unlock calendar quotes a far larger **94.8M** for the same window, because it counts a coin as released the instant it vests on paper, even while that coin stays locked inside the vault. Because the escrows are readable on-chain, the framework books the realised outflow, not the paper entitlement.

Sell #3 — foundation and unscheduled unlocks — is about **13.3M GRASS** this window, from a single discretionary Foundation deployment of roughly **13.3M GRASS** on **Jun 10 2026**. It is a one-off with no published schedule, so the forward projection carries none of it — the reason the next-90-day figure is lower than the trailing one. Sell #4 — long-term locked or bankruptcy — is **zero** permanently: no bankruptcy estate, trustee schedule or court-ordered distribution holds GRASS.

## Buy pressure: where new GRASS goes

Buy #1 — programmatic buyback — is **zero**, and it is the row to watch. Grass markets a revenue model that can either buy back and burn GRASS or instead route revenue to node operators, and a revenue-share vote was raised at the **Jul 7 2026** token-holder call. But nothing is running on-chain yet: there is no measurable GRASS buyback or burn this window, and the mint and vault reads show no burn. The framework books executed flow, not intent, so Buy #1 stays zero and monitored until an on-chain burn or buyback run-rate is measurable.

Buy #2 — protocol fee burn — is **zero** because Grass bills its AI customers off-chain for data access, so network revenue never passes through an on-chain GRASS burn. Buy #3 — foundation buy — is **zero**: the treasury vault only sent coins out this window and took none in, so there is no discretionary open-market buying. Buy #4 — new long-term lock — is **zero** as well; no new multi-year GRASS lock or escrow contract was announced in the window.

## Foundation and overhang

The team-controlled overhang on Grass is large and easy to size because the supply is fixed. The Grass Foundation treasury vault — a Squads multisig at **7oMjvD5MW…** — still holds about **259.5M GRASS**, the single largest non-circulating holding, and it is the source of both the reward stream in Sell #1 and the discretionary deployment in Sell #3. Alongside it, the three vesting lock vaults hold about **13.6M GRASS** each — roughly **40.9M** of undrawn investor and contributor entitlement — releasing **1.95M** per vault on the 28th of each month. There is also a gap of roughly **22M GRASS** between what the unlock calendar treats as circulating and what has actually left the vaults; that is vested-but-unclaimed entitlement, not a market flow. All of these balances are read every rebuild. If any of them leaves its vault into the market ahead of schedule between refreshes, the outflow enters Sell #3 at the next refresh.

## How GRASS compares to other DePIN tokens

GRASS belongs to the fixed-supply DePIN class — networks that pay contributors for a physical resource, here spare residential bandwidth resold as AI web data — and it shares a structural quirk with several of them: the token is not minted to pay rewards, it is distributed from a pre-minted reserve. That makes GRASS cleaner than an uncapped, continuously-minting Layer 1, whose validators earn genuinely new coins forever on a schedule nobody controls. Grass will never create a billion-and-first GRASS; its dilution has a hard ceiling and, eventually, an end date. What it shares with the wider DePIN class is that the emission looks like inflation to the market even though the accounting calls it a reserve transfer — a coin leaving a vault to reach a seller weighs on price exactly as a freshly minted one would.

The sharper comparison is to an exchange token or a fee-burning chain that converts real revenue into token demand. Grass earns meaningful revenue — bandwidth and data sold to AI companies — but, unlike those tokens, none of that cash currently removes a single GRASS from supply. A fee-burning Layer 1 destroys base-fee tokens every block; an exchange token buys and burns every quarter. Grass has the revenue to build the same plumbing, and the **Jul 7 2026** holder call floated exactly that, but until a vote executes and an on-chain burn appears, the buy side is effectively empty while the vaults keep releasing.

Against its own class on timing, GRASS is still mid-schedule. About a third of the supply is unreleased, the early-investor stream runs until late October 2026, and the reward emission is continuous, so the sell ledger will keep the token inflationary on its active float for as long as the calendar runs. The honest reading is that GRASS's inflation profile is fully knowable and, for now, clearly positive — the entire question is whether Grass converts its AI revenue into a buyback before the market notices the vaults never stop.

## What to watch in the next 90 days

Watch the revenue-share vote from the **Jul 7 2026** holder call for execution — the day a buyback or burn goes live on-chain is the day Buy #1 can move off zero and the framework starts crediting it. Watch the three monthly lock-vault releases of **1.95M** each on the 28th of **Aug 2026**, **Sep 2026** and **Oct 2026**, plus the reserve reward stream, which together make up the sell ledger. Watch the early-investor vesting completion around **Oct 28 2026**, which ends one of the two lock streams and softens the forward reading afterwards. And watch the roughly **170M GRASS** Season 2 airdrop-and-governance distribution planned for the second half of 2026 — it is undated, so it books nothing yet, but it is the largest single dilution event on the horizon.

## Summary

Grass is a fixed-supply, zero-mint DePIN token whose float still grows quickly because pre-minted reserve, vesting and reward coins keep leaving their vaults. About **45.4M GRASS** reached the market over the trailing 90 days and about **32M** is projected forward, against a buy side of **zero**, leaving the framework at **+6.93%** net trailing and **+4.89%** forward. Our supply monitor reads **+11.49%**, a **4.56-point** gap that reconciles to the difference between vested-on-paper entitlement and the roughly **45.4M** that actually left the vaults. The key variable is the buy side: Grass earns real AI revenue, and if the token-holder vote turns that revenue into an on-chain buyback and burn, it would be the first structural force pulling GRASS out of supply — but until then, the vaults dominate and the token remains inflationary.

---

*MrNasdog Pressure Framework analysis of Grass (GRASS), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated August 2, 2026.*
