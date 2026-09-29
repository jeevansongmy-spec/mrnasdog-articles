---
title:         "BGB Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "BGB supply is steady at 0.00% over 90 days. No new BGB can be minted, and the 3.01M BGB Morph burn came from a locked reserve, so the 700.0M float did not move."
canonical_url: "https://mrnasdog.com/research/bgb/inflation"
tags:          ["crypto", "bgb", "bitget", "exchange"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/bgb/inflation](https://mrnasdog.com/research/bgb/inflation)*

# BGB Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

BGB supply held flat: **0.00%** net over the last 90 days, and **0.00%** projected for the next 90. The Bitget Token contract can never mint a new BGB, no team or investor tranche is left to vest, and the Morph quarterly burn — **3,010,400 BGB** on Jul 14 2026 — was paid out of the locked Morph Foundation reserve, so the **700.0M BGB** circulating float did not move. The monitor reads **+0.28%**, within tolerance.

## The verdict, in one paragraph

Over the 90 days from Jul 1 to Sep 29 2026 the MrNasdog Pressure Framework reads BGB at **0.00%** net: **0 BGB** of new sell pressure against **0 BGB** of buy pressure on a circulating supply of **699.99M BGB**. The next 90 days project the same **0.00%**. The supply monitor reads **+0.28%** for the same stretch, a gap of **0.28** percentage points — inside the 0.5-point tolerance, so no warning chip is shown. The monitor's small rise comes from dividing market value by price day to day; on-chain, the circulating BGB count was identical to the single coin at both ends of the window. BGB is a **fixed-supply exchange token with a burn that runs outside the float**.

## Sell pressure: where new BGB comes from

Protocol inflation is **0**. BGB has no block rewards and no staking emission. All 2B BGB were minted once, when the Bitget Token contract was deployed on Ethereum, and the contract carries only the standard token functions — there is no mint, no owner and no upgrade path. The on-chain total read exactly 2B at both ends of the window. BGB also lives on the Morph chain, but that copy only mirrors BGB locked in a bridge pool on Ethereum: **22.7M BGB** on each side, matching to the last decimal.

Vesting unlocks are **0**. No team, investor or sale allocation of BGB is still waiting on a cliff. The only locked BGB is the Morph Foundation reserve, which the Morph rules allow to release up to 2% a month for ecosystem programs. That 2% is a ceiling, not a timetable, and in the 13 months since the reserve was set up it has not sent a single coin to the market.

Foundation and unscheduled unlocks are **0**: the reserve's only outflows have been burns. Long-term locks and bankruptcy are also **0** — no estate or trustee holds BGB. The Sep 24 2026 hack of the Bitget exchange drained other coins from its hot wallets; it created and released no BGB.

## Buy pressure: where new BGB goes

The programmatic buyback is **0**. Bitget used to buy BGB on the market and burn it every quarter; the last of those burns, **30.0M BGB**, went through on Jul 15 2025. Since Bitget handed 440M BGB to the Morph Foundation in September 2025 — 220M burned at once, 220M locked — the exchange-funded burns have stopped.

The protocol fee burn is **0** on the float, and this is the key point of the BGB supply story. The Morph quarterly burn is real. Its size is Morph network fees divided by the average BGB price, times a governance factor and a large booster. For April to June 2026 that was $4,071 of fees at $1.92, times a booster of 1,420: **3,010,400 BGB**, sent to the burn address on Jul 14 2026. But every one of those coins came out of the locked Morph Foundation reserve, which was never part of the circulating count. Total supply fell; tradable supply did not. The earlier burns — 3,060,425 BGB in January 2026 and 3,000,330 BGB in April 2026 — came from the same reserve.

Foundation buying is **0**: the reserve received nothing in the window. New long-term locks are **0** too. BGB staking on Morph locks coins for 90 days, capped at 2M BGB, but staked BGB stays inside the circulating count.

## Foundation and overhang

The Morph Foundation reserve is the one overhang outside the float: **210.9M BGB** in a two-signature multisig, down from 213.9M at the start of the window, and it is the entire gap between the 910.9M total and the 700.0M circulating. We read its balance on-chain every day. If the reserve ever sends BGB anywhere other than the burn address, those coins enter the market and count as Foundation unlocks at the next refresh.

Inside the float sit large wallets we also watch. A Bitget-linked wallet holds about **229.5M BGB**, a third of the circulating supply, and 33 more multisig wallets hold between 3.5M and 54M each, about 383M together. Because the circulating count already includes them, their moves add nothing to this ledger, but a large sale from any of them would still hit the market price.

## How BGB compares to other exchange tokens

Among exchange tokens, the usual model is an exchange that buys its own token with part of its profit and burns it. That takes coins out of the hands of traders, so it shrinks the float. BGB ran that model until mid-2025. Today its burn is funded from a locked reserve instead, which shrinks total supply but leaves the tradable float untouched — a cap-table change, not buying pressure.

BGB also differs from exchange tokens that mint new coins for staking or validators. It has no issuance at all, so its float cannot grow from rewards. The only way new BGB can reach the market is a release from the Morph Foundation reserve, and that has not happened. Compared with a Layer 2 gas token that pays new coins to sequencers, BGB pays nothing out: gas on Morph is paid in existing BGB.

## What to watch in the next 90 days

The Morph quarterly burn for July to September 2026 is expected around mid-October 2026. Watch where it is paid from: from the reserve it changes nothing on the float; if it is ever paid with BGB bought on the market, it becomes real buy pressure.

Watch the Morph Foundation reserve at 210.9M BGB for any transfer that is not a burn — that would be the first real release. Watch the booster vote too: the Morph community can lower it as fees grow, which would make the burns smaller.

Watch the Bitget-linked wallet at 229.5M BGB after the Sep 24 2026 exchange hack, as Bitget refills its user protection fund from company reserves. And watch whether Bitget restarts buying BGB for its own burns; it has not done so since Jul 15 2025.

## Summary

BGB supply is steady at **0.00%** for the last 90 days and the next 90. The Bitget Token contract can never mint new BGB, nothing is left to vest, and the Morph quarterly burn is paid from a locked reserve of **210.9M BGB**, so it reduces total supply without shrinking the 700.0M BGB float. The main supply risk is that reserve being released rather than burned, together with a few large wallets already in the float. Supply can only fall from here: the 2B cap is fixed in code.

---

*MrNasdog Pressure Framework analysis of BGB, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*
