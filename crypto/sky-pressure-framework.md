---
title:         "SKY Inflation Analysis · August 2026 · Supply was growing · trend cooling"
description:   "SKY nets +0.76% over 90 days: 234.9M of staking rewards out, 57.4M bought back into the DAO treasury and never burned. On-chain supply flat since Jul 2025."
canonical_url: "https://mrnasdog.com/research/sky/inflation"
tags:          ["crypto", "sky", "makerdao", "defi"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/sky/inflation](https://mrnasdog.com/research/sky/inflation)*

# SKY Inflation Analysis · August 2026 · Supply was growing · trend cooling

Sky, the protocol formerly called MakerDAO, has not created or destroyed a single **SKY** in thirteen months: the token's on-chain supply has read exactly **23,462,665,147** at both ends of this window and has not moved since **Jul 2025**. What looks like inflation is one balance emptying — the DAO treasury paid **234.9M SKY** of staking rewards into the market over 90 days while the Smart Burn Engine bought **57.4M SKY** back into that same treasury, for a net of **+0.76%** against our monitor's **+0.92%**. The Smart Burn Engine, despite its name, burns nothing. And the reserve it feeds is down to **55.0M SKY**, which is why the forward read cools to **+0.23%**.

## The verdict, in one paragraph

Over the trailing 90 days the SKY ledger books **234.9M SKY** of sell pressure against **57.4M SKY** of buy pressure on a circulating float of **~23.41B SKY**, a net of **+0.76%**. Our supply monitor independently reads **+0.92%** over the same window, a gap of **0.165** percentage points — comfortably inside tolerance, so no data-conflict flag is raised, and the residual is rounding noise on a 23-billion base. Both numbers are measuring the same single event: the DAO's treasury balance fell from **232.6M SKY** to **55.0M SKY**, and every coin that left it entered the float. The label for SKY today is a **closed-loop float release** — a token with zero issuance and zero destruction, whose entire supply reading is one reserve draining, partly refilled by its own buyback.

## Sell pressure: where new SKY comes from

It does not come from a mint. Sky's Sell #1 of **234.9M SKY** is the staking-rewards stream: the DAO treasury transfers SKY to the rewards distributor once a week, and stakers claim it. Those transfers ran at **18.6M SKY** a week from **May 18 2026** through **Jul 20 2026**, then stepped up to **22.3M SKY** a week from **Jul 27 2026**. The step-up is not a decision to emit more. Sky sets the reward as a fixed dollar amount — a share of net revenue, most recently **5,892,250 USDS** for the month — and reprices it into SKY at the previous month's average price. SKY fell, so the same dollars now buy more tokens to hand out. That is the single most important mechanical fact about SKY inflation: a lower SKY price automatically increases the number of SKY emitted.

The other three sell rows are measured zeros rather than assumed ones. Vesting unlocks are **0** because SKY has no vesting calendar in existence: it was issued one-for-24,000 against the predecessor MakerDAO governance token, so there is no venture, team or seed tranche waiting behind a cliff, and Sky's treasury vesting contract holds zero SKY. Foundation and unscheduled unlocks are **0** because a full reconciliation of every SKY transfer in and out of the DAO treasury this window returns exactly one outbound counterparty — the rewards distributor already counted above — and no discretionary transfer at all. Long-term locked or bankruptcy is **0** because Sky has no bankruptcy estate and no locked tranche unwinding.

## Buy pressure: where new SKY goes

Sky's Smart Burn Engine routes the protocol surplus into open-market SKY purchases in **6,000 USDS** clips. This window it executed **561** of them — **3.37M USDS** spent, **57.4M SKY** bought, an average fill around **$0.0586**. That is Buy #1, and it counts as real absorption for one specific reason: the bought SKY is delivered to the DAO treasury, and the treasury is the only balance the market does not count as circulating. Take SKY off the exchange and put it in that address and the float genuinely shrinks.

Protocol fee burn is **0**, and this is the correction that matters most on SKY. The Smart Burn Engine does not burn. Sky's on-chain total supply has been pinned at **23,462,665,147** SKY since **Jul 2025**; not one token has been destroyed. The engine's receiver address is the DAO treasury, and the DAO pays that same treasury straight back out as staking rewards. The buyback and the reward stream are the same coins going round in a circle — **1.83B SKY** has been bought back cumulatively since the programme began, and essentially all of it has been recycled into the float again. Foundation buy is **0** because the programmatic engine is the only protocol bid, and it is already counted. New long-term lock is **0**: **10.21B SKY** is staked in Sky's staking engine and rose **131.1M** this window, but stakers can withdraw and staked SKY sits inside circulating supply either way.

## Foundation and overhang

SKY has two identified overhangs and neither is a conventional insider allocation. The first is the DAO treasury itself at **55.0M SKY** — the reserve that pays the rewards, the destination of the buyback, and the only SKY the market does not already count. It is read from the chain on every rebuild. The second is the MKR-to-SKY upgrade contract, which holds **2.15B SKY** against the **88,146** predecessor tokens still un-upgraded; about **34.1M SKY** of that is spare beyond what the outstanding claims require. Both are on-chain and read directly, not inferred. The forward risk here is unusual: the treasury is not an overhang waiting to be dumped, it is a reserve about to run out. It has fallen from **232.6M SKY** to **55.0M SKY** in 90 days with no top-up since **Dec 2025**, and at **22.3M SKY** a week against roughly **4.5M SKY** a week coming back in from the buyback, it funds about three more weeks. If either overhang's balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How SKY compares to other revenue-funded buyback tokens

The instinctive comparison is to an exchange token running a quarterly buyback-and-burn, where the protocol buys its own token and destroys it. Those programmes show up as a falling total supply on-chain — the destruction is verifiable and permanent. SKY's engine looks similar from the outside and behaves completely differently underneath: the supply number does not fall, because the tokens are held rather than destroyed, and they are then re-emitted. A buyback that recycles is a transfer between holders, not a reduction. It supports the price at the moment of the buy and gives that support back at the moment of the reward payout.

The contrast with a fee-burn chain is sharper still. On an EIP-1559-style network the burn is a byproduct of usage, it is irreversible, and it competes directly with issuance, which is why such chains can print a genuinely negative net. SKY has no fee burn at all, so its only structural sink is discretionary spending out of surplus — and governance has throttled that spending hard, from the **$1M**-a-day era down to roughly **$37,400** a day across this window. Against other DeFi governance tokens funded by real revenue, Sky's distinguishing feature is not the size of the buyback but the direction of the loop: most peers either burn what they buy or hold it permanently, while Sky hands it back out. The second distinguishing feature is the price-linkage on the sell side — a fixed dollar reward repriced monthly into a falling token means SKY inflation accelerates exactly when the price is weakest, which is the opposite of the self-balancing behaviour a capped-supply model gives you.

## What to watch in the next 90 days

First, the treasury balance. At the current rate the reserve behind the rewards empties around **Sep 6 2026**; whether the DAO refills it, cuts the rate, or mints is the single largest swing factor in this reading. Second, the monthly settlement that reprices the reward — the next one lands around **Sep 16 2026**, and a lower SKY price at that moment means more SKY paid out, not less. Third, the mint authority: the DAO still holds it on the SKY token, so the **23.46B** figure is a governance-held ceiling rather than a hard cap, and any spell that lifts total supply would change this page's structure entirely. Fourth, the Smart Burn Engine's spending rate, currently **6,000 USDS** a clip at roughly six clips a day — a restoration toward earlier levels is the one realistic route to a negative net. Fifth, the un-upgraded predecessor tokens: **88,146** remain, and each conversion releases **24,000 SKY** from the upgrade contract into holder hands.

## Summary

SKY is a fixed-supply token with a moving float. On-chain supply has been unchanged at **23,462,665,147** since **Jul 2025**, so the framework's **+0.76%** reading over the last 90 days and **+0.23%** forward describe a reserve emptying into the market, not issuance. The structural mechanism is a closed loop: the Smart Burn Engine buys **57.4M SKY** into the DAO treasury and the DAO pays **234.9M SKY** straight back out as staking rewards, so what is marketed as a burn is a recycle. The key risk is the price linkage — the reward is fixed in dollars and repriced monthly, so a falling SKY price mechanically increases the SKY emitted — compounded by a treasury that funds roughly three more weeks at the current rate. The ceiling is **23.46B SKY**, but it is a governance-held ceiling, not a protocol-encoded cap: the DAO retains mint authority on the token.

---

*MrNasdog Pressure Framework analysis of SKY, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 17 2026.*
