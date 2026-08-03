---
title: "AVAX Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description: "A MrNasdog Pressure Framework read of Avalanche (AVAX): ~2.9M staking mint per 90 days against only ~0.2M of fee burn and no buyback. Net +0.63%, projected +0.63% forward, versus a supply monitor stuck near flat at -0.09%."
canonical_url: "https://mrnasdog.com/research/avax/inflation"
tags: ["crypto", "avax", "avalanche", "proofofstake"]
published: true
---

> Originally published at **[mrnasdog.com/research/avax/inflation](https://mrnasdog.com/research/avax/inflation)** by MrNasdog.

Avalanche has one supply engine and one thin brake. Staking rewards mint about **2.9M AVAX** over 90 days — roughly **11.8M AVAX** a year to validators — while the C-Chain base-fee burn removes only about **0.2M**, and there is **no buyback**. The MrNasdog Pressure Framework reads **+0.63% net**, mildly inflationary under a **720M** hard cap. Our supply monitor reads about **-0.09%**, a gap of roughly **0.71 percentage points**, because the market-data supply feed it uses has sat flat near **432M AVAX** while the chain keeps minting.

## The verdict, in one paragraph

For the 90-day window ending **Aug 3 2026**, the MrNasdog Pressure Framework reads **Avalanche at +0.63% net**. Sell pressure is **2.9M AVAX** of newly minted staking rewards, buy pressure is the **0.2M AVAX** base-fee burn, against a circulating base of **431.8M AVAX**, with the forward window projected at the same **+0.63%**. Our supply monitor reads about **-0.09%**, a gap of roughly **0.71 percentage points**, so a monitor-gap flag ships with this page. The gap is not a disagreement about mechanism — it is a flat data feed: the monitor derives supply from market cap over price, and that figure has stayed near **432M AVAX** across the window even though staking mints new AVAX every period. On-chain, Avalanche has minted **463.4M AVAX** of its **720M** cap, and its own tokenomics proposal, ACP-285, puts trailing one-year inflation near **5.5%**. AVAX is best characterised as **steadily inflationary by staking, with only a thin burn to offset it** — a slow, predictable drift rather than a cliff.

## Sell pressure: where new AVAX comes from

Sell #1, protocol inflation, is **2.9M AVAX**, and it is the entire sell side. Avalanche mints new AVAX as staking rewards, paid directly to validators and delegators each staking period out of a genesis-defined reward pool that runs toward the **720M** cap. With roughly **196M AVAX** staked — about **41.5%** of supply — earning near **6%** a year, the network issues on the order of **11.8M AVAX** annually, or about **2.9M** over the 90-day window. Those coins are liquid the moment they are paid, so the mint is genuine new float. The rate held constant across the window: the proposal to lower the reward floor, ACP-285, is still in discussion and has not activated, so issuance ran at the standing 10% minimum consumption rate throughout, and the trailing pace equals the live pace.

The remaining sell rows are all **zero**. Sell #2, vesting unlocks, is zero because Avalanche's genesis vesting is largely spent: the Ava Labs team allocation finished its four-year lockup around **Sept 2024**, and the strategic-partner, private and seed rounds vested years ago on one-to-two-year schedules, so no team or investor cliff lands in this window. Sell #3, foundation and unscheduled unlocks, is zero as a market figure — the still-locked genesis supply is Foundation-controlled and treated as overhang below rather than as observed selling. Sell #4, long-term locked or bankruptcy, is zero: there is no Avalanche estate, no trustee and no court-ordered AVAX distribution.

## Buy pressure: where new AVAX goes

The buy side is almost as quiet. Buy #1, programmatic buyback, is **zero** — Avalanche has never run a buyback, and no treasury bought AVAX on the open market during the window. Buy #2, protocol fee burn, is the one active offset: every C-Chain transaction burns its base fee in the EIP-1559 style, permanently destroying the AVAX paid. Since the base-fee cut in ACP-125, daily burns run only about **1,000** to **8,000 AVAX**, so roughly **0.2M** was burned over 90 days — real, but far smaller than the **2.9M** minted, so it only lightly offsets staking. Buy #3, foundation buy, is zero because no Avalanche Foundation open-market purchase has been disclosed. Buy #4, new long-term lock, is zero because staking is a delay, not a lock: bonded AVAX can be withdrawn after a short unbonding period and counts as circulating the whole time. With the burn thin and everything else at zero, the staking mint runs nearly unopposed.

## Foundation and overhang

Avalanche's tracked overhang is the piece of genesis supply still locked: roughly **31.7M AVAX**, the difference between the **463.4M** minted and the **431.8M** circulating. This is the Foundation and ecosystem endowment on a ten-year vest that runs into about **Sept 2030**, with the next scheduled release near **Aug 10 2026**. Those unlocks land in the Foundation treasury and fund grants and ecosystem work rather than open-market dumps, and no discretionary AVAX sale was observed in the trailing year, which is why Sell #3 is zero rather than a projected number. The balance is re-read on every rebuild, and if a Foundation wallet is seen selling into the market between refreshes, that outflow enters Sell #3 at the next refresh. Note that these coins already exist inside total supply — when they unlock they move locked to liquid, they are not newly minted, so they are counted as overhang here and never double-booked into the staking-mint row above.

## How AVAX compares to other capped-supply staking L1s

The first comparison is cap versus no cap. Avalanche shares the hard-cap idea with the halving chains — a fixed **720M** ceiling AVAX asymptotically approaches — but its issuance path is nothing like a halving. Instead of a step-down every few years, Avalanche mints continuously as staking rewards, and the rate falls only slowly as circulating supply climbs toward the cap. That makes AVAX inflationary today in a way a post-halving fixed-issuance coin is not, even though both carry a ceiling. The cap bounds the endgame; it does not stop the drift now.

The second comparison is burn versus no burn. Some smart-contract L1s pair emission with an aggressive base-fee burn that can flip net supply negative on a busy day; Avalanche has the same EIP-1559 burn plumbing, but after the ACP-125 base-fee cut its burn is thin — about **0.2M AVAX** a quarter against **2.9M** minted. So where a high-throughput fee-burner can be structurally deflationary, AVAX sits in the pure-emission camp, offset only lightly, until either activity rises sharply or governance adds a stronger sink. The pending ACP-285, which would cut the minimum reward rate and is projected to trim inflation by **0.5** to **1** percentage point a year, is the clearest lever on the table.

The third comparison is what the market data shows. Unlike coins whose headline risk is a lumpy monthly unlock calendar, AVAX's subtler issue is that its widely-quoted circulating figure has stayed near **432M** while the chain minted past **463M**. An observer trusting the headline supply would read AVAX as flat when it is in fact drifting up every staking period. The framework reads the chain, not the frozen feed, which is the whole reason the two numbers disagree by more than half a point.

## What to watch in the next 90 days

First, ACP-285: if the proposal to lower the minimum consumption rate from **10%** to **7.5%** activates at a network upgrade, forward issuance re-bases lower and the net reading softens. Second, the amount staked — issuance scales with it, and the recent **196M** sits in a **183M**–**225M** band, so a move either way shifts the mint. Third, the base-fee burn: a sustained rise in C-Chain activity would thicken the only offset AVAX has. Fourth, the Foundation unlock near **Aug 10 2026** — harmless while it stays in treasury, but a Sell #3 event if it reaches the market. Fifth, whether the quoted circulating figure un-freezes from **432M**; the day the market data catches up to the real on-chain supply, the monitor gap on this page closes on its own.

## Summary

The MrNasdog Pressure Framework reads AVAX at **+0.63% net** over 90 days and projects the same for the next 90. The structure is simple: staking mints about **2.9M AVAX** a quarter, roughly **11.8M** a year, and only a thin **0.2M** base-fee burn and no buyback offset it, so supply drifts steadily upward. The key risk is not a vesting cliff — genesis vesting is nearly spent — but the absence of a strong sink, which the pending ACP-285 reward cut could partly address. The ceiling is the **720M** hard cap the chain is minting toward, now at **463.4M**. The market-data supply feed, stuck near **432M**, understates all of this, which is why our monitor reads near flat while the chain is not.

---

*MrNasdog Pressure Framework analysis of AVAX, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 3 2026.*
