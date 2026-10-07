---
title: "FLR Inflation Analysis · October 2026 · Supply growing · projected to keep growing"
description: "FLR supply is growing: 635.7M FLR of staking and data rewards and 305.9M of rFLR and escrow unlocks against 26.5M burned or captured gives +1.05% in 90 days."
canonical_url: "https://mrnasdog.com/research/flr/inflation"
tags: ["crypto", "flr", "flare", "oracles"]
published: true
---

Originally published at [FLR Inflation Analysis · October 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/flr/inflation).

# FLR Inflation Analysis · October 2026 · Supply growing · projected to keep growing

Flare (FLR) supply is growing, and the MrNasdog Pressure Framework expects it to keep growing at about the same pace. Over the 90 days to Oct 7 2026, **941.6M FLR** reached the market from staking and data rewards and from rFLR vesting, while burns and fee capture removed only **26.5M FLR**. That is a net **+1.05%** of the **87.10B FLR** in circulation, with **+1.04%** projected for the next 90 days. The FIP.16 vote cut Flare inflation to 3% a year and made the fee burn real, but burns and fee capture are still about one thirty-fifth of what is paid out.

## The verdict, in one paragraph

The framework reads FLR at **+1.05%** net supply growth over 90 days. The inflation monitor reads **+0.39%** for the same stretch, a gap of **−0.66 percentage points**, which is above our 0.5-point line, so the page carries a monitor-gap warning. We walked every source class for it: the supply figure the monitor reads fell by 265M FLR on Jul 31, 244M on Aug 25 and 367M on Sep 2 2026, while Flare's own on-chain count of coins in the market rose on each of those days and rose **915M FLR** across the window. Our number stays. In one line: FLR is a reward-funded chain whose new burns are real but small, so supply still grows about 1% a quarter.

## Sell pressure: where new FLR comes from

Protocol inflation is the largest source. Flare mints new FLR every day at 3% a year of the inflatable balance, under the FIP.16 rules in force since May 2026, and pays it to validators, stakers, FTSO data providers and the voters who answer Flare Data Connector requests. In the window **697.8M FLR** was minted; **59.7M** of it was burned at the source as unearned or expired rewards, so about **635.7M FLR** reached holders, close to 7.1M FLR a day. The claims paid out of the reward pools give the same figure to within a few thousand FLR.

Vesting unlocks are the second source, at **305.9M FLR**. Most of it is rFLR: app rewards are paid as rFLR, which vests over 12 months, and holders withdrew **312.8M FLR** this window. Anyone who leaves early loses half of the unvested part, and **11.4M FLR** was burned that way, so **301.5M** reached the market. The old sale escrow paid out another **4.4M FLR**; its claims are rare, so the next 90 days books only the rFLR part, **301.5M FLR**.

Foundation and unscheduled unlocks book zero. The reserve that funds rFLR moved 439.0M FLR into the vesting pool, but those coins only count once a holder withdraws them, which the vesting row already does. Team, foundation and backer coins from the original Flare distribution were handed out in earlier years and already count as circulating, so moving or selling them adds nothing new. Long-term locked or bankruptcy supply is also zero: no estate or trustee pays out FLR.

## Buy pressure: where new FLR goes

The biggest buyer is a burn, not a buyback. One large staking wallet burns most of the rewards it earns about once a month: **12.0M FLR** on Aug 14 and **5.0M FLR** on Sep 9 2026, for **17.0M** this window and ten burns since Nov 2025. At its last size, three more burns would remove about **15.0M FLR** in the next 90 days.

The protocol fee burn is now real. The Jul 14 2026 hard fork raised the Flare base fee from 25 to 500 gwei, and all gas goes to the burn address. It removed about **6.07M FLR** this window with small app fees, near 71,000 FLR a day since the fork, so the next 90 days project **6.40M FLR**. Data providers' price submissions are refunded and burn almost nothing, which is why the nominal fee total looks larger than what is actually destroyed.

The programmatic buyback row holds the new FIRE pool. Since Aug 18 2026 part of Flare's fee revenue collects in a wallet the chain leaves out of circulation: **3.43M FLR** so far, about **6.12M** next 90 days at that pace. FIRE's job under FIP.16 is to buy back and burn FLR, but it has not made an open-market purchase yet. A foundation buy is zero, and a new long-term lock is zero: staked and delegated FLR still counts as circulating and can be withdrawn.

## Foundation and overhang

The largest overhang is the incentive reserve that funds rFLR: **17.27B FLR** held outside the market, paying out about 4.9M FLR a day into the vesting pool, which itself holds **783.5M FLR**. Next comes about **218.6M FLR** of rewards waiting to be claimed in the reward pools, the **200.1M FLR** of fully vested but unclaimed sale escrow, and **3.5M FLR** in the foundation-listed wallets, almost all of it the FIRE fee pool. The monthly-burn staking wallet holds 7.6M FLR, already inside the market. We read every one of these balances on-chain at each rebuild. If any of them falls between rebuilds without a matching burn, the outflow enters the foundation and unscheduled unlocks row at the next refresh.

## How FLR compares to other reward-funded Layer 1s

FLR sits in the group of uncapped proof-of-stake chains that pay security and service rewards in new coins. Like Ethereum or Avalanche, Flare has no hard cap and destroys transaction fees, but on Flare the burns cover under 3% of what the chain pays out. Flare also pays for more than block production: the FTSO price feeds and the data connector are rewarded from the same 3% mint, so a share of FLR inflation is the price of its oracle services.

The second difference is rFLR. Most chains finished their app-incentive programs with a one-off airdrop; Flare runs a standing reserve of 17.27B FLR that pays rewards which vest for a year. That keeps a second, steady stream of unlocks on top of inflation, about 300M FLR a quarter, which a chain with only staking issuance does not have.

The newest piece is FIRE, a revenue pool meant to buy back and burn FLR, in the spirit of exchange tokens and DeFi coins that route fees into buybacks. Today it is tiny next to the mint. If Flare's XRP-DeFi activity and the planned block-building revenue grow, FIRE is the mechanism that could change the verdict.

## What to watch in the next 90 days

**The monthly reward burn:** the staking wallet has burned ten times in the last eleven months, skipping only May; another skipped month or a much bigger burn moves the buy side by several million FLR.

**FIRE's first buyback:** the pool held 3.43M FLR on Oct 7 2026; an open-market purchase and burn would be the first real buyback on Flare.

**The rFLR pace:** withdrawals ran faster in the last 30 days (about 127.5M FLR) than the 90-day average; if that holds, the vesting row rises toward 380M FLR a quarter.

**Fee burn after the fork:** busier blocks from FXRP vaults and the new DeFi cover products raise the burn; quiet weeks pull it lower.

**Governance:** any new FIP that changes the 3% rate, the fee level or FIRE's mandate; none was open on Oct 8 2026.

## Summary

Flare (FLR) supply grows about **1.05%** every 90 days: 635.7M FLR of staking and data rewards plus 305.9M FLR of rFLR and escrow unlocks, against 26.5M FLR burned or captured. The FIP.16 overhaul cut inflation to 3% and made the fee burn real, yet the burn and the new FIRE pool are still small next to the mint. The key risk is the 17.27B FLR incentive reserve, which keeps feeding rFLR unlocks for years. There is no supply cap; only a much larger FIRE buyback or burn could turn FLR flat.

*MrNasdog Pressure Framework analysis of FLR, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 8 2026.*
