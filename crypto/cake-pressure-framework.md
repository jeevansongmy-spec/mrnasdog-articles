---
title: "CAKE Inflation Analysis · September 2026 · Supply shrinking, projected to keep shrinking"
description: "Supply shrinking: CAKE reads -1.55% over 90 days. PancakeSwap fee buybacks burned 6.99M CAKE while only 1.61M of new farm emission reached the market."
canonical_url: "https://mrnasdog.com/research/cake/inflation"
tags: ["crypto", "cake", "pancakeswap", "defi"]
published: true
---

> Originally published at **[mrnasdog.com/research/cake/inflation](https://mrnasdog.com/research/cake/inflation)** by MrNasdog.

# CAKE Inflation Analysis · September 2026 · Supply shrinking, projected to keep shrinking

PancakeSwap's CAKE is shrinking: the Pressure Framework reads CAKE at **−1.55%** over the trailing 90 days and **−1.55%** over the next 90, because trading fees bought and burned **6.99M CAKE** while only **1.61M CAKE** of new emission reached the market. The mint itself never stops — the PancakeSwap farm contract creates 44 CAKE in every block on BNB Chain — but about 96% of it is destroyed at the weekly burn before any holder sees it. The only ceiling is a 400M limit set by a holder vote, not by code.

## The verdict, in one paragraph

Against a circulating base of **348.47M CAKE**, the framework books **1.61M CAKE** of sell pressure and **6.99M CAKE** of buy pressure over the trailing 90 days — a net of **−1.55%** — and projects **−1.55%** for the next 90 days on unchanged contract settings and an unbroken weekly burn. The inflation monitor reads **+7.40%** for the same window, a gap of **8.95 percentage points**, which is far over the framework's 0.5pp tolerance and ships with a monitor-gap warning on the overview page. The gap comes from CAKE that has been minted for the weekly burn but not yet destroyed, which the monitor counts as supply. At its base reading on **Jun 20 2026** only **0.35M CAKE** of it existed — that week's emission had built up in the farm contract but had not been minted yet. At its reading on **Sep 18 2026**, **29.40M CAKE** had been minted and was waiting for the next burn. That **29.05M CAKE** rise accounts for **8.95pp**; price rounding in the monitor adds **0.06pp**, the base convention takes off **0.11pp**, and **0.05pp** is unexplained. The label for CAKE is a **deflationary exchange token whose burn outruns a mint that never stops**.

## Sell pressure: where new CAKE comes from

All new CAKE comes from one place, the PancakeSwap farm contract, and Sell #1, protocol inflation, is **1.61M CAKE**. The headline mint is enormous: the contract makes 40 CAKE per block for rewards plus 4 CAKE per block for a team wallet, and BNB Chain now produces a block roughly every 0.45 seconds, so **797.7M CAKE** was created in these 90 days. But the contract is set to send 99.72% of its reward share, and the team wallet sends all of its share, to a burn wallet that empties into the burn address every Monday. **774.1M CAKE** was destroyed that way in the window, and another **29.05M CAKE** was waiting for the next burn at the close. None of that churn ever becomes tradable, so the framework books it on neither side. What did get out is **1.61M CAKE**: payments to PancakeSwap liquidity farms and to a team-run ecosystem fund. PancakeSwap's own target is about 21,750 CAKE a day; the part of the farm share not yet claimed waits inside the contract. None of the contract settings changed in the window.

Sell #2, vesting unlocks, is **0**. CAKE launched in 2020 with no presale and no team or investor allocation, so nothing vests — every freshly made CAKE in the window went to only two addresses, the farm contract's reward pot and the burn wallet. Sell #3, Foundation and unscheduled unlocks, is **0**: the ecosystem fund sent nothing out in the window, and what it received is already counted in Sell #1. Sell #4, long-term locked or bankruptcy, is **0**, because CAKE has no bankruptcy estate and no trustee.

## Buy pressure: where new CAKE goes

Buy #1, programmatic buyback, is **6.98M CAKE**, and it is the whole story on this side. Three PancakeSwap contracts swap trading fees into CAKE on the open market; about three quarters of what they buy goes to the burn wallet and is destroyed at the Monday burn. There were **13 weekly burns** in the window, from **Jun 22 2026** to **Sep 14 2026**, and the fee-bought CAKE in them came to **6.98M CAKE**. The other quarter — **2.52M CAKE** — was sent through a pass-through wallet to an exchange, so it stays in the market and the framework counts it on neither side.

Buy #2, protocol fee burn, is **0.0076M CAKE**: a few smaller product fee streams sent CAKE straight to the burn wallet, and holders burned about 3 CAKE of their own. A PancakeSwap governance vote that closed on **Jun 21 2026** moves fees from products outside the main exchange to the treasury; those streams were still arriving on **Sep 3 2026**, and they are too small to move the reading either way. Buy #3, Foundation buy, is **0** — no team wallet bought CAKE and kept it. Buy #4, new long-term lock, is **0**: PancakeSwap retired time-locked CAKE on **Apr 23 2025**, and the remaining staking pool has no lock at all.

## Foundation and overhang

The largest team-controlled pot is the PancakeSwap ecosystem fund, a wallet that needs three signers and holds **5.26M CAKE**. It receives a slice of the farm contract's output every week — **0.94M CAKE** in this window — and it sent nothing out. Its last payout was **Jun 17 2026**, and it has paid out about **0.37M CAKE** since January with no published schedule. Because the framework counts its intake when it arrives, its spending later will not be counted a second time. The second item is not team money: **18.66M CAKE** of holders' own coins still sits in two retired lock contracts, and **0.72M CAKE** left them over the window as holders withdrew. The third is the PancakeSwap treasury, which now collects side-product fees under the Jun 21 2026 vote at an address not yet disclosed. All three are read again at every rebuild; if any team-controlled balance falls between refreshes by more than its known payouts, that outflow enters Sell #3 at the next refresh.

## How CAKE compares to other exchange tokens with buyback and burn

CAKE belongs to the class of exchange tokens that turn trading fees into a burn, alongside BNB's quarterly auto-burn and the fee-funded buybacks run by perpetual exchanges. What sets CAKE apart is that it still mints on every block. BNB has no emission left to offset, so its burn is pure removal; CAKE has to out-burn a live farm emission every single week, and it has now done so for 36 months in a row by PancakeSwap's own count. The farm emission is small next to the burn — **1.61M CAKE** out against **6.99M CAKE** destroyed — but it is permanent, and it keeps running whether trading volume holds up or not.

The second difference is the cap. A halving-model chain like Bitcoin has a supply limit written into the protocol. CAKE's **400M** ceiling, cut from 450M by a vote that closed on **Jan 19 2026**, is a promise about the net count, and it is kept by burning, not by the contract: the mint function is live and has no built-in limit. Against uncapped continuous-emission tokens, CAKE looks strong, because its burn is tied to real usage. Against capped, non-minting tokens, it carries a risk they do not — if fees fall far enough, the emission wins.

## What to watch in the next 90 days

First, the Monday burns — 13 of them fall between **Sep 21 2026** and **Dec 14 2026**, and each one both destroys the week's fee buyback and clears the parked emission, which is why the monitor reading swings. Second, trading volume on PancakeSwap: the buyback is paid in fees, so a quieter market or a higher CAKE price means fewer CAKE burned for the same revenue. Third, the farm contract's settings — any governance change to the burn share or the per-block mint moves Sell #1 directly. Fourth, the ecosystem fund at **5.26M CAKE**, the only team pot with a spender and no schedule. Fifth, where the side-product fees redirected on **Jun 21 2026** actually land once the treasury address is published.

## Summary

The MrNasdog Pressure Framework reads PancakeSwap's CAKE at **−1.55%** over the trailing 90 days and **−1.55%** projected forward: supply shrinking, projected to keep shrinking. The mechanism is a fee-funded open-market buyback that destroyed **6.99M CAKE** against **1.61M CAKE** of farm emission that actually reached the market, while about 96% of the 44 CAKE minted every block is burned before it circulates. The key risk is that the mint never stops and the burn depends on trading fees. The ceiling is a **400M** limit set by holders, kept by the burn rather than by the contract.

---

*MrNasdog Pressure Framework analysis of CAKE, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 18 2026.*
