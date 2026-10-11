---
title:         "ZEC Inflation Analysis · October 2026 · Supply growing · projected to keep growing"
description:   "ZEC supply is growing: Zcash mined 161,241 ZEC in 90 days at 1.5625 ZEC per block, with no burn or buyback, so supply rose +0.95% and should do the same next."
canonical_url: "https://mrnasdog.com/research/zec/inflation"
tags:          ["crypto", "zec", "zcash", "privacy"]
published:     true
---
*Originally published at [https://mrnasdog.com/research/zec/inflation](https://mrnasdog.com/research/zec/inflation)*

<!-- main-page -->
**Main page:** the full ZEC coin page — signal, price drivers and the buy/sell questions → [mrnasdog.com/research/zec](https://mrnasdog.com/research/zec)

# ZEC Inflation Analysis · October 2026 · Supply growing · projected to keep growing

Zcash (ZEC) supply is growing, and the MrNasdog Pressure Framework expects it to keep growing at the same pace. Proof-of-work mining created **161,240.6 ZEC** in the last 90 days, and nothing was burned or bought back, so the net change is **+0.95%** of the **16.98M ZEC** in circulation, with the same **+0.95%** projected for the next 90 days. Like Bitcoin, Zcash has a hard cap of **21M ZEC** and halves its block reward about every four years; the next halving is not due until about November 2028.

## The verdict, in one paragraph

The Zcash ledger nets to **+0.95%** over the last 90 days and **+0.95%** over the next 90. Our supply monitor reads **+1.10%** for the same stretch, a gap of **0.15 percentage points**, well inside our half-point tolerance, so no warning chip is shown. Every new ZEC comes from the block reward; there is no token sale left to unlock, no vesting cliff, no burn and no buyback. In one line: Zcash is a capped proof-of-work coin in its third emission era, adding just under 1% of supply every 90 days and slowing only at the next halving.

## Sell pressure: where new ZEC comes from

Protocol inflation is the whole Zcash sell side. Each block pays a subsidy of **1.5625 ZEC**, and the 90-day window from Jul 13 2026 to Oct 11 2026 held **103,194 blocks**, one every 75.35 seconds against a 75-second target. That is **161,240.6 ZEC**, about **1,792 ZEC a day**. We checked it two ways: the Zcash chain's own supply count rose by exactly that amount between the two window ends, and so did the sum of block rewards, with nothing left over.

The block reward is split three ways. Miners keep **80%** (1.25 ZEC per block). A community grants fund gets **8%** (0.125 ZEC). The last **12%** (0.1875 ZEC) goes into a protocol lockbox that ZEC holders steer by coin-weighted vote; it took in **19,348.9 ZEC** this window. Lockbox coins cannot be spent until a vote and a payout, but they are already counted as circulating, so we book them as new supply on the day they are mined, together with the miners' share.

Vesting unlocks are zero. Zcash had no token sale; its founders were paid from mining, and that share ended by protocol rule in November 2020. Foundation and unscheduled unlocks are zero too: the team-side pots are already counted as circulating, so a payout moves coins between holders and adds nothing to supply. Long-term locked or bankruptcy supply is zero: no bankruptcy estate, trustee or court-ordered distribution holds ZEC.

The next 90 days keep the same quantum. The NU7 network upgrade, targeted for Nov 5 2026, cuts the block time from 75 to 25 seconds and divides the reward per block by three, so the number of ZEC mined per day does not change. The halving schedule keeps its calendar date, so the next 90 days carry no halving.

## Buy pressure: where new ZEC goes

Nothing on the Zcash buy side is active today. There is no programmatic buyback: no contract, foundation or treasury repurchases ZEC. There is no protocol fee burn yet: every transaction fee goes to the miner, and the chain's supply rose by exactly the block rewards, which proves nothing was destroyed. Foundation buying is zero; companies and exchange-traded funds that hold ZEC buy it in the open market from coins already circulating, which is demand, not a change in supply.

NU7 adds the first fee burn. Its Network Sustainability Mechanism sets aside **60%** of every fee in a reserve that is not counted as issued supply, to be paid back out to miners slowly from February 2031. But Zcash fees are tiny, about **1.27 ZEC a day**, so from Nov 5 2026 to Jan 9 2027 it would remove only about **50 ZEC**. The mainnet block height is not fixed until Oct 20 2026, so we do not count it yet.

New long-term lock is zero, with one note. NU7 also makes the oldest private pool, Sprout, unspendable: about **22.31K ZEC** still sits there, after 3,100 ZEC moved out in the last 90 days. Those coins stay in the supply count and were mostly idle for years, so the float does not shrink. Coins held in shielded pools are private, not locked.

## Foundation and overhang

We track four team-side pots, all counted as circulating. The protocol lockbox holds about **68.94K ZEC** and grows by 0.1875 ZEC every block; it pays out only through a coinholder decision or a network upgrade, and the last payout was **78,750 ZEC** on Nov 24 2025. That payout sits in a coinholder multisig held by Zcash ecosystem organisations, now about **78.18K ZEC**, unmoved since Apr 14 2026; coinholders approved about $8.39M of grants in their latest vote, so a payout of several thousand ZEC is likely soon. The Zcash Foundation reported **78,986 ZEC** at Jun 30 2026. The community grants fund address holds about 464 ZEC and pays out often.

We read the lockbox, the multisig and the grants address from the chain every refresh, and the Foundation from its quarterly report. If any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh; because each pot is already inside the circulating count, a payout books as zero new supply, but it is coins that can reach the market.

## How ZEC compares to other privacy and proof-of-work coins

Zcash copies the Bitcoin money rules: a **21M** hard cap, proof-of-work mining and a halving about every four years. The difference is the stage. Bitcoin has mined about 95% of its coins and adds roughly 0.2% every 90 days; Zcash has mined about **81%** of its cap and adds **0.95%**, about four times faster, until its next halving. Zcash also sends 20% of each block to two community funds, where Bitcoin pays all of it to miners.

Against Monero, the other large privacy coin, the shape is opposite. Monero has no cap: after its main emission ended it moved to a fixed tail emission of 0.6 XMR per block forever, so its supply growth falls slowly but never reaches zero. Zcash keeps halving toward a hard ceiling. Neither coin burns fees today; NU7 will make Zcash the first of the two to set part of its fees aside.

Compared with proof-of-stake chains, Zcash has no staking lock and no validator queue, so nothing takes coins out of the float. Its new supply is simple and predictable: one block reward, set by code, measured on-chain every block.

## What to watch in the next 90 days

**Oct 20 2026:** developers decide whether NU7 goes to mainnet and set its block height; a delay changes nothing in issuance.

**Nov 5 2026 (target):** NU7 activates. Blocks every 25 seconds, the same ZEC per day, 60% of fees set aside, and Sprout coins frozen; if the height is fixed, the fee set-aside enters the ledger.

**Coinholder grant payouts:** about $8.39M of approved grants should leave the coinholder multisig, and the next round opens for proposals from Oct 30 to Nov 13 2026, with voting from Dec 17 to Dec 29 2026.

**Zcash Foundation Q3 2026 report:** it shows whether the Foundation's 78,986 ZEC moved since Jun 30 2026.

## Summary

Zcash (ZEC) supply grows **+0.95%** every 90 days, all of it from the proof-of-work block reward of about 1,792 ZEC a day, with no burn, no buyback and no vesting. Our monitor agrees within 0.15 percentage points. The NU7 upgrade makes blocks three times faster without changing the ZEC mined per day, and its fee set-aside is too small to matter for now. The main risk to holders is the team-side pots of roughly 226K ZEC that can reach the market as grants are paid; the ceiling is the 21M cap, with the next halving in about November 2028.

---

*MrNasdog Pressure Framework analysis of ZEC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 11 2026.*
