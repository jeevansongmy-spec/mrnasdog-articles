---
title: "GT Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description: "Mixed flows, supply roughly steady: GT reads +0.10% over 90 days. GateChain mints 0.4 GT a block; the Jul 4 2026 burn was refilled from a frozen reserve."
canonical_url: "https://mrnasdog.com/research/gt/inflation"
tags: ["crypto", "gt", "gate", "exchange-token"]
published: true
---

> Originally published at **[mrnasdog.com/research/gt/inflation](https://mrnasdog.com/research/gt/inflation)** by MrNasdog.

GateToken (GT) is roughly steady, not deflationary: the MrNasdog Pressure Framework reads GT at **+0.10%** over the trailing 90 days and **+0.10%** over the next 90. The only thing adding GT to the market is GateChain, which mints **0.4 GT** every block for its validators and stakers — **0.10M GT** across the window. The famous quarterly burn did fire, removing **2,570,063 GT** on **Jul 4 2026**, but a frozen reserve that the circulating count already excludes paid the same amount back within the hour, so buy pressure on the tradable float is **0**. The ceiling is shrinking; the float is not.

## The verdict, in one paragraph

Against a circulating base of **106.63M GT**, the framework books **0.10M GT** of sell pressure and **0** of buy pressure over the 90 days to **Sep 18 2026** — a net of **+0.10%** — and projects **+0.10%** for the next 90 days on the same block-by-block mint. The inflation monitor reads **+0.23%** for the same window, a gap of **0.13 percentage points**, inside the framework's half-point tolerance, so no monitor-gap warning is raised and the two readings agree that GT's tradable supply is close to flat and edging up. The label for GateToken is **an exchange token whose burn shrinks the ceiling while its own chain slowly grows the float**.

## Sell pressure: where new GT comes from

Sell #1, protocol inflation, is **0.10M GT**, and it is the row that decides the sign of this page. GateToken is usually described as fixed at **300M**, and the Ethereum copy of GT is exactly that: a 2019 token contract that reads **300,000,000** at both ends of the window and has no way to make another coin. GateChain, the proof-of-stake chain where GT is native, is the part that gets missed. Every GateChain block carries a mint of **0.4 GT**, paid to consensus nodes and their stakers. The window held **257,528** blocks, so GateChain created **103,011 GT**. That figure was checked three ways: the chain's own 24-hour reward counter (about **1,146 GT** a day), the circulating count itself, which rose by almost exactly that amount a day, and Gate's published mining total, which has climbed to **8.83M GT** out of a **30M GT** reward pool. With **21.17M GT** still unmined, this row has decades left to run at today's pace.

Sell #2, vesting unlocks, is **0**. GateToken has no vesting contract, no cliff calendar and no escrow, and Gate's own supply split has no vesting bucket in it. The one unlock tracker page for GT that suggests otherwise shows placeholder data — a release, in another token's name, larger than every GT in existence — so it was set aside and the question settled against the wallets themselves.

Sell #3, foundation and unscheduled unlocks, is **0**, although GateToken's frozen reserve did pay out **2,570,063 GT** in the window. Where that payment went is the whole point of this page, and it is covered in the buy section below: it replaced the coins burned the same hour, so it added nothing to the float. Sell #4, long-term locked or bankruptcy, is **0**: GT has no bankruptcy estate, no trustee and no court-ordered distribution.

## Buy pressure: where new GT goes

Buy #1, programmatic buyback, is **0** on the float, and this is the row most worth explaining, because the GT burn is real. Gate sizes each quarterly burn from a share of its platform revenue, and the Q2 2026 burn settled on Ethereum on **Jul 4 2026**, sending **2,570,063 GT** to the burn address and lifting the total ever burned from **187.38M** to **189.95M GT**, about **63%** of the original 300M. Both supply surfaces were read at both ends of the window: the token contract's total never moved, because GT is burned by sending it to a dead address, while the burn address rose by the full amount. A build that watched only total supply would have missed the burn entirely.

What decides the row is who paid. Fifty-two minutes after the burn cleared, the frozen GT reserve sent the burn wallet exactly **2,570,063 GT**, leaving the burn wallet at the same **12.62M GT** it held when the window opened. That frozen reserve is the only GT the circulating count leaves out: total supply minus circulating supply is **12,251,294 GT**, and the reserve now holds **12,251,232 GT**, sixty-two GT apart. So the coins that left counted supply came out of a pot that was never counted, and the tradable float did not move. The count confirms it: circulating GT shows no drop on the burn day and has risen only by the GateChain mint since. It has not always worked this way — the Apr 2026 burn was not refilled, and circulating GT fell by **2.56M** — which is why the next burn gets watched by sender rather than by headline.

Buy #2, protocol fee burn, is **0**. GateChain does burn part of each transaction fee, but the chain is nearly idle and its burn counter moved by about **3 GT** across the whole quarter. Gate Layer, the newer layer-2 that also uses GT for gas, shows no fee burn on its transactions. Buy #3, foundation buy, is **0**: Gate disclosed no open-market GT purchase, and the reserve received nothing. Buy #4, new long-term lock, is **0**: no new lockup was created, and the **39.96M GT** staked on GateChain already counts as circulating in Gate's own definition, so staking cannot take GT off the market in this reading.

## Foundation and overhang

The overhang that matters most on GateToken is the frozen reserve at **12.25M GT**, down from **14.82M GT** when the window opened. It is the only GT outside the circulating count, and at about **2.6M GT** per burn it holds four to five more quarters of burn funding. Inside the count sit several Gate-linked wallets that need no unlock to reach an exchange: the burn wallet at **12.62M GT**, unchanged across the window; a large wallet at **52.40M GT** that took its balance during the Jan 2026 cross-chain launch and has not moved since; a second at **24.33M GT** that grew by **236,829 GT**; and a third at **7.04M GT**, flat. Beyond the wallets, the **21.17M GT** still unmined in the GateChain reward pool reaches the market a block at a time. All of these are read from the chain at every rebuild. If any balance falls between refreshes by more than its known mechanism explains, that outflow enters Sell #3 at the next refresh.

## How GT compares to other exchange tokens

GateToken belongs to the exchange-token class, where a platform spends part of its revenue on a token and destroys it. In the purest form of that model the tokens are bought on the open market, so every burn removes tradable float and the inflation reading can go clearly negative. GateToken's burn is sized the same way, by revenue, but in the latest quarter the destroyed coins were replaced from a frozen internal reserve. That makes GT's burn a reduction of the ceiling rather than of the float. Both shrink total supply; only the market-funded kind competes with sellers for the coins people can actually trade.

GateToken also differs from most exchange tokens by having a chain of its own. A pure exchange token has no issuance at all, so its supply can only fall. GT is the native staking coin of GateChain, and that chain mints a steady **0.4 GT** per block — a small, permanent issuance leg of about **0.10%** a quarter. Against a hard-capped chain with a halving clock, GateToken has no code-enforced scarcity schedule; its path is set by how Gate funds its burns and how long the **30M GT** reward pool lasts. Against an uncapped proof-of-stake chain, where yearly issuance of several percent is normal, GT's mint is tiny, which is why the page reads as roughly steady rather than inflationary.

## What to watch in the next 90 days

First, the Q3 2026 burn, expected around **Oct 2026** on the pattern of **Oct 15 2025**, **Jan 8 2026**, **Apr 26 2026** and **Jul 4 2026**: the number to check is the sender, because a burn that is not refilled from the frozen reserve would take about **2.6M GT** out of the float and move the next reading to roughly **-2.3%**. Second, the frozen reserve at **12.25M GT**, four to five burns from empty. Third, the **52.40M GT** wallet from the Jan 2026 cross-chain launch, the largest single balance inside the count. Fourth, GateChain's block pace, currently about **2,863** blocks a day; the mint is paid per block, so a faster or slower chain issues more or less GT. Fifth, any Gate announcement that changes the **0.4 GT** block reward or moves GT issuance to Gate Layer.

## Summary

The MrNasdog Pressure Framework reads GateToken (GT) at **+0.10%** over the trailing 90 days and **+0.10%** projected forward: mixed flows, supply roughly steady. The structural mechanism is a split one — GateChain mints **0.4 GT** a block, about **0.10M GT** a quarter, while the **2,570,063 GT** burned on **Jul 4 2026** was paid back from a frozen reserve outside the circulating count, so it cut the ceiling and not the float. The key risk is that the reserve is finite at **12.25M GT**, and the funding choice flips the reading: a burn paid from circulating GT would turn this page deflationary overnight. The ceiling is the **189.95M GT** already burned against a **30M GT** reward pool that still has **21.17M GT** to mint.

---

*MrNasdog Pressure Framework analysis of GT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 18 2026.*
