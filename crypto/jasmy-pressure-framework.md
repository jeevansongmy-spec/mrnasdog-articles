---
title:         "JASMY Inflation Analysis · August 2026 · Supply flat, projected to stay flat"
description:   "JasmyCoin is a fixed 50B ERC-20 with no mint and no burn, total supply exactly 50B across 90 days. Framework 0.00%, monitor +0.235% — pure rounding noise. All eight ledger rows zero."
canonical_url: "https://mrnasdog.com/research/jasmy/inflation"
tags:          ["crypto", "jasmy", "jasmycoin", "erc20"]
published:     true
---

*Originally published at [mrnasdog.com/research/jasmy/inflation](https://mrnasdog.com/research/jasmy/inflation)*

JasmyCoin is a fixed **50 billion** ERC-20 on Ethereum, and reading the contract directly shows total supply held at exactly **50B** at both ends of the last 90 days — no new tokens were created and none were burned. All eight Pressure Framework rows read **zero**, so the framework reads **0.00% net** against our supply monitor at **+0.235%**, a gap of **0.235 percentage points** that is pure market-cap-to-price rounding noise on a fixed supply and stays inside tolerance, so no monitor-gap chip ships. With **98.9%** of supply already circulating, no mint function and no fee burn, JASMY is about as structurally quiet as a token gets.

## The verdict, in one paragraph

For the 90-day window ending Aug 3 2026, the Pressure Framework reads **JASMY at 0.00% net**. Sell pressure is **zero** and buy pressure is **zero**, against a circulating base of **49.44B JASMY**. Our supply monitor reads **+0.235%**, a gap of **0.235 percentage points** that comes entirely from the monitor deriving supply as market cap divided by price — a figure that jitters day to day around a constant 49.44B even when the real token count never moves. The confirmation is on-chain and exact: JASMY's total supply returned exactly **50,000,000,000** at both block heights bounding the window, the contract exposes no working mint authority, and the burn address held the same **315 JASMY** start to finish. JASMY is best characterised as **a fixed-supply token with nothing added and nothing removed** — flat by construction.

## Sell pressure: where new JASMY comes from

Nowhere — and that is the finding. Sell #1, protocol inflation, is **zero**: JASMY is a fixed 50B ERC-20 minted once at genesis, with no staking emission, no block reward and no live mint function, and the on-chain total supply read exactly **50B** at both ends of the window. Sell #2, vesting unlocks, is **zero**: the early team, investor and ecosystem allocations were distributed years ago, and there is no live vesting cliff still releasing tokens into the market.

Sell #3, foundation and unscheduled unlocks, is **zero** but carries the one thing worth watching. Roughly **555M JASMY** — about 1.1% of supply — sits outside circulation as an undistributed reserve. It has no published release schedule and showed no outflow across the trailing year, so under the framework's evidence rule it is a monitored overhang rather than active sell pressure, and the row stays at zero until a release is actually observed. Sell #4, long-term locked or bankruptcy, is **zero**: there is no estate, trustee distribution or court-ordered JASMY tranche anywhere in the picture.

## Buy pressure: where new JASMY goes

Also nowhere. Buy #1, programmatic buyback, is **zero**: JasmyCoin runs no protocol buyback. A promoted "buyback and burn" scheme circulating on social media is an unrelated Binance-Smart-Chain pledge program on a different contract that asks users to stake BNB for percentage bonuses — a promotional scheme, not a Jasmy protocol mechanism, and it does not touch the Ethereum token measured here. Buy #2, protocol fee burn, is **zero**: the deployed ERC-20 has no fee-burn function, and the burn address balance was identical at both ends of the window. The one real burn in the Jasmy ecosystem is on the separate **JasmyChain** Layer-2, where a MemePad destroys about 10 JASMY per token launch — a quantity too small to register and, crucially, off the Ethereum token that defines circulating supply.

Buy #3, foundation buy, is **zero**: no Jasmy entity has disclosed an open-market JASMY purchase program, and no accumulation wallet has been identified. Buy #4, new long-term lock, is **zero**: no new lockup or staking-vault contract removed JASMY from the float over the window. With both sides of the ledger empty, there is no offset to compute — the token neither grows nor shrinks.

## Foundation and overhang

There is exactly one item to enumerate: the **~555M JASMY** non-circulating reserve, the difference between the 50B total supply and the 49.44B counted as circulating. It has no published release schedule, so its status is unscheduled, and it is tracked on a chain-read cadence. The trigger condition is simple: if that reserve's balance falls between refreshes — that is, if the undistributed remainder starts moving onto the market — the outflow enters Sell #3 at the next refresh and the framework re-rates from flat to mildly inflationary. As of this build it has not moved, sitting at the identical balance at both ends of the window, so it remains a monitored overhang and nothing more.

## How JASMY compares to other fixed-supply tokens

The cleanest comparison is to other hard-capped ERC-20s that finished distribution. Unlike an uncapped Layer-1 such as Ethereum or Solana, which mints new coins every block to pay validators, JASMY has no issuance engine at all — its 50B was created once and the contract cannot add to it. That puts it in the same structural bucket as fully-distributed governance tokens whose emission has ended: the supply question is settled, and the only live variables are custody and lockups, not issuance.

It differs from deflationary burn tokens in the other direction. A token with an EIP-1559-style fee burn or a revenue-funded buyback-and-burn actively shrinks its float, scoring higher on the framework because net supply falls. JASMY has neither on its Ethereum contract, so it does not shrink — it holds. The JasmyChain L2 introduces a token-launch burn, but at current volume it is immaterial and, because it does not reduce the Ethereum ERC-20, it does not move this reading; it would only matter if a large, sustained share of JASMY were bridged and burned on the L2, which is not the case today.

Finally, it differs from vesting-heavy tokens still working through unlock cliffs. Many top-200 assets carry a schedule that drips team and investor allocations into circulation for years, producing persistent structural sell pressure. JASMY's distribution is essentially complete at 98.9% circulating, so there is no unlock overhang beyond the single static reserve — the supply-side risk that dominates younger tokens simply does not apply here.

## What to watch in the next 90 days

First, the **~555M** non-circulating reserve: any transfer out of it is the only event that would flip JASMY from flat to inflationary, so a change in that balance is the single most important thing to monitor. Second, JasmyChain adoption: if a large volume of JASMY were bridged to the L2 and burned through MemePad and gas at scale, a genuine deflationary force could emerge — worth tracking even though it is negligible today. Third, any contract-level change: JASMY's supply is fixed by the deployed code, so a new token contract, a migration, or a wrapped-supply program would be the only way issuance could ever restart. Fourth, exchange and custody reclassification: because the monitor derives supply from market data, a large custody or classification shift could move the reported circulating figure without any real token creation. None of these has a scheduled date; all are watch lines rather than events.

## Summary

JasmyCoin (JASMY) is a fixed-supply token that neither grows nor shrinks: the on-chain total supply held at exactly **50B** across the 90-day window, all eight ledger rows read zero, and the framework reads **0.00% net** against a monitor reading of **+0.235%** that is rounding noise, not real issuance. The defining feature is structural absence — no mint function, no vesting cliff, no fee burn and no buyback — so the only supply lever is a single **~555M** reserve that has stayed put. The key risk is mild and one-directional: if that reserve begins to move, JASMY tips from flat to slightly inflationary; absent that, supply is capped at 50B and effectively frozen at today's 98.9% circulating.

---

*MrNasdog Pressure Framework analysis of JASMY, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 3 2026.*
