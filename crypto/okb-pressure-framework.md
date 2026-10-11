---
title:         "OKB Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "OKB supply is flat: no new OKB minted and no burn, so 0.00% net over 90 days and the same next. 21M coins, all unlocked, since OKX's 2025 reset."
canonical_url: "https://mrnasdog.com/research/okb/inflation"
tags:          ["crypto", "okb", "okx", "layer2"]
published:     true
---
# OKB Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

*Originally published at [https://mrnasdog.com/research/okb/inflation](https://mrnasdog.com/research/okb/inflation)*

<!-- main-page -->
➜ Start with the OKB coin page for the short answer (should you buy OKB?) and its price drivers: [mrnasdog.com/research/okb](https://mrnasdog.com/research/okb)

The MrNasdog Pressure Framework reads OKB, the gas token of OKX's X Layer network, as **flat at 0.00%** over the last 90 days and the next 90: **0 OKB** of new supply against **0 OKB** removed, with **21M OKB** in circulation and all of it unlocked. OKX fixed the OKB supply at 21 million in August 2025, after a one-time burn of **65.26M OKB**, and removed the mint function from the token contract. Since then nothing adds OKB and nothing takes it away: there is no block reward, no vesting, no buyback and no fee burn. The inflation monitor agrees at **+0.01%**.

## The verdict, in one paragraph

OKB supply moved **0.00%** net over the 90 days from Jul 13 2026 to Oct 11 2026, and we project **0.00%** for the next 90 days to Jan 9 2027. The inflation monitor, which reads circulating supply day by day, shows **+0.0055%** over its own 90-day window, a gap of **0.006 percentage points** — far inside the 0.5-point line, so no warning chip is shown. OKB is a **fixed-supply exchange chain token**: every OKB that will exist already exists, and no programme is shrinking the count either.

## Sell pressure: where new OKB comes from

Protocol inflation is **0 OKB**. X Layer pays no block reward, and the OKB token contract has had no mint function since OKX upgraded it on Aug 18 2025. We read the Ethereum version of OKB at both ends of the window and it held at exactly **429,065 OKB**, and we confirmed that this number sits in storage that can change — so the flat reading is a real measurement, not a frozen constant. New OKB can only appear on X Layer through the bridge from Ethereum, and the bridge token that backs it stayed at **559,345** at both ends: no OKB was bridged in. OKX can still upgrade the contract, so this row is re-checked at every build rather than marked as permanent.

Vesting unlocks are **0 OKB**. All 21 million OKB already count as circulating, and no team, investor or reward schedule is left to release. Foundation and unscheduled unlocks are also **0 OKB**: OKX's own wallets do move OKB, but every coin in them is already counted as circulating, so a transfer out of them changes who holds OKB, not how much exists. Long-term locked or bankruptcy supply is **0 OKB**, because no estate, trustee or lock holds OKB that could come back to the market.

## Buy pressure: where new OKB goes

The programmatic buyback is **0 OKB**. For years OKX bought back and burned OKB every quarter; that programme ended with the one-time burn of **65,256,712 OKB** on Aug 15 2025, which used up the coins OKX had bought back and held in reserve. No new buyback has been announced since.

The protocol fee burn is **0 OKB**. Every transaction on X Layer pays gas in OKB, but the fees are kept in the network's gas vaults rather than destroyed: about **1,077 OKB** of fees piled up there in these 90 days. Checked on both Ethereum and X Layer, the burn addresses received only **0.47 OKB**, stray transfers too small to show. Gas on X Layer is so cheap — a fraction of a cent per transaction — that even a real fee burn would remove very little OKB.

A foundation buy is **0 OKB**: OKX raised fresh money from outside investors in October 2026, but nothing shows it buying OKB in the market. A new long-term lock is also **0 OKB**. Builders who want to run a market on OKX's Exchange OS must stake OKB, and OKX Earn lets holders lock theirs, but locked OKB still counts as circulating, so a bigger lock takes nothing out of the float.

## Foundation and overhang

OKX is the only team holder that matters for OKB, and almost everything it holds belongs to its customers. Sixteen OKX-labelled wallets on X Layer held about **19.45M OKB** at the end of the window, down from **19.56M** at the start, as customers moved coins in and out of the exchange. OKX's latest reserve report shows **19.75M OKB** in its wallets against **19.72M OKB** owed to customers, which leaves OKX's own share at only about **38K OKB**. Two smaller wallets belong to X Layer itself: the fee wallet that collects gas income holds **12,853 OKB** and did not move in the window, and the gas vaults hold about **2,161 OKB** waiting to be paid out to it.

None of these balances is new supply, because every OKB in them already counts as circulating. We read the OKX wallets and the fee wallet on-chain at every build and the reserve report each month. If any of these balances falls between refreshes, the outflow is recorded under foundation and unscheduled unlocks at the next refresh — and if it ever came from coins outside the circulating count, it would add to OKB supply.

## How OKB compares to other exchange tokens

Most exchange tokens still change their supply on purpose. BNB runs a quarterly auto-burn tied to its price and on-chain activity, and also destroys part of the gas paid on BNB Chain, so its supply keeps shrinking toward a target. UNUS SED LEO is bought back and burned with revenue from its parent exchange, and other exchange tokens run monthly or quarterly buybacks. In each case the token holder gets a steady buyer that takes coins off the market.

OKB took the opposite path in 2025. OKX burned its whole buyback reserve in one go, cut the supply to a Bitcoin-like 21 million, and then stopped both minting and burning. That makes OKB's supply the most predictable of the large exchange tokens — nothing comes in and nothing goes out — but it also means OKB no longer has a built-in buyer. Any lift in demand has to come from people using X Layer, staking for Exchange OS, or simply choosing to hold OKB.

Compared with chain tokens such as ETH, which pay validators in new coins, OKB has no issuance at all, because X Layer is a layer-2 network run by OKX and its block producers are paid from gas fees. The trade-off is control: the supply rules hold because OKX keeps them, not because the code makes a change impossible.

## What to watch in the next 90 days

First, OKX's roadmap lists open market deployment on Exchange OS and protocol upgrades for the rest of 2026; when outside builders start staking OKB to open markets, the stake size will show how much OKB gets locked, though it still stays inside the float. Second, any OKX announcement that restarts a buyback, adds a burn, or upgrades the OKB contract would change this reading at once. Third, OKX's monthly reserve report shows whether OKX's own share of OKB grows or shrinks. Fourth, the X Layer fee wallet: its **12,853 OKB** has not moved, and a payout would show up here first.

## Summary

OKB supply is flat: **0.00%** net over the last 90 days and the next 90, with **21M OKB** in circulation, all of it unlocked. Since the August 2025 reset, no new OKB is minted, nothing vests, and neither a buyback nor a fee burn removes coins, because X Layer keeps its gas fees instead of destroying them. The key risk is that this rests on OKX's choices — the token contract can still be upgraded — while the upside case is that Exchange OS and X Layer growth create demand for a supply that cannot grow. Until OKX changes the rules, OKB's supply stays at 21 million.

---

*MrNasdog Pressure Framework analysis of OKB, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 11 2026.*
