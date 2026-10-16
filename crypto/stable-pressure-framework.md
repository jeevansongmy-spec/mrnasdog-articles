---
title:         "STABLE Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "STABLE supply is flat: 0 new coins in 90 days and 0 projected next. All 100B are minted, none can be burned, and 82B stay locked until Dec 8 2027."
canonical_url: "https://mrnasdog.com/research/stable/inflation"
tags:          ["crypto", "stable", "layer1", "tokenomics"]
published:     true
---
*Originally published at [https://mrnasdog.com/research/stable/inflation](https://mrnasdog.com/research/stable/inflation)*

<!-- main-page -->
Looking for the buy-or-sell answer? It is on the STABLE coin page, with demand and price drivers: [mrnasdog.com/research/stable](https://mrnasdog.com/research/stable)

# STABLE Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

STABLE supply did not grow at all in the last 90 days, and it will not grow in the next 90 either: the Pressure Framework books **0 STABLE** of sell pressure and **0 STABLE** of buy pressure, a net of **0.00%** both ways. All **100B STABLE** were created on Dec 8 2025, the token refuses any new mint or burn, and a new lock that began on Oct 5 2026 keeps all **82.0B** locked coins shut until **Dec 8 2027**. The monitor reads **+10.96%**, because the supply figure it follows still adds coins on Stable's old monthly release plan.

## The verdict, in one paragraph

Over the 90 days from Jul 18 to Oct 16 2026, STABLE's net supply change was **0.00%**, and the projection for the next 90 days is also **0.00%**. The inflation monitor reads **+10.96%** for its own 90-day window, a gap of **10.96 percentage points**, which is far above our 0.5-point limit, so the page carries a ⚠ monitor gap note. We walked every source we could reach to explain it: the gap comes from a supply figure that still adds about **29.7M STABLE a day** on the old Foundation release plan, while on-chain the locked wallets did not move by a single coin. Our number stays. In one line: STABLE is a fully minted, fully locked-up token whose supply is frozen until late 2027.

## Sell pressure: where new STABLE comes from

Protocol inflation is **0**. Stable is a Layer 1 where gas is paid in USDT, and STABLE is the coin used for staking and voting. The whole supply of 100B STABLE was issued in a single event on Dec 8 2025, and when we asked the token to mint one new coin, it refused with its own message that minting the governance token is not allowed. Stakers earn a share of network fees in USDT, so security is not paid for with new STABLE, and total supply read exactly 100B at both ends of the window.

Vesting unlocks are **0**. Under the plan Stable published at launch, the Foundation's 32% share was due to drip out at **888.89M STABLE** on the 8th of every month, and the team and investor shares were due to start unlocking after a one-year cliff on Dec 8 2026. On Aug 14 2026 Stable published a new version of its whitepaper that replaces all of that with one lock for every locked holder. It took effect on Oct 5 2026, covers **82B STABLE**, and also pulls back the Foundation coins that had unlocked on paper since launch. We read the lock wallets at both ends of the window: they held the same coins on Jul 18 and on Oct 16 2026, so the Aug 8 and Sep 8 releases never reached the market.

Foundation and unscheduled unlocks are **0**. The Foundation's day-one wallet holds **7.54B STABLE** that it may spend, but it did not move in the window and it already counts as circulating, so spending it would move coins between holders without adding supply. The long-term locked or bankruptcy row is also **0**: no estate, trustee or court plan holds STABLE.

## Buy pressure: where new STABLE goes

Every buy row is **0** as well. There is no programmatic buyback: fees are collected in USDT and shared with stakers in USDT, and none of that money is used to buy STABLE. There is no fee burn: the token refuses a burn call, total supply stayed at exactly 100B, and the dead addresses held no STABLE at either end of the window. We found no Foundation or treasury purchase of STABLE.

The new long-term lock row is **0** too, though it is the most important event of the quarter. The lock took effect on Oct 5 2026, but the coins it covers never left the lock wallets, so it took nothing out of the market. What it does is stop new supply: no locked STABLE can be released before Dec 8 2027.

## Foundation and overhang

STABLE's overhang is large and easy to track. Two wallets hold **25B STABLE** each for the team and for investors and advisors. The Foundation's locked wallet holds **21B**, and **11.0B** more is staked through 11 validators that each carry about 1B STABLE from the Foundation's validator share. Together that is **82.0B** locked STABLE, more than four times the roughly **18B** that sits outside the lock. The Foundation's day-one wallet adds **7.54B** that is free to spend. We read these balances from the chain at every rebuild.

One detail matters for anyone comparing numbers: the circulating figure the market quotes is about **27.27B**, which still includes about **9.27B** of coins that are back under the lock. The new lock releases in seven steps: **4.1B** from Dec 8 2027, 4.1B from Mar 8 2028, 8.2B from Jun 8 2028, 12.3B from Sep 8 2028, 12.3B from Dec 8 2028, 16.4B from Mar 8 2029 and **24.6B** from Jun 8 2029, each spread out day by day over about 180 days, with the last coins out by Dec 8 2029. If the 30-day average price is below $0.025 the day before a step, that step waits three months, up to nine months in total. If any of these wallets' balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How STABLE compares to other stablecoin payment chains

Stable belongs to a new group of chains built around dollar stablecoins, where users pay fees in the stablecoin itself. That design changes what the chain's own coin is for. On a chain like Ethereum, the native coin pays for gas, validators are paid in newly created coins, and part of every fee is burned, so supply moves every block. STABLE pays for no gas at all: fees arrive in USDT, stakers are paid in USDT, and the coin's supply is fixed at 100B with no mint and no burn. That makes STABLE's inflation reading very simple. It does not depend on how busy the chain is; it depends only on when locked coins are released.

Other stablecoin-first chains mix more moving parts. Some pay validators in new coins of their own and burn part of their fees, which turns usage into a tug of war between new supply and the burn. TRON, the largest chain for USDT transfers, burns TRX when users pay for network resources and also pays block rewards, so its supply drifts with traffic. STABLE has neither lever. Its supply story is a calendar of lock steps, which is easy to read but heavy: the 82B still locked is more than four times the coins outside the lock.

The trade-off is clear. Because stakers earn USDT rather than new STABLE, holders are not diluted to pay for security. But nothing takes STABLE out of the market either, so every step of the lock from Dec 8 2027 lands in full, with no buyback or burn to soak it up.

## What to watch in the next 90 days

**Nov 8 2026** is the date the old plan would have released another 888.89M Foundation STABLE. Under the new lock it should release nothing; a move out of the Foundation's locked wallet that day would be new sell pressure.

**Dec 8 2026** was the original one-year cliff for the team and investor wallets. The new lock replaces it, so the two 25B wallets should stay full; any outflow would land in Sell #3.

**Validator stake**: 11 validators each carry about 1B STABLE from the Foundation's share. Coins that leave staking and then leave the lock wallets would count as new supply, so we watch the stake and the unbonding pool at every rebuild.

**Governance**: locked STABLE carries voting rights, and holders vote on validator rewards and treasury use. A vote that adds STABLE rewards, a buyback or a burn would change this reading; none was on the chain on Oct 16 2026.

**The supply figure the market quotes**: it still adds about 29.7M STABLE a day on the old plan. If it is corrected down toward the 18B outside the lock, the quoted market cap will drop with it, even though no coin moved.

## Summary

STABLE's supply was flat at **0.00%** over the last 90 days and is projected at **0.00%** for the next 90, because all 100B coins already exist, the token cannot be minted or burned, and a lock that began on Oct 5 2026 holds all **82.0B** locked coins until Dec 8 2027. The monitor's **+10.96%** comes from a supply figure still running on the old monthly plan, not from coins moving. The key risk is size: from Dec 8 2027 to Dec 8 2029 the locked supply, more than four times what trades today, is due to enter the market, with no buyback or burn to absorb it.

---

*MrNasdog Pressure Framework analysis of STABLE, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 16 2026.*
