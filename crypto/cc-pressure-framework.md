---
title:         "CC Inflation Analysis · October 2026 · Supply growing · projected to keep growing"
description:   "Canton Coin supply is growing: 2.11B new CC in 90 days against a 1.35B fee burn gives +1.91% net, the same next. No pre-mine, no vesting, no supply cap."
canonical_url: "https://mrnasdog.com/research/cc/inflation"
tags:          ["crypto", "cc", "canton", "layer1"]
published:     true
---
*Originally published at [https://mrnasdog.com/research/cc/inflation](https://mrnasdog.com/research/cc/inflation)*

<!-- main-page -->
This is the long supply read. For the signal, the price drivers and the questions people ask about Canton Coin, see [mrnasdog.com/research/cc](https://mrnasdog.com/research/cc).

# CC Inflation Analysis · October 2026 · Supply growing · projected to keep growing

Canton Coin (CC) supply is growing at a steady pace. Over the 90 days to Oct 11 2026, the Canton Network minted **1.95B CC** in rewards, the Canton Foundation's development fund paid out **76.5M CC** in grants and super-validator votes released **91.0M CC** from the unclaimed-reward pool, while the traffic-fee burn destroyed **1.35B CC**. Net supply rose **+1.91%**, and the MrNasDog Pressure Framework projects about the same **+1.91%** for the next 90 days. CC has no cap: the burn only slows the growth, and right now it removes about two coins for every three that are created.

## The verdict, in one paragraph

The framework reads Canton Coin at **+1.91% net** over the last 90 days: **2.11B CC** of new supply against **1.35B CC** burned, on a circulating base of **39.83B CC**. The monitor, which measures the change in the supply count itself, reads **+1.94%** for almost the same window. The gap is **0.02 percentage points**, well inside the 0.5-point line, so there is no warning chip and no deep walk was needed. The forward reading stays at **+1.91%** because nothing in the issuance schedule changes before 2029. In one line: CC is a burn-and-mint coin whose mint still runs ahead of its burn.

## Sell pressure: where new CC comes from

**Protocol inflation: 1.95B CC.** Canton Network runs in rounds of about ten minutes, and in every round it mints new CC for the parties that earned it. Over the window, 12,608 rounds minted **1,946.9M CC**, about **21.6M CC a day**. Apps took **1,411.5M**, validators **268.3M** and super validators **267.2M**. The Canton Coin issuance curve allows up to 10B CC a year until its next cut in 2029, and 5% of every round is set aside for the development fund, so up to about 2.34B CC could have been minted as rewards in these 90 days. Only about 83% was claimed; the rest falls into the unclaimed-reward pool. Each 30-day slice of the window minted close to 650M CC, so the next 90 days are projected at the same pace.

**Vesting unlocks: 0.** Canton Coin was a fair launch with no pre-mine, no team share and no investor allocation, so there is no vesting schedule and no unlock cliff to wait for.

**Foundation and unscheduled unlocks: 76.5M CC.** Under CIP-0082, 5% of every round goes to a development fund governed by the Canton Foundation. Those coins only exist once a grant is paid and the grantee claims it. The fund paid **96 grants worth 76.5M CC** in the window, out of **108.2M CC** since its first payout in April 2026. It has paid out every month since May 2026, so the framework projects about the same amount for the next 90 days.

**Long-term locked or bankruptcy: 0.** No bankruptcy estate, court trustee or old lock holds Canton Coin outside the float.

**Releases from the unclaimed-reward pool: 91.0M CC.** Rewards nobody claims are not lost for good: they sit in a pool that super validators can release by vote. Ten releases landed in the window, **91.0M CC** in all, mostly to new network partners that met agreed goals: Zenith **25.4M**, LayerZero **19.6M**, Chainlink **19.2M** and Wormhole **15.1M**, plus smaller ones to Canton Strategic Holdings, Blockdaemon, QCP Group and Franklin Templeton. One earlier Zenith release expired unminted and was voted again, so it is counted once. Releases came in 11 of the last 12 months, and six new super validators approved in September 2026 have goal-linked releases ahead, so the next 90 days are projected at the same size.

## Buy pressure: where new CC goes

**Programmatic buyback: 0.** No contract and no treasury buys Canton Coin back. Listed companies that hold CC as a treasury asset buy it on the market, so those coins were already circulating.

**Protocol fee burn: 1.35B CC.** Every transaction on the Canton Network needs traffic on the Global Synchronizer, and that traffic is priced in dollars but paid by burning CC. The burn destroyed **1,352.9M CC** in the window, about **15.0M CC a day**, or about **64%** of all new coins. The three 30-day slices burned 451.0M, 466.4M and 435.5M, so the forward figure keeps the 90-day rate. Because fees are set in dollars, a higher CC price burns fewer coins for the same activity, and a lower price burns more.

**Foundation buy: 0.** Nothing in the window shows the Canton Foundation or its development fund buying CC; the fund pays out new coins.

**New long-term lock: 0.** Under CIP-0105, super validators must lock most of the CC they have earned to keep their voting weight, and their lock wallets hold about **18.4B CC**. Featured apps lock about **0.89B CC** under CIP-0116. These locks are real, and an unlock pays out only 1/365 a day, but the locked coins still count as circulating, so a bigger lock takes nothing out of the float.

## Foundation and overhang

Two pools sit outside the float and can add new CC. The first is the development fund: about **280M CC** has been set aside for it so far and **108.2M** has been paid, so roughly **172M CC** is still unminted. The second is the unclaimed-reward pool, whose size is not published; it grows every round by the rewards nobody claims, and only a super-validator vote can release it. Both are checked at every rebuild against the payout list and the vote list.

Inside the float, the biggest holders we track are the super-validator lock wallets (about **18.4B CC**, of which the Foundation's own lock is about **1.4B**) and the featured-app lock wallets (about **0.89B**). Their coins are already counted, so moving or selling them adds no new supply. If the development fund or the unclaimed-reward pool pays out more between refreshes, that outflow enters the sell side at the next refresh.

## How CC compares to other burn-and-mint Layer 1s

Canton Coin is a burn-and-mint equilibrium design: users pay a dollar-priced fee by destroying the coin, and the network mints new coins to reward the people who run and use it. Helium's HNT made this model known, and the logic is the same: supply only stops growing when the dollar value of fees burned matches the rewards minted. On Canton the burn already covers about two thirds of new coins, which is a high share for a young network, but the gap is still clearly positive.

Ethereum also mints and burns, but its two sides work differently. Ether is created for stakers in proportion to the stake, and its base fee is burned in ETH, not set in dollars. Canton Coin fixes the reward budget by a time schedule instead, and its burn moves with network use measured in dollars. Solana sits further away: a fixed inflation curve with only part of each fee burned. Among these, CC has the most direct link between real usage and supply, because every unit of Global Synchronizer traffic is paid for by burning CC.

The other difference is the start. Most Layer 1s launched with large team and investor shares that unlock for years. Canton Coin had none, so its supply growth comes only from rewards, the development fund and voted pool releases, and there is no vesting cliff to watch.

## What to watch in the next 90 days

**New super validators.** Six were approved between Sep 11 and Sep 25 2026, including a16z crypto, LSEG, Paxos and Marex; their goal-linked releases from the unclaimed-reward pool would land in the sell side as they are voted.

**CIP-0120.** The proposal for traffic-based validator rewards is still under discussion; if it passes, the split of the round mint changes, and possibly the share that goes unclaimed.

**On-chain locking.** CIP-0127 would move super-validator and featured-app locks into on-chain contracts. That changes how locks are checked, not how many coins exist.

**Traffic growth.** Large institutions started tokenization work on Canton in October 2026. More traffic means a bigger burn, which is the one force that can bring CC closer to flat supply.

**Development fund payouts.** Grants have been paid every month; a much larger month would raise the sell side above the projection.

## Summary

The MrNasDog Pressure Framework reads Canton Coin (CC) at **+1.91% net** over the last 90 days and the next 90: **1.95B CC** of reward mints, **76.5M CC** of development-fund grants and **91.0M CC** of voted pool releases against a **1.35B CC** traffic-fee burn, with no pre-mine, no vesting and no supply cap. The burn is large and tied to real network use, but the reward mint still runs ahead of it. The key risk is that the reward budget and the two outside pools keep adding coins faster than fees burn them; the upside case is traffic growth that lifts the dollar burn toward the mint. Until one of those changes, CC supply keeps growing a little under 2% every 90 days.

---

*MrNasDog Pressure Framework analysis of CC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 12 2026.*
