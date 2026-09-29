---
title: "CAKE Inflation Analysis · September 2026 · Supply shrinking · projected to keep shrinking"
description: "CAKE supply is shrinking: PancakeSwap's fee buyback burned 7.11M CAKE against 2.37M new, net −1.49% over 90 days and about −0.86% expected in the next 90 days."
canonical_url: "https://mrnasdog.com/research/cake/inflation"
tags: ["crypto", "cake", "pancakeswap", "defi"]
published: true
---

> Originally published at **[mrnasdog.com/research/cake/inflation](https://mrnasdog.com/research/cake/inflation)** by MrNasdog.

# CAKE Inflation Analysis · September 2026 · Supply shrinking · projected to keep shrinking

CAKE supply is shrinking. Over the 90 days to Sep 29 2026, PancakeSwap’s fee buyback and fee burns destroyed **7.11M CAKE**, while only **2.37M CAKE** of new supply reached the market, so the circulating supply of **318.69M** fell by **1.49%**. The farm contract mints far more than that — 44 CAKE every block — but almost all of it is burned back each week before it reaches anyone. Because the buyback is set in dollars and CAKE now costs more, we expect a smaller shrink of about **0.86%** in the next 90 days.

## The verdict, in one paragraph

Our ledger puts CAKE’s net supply change at **−1.49%** over the last 90 days and **−0.86%** for the next 90 days. The inflation monitor reads **+16.13%**, a gap of **17.62 percentage points**, so the page carries a ⚠ monitor gap chip. We traced the gap to one cause: the monitor’s Sep 28 2026 reading fell on burn day, when **57.15M CAKE** minted for the weekly burn was sitting in the farm contract and the burn wallet, waiting to be destroyed. On its Jun 30 2026 starting point only **0.38M** was waiting. That swing of **56.77M CAKE** explains **17.59** of the 17.62 points; it is not new supply, and it was destroyed within hours. Our number stays. In one line: CAKE is a token that is deflationary by structural buyback, with a large mint that is almost entirely burned back.

## Sell pressure: where new CAKE comes from

Protocol inflation added **1.62M CAKE**. PancakeSwap’s original farm contract still mints 40 CAKE per block plus a 10% extra share, and BNB Chain now makes a block about every 0.45 seconds, so the chain minted **769.6M CAKE** in these 90 days. A second farm contract sends 99.7% of its share to the burn wallet, and the whole 10% extra share goes there too: **768.0M CAKE** was burned back without ever reaching a holder. What stayed out — about 18,000 CAKE a day — paid rewards to farms and pools and filled the ecosystem wallet. The emission settings read the same at both ends of the window, so the next 90 days hold the same 1.62M.

Vesting unlocks are zero. CAKE launched with no token sale, no investor allocation and no team vesting; every coin comes out of the farm contract, and the only two wallets that receive new mints are the reward contract and the burn wallet. Foundation and unscheduled unlocks are also zero: the ecosystem wallet grew this window rather than selling, and its coins were already counted once, as emission, when they arrived.

The one sell row that is easy to miss is the old locked staking. PancakeSwap retired its lock model, and every lock ended on Apr 23 2025, but holders still leave coins in the old contracts until they choose to take them out. Those contracts held **19.36M CAKE** at the start of the window and **18.61M** at the end, so **749,121 CAKE** came out — about 8,300 a day. The circulating count leaves these contracts out, so every coin that leaves them is new supply for the market. There is no bankruptcy estate and no trustee holding CAKE.

## Buy pressure: where new CAKE goes

The programmatic buyback is the whole story on this side. Every week, three contracts use part of the trading fees from PancakeSwap’s pools to buy CAKE on the open market and pass it to the burn wallet, which sends everything to the burn address. That came to **7.10M CAKE** in 13 weekly burns, worth about **$12.98M** at each week’s price. The weekly amount climbed from about 376,000 CAKE in early July to a peak of 888,003 in mid-September, as trading grew even while the price rose.

The buyback is set in dollars, not in coins. CAKE traded near $1.31 at the start of the window and **$2.54** now, so the same fees buy fewer coins: at today’s price the last 90 days of fees would buy about **5.11M CAKE**, and that is what we project for the next 90 days. If the price falls, the burn grows again; if it keeps rising, the burn shrinks.

The protocol fee burn is small: two side-product fee streams sent **7,480 CAKE** to the burn wallet once a month. A community vote that closed on Jun 21 2026 moves side-product fees to the PancakeSwap Treasury instead, so this row may fall to zero; it holds about 4,570 CAKE ahead. There was no foundation buy, and there is no new long-term lock, because locking was retired.

## Foundation and overhang

Four overhangs are tracked. The ecosystem wallet, a multisig fed by a share of the farm emission, held **5.41M CAKE** at the end of the window, up from 4.45M; it is checked on-chain every day, and because its coins were counted as emission on arrival, spending them would not be counted again. The old lock contracts hold **18.61M CAKE** that belongs to holders, not the team, and drains a little every day. The PancakeSwap Treasury now takes side-product fees, but its address is not disclosed, so its size is unknown and it is watched through governance and monthly reports. Finally, the 400M supply cap leaves about **63.8M CAKE** of room to mint above today’s supply; the team has said it does not plan to use it. If any of these balances falls between our checks, the outflow enters the foundation and unscheduled unlocks row at the next check.

## How CAKE compares to other DEX tokens

Most exchange tokens that return value to holders do it one of two ways: they share fees with people who lock the token, or they buy the token and burn it. PancakeSwap tried the first model with its vote-escrow locks and then retired it in 2025; CAKE now runs purely on the second. That makes CAKE’s supply depend on trading volume in dollars and on the CAKE price, not on how many people choose to lock.

Against DEX tokens that still pay out new tokens to liquidity providers with no burn behind them, CAKE is the rare case where the buyback is larger than the emission — here more than three to one. Against exchange tokens that burn on a fixed quarterly calendar, CAKE burns every week and the size moves with fees, so its supply path is smoother but less predictable.

The structural risk is the same as for any fee-funded burn: when trading slows or the price climbs, the burn shrinks, while the emission of about 18,000 CAKE a day and the drain from the old lock contracts keep running. A fixed-supply token has no such exposure; CAKE trades a hard cap for a buyback that must keep earning its place.

## What to watch in the next 90 days

The weekly burn lands every Monday, starting Oct 5 2026; a week under about 184,000 CAKE bought back would mean the burn no longer covers emission plus lock exits. The September 2026 monthly burn report is due in early October and will show whether the late-September pace held. Watch whether the side-product fee streams stop arriving, as the June 2026 vote allows. Watch the old lock contracts: a large holder taking out millions at once would lift the sell side. And watch governance for any change to the 44-CAKE-per-block mint or the 400M cap.

## Summary

CAKE supply fell **1.49%** in the 90 days to Sep 29 2026 and is projected to fall about **0.86%** in the next 90 days. PancakeSwap mints 44 CAKE per block but burns almost all of it back, so only 1.62M CAKE of emission and 749,121 CAKE from old locks reached the market, against 7.10M CAKE bought with trading fees and burned. The key risk is that the buyback is set in dollars: a higher CAKE price or lower trading volume shrinks the burn while new supply keeps coming. The 400M cap sits about 63.8M CAKE above today’s supply.

---

*MrNasdog Pressure Framework analysis of CAKE, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*
