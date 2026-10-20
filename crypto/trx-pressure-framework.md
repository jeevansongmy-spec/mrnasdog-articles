---
title:         "TRX Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "TRX supply is roughly steady: TRON minted 352.4M TRX in block rewards against a 223.55M TRX fee burn, +0.14% net over 90 days and about the same next. No cap."
canonical_url: "https://mrnasdog.com/research/trx/inflation"
tags:          ["crypto", "trx", "tron", "payments"]
published:     true
---
# TRX Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

*Originally published at [mrnasdog.com/research/trx/inflation](https://mrnasdog.com/research/trx/inflation).*

<!-- main-page -->
**Main page:** the full TRX coin page — signal, price drivers and the buy/sell questions → [mrnasdog.com/research/trx](https://mrnasdog.com/research/trx)

TRX supply is growing, but only a little. In the 90 days to Oct 19 2026, TRON created **352,395,176 TRX** in block rewards, and its fee burn destroyed **223,553,597 TRX**, so net supply rose **+0.14%** — and the next 90 days look the same. TRX has no supply cap: every block mints 136 new TRX, and only the fee burn pulls coins back out.

## The verdict, in one paragraph

Our ledger reads TRX at **+0.14%** net over the last 90 days and **+0.14%** over the next 90. The inflation monitor reads **+0.11%** for the same stretch, a gap of **0.02 percentage points** — the two agree, so no warning chip is shown. TRON adds **352.4M TRX** every 90 days and burns back **223.55M TRX**, about 63% of it. Label: **a mint-and-burn chain where the burn falls short** — mildly inflationary, with the size of the gap set by how much TRON is used.

## Sell pressure: where new TRX comes from

**Protocol inflation is the only source of new TRX: 352.4M TRX in 90 days.** TRON is run by 27 Super Representatives, elected by TRX holders who stake and vote. Every block pays 8 TRX to the Super Representative that produced it and 128 TRX into a pool shared with the voters, so each block mints 136 TRX. Between Jul 22 and Oct 19 2026 the chain produced 2,591,141 blocks, which works out to 352,395,176 new TRX — about 3.92M TRX a day. Both reward sizes were last set by a holder vote in June 2025. The only change voted in this window, on Aug 28 2026, upgraded the smart-contract engine and did not touch rewards.

**Vesting unlocks add 0 TRX.** The 2017 token sale and the early team and foundation shares were released years ago. Circulating TRX equals total TRX within about 72K coins, so there is nothing left on a vesting calendar.

**Foundation and unscheduled unlocks add 0 TRX.** The old TRON Foundation fund accounts now hold only about 283 TRX and have not moved since 2022. The biggest named holder is Tron Inc., a Nasdaq-listed company with about 718.9M TRX, but it bought those coins in the market, so they were already part of the circulating supply. If it sold, coins would change hands; no new TRX would appear.

**Long-term locks and bankruptcy releases add 0 TRX.** No court estate, trustee or long lock holds TRX that is waiting to come out. Staked TRX can be withdrawn after a 14-day wait, but it is counted as circulating the whole time, so unstaking adds nothing new.

## Buy pressure: where new TRX goes

**The protocol fee burn removed 223.55M TRX in 90 days.** On TRON, every transaction needs bandwidth, and smart-contract calls such as stablecoin transfers also need energy. Users either stake TRX to get these resources for free or pay for them in TRX, and every TRX paid this way is destroyed. Over the window the burn came to 223,553,597 TRX, about 2.48M TRX a day — enough to cancel about 63% of the new block rewards. The burn was heavier at the start: 81.2M TRX in the first 30 days, then 71.8M and 70.6M, with no change to fee rules behind the drop. Our forward figure keeps the full 90-day amount.

**There is no programmatic buyback (0 TRX).** The TRON protocol never buys TRX back; its only sink is the fee burn above.

**There is no foundation buy (0 TRX).** Tron Inc. buys about $50K of TRX every day under a 360-day plan that began on Jan 22 2026, and on Oct 14 2026 it set up a share sale of up to $200M to buy more. That is real buying, but the company holds the coins in a wallet that is already counted as circulating, so the float does not get smaller.

**New long-term locks add 0 TRX.** About 45.37B TRX is staked for votes and free resources, down from 45.83B on Jul 21 2026. Staked TRX still counts as circulating, so staking does not take coins out of the float.

## Foundation and overhang

TRX has almost no team-controlled overhang. The legacy TRON Foundation fund accounts hold about 283 TRX in total, last active in 2022; we read them on-chain at every rebuild. Total supply is only about 72K TRX above circulating supply, so there is no large reserve waiting outside the float. The largest named holder, Tron Inc., held about 718.9M TRX in mid-October 2026 and keeps adding to it; those coins are inside the float, and we check its disclosures at every rebuild. If the foundation accounts or the company treasury start sending TRX out between our checks, that outflow goes into the foundation row at the next refresh.

## How TRX compares to other high-throughput Layer 1s

TRX sits in the same family as Ethereum: both mint new coins for the people who secure the chain and burn part of every fee, and neither has a supply cap. The difference is scale. On TRON the burn cancels about 63% of new TRX, because stablecoin transfers create steady fee demand all day. That is why TRX supply grows by only about 0.14% a quarter even though its block rewards are large.

Against BNB, the contrast is policy. BNB runs a scheduled burn toward a fixed target supply, so its supply is planned to shrink no matter how busy the chain is. TRX has no such target: its supply only shrinks in a quarter when fees burn more than the 136 TRX a block that the chain mints. Against Bitcoin, the contrast is the cap. Bitcoin has a hard limit and halvings that cut new supply on a fixed calendar, while TRX block rewards can only change through a holder vote — and the last one, in June 2025, cut them.

So TRX supply depends on use more than on any schedule. A busy month pushes it toward flat or shrinking; a quiet month, or cheaper fees, lets the mint pull ahead.

## What to watch in the next 90 days

**Fee-cut proposals.** Two open ideas on TRON's improvement board would lower the fee for changing account permissions (last discussed Oct 7 2026) and for multi-signature transactions (opened Oct 6 2026). Neither has an on-chain vote yet; if they pass, the burn would shrink slightly.

**Block-reward votes.** No proposal is pending on-chain as of Oct 20 2026. Any vote that changes the 8 TRX or 128 TRX block rewards would move the 352.4M TRX quarterly mint at once.

**The burn trend.** The last 30 days burned 70.6M TRX. If stablecoin traffic moves elsewhere or more users stake for free energy, the burn falls and net inflation rises; a busier chain does the opposite.

**Tron Inc.'s buying.** The company's share sale of up to $200M, set up on Oct 14 2026, and its purchases every day add buyers, but they do not change supply. Tron Inc. said on Oct 19 2026 it had been elected one of the 27 Super Representatives, so it now also earns block rewards.

## Summary

TRX is mildly inflationary: TRON mints **352.4M TRX** every 90 days in block rewards and burns about **223.55M TRX** in fees, so supply grows about **+0.14%** a quarter, in line with the monitor's **+0.11%**. There are no unlocks, no foundation reserve outside the float and no buyback; the only lever is how much people pay in fees. The key risk is a weaker burn — cheaper fees or fewer paid transfers would let the fixed 136 TRX a block pull further ahead. TRX has no supply cap, and its block rewards can change only by a vote of the Super Representatives.

---

*MrNasDog Pressure Framework analysis of TRX, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 20 2026.*
