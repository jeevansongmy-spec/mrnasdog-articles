---
title: "JASMY Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description: "JASMY supply is roughly steady at 0.00% net over 90 days: a fixed 50B supply with no mint, no unlock and no burn. One 555.0M issuer wallet is the only overhang."
canonical_url: "https://mrnasdog.com/research/jasmy/inflation"
tags: ["crypto", "jasmy", "tokenomics", "ethereum"]
published: true
---

Originally published at [JASMY Inflation Analysis · September 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/jasmy/inflation).

# JASMY Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

The MrNasdog Pressure Framework reads JasmyCoin (JASMY) at **0.00% net** over the last 90 days and **0.00%** over the next 90: no JASMY was created, none was released from a locked wallet, and none was burned or bought back. The reason is structural — the JASMY token on Ethereum has a fixed supply of **50B** that no function can raise, and **49.44B** of it already counts as circulating. The one limit on that calm reading is a single issuer wallet holding **555.0M JASMY** with no public release plan.

## The verdict, in one paragraph

Over the 90 days from Jul 1 2026 to Sep 29 2026, JASMY sell pressure was **0 JASMY** and buy pressure was **0 JASMY**, for a net supply change of **0.00%** of the **49.44B** circulating coins. Our supply monitor, which tracks the circulating count day by day, read **+0.01%** over the same stretch — a gap of about **0.01 percentage points**, well inside the 0.5-point tolerance, so no data-conflict flag is shown. The next 90 days project the same **0.00%**, because nothing on the JASMY calendar mints, unlocks or burns coins. JASMY is a fixed-supply token with a quiet ledger: every move this quarter happened between wallets that were already part of the market.

## Sell pressure: where new JASMY comes from

Protocol inflation is **0 JASMY**, and it can stay nowhere else. JasmyCoin is a plain ERC-20 token on Ethereum. All 50B JASMY were minted once, on Dec 26 2019, into the issuer wallet. We read the token contract directly: total supply sat at exactly **50,000,000,000** at both ends of the window, the number lives in ordinary contract storage rather than being hard-coded, and the contract exposes only the eleven standard token functions — no mint, no owner, no upgrade path. JASMY has no block rewards and no staking emission, so there is nothing for the network to pay out in new coins.

Vesting unlocks are **0 JASMY**. No JASMY vesting calendar exists: the unlock trackers show no schedule and no next unlock date, and about **98.9%** of all coins are already counted as circulating. Foundation and unscheduled unlocks are also **0 JASMY**. The issuer wallet that received the original mint still holds **555.0M JASMY**, and it did not move at all in the window — its last release was **50M JASMY** on Jan 16 2025, more than a year ago. Long-term locked or bankruptcy supply is **0 JASMY**: there is no estate, no trustee and no expiring lock. Large holders and exchange wallets did shift coins — one wallet took 250M JASMY off an exchange on Sep 16 2026 and passed 43.5M on — but those coins were already inside the circulating count, so they add no new supply.

## Buy pressure: where new JASMY goes

Programmatic buyback is **0 JASMY**. Jasmy has no buyback programme, and no official post or wallet flow this window shows JASMY being bought back and taken out of the market. The protocol fee burn is also **0 JASMY**. We checked both burn surfaces: the Ethereum burn address held the same **315 JASMY** at both ends of the window, and total supply did not fall by a single coin. JasmyChain — the Jasmy Layer 2 built on Arbitrum Orbit, live since Jan 17 2026, where JASMY is the gas coin — pays its fees to two operator accounts that can spend them; it does not destroy gas. The chain is still small, with about 17,000 transactions since launch.

Foundation buy is **0 JASMY**: no announcement or on-chain flow shows the Jasmy company buying JASMY off the market. New long-term lock is **0 JASMY**. JASMY bridged to JasmyChain is backed one-for-one by JASMY held in the bridge on Ethereum, and those coins stay inside the circulating count, so moving to the Layer 2 locks nothing away. The earlier Jasmy plan to lock tokens at an exchange account also keeps them in the market count.

## Foundation and overhang

JASMY has exactly one tracked overhang: the issuer wallet that received all 50B JASMY in 2019. It now holds **555,000,322 JASMY**, and that balance matches, to the coin, the gap between total supply and the circulating count — so it is the whole of the JASMY supply that sits outside the market. It carries no release schedule. Over its life it has sent coins out in bursts — large distributions in 2020, tranches of 40M–700M JASMY from Jun to Nov 2023, then 95M JASMY in Sep 2024 and 50M JASMY in Jan 2025 — since 2023 always through the same forwarding wallet. That history makes it a real overhang, but with no firing in the last year it books zero for the coming 90 days. We read this wallet from the chain at every rebuild; if its balance falls between refreshes, the outflow enters Sell #3 as new supply at the next refresh.

## How JASMY compares to other fixed-supply utility tokens

JASMY belongs to the family of fixed-supply ERC-20 utility tokens, where everything was minted up front and the only supply question is when held-back coins reach the market. That is a very different shape from an uncapped proof-of-stake coin such as Ethereum's ETH, which creates new coins every block and relies on a fee burn to offset part of them, and from a halving coin such as Bitcoin, whose supply still grows on a fixed schedule toward its cap. With a fixed 50B JASMY and no mint path, JASMY cannot inflate from the protocol at all.

The comparison that matters is with other fixed-supply tokens that still carry large vesting calendars. Many newer tokens have 50% or more of supply locked and release a fixed slice each month, which shows up as steady sell pressure. JASMY is at the other end: about **98.9%** of supply already circulates, and the one remaining 555.0M JASMY pile has no calendar. The trade-off is that JASMY also has no buyback and no burn, unlike exchange tokens that remove coins every quarter. So the JASMY supply neither grows nor shrinks on its own; its reading moves only if the issuer wallet releases coins or Jasmy adds a burn.

## What to watch in the next 90 days

First, the **555.0M JASMY** issuer wallet: any outflow would be the first new JASMY supply since Jan 2025 and would enter the sell ledger at once. Second, exchange access: Upbit and Bithumb ended JASMY trading on Sep 14 2026 with withdrawals open until about Oct 14 2026, and BITPOINT and SBI VC Trade in Japan stop JASMY buying on Oct 7 2026 and end sales and withdrawals on Oct 28 2026 — these move coins already in the market, so they change who holds JASMY, not how much exists. Third, JasmyChain fees: a change that sent gas to a burn instead of to operator accounts would create the first JASMY buy pressure. Fourth, the planned JANCTION GPU network and the AppBank partnership announced on Sep 28 2026, which could lift JASMY use on the Layer 2 but add no supply by themselves.

## Summary

JASMY supply was flat at **0.00%** over the last 90 days and is projected flat for the next 90, with our monitor in agreement at **+0.01%**. JasmyCoin is a fixed-supply ERC-20 token of **50B JASMY** with no mint function, no vesting calendar, no buyback and no burn, and **49.44B** of it already circulates. The key risk is the issuer wallet holding **555.0M JASMY** — about 1.1% of circulating supply — which has no public plan and last released coins in Jan 2025. The hard ceiling is 50B JASMY: supply can never exceed it, and it can only fall if Jasmy starts burning coins.

*MrNasdog Pressure Framework analysis of JASMY, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*
