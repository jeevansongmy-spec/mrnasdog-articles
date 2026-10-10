---
title: "ATOM Inflation Analysis · October 2026 · Supply growing · projected to keep growing"
description: "Supply growing, projected to keep growing: ATOM reads +3.04% over 90 days. Cosmos Hub minted 16.24M ATOM at a real 12.7% rate and burned only 2.02K by slashing."
canonical_url: "https://mrnasdog.com/research/atom/inflation"
tags: ["crypto", "atom", "cosmos", "staking"]
published: true
---
*Originally published at [https://mrnasdog.com/research/atom/inflation](https://mrnasdog.com/research/atom/inflation)*

<!-- main-page -->
This is the long supply read. For the signal, the price drivers and the questions people ask about Cosmos Hub, see [mrnasdog.com/research/atom](https://mrnasdog.com/research/atom).

# ATOM Inflation Analysis · October 2026 · Supply growing · projected to keep growing

**ATOM supply is growing fast, and it should keep growing.** In the 90 days to Oct 4 2026 the Cosmos Hub minted **16.24M ATOM** for stakers, while slashing destroyed only **2,021 ATOM**, so net supply rose **+3.04%**; the next 90 days project **+3.17%**. ATOM has no supply cap and no fee burn, and its staking reward runs at the 10% ceiling — closer to **12.7%** a year in practice, because Cosmos Hub blocks arrive faster than the mint rule assumes.

## The verdict, in one paragraph

Our ledger reads **+3.04%** net new ATOM over the last 90 days and **+3.17%** for the next 90. The inflation monitor, which tracks the circulating figure the market reads, shows **+2.99%** for the same stretch. The gap is **−0.05 percentage points**, well inside our 0.5-point tolerance, so no warning chip is shown and no deep walk was needed: two independent reads of ATOM supply agree. ATOM is **a high-issuance staking chain with almost no sink** — new coins flow to stakers every block, and close to nothing leaves.

## Sell pressure: where new ATOM comes from

**Protocol inflation is the whole story: 16.24M ATOM in 90 days.** The Cosmos Hub mint module pays new ATOM to stakers in every block. Its yearly rate moves between 7% and 10% depending on how much ATOM is staked against a 67% goal. Only **63.3%** is staked today (338.39M ATOM), so the rate is pinned at its **10%** maximum, and it stayed there at every check through the window. We read the supply at both ends — 517.94M ATOM on Jul 6 2026 and 534.18M ATOM on Oct 4 2026 — and added back the coins that were burned, which gives **16,244,654 new ATOM**, about 180,500 a day. Of each block reward, 2% goes to the community pool and the rest to validators and their delegators.

**Why ATOM issuance runs above the headline 10%.** The rate is split per block, on the assumption of 4.36M blocks a year — one every 7.23 seconds. Cosmos Hub blocks actually arrive about every **5.71 seconds**, roughly 5.5M blocks a year, and nothing in the rule corrects for it. So each block pays its full share more often, and real issuance comes to about **12.7%** a year before compounding. The window also held a **25-hour halt**, from Sep 22 to Sep 23 2026, when validators stopped the chain after the Neutron governance attack; no ATOM was minted while it was down. Our next-90-day figure of **16.95M ATOM** uses today's larger supply and today's block pace, and does not assume another halt.

**Vesting unlocks: zero.** The 2017 fundraiser and the genesis allocations finished unlocking years ago, unlock trackers list the Cosmos Hub as fully unlocked, and circulating supply sits within about 10.6K ATOM of total supply. There is no locked pile left to open.

**Foundation and unscheduled unlocks: zero.** The large ATOM holders we track — the community pool, the Interchain Foundation, a recovery multisig and the fee account — are all already counted as circulating. If they move or sell, coins change hands, but no new ATOM enters the market.

**Long-term locks or bankruptcy: zero.** No court estate or trustee pays out ATOM, and staked ATOM unbonds in 21 days, so staking never acts as a long lock.

## Buy pressure: where new ATOM goes

**Programmatic buyback: zero.** No contract or treasury buys ATOM back. A tokenomics review run for the Hub has delivered its second-phase recommendations, but they are still in review, with no vote and no date.

**Protocol fee burn: zero.** Unlike Ethereum's base-fee burn, Cosmos Hub fees are not destroyed. Base fees gather in a fee account that holds **61.05K ATOM**, and its balance kept rising between two reads minutes apart. Those coins stay in circulation.

**Foundation buy: zero.** Nothing shows the Interchain Foundation or the community pool buying ATOM in the window.

**New long-term lock: zero.** Staking is real and slashable, but staked ATOM still counts as circulating, so a larger stake removes nothing from the float. It only keeps the mint rate where it is.

**Slashing burn: 2,021 ATOM.** This is the one place ATOM is destroyed. When a validator misses too many blocks, a small slice of its stake is burned. It happened in bursts on about Jul 9, Aug 6, Sep 3, Sep 9 and Sep 22 2026, and the burn events at those blocks match the drop in supply to the cent. That is about **8,000 times smaller** than the new issuance. Spam governance proposals were vetoed in the window too, but none reached quorum, so their deposits were returned rather than burned.

## Foundation and overhang

Four large ATOM piles sit under group control, and every one is already inside the circulating count. The **community pool** holds **11.40M ATOM** and grows from the 2% tax on rewards; it can only be spent by a passed governance vote, and we read it from the chain at each rebuild. The **Interchain Foundation** reported **14.93M ATOM** at Jun 30 2026 in its monthly treasury snapshot, the last one published; it names no wallets, so we follow its reports. A **recovery multisig** holds **1.23M ATOM** that the Hub took back from the Neutron attacker when it restarted on Sep 23 2026; a proposal to send it back to Neutron users is being drafted. The **fee account** holds **61.05K ATOM**. If any of these balances falls between our checks, we look at where the coins went and, if they reached the market from outside the float, they enter Sell #3 at the next refresh.

## How ATOM compares to other proof-of-stake Layer 1s

Most large proof-of-stake chains pair issuance with some kind of sink. Ethereum burns its base fee, which offsets part of validator pay; Solana's yearly rate steps down a little each year toward a floor. ATOM has neither: no fee burn, no scheduled step-down, and a mint rate that rises to its 10% ceiling whenever less than 67% of supply is staked — which has been the case through this whole window. Its only removal, slashing, is a penalty rather than a design feature.

The other difference is mechanical. Chains that pay rewards by time, or that rescale when block times change, issue what their headline rate says. ATOM pays per block against a fixed 4.36M-blocks-a-year assumption, so faster blocks quietly raise issuance — here by about a quarter, from 10% to roughly 12.7%. Compared with capped, halving-based coins like Bitcoin, ATOM is at the opposite end: uncapped, continuous, and adding about 3% to supply every quarter.

## What to watch in the next 90 days

**Tokenomics Phase 2.** The Hub's tokenomics review has handed in its recommendations, and a wrap-up post with the full report and a timeline is promised next. Any vote that lowers the 10% ceiling or adds a burn would change this ledger.

**The staked share.** At **63.3%** staked, the mint stays at its maximum. Only a climb above 67% would let the rate drift down toward 7%.

**Block pace.** If Cosmos Hub blocks speed up or slow down, issuance follows, because the mint rule does not adjust for it.

**The 1.23M ATOM recovery vote.** A Hub proposal to send the recovered coins back to Neutron users is being drafted. The coins are already circulating, so this moves no supply, but it decides who can sell them.

**Community pool spending.** The pool holds 11.40M ATOM; large spending proposals put more ATOM in active hands even though the coins already count as circulating.

## Summary

ATOM is inflationary by design: the Cosmos Hub minted **16.24M ATOM** in 90 days against a **2,021 ATOM** slashing burn, a net **+3.04%**, with **+3.17%** projected for the next 90 days. The mint rate is pinned at its 10% ceiling because less than 67% of ATOM is staked, and faster-than-assumed blocks lift real issuance to about 12.7% a year. There is no supply cap, no fee burn and no buyback, so the key risk is steady dilution for anyone who does not stake. Only a governance change to the mint rules, or a much higher staked share, would slow it.

---

*MrNasdog Pressure Framework analysis of ATOM, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 4 2026.*
