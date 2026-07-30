---
title: "OKB Inflation Analysis · July 2026 · Mixed flows, supply roughly steady"
description: "A MrNasdog Pressure Framework read of OKB: fixed at 21M with mint and burn removed from the token contract. Framework 0.00% net; the supply monitor agrees at −0.017%."
canonical_url: "https://mrnasdog.com/research/okb/inflation"
tags: ["crypto", "okb", "okx", "exchange-token"]
published: true
---

> Originally published at **[mrnasdog.com/research/okb/inflation](https://mrnasdog.com/research/okb/inflation)** by MrNasdog.

OKB, the OKX exchange token and the mandatory gas token of X Layer, has no mint function, no vesting calendar and no active burn — all three were settled in **August 2025** when OKX fixed the total supply at **21 million** and upgraded the token contract to remove both minting and burning. Over the 90 days to **Jul 30 2026** nothing was issued and nothing was retired, so the MrNasdog Pressure Framework reads OKB at **0.00% net** on a **21M** float. Our independent supply monitor reads **−0.017%** across the same window — a gap of **0.02 percentage points**, which is agreement, not conflict.

## The verdict, in one paragraph

For the 90-day window ending **Jul 30 2026**, the Pressure Framework reads **OKB at 0.00% net**: every sell row and every buy row in the OKB ledger is zero. Nothing mints OKB, no vesting remains, no reserve is being released, and — since the **Aug 18 2025** contract upgrade removed the burn function — nothing is being retired either. Our supply monitor reads the realized change at **−0.017%** over the same window, and the gap between the two readings is **0.02 percentage points** — well inside the framework's half-point tolerance, so OKB ships with **no monitor-gap flag**. The label for OKB is **fixed by contract**: a hard 21 million cap that no longer grows and no longer shrinks. This is a Bitcoin-style scarcity story with one asterisk, covered below.

## Sell pressure: where new OKB comes from

It does not come from anywhere, and that is the defining fact about OKB today. Sell #1, protocol inflation, is **zero**. OKB is not a blockchain — it is a token issued by the OKX exchange — so there are no block rewards, no staking emissions and no security budget denominated in OKB. Even the theoretical route to new supply is closed: the mint function was stripped out of the OKB token contract in the **Aug 18 2025** upgrade, so the implementation cannot create a single new unit. Sell #2, vesting unlocks, is **zero** for a structural reason and is the one row the framework marks permanent: the original OKB allocation finished vesting back in **2018**, all 21 million is already unlocked, and there is no team, seed or treasury release calendar left to run down.

Sell #3, Foundation and unscheduled unlocks, is **zero** and, unusually, there is no meaningful overhang behind it. When OKX fixed the supply at 21 million it did so by burning **65,256,712** OKB drawn from its historical repurchases and treasury reserves, so the large exchange-controlled stockpile that used to sit off to the side was destroyed rather than parked. There is no non-circulating bucket left — circulating supply equals total supply equals the cap, all three at 21 million — and no identified OKX wallet carries a published release schedule. Sell #4, long-term locked or bankruptcy, is **zero**: no bankruptcy estate holds OKB and no trustee distribution schedule exists. Four sell rows, four zeros, and none of them rests on a judgement call.

## Buy pressure: where new OKB goes

There is no active buy pressure either, which is the deliberate consequence of the August 2025 redesign. Buy #1, programmatic buyback, is **zero**. For years OKB ran a quarterly buyback-and-burn funded by OKX profits — that programme is retired, and the burn function itself was removed from the token contract in the same **Aug 18 2025** upgrade that removed minting, so there is no on-chain mechanism left to retire OKB even if OKX wanted to. Buy #2, protocol fee burn, is **zero**: OKB is the mandatory gas token of X Layer, but X Layer does not burn its gas the way an EIP-1559 base fee does — gas paid in OKB accrues to the sequencer and is recycled, not destroyed, so on-chain usage does not shrink the supply.

Buy #3, Foundation buy, is **zero**: OKX runs no open-market OKB accumulation programme, and the old buyback was wound down precisely because the supply is now fixed. Buy #4, new long-term lock, is **zero**: OKB has no staking-lock or escrow mechanism, and none was announced in the window. Every buy row is zero, and every zero is structural rather than a quiet quarter — the mechanisms that could move these rows have been removed from the contract, not merely paused.

## Foundation and overhang

The overhang picture for OKB is unusually clean, and it is worth stating why. The historical concern with an exchange token is the exchange's own reserve — a large treasury of unissued or repurchased tokens that could be sold into the market. For OKB that reserve no longer exists as an overhang: the **65,256,712** OKB that OKX held from past buybacks and treasury was burned outright in **August 2025**, cutting total supply by roughly 76% in a single event and leaving a float of exactly **21,000,000**. There is no Foundation multisig, no unscheduled-unlock pool and no DAO treasury with a published schedule that the framework can enumerate as team-controlled supply.

The one asterisk is the contract itself. The OKB token is an upgradeable proxy, and an on-chain read this cycle shows its owner/admin slots are still populated — the mint and burn functions were removed at the **implementation** level, not made immutable. So the correct reading is that OKB's fixed supply is a policy enforced by code that a live contract owner could, in principle, replace. That is why the framework tags these rows **checked** rather than permanent: nothing in the current implementation can issue or burn OKB, but the authority to change the implementation has not been renounced. If that authority were ever used to re-add a mint, it would surface here first.

## How OKB compares to other exchange tokens

OKB now sits in a small class of **fixed-supply exchange tokens**, and the comparison that matters is with how other exchange tokens manage supply. The most common model is a recurring buyback-and-burn: BNB runs an automatic quarterly burn tied to on-chain activity and a real-time gas burn, and LEO runs a continuous buyback funded by a share of exchange revenue. Both of those tokens are deflationary — their supply falls over time — but both depend on the exchange keeping the programme running, and both leave a live burn mechanism in the contract. OKB has taken the opposite path: rather than burn a little each quarter forever, it did one enormous terminal burn, fixed the number at 21 million, and then removed the machinery entirely.

Against those peers, OKB reads flat at **0.00%** where BNB and LEO read mildly negative, so on a pure supply-pressure basis OKB is very slightly worse than a token that is still actively shrinking — a fixed cap is favourable, but a falling supply is marginally more so. The far more useful comparison is with Bitcoin, whose 21-million cap OKB is consciously imitating: both have a hard ceiling and no path to new issuance in the running code. The mechanism differs in one way that the framework cares about — Bitcoin's cap is enforced by a decentralised consensus that no single party can rewrite, whereas OKB's cap is enforced by an upgradeable contract with a live owner. Same number, different immutability guarantee.

## What to watch in the next 90 days

First, watch the token contract owner for any upgrade transaction: because the mint and burn functions were removed at the implementation level rather than made immutable, a contract upgrade is the only event that could change OKB's supply mechanics, and it would be visible on-chain before any announcement. Second, watch X Layer for any change to its gas policy — if OKX ever introduced a fee burn on X Layer gas paid in OKB, that would turn Buy #2 positive and make the token genuinely deflationary. Third, watch for any renewed buyback announcement; OKX explicitly retired the programme when it fixed the supply, so a reversal would be a material signal. Fourth, expect the framework and the supply monitor to keep agreeing near flat, both hovering within a couple of hundredths of a percent of zero as the derived supply series rounds around 21 million.

## Summary

OKB is a fixed-supply exchange token whose supply neither grows nor shrinks: OKX burned the token down to a hard **21 million** cap in **August 2025** and upgraded the contract to remove both minting and burning, the vesting finished in 2018, and X Layer gas is not burned. Over the 90 days to **Jul 30 2026** the framework reads **0.00% net**, matched by the supply monitor at **−0.017%**. The structural strength is a Bitcoin-style hard cap with no live issuance path; the structural risk is that the cap is enforced by an upgradeable contract whose owner slot is still populated, so the guarantee is a policy in code rather than true immutability. The ceiling on the story is simple arithmetic: with nothing minting and nothing burning, 21 million is where OKB stays until the contract owner acts.

*MrNasdog Pressure Framework analysis of OKB, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 30 2026.*
