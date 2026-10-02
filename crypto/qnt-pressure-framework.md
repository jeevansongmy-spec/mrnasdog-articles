---
title:         "QNT Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "QNT supply is flat: no new QNT since 2018, no unlocks, no burn. Only 6.25 QNT was lost in 90 days, net 0.00%, the same next. Sale contract still open."
canonical_url: "https://mrnasdog.com/research/qnt/inflation"
tags:          ["crypto", "qnt", "quant", "interoperability"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/qnt/inflation](https://mrnasdog.com/research/qnt/inflation)*

# QNT Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

QNT supply is flat. Quant has created **no new QNT** since June 2018, nothing vests, and nothing buys back or burns QNT. Over the 90 days to Oct 2 2026 the only flow was **6.25 QNT** lost by mistake in the token's own contract, against **14.54M QNT** in circulation: a net change of **0.00%**, and the same for the next 90 days. The monitor reads **+0.05%**. The one ceiling worth knowing is not a cap in the code: the owner of the 2018 sale contract could still create up to **27.50M QNT**, and has not used that power since 2018.

## The verdict, in one paragraph

Our ledger for Quant (QNT) shows **0 QNT** of new supply and **6.25 QNT** taken out of the market over the last 90 days, so net supply moved **0.00%**. The monitor, which divides market value by price each day, reads **+0.05%**. The gap is **0.05 percentage points**, well inside our 0.5-point limit, so no warning chip is needed and the two readings agree. QNT is a **fixed-float token**: no emission, no unlocks, no burn, and a supply that has not grown since the 2018 token sale ended.

## Sell pressure: where new QNT comes from

**Protocol inflation is 0.** QNT is an ERC-20 token on Ethereum with no block rewards, no staking pay and no emission. The only way to create QNT is the mint function, and only the 2018 token-sale contract may call it. We read that sale contract at both ends of the window: the sale stayed closed, and the owner wallet that could reopen it did not send a single transaction. The chain shows no new QNT minted in these 90 days; all **24.43M QNT** ever created were minted in June 2018.

**Vesting unlocks are 0.** Quant has no vesting calendar. The whole supply was handed out in one go in 2018, unlock trackers list no QNT schedule, and **99.5%** of the counted supply already circulates. There is no team or investor tranche waiting for a date.

**Foundation and unscheduled unlocks are 0.** Two twin wallets, one of them publicly linked to the Quant founder, hold **600,000 QNT** each. On Sep 29 2026, after about seven years without a move, they sent **25,776 QNT** and **22,807 QNT** to new wallets. Those coins were already counted as circulating, so the move adds nothing new to supply, even if some of it is later sold.

**Long-term locked or bankruptcy is 0.** No estate, trustee or long lock pays QNT out. The **9.55M QNT** held by the token contract can never be moved, so it is gone for good rather than locked.

## Buy pressure: where new QNT goes

**Programmatic buyback is 0.** Quant runs no buyback. When clients pay for Overledger licences in stablecoins, the company sets aside QNT it already holds rather than buying QNT on the market.

**Protocol fee burn is 0.** Using the Overledger network does not destroy QNT, and the QNT token has no burn function at all.

**Foundation buy is 0.** No announcement and no wallet flow in the window shows Quant or any treasury buying QNT.

**New long-term lock is 0.** Client licences do lock QNT, but the locked coins come from holders who are already counted as circulating, and Quant does not publish the size. A lock of counted coins takes nothing out of the count.

**Coins lost in the token contract: 6.25 QNT.** People sometimes send QNT to the token's own address by mistake, and from there it can never come back. In these 90 days that happened 22 times for **6.25 QNT**; over the past year it added up to **288 QNT**. It is a real removal from supply, and far too small to move the reading.

## Foundation and overhang

The largest overhang is not a wallet but a door: the owner of the 2018 sale contract can still record and mint about **6.47M QNT** on its own, and up to **21.04M QNT** more by reopening the sale to buyers. Together that is more than the whole circulating supply. The owner wallet last sent a transaction in June 2019. We check the sale contract and the owner wallet at every rebuild.

The two twin wallets still hold **600,000 QNT** each after the Sep 29 2026 moves. A third large wallet, quiet for years, moved **492,721 QNT** to a new wallet on Sep 30 2026, also inside the circulating count. Quant also keeps QNT to back client licences: the treasury contracts it publishes hold none, and the rest sits at no public address with no published balance. A further **68,317 QNT** of the counted supply is classed as not circulating, with no named owner.

If any of these balances falls between refreshes, or the sale contract creates new coins, the outflow enters Sell #3 at the next refresh.

## How QNT compares to other enterprise and infrastructure tokens

Most infrastructure tokens add supply in one of two ways: a staking reward paid in new coins every block, or a calendar of team and investor unlocks. QNT has neither. Its supply was fixed at the 2018 sale, so its 90-day inflation sits at **0.00%**, below chains that pay validators in fresh coins and far below tokens still working through multi-year vesting.

The flip side is that QNT has no built-in buyer. Tokens with a fee burn or a revenue buyback take coins off the market as their networks get used. Quant earns from software licences, and that income does not turn into QNT bought on the market. So QNT is neither shrinking nor growing: a **fixed float**, where the price depends on demand alone.

Compared with fixed-cap coins whose limit is written into the protocol, the QNT limit is a matter of practice rather than code: the mint path still exists in the old sale contract. It has been unused for eight years, which is a strong habit, but it is not the same as a cap that cannot be changed.

## What to watch in the next 90 days

**The two twin wallets.** After the Sep 29 2026 moves, any transfer of the remaining 1.2M QNT to exchanges would be selling from inside the float; it would not change supply, but it would change the market.

**The 2018 sale contract.** Any transaction from its owner, or any new mint event, would be the first new QNT since 2018 and would enter the ledger at once.

**The Clearing House rollout.** The Clearing House named Quant as technology provider for its on-chain money network on Sep 24 2026, with bank access planned for the first half of 2027. Watch whether the bank fees create any need for QNT bought on the market.

**Staking on Overledger Fusion.** Quant plans node staking paid from network fees, not new coins, but has not published the final rules. Staked QNT would still count as circulating, so it would not change supply unless the rules move coins outside the count.

**A new licence or token rule.** If Quant changed how licences use QNT, for example by buying QNT with stablecoin fees, Buy #1 would turn on.

## Summary

Quant (QNT) supply is flat: no new QNT since 2018, no vesting, no burn and no buyback, so net supply moved **0.00%** over the 90 days to Oct 2 2026 and is projected to stay there. The only removal was **6.25 QNT** lost in the token contract. The key risk is not inflation by design but the old sale contract, whose owner could still create up to **27.50M QNT**. Until that changes, QNT is a fixed float whose price rests on demand alone.

---

*MrNasdog Pressure Framework analysis of QNT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 2 2026.*
