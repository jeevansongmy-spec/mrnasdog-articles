---
title:         "VET Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "VET supply is steady: 0.00% net over 90 days and 0.00% next. Every VET was made at launch, staking pays and fees burn in VTHO, and 727.58M VET stay frozen."
canonical_url: "https://mrnasdog.com/research/vet/inflation"
tags:          ["crypto", "vet", "vechain", "tokenomics"]
published:     true
---

Originally published at [VET Inflation Analysis · September 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/vet/inflation).

# VET Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

The MrNasdog Pressure Framework reads VET at **0.00% net** over the trailing 90 days and **0.00%** over the next 90: **0 VET** of sell pressure against **0 VET** of buy pressure, on a circulating supply of **85.99B VET**. VeChain made every VET at launch in 2018, pays its stakers and burns its fees in a second token, VTHO, and keeps **727.58M VET** from a 2019 theft frozen outside the market. The monitor reads **−0.01%**, a gap of **0.01 percentage points** — no warning is needed.

## The verdict, in one paragraph

Over the 90 days from Jul 1 2026 to Sep 29 2026, VeChain created no new VET and destroyed none, so the framework's net for VET is **0.00%**, and the projection for the next 90 days is also **0.00%**. The inflation monitor, which reads supply from market value divided by price each day, shows **−0.01%** over the same stretch. The gap between the two is **0.01 percentage points**, far inside the 0.5-point line, so no monitor-gap warning ships. The small monitor figure is day-to-day rounding in that division, not a real change: the VET supply count itself did not move. VET is a **fixed-supply coin with a second token doing all the flowing**.

## Sell pressure: where new VET comes from

**Protocol inflation is 0.** VeChainThor made its whole supply of **86.71B VET** in the first block in 2018 — 25M VET to each of 101 node endorsers and four large launch allocations. We read the current VeChainThor node software, the Interstellar release of Sep 2026, and every place it writes a VET balance: the launch, an ordinary transfer, and a contract closing and handing its coins to someone else. None of them creates VET. Staking changed in the Hayabusa upgrade of Dec 2 2025, when VeChain moved to delegated proof of stake, but the rewards are paid in VTHO, a separate token whose issuance grows with the square root of the VET staked. VTHO is not counted here, so staking rewards add nothing to VET.

**Vesting unlocks are 0.** VET has no vesting schedule. The launch allocations have been free to move since 2018, no unlock tracker lists a future VET release, and the circulating count equals total supply — there is no locked bucket that could open.

**Foundation and unscheduled unlocks are 0.** The VeChain Foundation holds VET in its treasury, but every coin it holds is already counted as circulating, so a sale would move coins that are already in the market rather than add new ones. No release was planned or seen in the window.

**Long-term locked or bankruptcy is 0.** In Dec 2019 a thief took about 1.16B VET from a Foundation buyback wallet; the network blocked 469 of the thief's accounts and holders voted in Jan 2020 to treat the coins in them as burned. Those accounts held **727,582,189 VET** on Jul 1 2026 and exactly the same on Sep 29 2026 — not one of the 469 changed. They stay frozen unless a future network upgrade frees them. There is no bankruptcy estate and no trustee schedule for VET.

## Buy pressure: where new VET goes

**Programmatic buyback is 0.** Nothing buys VET off the market. The Foundation's old 2019 buyback wallet holds 0 VET, and VeChain has announced no new VET buyback.

**Protocol fee burn is 0.** VeChain does burn every transaction fee, but the fees are paid in VTHO, so the burn shrinks VTHO and leaves VET untouched. We also checked the two accounts people use to throw coins away: the zero account held **249,020 VET** and the common dead account **2,014 VET**, the same at both ends of the window.

**Foundation buy is 0.** No announcement and no on-chain flow in the window shows the Foundation buying VET for the project.

**New long-term lock is 0.** Staking did grow: the VeChainThor staking contract held **14.39B VET** on Jul 1 2026 and **14.82B VET** on Sep 29 2026, while one staking pool fell from 866.1M to 704.1M VET. But staked VET is still counted as circulating, so more staking removes nothing from the market supply. What staking changes is how much VTHO is paid out, not how much VET exists.

## Foundation and overhang

Three holdings are watched. First, the **VeChain Foundation treasury**: the Foundation does not name its wallets, and its latest financial report, for the quarter to Jun 30 2025, gave only a total of about **$167.2M** across stablecoins, BTC, ETH and VET, without the VET amount. We check it by reading the Foundation's reports every two weeks. Second, the **469 frozen theft accounts** with **727.58M VET** — the only VET outside the circulating count — read straight from the chain. Third, the retired **2019 buyback wallet**, which holds 0 VET. One large unnamed wallet grew from 112.9M to 3.36B VET in the window; we do not know who owns it, and it is inside the circulating count either way.

If the frozen accounts or the Foundation's holdings ever fall between our checks, the coins that leave them enter the Foundation and unscheduled unlocks row at the next refresh. For the frozen pile, only a new network upgrade approved by VeChain's stakeholders could make that happen.

## How VET compares to other fixed-supply Layer 1s

VET belongs to a small group of Layer 1 coins whose whole supply was created at launch. Unlike Ethereum's ETH, which pays validators in new coins with no cap and burns part of each fee in the same coin, VeChain splits the jobs across two tokens: VET is the fixed, staked coin and VTHO is the flowing one that is issued to stakers and burned as fees. That split is why VET's own supply line is flat while its network still pays stakers and burns fees every block.

The closest match is NEO, which also pairs a fixed coin with a second gas token, and the contrast is XRP: XRP was also made in full at launch, but its fees are burned in XRP itself, so XRP's supply slowly shrinks, while VET's cannot. Compared with coins still releasing locked allocations to teams and investors, VET has none left — the only VET outside the market is the frozen 2019 pile, and it has not moved.

The trade-off is that nothing on the VET side works like a buyer. With no burn and no buyback in VET, all of the pressure on VET comes from people choosing to buy, sell or stake it, not from the protocol adding or removing coins.

## What to watch in the next 90 days

**Any new VeChain upgrade proposal.** The Interstellar upgrade went live on Sep 16 2026 and changed only the smart-contract engine; a future proposal that touched VET issuance or the frozen accounts would change this reading, and would have to pass a stakeholder vote first.

**The next Foundation financial report.** A new report could show how much VET the Foundation holds and whether it sold or bought any.

**The 469 frozen accounts.** Their balance of 727.58M VET should stay flat; any change would show up at our next check.

**The staking total.** More VET staked means more VTHO paid out, but it does not change the VET count; a VET-denominated reward would.

## Summary

The MrNasdog Pressure Framework reads VeChain's VET at **0.00%** net over the last 90 days and **0.00%** over the next 90, against a monitor reading of **−0.01%**. Every one of the **85.99B circulating VET** was made at launch in 2018; staking rewards and the fee burn both run in VTHO, so no VET is created or destroyed. The main risk to this reading is a future network upgrade that changes VET itself or frees the **727.58M VET** frozen since 2019. Until then, the VET supply is fixed at its launch total minus the frozen pile.

---

*MrNasdog Pressure Framework analysis of VET, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*
