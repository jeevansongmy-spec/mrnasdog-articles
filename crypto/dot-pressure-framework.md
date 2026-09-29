---
title:         "DOT Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "DOT supply is growing: 13.78M new DOT in 90 days under a 2.1B hard cap and nothing burned gives +0.81% net, the same next. Monitor +0.55%, gap 0.26pp."
canonical_url: "https://mrnasdog.com/research/dot/inflation"
tags:          ["crypto", "dot", "polkadot", "layer0"]
published:     true
---

> Originally published at **[mrnasdog.com/research/dot/inflation](https://mrnasdog.com/research/dot/inflation)** by MrNasdog.

# DOT Inflation Analysis · September 2026 · Supply growing · projected to keep growing

**DOT supply is growing slowly and steadily.** Polkadot minted **13.78M DOT** in the 90 days to Sep 29 2026 and destroyed nothing that counts: sell pressure **13.78M DOT**, buy pressure **0 DOT**, net **+0.81%** of the **1.70B DOT** circulating supply. Our monitor reads **+0.55%**, a gap of **0.26** percentage points, inside our tolerance. The rate comes from the **2.1B DOT hard cap** that took effect on Mar 14 2026, which more than halved Polkadot issuance to about **55.9M DOT a year** and holds it there until Mar 14 2028.

## The verdict, in one paragraph

Over the last 90 days, DOT supply grew **+0.81%**, and at the same minting rate it grows another **+0.81%** in the next 90 days. The monitor, which reads supply from market value and price, shows **+0.55%** over the same window. The gap is **0.26 percentage points**, below our 0.5-point line, so no warning chip is shown: both readings agree that Polkadot supply is rising, and the on-chain reading is the more exact of the two because it reads the supply counter itself at both ends of the window. Polkadot is a **capped, slowly inflating chain with its burn switched off**: every new DOT comes from one steady mint, and since March 2026 nothing on the main ledger takes DOT out again.

## Sell pressure: where new DOT comes from

**Protocol inflation is the whole sell side: 13.78M DOT in 90 days.** Polkadot mints new DOT every 72 seconds, about **127.6 DOT** each time, which is **153,132 DOT a day**. We read the supply counter at the start and end of the window: it rose from **1,691.18M** to **1,704.96M DOT**, which matches the minting rate to within 142 DOT. The mint amount was the same at both ends of the window, so the next 90 days carry the same **13.78M DOT**. Of each mint, 45.2% goes to stakers, 22.6% to validators who put up their own stake, and 32.2% to a governance-run pool.

**Vesting unlocks are 0.** Polkadot has no team or investor unlock calendar left. About **16.18M DOT** still sits in vesting locks across 1,076 accounts, and **3.36M DOT** of it frees up in the next 90 days, including grants of about 6.83M DOT that started a two-year release in September 2026. Those coins are already counted as circulating, so their release adds nothing new to the float.

**Foundation and unscheduled unlocks are 0.** The Polkadot Treasury and the new governance pool both hold large balances, but every coin in them is already in the circulating count, and spending them is a move inside the float. They are covered in the overhang section below.

**Long-term locked or bankruptcy supply is 0.** No estate, trustee or long lock is releasing DOT. The old parachain crowdloan and lease deposits have already been handed back, and funds that hold DOT bought it on the open market.

## Buy pressure: where new DOT goes

**Programmatic buyback is 0.** No contract or treasury buys DOT off the market, and no vote to start one is open. The governance pool fills with new DOT, fees and penalties; nothing in it was bought.

**Protocol fee burn is 0.** This is the big change of 2026. Until March, Polkadot burned a slice of its unspent treasury funds at regular intervals. The Mar 12 2026 upgrade stopped the treasury burn and sent transaction fees and validator penalties into the governance pool instead of destroying them. The supply counter confirms it: supply rose by the full minted amount. One small burn still runs — the fee projects pay to buy blockspace is destroyed about once a day — but it is at most about 10K DOT a month, too small to change the result at two decimals, and we could not measure it from two independent reads, so it books 0.

**Foundation buy is 0.** No foundation or treasury purchase of DOT was announced or seen on-chain in the window.

**New long-term lock is 0.** About **907.68M DOT** is staked, up from 862.35M at the start of the window — more than half of all DOT. But staked DOT stays in the circulating count, and since 2026 nominators can leave staking in one to two days, so a bigger stake removes nothing from the float.

## Foundation and overhang

We track three pools of DOT that a group controls. The **Polkadot Treasury** holds **24.31M DOT**, up from 23.36M at the start of the window; it pays out only when DOT holders vote for a spend. The **governance pool** that keeps 32.2% of all new DOT grew from **0.48M** to **4.94M DOT** and has not spent any yet. A **grant wallet** that handed out about 6.83M DOT as two-year vesting in September still holds **175.8K DOT**. The foundation behind Polkadot does not publish its wallets, so its holdings are not tracked. We re-read these balances on-chain at every rebuild. If any of these balances falls between checks, the outflow is booked as a Foundation + unscheduled unlock at the next check — though for DOT, where these coins already count as circulating, spending them moves coins inside the float rather than adding new ones.

## How DOT compares to other proof-of-stake Layer 0 and Layer 1 chains

**DOT vs ETH.** Both pay stakers in newly created coins. Ethereum mints more as more ETH is staked and burns part of every fee, so its net rate depends on how busy the chain is. Polkadot now mints a fixed amount per unit of time, set by a cap schedule, and burns almost nothing. DOT supply growth is therefore easier to predict than ETH supply growth, but there is no fee burn to pull it down when the chain gets busy.

**DOT vs ATOM and other uncapped staking chains.** Many staking chains have no hard cap and set their rate by how much is staked. Polkadot moved the other way in 2026: a **2.1B DOT hard cap** and a stepped cut every two years, each time issuing 13.14% of the room left under the cap. That makes DOT closer to a Bitcoin-style curve than to an open-ended staking coin, although the cap was set by a community vote and could in principle be changed by another.

**DOT vs burn-heavy chains.** Chains such as BNB Chain and Ethereum remove coins through burns. Polkadot chose to keep fees and penalties in a pool that governance can spend on stakers, the treasury or a reserve. That trades a deflationary lever for a budget: the coins stay in supply, and the question becomes how the pool is spent.

## What to watch in the next 90 days

**The dotUSD vote.** Referendum 1944 would launch a DOT-backed stablecoin, with DOT locked as collateral and some Treasury DOT used to start a trading pool; it was still in its decision period on Sep 29 2026 with strong support. Locked collateral stays in the circulating count, so it would not change the 90-day number.

**The governance pool.** The pool held 4.94M DOT on Sep 29 2026 and grows by about 49K DOT a day. A vote to spend it, or to change its 45.2% / 22.6% / 32.2% split, would move coins inside the float; a vote to change the minting rate would change the sell row.

**Treasury spends.** A recovery loan for people hit by the April 2026 bridge exploit, about 795K DOT, was still at the discussion stage in September 2026. Any large Treasury payout is watched as a Foundation + unscheduled unlock.

**The blockspace burn.** Plans to send blockspace fees into the pool instead of burning them would remove the last small burn. The next scheduled cut to DOT issuance is not until Mar 14 2028.

## Summary

DOT supply is growing about **0.81% every 90 days**: Polkadot mints about **153,132 DOT a day** under a **2.1B DOT hard cap**, and since March 2026 it burns almost nothing, because fees and penalties now go into a governance pool. The minting rate is fixed until the next step down on Mar 14 2028, so the next 90 days should look like the last. The main risk to that reading is governance: the cap, the rate and the pool are all set by DOT holder votes. With about 1.70B DOT out of a 2.1B cap already created, roughly 395M DOT is left to mint over the coming decades.

---

*MrNasdog Pressure Framework analysis of DOT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*
