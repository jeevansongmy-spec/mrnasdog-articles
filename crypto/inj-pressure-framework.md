---
title: "INJ Inflation Analysis · October 2026 · Supply growing · projected to keep growing"
description: "INJ supply is growing: 1.07M INJ of staking issuance against a 125K INJ buyback burn gives +0.95% net over 90 days and about +1.03% next. No vesting, no cap."
canonical_url: "https://mrnasdog.com/research/inj/inflation"
tags: ["crypto", "inj", "injective", "staking"]
published: true
---

Originally published at [INJ Inflation Analysis · October 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/inj/inflation).

# INJ Inflation Analysis · October 2026 · Supply growing · projected to keep growing

INJ supply is growing. Over the 90 days to Oct 5 2026, Injective paid stakers **1,074,521 new INJ**, while the monthly Community BuyBack burned **125,345 INJ**, so net supply rose **+0.95%** of the 100M INJ counted as circulating, and the next 90 days project **+1.03%**. The monitor reads **+0.06%** only because the count it follows never moves. INJ has no supply cap: issuance is a staking rate pinned at its 4.4% ceiling, and the burn is set in dollars, so it buys back fewer coins when the price rises.

## The verdict, in one paragraph

The MrNasdog Pressure Framework puts INJ at **+0.95% net** over the last 90 days and **+1.03%** over the next 90. The inflation monitor reads **+0.06%**, a gap of **0.89 percentage points**, which is above our 0.5-point line, so the page carries a ⚠ monitor gap chip. We walked the gap and it does not close: the monitor divides by a count of INJ that sits at 100M every day, the fixed size of the original Ethereum token, so coins minted on Injective itself never show up in it. On-chain, the Injective supply rose with every block we read. INJ is a staking chain that is mildly inflationary by design, with a burn that offsets a little over one new coin in nine.

## Sell pressure: where new INJ comes from

Protocol inflation is the whole sell side: **1,074,521 INJ** was minted to stakers between Jul 7 and Oct 5 2026. Injective's mint sets a yearly rate between 2.2% and 4.4% and pushes it up whenever less than 60% of INJ is staked. Only **47.5%** is staked today (58.52M INJ), so the rate sits at the 4.4% ceiling set by the INJ Supply Squeeze vote in January 2026.

The real rate is lower than the headline. Injective pays a fixed slice per block and assumes a block every 0.5 seconds, but blocks in this window came every **0.61 seconds**, so INJ issuance ran at about **3.6% a year**. The base also grew: on Jul 21 and Jul 22 2026 about 12.2M INJ moved from Ethereum onto Injective as a major exchange switched to native INJ. Those coins already existed, so the move is not new supply, but the staking rate is paid on every INJ held on Injective, so issuance stepped up after it. That is why the next 90 days project **1.10M INJ**, slightly more than the last 90.

Vesting unlocks add nothing. Every team, investor and ecosystem allocation finished its schedule on Jan 20 2024, and INJ is listed as fully unlocked. Foundation and unscheduled unlocks are zero because nothing sits outside the circulating count: the community pool, the buyback contract and the Foundation's coins all already count as circulating. There is no bankruptcy estate or long-term lock paying INJ out.

## Buy pressure: where new INJ goes

The programmatic buyback is the only buy-side row. Every four weeks the Injective Community BuyBack opens a round: holders commit INJ, receive a share of a basket of fees the chain earned, and the committed INJ is burned. Four rounds closed in this window, on Jul 8 (43,500 INJ), Aug 5 (27,400), Sep 2 (25,200) and Sep 30 2026 (29,246), for **125,345 INJ** burned, about **$683K** at the price of each day. We checked the last burn on-chain: supply fell by the committed amount, less the few new coins minted in the same blocks.

The rounds are sized by the dollar value of the fee basket, not by a fixed number of coins. INJ now trades well above where it did in July, so the three rounds due by Jan 3 2027 (Oct 28, Nov 25 and Dec 23) project about **67,573 INJ** burned at today's price. There is no separate protocol fee burn: gas is not destroyed, and exchange fees feed the buyback basket instead. No Foundation purchase showed up this window, and staking takes nothing out of the float because staked INJ counts as circulating and can be unbonded in 21 days.

## Foundation and overhang

INJ has no locked pile waiting to unlock. The circulating count and the total count are the same 100M, so every holder we can identify is already inside the float. The on-chain community pool holds **16,722 INJ**; it is filled by 5% of all new INJ and paid out by governance votes, mostly to market makers in a liquidity program. The buyback contract holds **14,796 INJ** that holders have committed or are about to claim, and its helper wallet holds 321 INJ. The Injective Foundation holds part of the ecosystem allocation, but it publishes no wallet address, so its balance is unknown. Listed companies that report INJ treasuries bought on the open market.

We read the community pool, the buyback contract and the helper wallet from the chain at every refresh, and walk the Foundation's announcements every two weeks. If any of these balances falls between refreshes and the coins leave for the market, the outflow enters Sell #3 at the next refresh.

## How INJ compares to other proof-of-stake Layer 1s

INJ belongs to the family of Cosmos-built chains whose staking rate floats with how much of the coin is staked. Like ATOM, Injective raises the rate when staking falls below its goal, and neither has a hard supply cap. The difference is the range: after the January 2026 vote INJ can only move between 2.2% and 4.4%, a narrow and low band, and Injective pairs it with a regular burn that most Cosmos chains do not have.

Against Ethereum, the burn works on a different clock. ETH destroys part of every transaction fee in every block, so its burn rises and falls with how busy the chain is. INJ collects fees from its trading apps for four weeks and burns them in one auction, and holders choose how much INJ to commit, so the burn comes in steps and is capped by the round size. Against BNB, which follows a set quarterly burn toward a fixed 100M target, INJ has no supply target at all; its net supply depends on whether yearly burns can ever catch staking issuance.

On the numbers in this window they do not: almost nine new INJ were minted for every one burned. For INJ to shrink, the buyback would need a fee basket roughly sixteen times larger at today's price, or more INJ would need to be staked, which lowers the rate once staking passes 60%.

## What to watch in the next 90 days

The next Community BuyBack rounds close on **Oct 28 2026**, **Nov 25 2026** and **Dec 23 2026**; each one sets how much INJ is burned, and a busier quarter for Injective's trading apps would raise them above our estimate.

Watch the staking ratio: at **47.5%** the rate stays at 4.4%, and only a move above 60% would start pulling it toward 2.2%. Two US funds tied to INJ, one of them holding staked INJ, are waiting on approval; a launch could lift the amount staked.

Watch block speed and the bridge: blocks ran at about 0.60 seconds in the last ten days of the window, slightly faster than the 0.61-second average, and every block pays the same slice, so faster blocks mean more new INJ. About 5.21M INJ still sits on Ethereum; moving it onto Injective would raise the base that staking pays on.

Watch governance: the October liquidity-program payout of about 24,850 INJ from the community pool closes its vote on Oct 6 2026. It stays inside the float and moves no row, but any vote to change the mint range would.

## Summary

The MrNasdog Pressure Framework reads INJ at **+0.95% net** over the last 90 days and **+1.03%** over the next 90: **1,074,521 INJ** of staking issuance against **125,345 INJ** burned by the Community BuyBack, with no vesting and no unlocks left. Injective's supply is driven by a staking rate pinned at its 4.4% ceiling, which works out near 3.6% a year because blocks are slower than the chain plans for. The key risk is that the burn is set in dollars, so a higher INJ price burns fewer coins while issuance keeps growing with supply; the upside case is more staking or busier trading apps. INJ has no supply cap, so supply keeps growing until the burn catches up with issuance.

*MrNasdog Pressure Framework analysis of INJ, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 5 2026.*
