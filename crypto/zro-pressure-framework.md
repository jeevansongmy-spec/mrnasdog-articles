---
title:         "ZRO Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description:   "LayerZero mints no ZRO — supply is fixed at 1B across seven networks — yet monthly cliffs released 46.7M in 90 days against a 0.43M buyback. Framework reads +13.08% net."
canonical_url: "https://mrnasdog.com/research/zro/inflation"
tags:          ["crypto", "zro", "layerzero", "interoperability"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/zro/inflation](https://mrnasdog.com/research/zro/inflation)*

# ZRO Inflation Analysis · August 2026 · Supply growing, projected to keep growing

LayerZero mints no ZRO at all — the supply is fixed at **1,000,000,000**, and adding the token up across the seven networks it lives on returns that number exactly, at both ends of the window. Yet ZRO is one of the most supply-pressured assets the MrNasdog Pressure Framework tracks, because the monthly vesting calendar put about **46.7M ZRO** into tradable hands over 90 days against only **0.43M** of buyback — a net of **+13.08%**, rising to **+19.69%** forward as three more cliffs land. LayerZero is a hard-capped token with an uncapped release calendar, and the calendar is the whole story.

## The verdict, in one paragraph

For the 90 days ending **Aug 19 2026**, the Pressure Framework reads **ZRO at +13.08% net**, and **+19.69%** on the forward view. Total sell pressure was **46.7M ZRO** against **0.43M** of buy pressure, on a circulating base of **353.3M**. Our independent supply monitor reads **+40.42%**, a gap of **27.34 percentage points**, which does trigger a monitor-gap flag on this build. The gap is bookkeeping, not supply: the monitor tracks a classified circulating-supply figure that sat flat for months and then jumped **+100.94M** in a single day on **Jul 8 2026**, catching up on cliffs that had already happened. No LayerZero contract moved anything close to that on that date. The label that fits ZRO is **a hard cap with a fast release calendar** — the 1 billion ceiling is permanent and real, but roughly two thirds of ZRO still sits outside the counted float, and it is walking in at 23.3M a month.

## Sell pressure: where new ZRO comes from

Protocol inflation, the first row of the ledger, is **zero** and will stay zero. ZRO is an omnichain token: bridging it burns the balance on the source network and re-mints it on the destination, so no single network's supply figure is the real one. Summing all seven LayerZero deployments — Ethereum, Arbitrum, BNB Chain, Base, Optimism, Polygon and Avalanche — gives **1,000,000,000.000000 ZRO** on **Aug 19 2026** and the same figure on **May 21 2026**. The legs moved against each other in both directions and netted to nothing, which is what bridge traffic looks like. There is no staking yield and no block reward paid in ZRO, because the Zero network LayerZero is building has not launched.

The whole of ZRO's sell pressure is vesting unlocks. Strategic-partner and core-contributor allocations release on the **20th** of every month: about **12.7M ZRO** to strategic partners — LayerZero's own published figure, reduced from 15M after the foundation repurchased 50M from early investors — plus roughly **10.6M** to contributors, for **23.3M ZRO** per cliff. Two of those cliffs fell inside this window, on **Jun 20 2026** and **Jul 20 2026**, giving **46.7M ZRO**. It matters that LayerZero has no on-chain vesting escrow: unlocked ZRO lands directly in the holder's own custody wallet and is tradable from that moment, whether or not it is sold. LayerZero itself reports that of the **134.7M ZRO** unlocked to investors by **May 31 2026**, **63.8%** is still held — held, which is not the same as locked.

The remaining two sell rows are zero. Foundation and unscheduled unlocks released nothing: the two large multisigs holding roughly **175.6M ZRO** did not move a single token across the window. And there is no bankruptcy estate distributing ZRO — the **40M** once tied to the FTX and Alameda claim was repurchased before the LayerZero token launch and returned to strategic partners under the settlement, so it arrives inside the ordinary vesting calendar rather than as a separate stream.

## Buy pressure: where new ZRO goes

LayerZero does run a real buyback. Revenue from Stargate, the largest application built on LayerZero, buys ZRO on the open market once a month, and since April 2026 the full revenue share goes to it. Reading the disclosed destination wallet directly rather than trusting the summary, the balance went from **1,765,167 ZRO** on **May 21 2026** to **2,191,569** on **Aug 19 2026** — three monthly purchases of **124,574**, **141,557** and **160,271**, for a realised **0.43M ZRO**. Every one of those increments reproduces LayerZero's published monthly figure to the token, and the wallet has never had an outflow. The bought ZRO is therefore accumulated, not destroyed, which is why it also appears on the sell side as a tracked overhang.

The protocol fee burn is **zero**, and this is the row most often reported wrongly. LayerZero's design lets holders switch on a protocol fee whose proceeds convert to ZRO and burn, voted every six months in an immutable on-chain referendum. It has been put to holders four times — December 2024, June 2025, December 2025 and the vote that closed on **Jun 27 2026**, inside this window — and resolved "off" every time. The cross-chain total settles it arithmetically: if any ZRO had ever burned, the seven-network sum could not still be exactly 1,000,000,000. The next referendum falls around **Dec 20 2026**, outside the forward window. Foundation buying is zero for the window as well: the 50M repurchase and a 10 million dollar discretionary purchase both happened in late 2025 with no repeating schedule. No new long-term lock started either.

## Foundation and overhang

Roughly **646.7M ZRO** sits outside the counted float, and the Pressure Framework tracks four pieces of it. First, the LayerZero Foundation's **183M ZRO** — the remainder of its original allocation plus the 50M repurchased from strategic partners — is re-locked until the Zero network launches, which LayerZero guides to **fall 2026** with no committed date. Second, two identified multisigs on the Ethereum leg hold about **175.6M ZRO** between them and read identically at both ends of the window. Third, the buyback accumulation wallet holds **2.19M ZRO**, its entire lifetime purchase, and has never sent any out. Fourth, the unvested balance of the strategic-partner and core-contributor allocations continues to arrive on the monthly calendar already counted in the sell ledger. None of these fired in the window, so all four carry a value of zero. If any of these balances falls between refreshes, the outflow enters the Foundation and unscheduled row at the next refresh.

## How ZRO compares to other cross-chain infrastructure tokens

The instinct is to file ZRO with the hard-capped assets, and on the mint side that is correct: like a fixed-supply proof-of-work coin, LayerZero can never create a ZRO above its ceiling, and unlike an uncapped continuous-emission layer-1 there is no validator subsidy quietly diluting holders every block. But a cap governs the numerator of dilution, not the denominator. A fixed-supply chain that distributed its coins over a decade of mining has a float close to its cap; ZRO's float is roughly a third of its cap, so the same absolute release is three times heavier as a percentage. That is why a token with no inflation reads more inflationary than most chains that do inflate.

Against fee-burning networks the difference is structural rather than a matter of size. A chain that burns a base fee has a destruction pipe wired into the protocol itself, firing on every transaction with no vote required; LayerZero has the same idea but gated behind a governance switch that has failed four times, so its burn capacity is real and its burn throughput is nil. And against exchange tokens that run scheduled buybacks and burns, the gap is what happens to the purchased token: those programmes destroy what they buy, while the LayerZero buyback parks it in a wallet, where it remains supply that could return. The buyback is also two orders of magnitude smaller than the unlock — **0.43M** against **46.7M** — so even burning every token bought would move the net reading by less than a percentage point.

## What to watch in the next 90 days

Three vesting cliffs of **23.3M ZRO** each land on **Aug 20 2026**, **Sep 20 2026** and **Oct 20 2026**; they are the entire forward sell ledger and the reason the forward reading is **+19.69%**. The Zero network mainnet launch, guided to fall 2026, is the single largest discrete risk on the board, because it releases the foundation's **183M ZRO** from its re-lock — no date has been committed, so the framework watches it rather than counting it. The buyback wallet is worth checking for its first ever outflow, which would convert an offset into sell pressure. LayerZero's monthly buyback disclosure will show whether Stargate revenue is still funding purchases at the recent pace of roughly **150K ZRO** a month. And the fifth fee-switch referendum falls around **Dec 20 2026**, just past this window; a first "on" vote would be the only mechanism capable of turning ZRO's ledger around.

## Summary

ZRO is a hard-capped token behaving like an inflationary one. LayerZero has never minted a token above its **1,000,000,000** ceiling and never burned one — the seven-network sum proves both — but a monthly vesting calendar released about **46.7M ZRO** into tradable hands over 90 days against a **0.43M** buyback, for **+13.08%** net and **+19.69%** ahead. The key risk is that the calendar runs into 2027 and the foundation's **183M ZRO** unlocks whenever the Zero network ships, while the one mechanism that could destroy supply, the protocol fee switch, has been voted down four times and stays off. The ceiling is real; the pressure is that most of ZRO has not walked through the door yet.

---

*MrNasdog Pressure Framework analysis of ZRO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 19 2026.*
