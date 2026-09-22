---
title:         "JST Inflation Analysis · September 2026 · Supply shrinking · projected to keep shrinking"
description:   "JST supply is shrinking: −4.34% in 90 days as JustLend DAO burned 355.0M JST, with no new JST minted. About 180M more burns in October, for −2.20% next."
canonical_url: "https://mrnasdog.com/research/jst/inflation"
tags:                    ["crypto", "jst", "just", "defi"]
published:     true
---

Originally published at [JST Inflation Analysis · September 2026 · Supply shrinking · projected to keep shrinking](https://mrnasdog.com/research/jst/inflation).

# JST Inflation Analysis · September 2026 · Supply shrinking · projected to keep shrinking

JST is shrinking, and it is projected to keep shrinking. The JUST governance token on TRON created no new JST in the last 90 days, while JustLend DAO destroyed **355.0M JST** in one quarterly buyback and burn on **Jul 17 2026**. The Pressure Framework books sell pressure of **0** against buy pressure of **355.0M JST**, a net of **−4.34%**, with **−2.20%** projected for the next 90 days; the inflation monitor reads **−4.15%**. The one constraint is the contract itself: its mint function is still live under a single owner address, so the 9,900M issued in 2020 is a record, not a cap written in code.

## The verdict, in one paragraph

Against a circulating base of **8,188.7M JST**, the framework books **0** of sell pressure and **355.0M JST** of buy pressure over the trailing 90 days — a net of **−4.34%** — and projects **−2.20%** for the next 90 days from one more quarterly round. The inflation monitor reads **−4.15%** for the same window, a gap of **0.18 percentage points**, inside the framework's 0.5-point tolerance, so the overview carries no warning. The small gap is simply the base: the monitor divides the same 355.0M JST by the larger supply at the start of the window. The label for JST is **deflationary by a revenue-funded buyback and burn**: a token that issues nothing and loses a slice of its float every quarter.

## Sell pressure: where new JST comes from

It does not come from minting. Protocol inflation, Sell #1, is **0**. The JST contract on TRON has recorded exactly one mint in its whole history — the full **9,900M JST** issued in April 2020 — and across this window the count of JST in existence only went down, from **9,900M** to **9,793.3M**. JST has no staking emission and no block reward. What JST does have is a live mint function. A test call to it from an outside address is refused by the contract's own permission check, and the same call from the owner address goes through. Nobody has used that power since 2020, but it exists, so the framework watches Sell #1 rather than closing it for good, and never describes JST supply as fixed.

Vesting unlocks, Sell #2, are **0**. The JUST launch release plan ran in 36 monthly steps from April 2020 to **March 30 2023** and is finished. Just as important, the circulating count for JST is simply every JST that has not been destroyed: the 9,793.3M in existence minus the 1,604.6M sitting at the unspendable burn address. Nothing live is held outside it, so no locked JST is left to unlock into the float.

Foundation and unscheduled unlocks, Sell #3, are **0** for the same reason: every project wallet is already counted as tradable, so a transfer out of one moves JST within the float rather than into it. Long-term locked or bankruptcy, Sell #4, is **0**: no estate, trustee or court distribution holds JST.

## Buy pressure: where new JST goes

Into two different kinds of burn. Programmatic buyback, Buy #1, is **248.4M JST**. Under a proposal approved in October 2025, JustLend DAO spends its lending revenue buying JST on the open market once a quarter and sends it to an address nobody can spend from. The **Jul 17 2026** round was paid for with **$10.28M** of second-quarter revenue plus **$10.34M** from a reserve set aside when the buyback started. The unspendable address grew by exactly **248.4M JST** across the window, and its balance of **1,604.6M JST** matches the four published JST buyback rounds to within a few thousand JST of old dust.

Protocol fee burn, Buy #2, is **106.7M JST**. For years, borrowers of the old USDJ stablecoin paid stability fees in JST, and those fees sat in a fee contract. On the same day, all **106.7M JST** was destroyed with the contract's own burn call, which is why the count of JST in existence fell. This burn and the buyback left through two separate doors: the earlier buyback rounds moved the burn address while the JST count stood still at 9,900M, and this one cut the count without moving any JST to the address. So both count, once each. The fee contract is now empty, and this was the only burn of its kind the JST contract has ever recorded.

Foundation buy, Buy #3, is **0**: the only buying is JustLend DAO's own programme in Buy #1. New long-term lock, Buy #4, is **0**: JST wrapped for JustLend DAO governance votes can be unwrapped at any time and is already counted as tradable.

## Foundation and overhang

The JST overhang is small in kind and fully inside the float. The largest identified item is the wallet that executes every JustLend DAO burn: it held **500.0M JST** at the end of the window against **300.0M JST** at the start. The rise is a 200.0M parcel it moves through the voting wrapper to open governance proposals and then takes back, not a purchase and not a sale. The second item is the owner address with mint power, which holds no JST at all and matters only as a capacity. The USDJ fee contract that fed Buy #2 now holds nothing. All three are read from the TRON chain at every rebuild. If the execution wallet's balance falls between refreshes by more than a burn round explains, that outflow enters Sell #3 at the next refresh; if the owner address ever mints, it enters Sell #1 the same day.

## How JST compares to other buyback-and-burn tokens

JST sits in the class of exchange and protocol tokens that turn revenue into burns, but its shape is unusual. Most buyback tokens still carry large locked team or investor pools, so their burns fight new unlocks. JST has none: its vesting ended in 2023 and nothing is minted, so every burned JST is a straight reduction of the float. A burn of **4.34%** in one quarter is large even within this class.

Against a hard-capped halving coin like Bitcoin, JST moves the other way. Bitcoin still mints on every block at a falling rate, so its reading stays slightly positive; JST mints nothing and shrinks. But Bitcoin's cap is enforced by every node, while JST's ceiling rests on one owner key choosing not to mint. On the burn itself, JST differs from a gas-fee burn like Ethereum's: the size of each JST burn depends on JustLend DAO's lending revenue and on the JST price on the day of purchase, not on network use, so it arrives in quarterly steps rather than a steady trickle.

## What to watch in the next 90 days

First, the fifth quarterly JST buyback and burn, due around **Oct 15 2026**: it spends the last reserve slice plus third-quarter revenue, about **$20.6M**, which is roughly **180.3M JST** at today's price and the entire **−2.20%** projection. Second, the size of the rounds after that: once the reserve is used up, each quarter carries only new revenue, so from January 2027 the JST burn should be about half its current size unless revenue grows. Third, USDD: the October 2025 proposal also sends USDD ecosystem revenue above $10M into JST buybacks, which has not happened yet and would add to the burn. Fourth, the mint function and its owner address — any mint event would reverse this reading at once. Fifth, the governance queue on JustLend DAO, where the latest proposal, posted Sep 16 2026, offboards a lending market and does not touch JST supply.

## Summary

The MrNasdog Pressure Framework reads JST at **−4.34%** over the trailing 90 days and **−2.20%** projected forward: supply shrinking, projected to keep shrinking. The mechanism is a revenue-funded buyback and burn run by JustLend DAO on TRON, plus a one-time burn of stored USDJ fees, against zero new issuance and no vesting left. The key risk is that the burn is only as large as JustLend DAO's revenue, and it roughly halves after the October round when the reserve runs out. The ceiling is soft: **9,793.3M JST** exist today, but a live mint function under one owner address means that ceiling is a choice, not a rule in code.

MrNasdog Pressure Framework analysis of JST, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 22 2026.
