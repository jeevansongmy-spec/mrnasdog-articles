---
title:         "ZEC Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "ZEC supply is growing: Zcash mined 161,227 ZEC in 90 days at 1.5625 ZEC per block, with no burn or buyback, so supply rose +0.95% and should do the same next."
canonical_url: "https://mrnasdog.com/research/zec/inflation"
tags:          ["crypto", "zec", "zcash", "privacy"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/zec/inflation](https://mrnasdog.com/research/zec/inflation)*

# ZEC Inflation Analysis · September 2026 · Supply growing · projected to keep growing

Zcash (ZEC) is mildly inflationary, and all of it comes from mining. In the 90 days to Sep 30 2026 the Zcash chain created **161,227 ZEC** through its fixed block reward of 1.5625 ZEC, and nothing was burned or bought back, so supply grew **+0.95%** — the inflation monitor reads **+0.98%**. The next 90 days should look the same: the November upgrade to faster blocks keeps ZEC per day unchanged, and the 21M cap and the halving in late 2028 set the ceiling.

## The verdict, in one paragraph

ZEC supply grew by a net **+0.95%** over the last 90 days: **161,227 ZEC** of new supply against **0 ZEC** removed, on **16.96M ZEC** circulating. The inflation monitor measures **+0.98%** for the same window, a gap of only **0.03 percentage points**, well inside the half-point tolerance, so no data-conflict warning is shown. The Zcash block reward is paid every 75 seconds and nothing offsets it, so the reading for the next 90 days is the same **+0.95%**. Zcash is a **steady-emission proof-of-work chain with no burn**: supply grows at a known, slowly falling pace until the next halving.

## Sell pressure: where new ZEC comes from

Protocol inflation is the only live sell row, at **161,227 ZEC** in 90 days. Every Zcash block creates 1.5625 ZEC. Miners receive 80% of it, 1.25 ZEC. A community grants fund receives 8%, 0.125 ZEC. The last 12%, 0.1875 ZEC, goes into a protocol lockbox whose spending is decided by ZEC holders. The chain produced **103,185 blocks** in the window — one every 75.4 seconds, slightly slower than the 75-second target — and total supply read from chain state rose by exactly 103,185 × 1.5625 = 161,226.56 ZEC, with no remainder. Of that, miners took 128,981 ZEC, the grants fund 12,898 ZEC and the lockbox 19,347 ZEC. Every one of those coins counts as circulating from the block it is made, so the full amount is new supply. The Ironwood upgrade on Jul 28 2026 added a new private pool inside this window but changed no reward, and the supply count moved through it without a gap.

Vesting unlocks are **0**. Zcash never sold tokens with locked tranches. Its only early allocation, the founders' reward, was paid out of each block and ended in the protocol at the first halving in Nov 2020, so there is nothing left to unlock. Foundation and unscheduled unlocks are also **0**: the lockbox, the grants wallets and the Zcash Foundation's treasury all hold coins that are already counted as circulating, so a payout moves coins inside the market rather than adding new ones. Long-term locked or bankruptcy supply is **0** — there is no estate, no trustee schedule and no unwinding lock holding ZEC.

## Buy pressure: where new ZEC goes

All four buy rows are **0**. There is no programmatic buyback: no contract, treasury or foundation program takes ZEC off the market. There is no protocol fee burn today — every Zcash transaction fee goes to the miner who includes it, and the supply count rose by exactly the block reward, which proves nothing was destroyed. Fees run at only about 2 ZEC a day. The NU7 upgrade plans to remove 60% of fees from circulation, which would take out roughly 1.2 ZEC a day, too little to move the figure, and its start block is not yet fixed, so the forward column stays at zero.

There is no foundation buy: the Zcash Foundation holds ZEC and dollars to fund its work and does not buy ZEC for the project. There is no new long-term lock either. Zcash has no staking, and the 12% lockbox share is counted as circulating the moment it is mined, so it is not a lock in this ledger. After NU7, about **22,311 ZEC** still sitting in Sprout, the oldest private pool, can no longer be spent. Those coins stay in the supply count, so nothing is booked for them.

## Foundation and overhang

Four team-held pots of ZEC are tracked, and all four already sit inside the circulating count. The protocol lockbox holds **66,578 ZEC** and grows by 0.1875 ZEC every block; it can only pay out after a coin-holder decision, and it has not paid anything since its one-time release of **78,750 ZEC** on Nov 24 2025. That release went to a 2-of-3 wallet whose keys are held by the Zcash Foundation, the Electric Coin Company and Shielded Labs. It now holds **78,183 ZEC**, did not move in this window, and last spent on Apr 14 2026. The Zcash Foundation reported **78,986 ZEC** on its books on Jun 30 2026. The grants fund's receiving wallet fills at 0.125 ZEC a block and is emptied every few days; it held about 888 ZEC at this check.

The lockbox, the key-holder wallet and the grants wallet are read from the chain at every refresh; the Foundation's balance is checked against its quarterly report. If any of these balances falls between refreshes, the outflow is noted in the Foundation and unscheduled row at the next refresh — and because these coins are already counted as circulating, a payout changes who holds ZEC, not how much ZEC exists.

## How ZEC compares to other capped proof-of-work coins

Zcash copies the Bitcoin supply model almost exactly: a 21M hard cap, a block reward that halves every four years, and no fee burn. The difference is the split. In Bitcoin the whole reward goes to miners; in Zcash 20% of every block funds development — 8% as grants and 12% into a lockbox that ZEC holders steer. That split does not change how fast supply grows, only who receives the new coins. Because Zcash launched in 2016, seven years after Bitcoin, it sits earlier on the same curve: about **0.95%** new supply per quarter against roughly a quarter of that for Bitcoin, with 80.8% of the cap already mined.

Against Monero, the other large privacy coin, the models split in the long run. Monero switched to a permanent tail emission of 0.6 XMR per block, so it never stops issuing. Zcash keeps halving toward its cap, so its inflation keeps falling: the next halving, due around Nov 27 2028, cuts the reward to 0.78125 ZEC a block. Against Ethereum, which burns part of every fee, Zcash has no burn today; the planned 60% fee removal would be the first, but at current fee levels it is a small offset next to mining.

## What to watch in the next 90 days

**Oct 6 2026:** the NU7 upgrade is due on the test network. **Oct 20 2026:** developers plan to fix the final mainnet activation block for NU7. **Nov 5 2026:** the target date for NU7 on mainnet — blocks every 25 seconds with one third of today's reward each, so ZEC per day stays the same; 60% of fees start leaving circulation; and coins left in the Sprout pool become unspendable. After activation, the block rate itself is worth watching: if 25-second blocks run faster than target, issuance runs slightly ahead of the trailing rate. Also watch the old Orchard pool, which still holds about 379,359 ZEC as holders move to Ironwood; the Ironwood turnstile makes any counterfeit coins visible as they cross. Finally, any coin-holder grant payout from the 78,183 ZEC key-holder wallet is a move inside the market, not new supply.

## Summary

Zcash (ZEC) is a capped proof-of-work coin whose supply grows **+0.95%** every 90 days, entirely from its 1.5625 ZEC block reward, with nothing burned or bought back to offset it. The reward is split between miners, a grants fund and a coin-holder lockbox, but every new coin counts as circulating the moment it is mined, and the team-held pots — about **66,578 ZEC** in the lockbox and **78,183 ZEC** in the key-holder wallet — are already inside that count. The main change ahead is the NU7 upgrade targeted for Nov 5 2026, which speeds up blocks without changing ZEC per day and adds a small fee removal. The hard ceiling is the 21M cap, and the next halving around Nov 27 2028 halves the rate.

---

*MrNasdog Pressure Framework analysis of ZEC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 30 2026.*
