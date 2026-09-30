---
title:         "BNB Inflation Analysis · September 2026 · Supply shrinking · projected to keep shrinking"
description:   "BNB supply is shrinking: no issuance, a 1.62M BNB quarterly Auto-Burn plus the gas-fee burn give −1.22% net over 90 days, −1.24% next, toward a 100M floor."
canonical_url: "https://mrnasdog.com/research/bnb/inflation"
tags:          ["crypto", "bnb", "binance", "auto-burn"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/bnb/inflation](https://mrnasdog.com/research/bnb/inflation)*

# BNB Inflation Analysis · September 2026 · Supply shrinking · projected to keep shrinking

BNB supply is shrinking. Over the last 90 days the MrNasdog Pressure Framework counts **0 BNB** of new supply against **1,623,167 BNB** destroyed, a net change of **−1.22%**, and it projects **−1.24%** for the next 90 days as the next quarterly Auto-Burn lands. BNB Chain has no block reward and no vesting left, so the only flows that matter are two burns — a quarterly Auto-Burn set by a fixed public calculation, and a small share of every block's gas fees — and they continue until total supply reaches **100M BNB**.

## The verdict, in one paragraph

The framework reads BNB at **−1.22%** over the trailing 90 days, from Jul 2 to Sep 30 2026, and at **−1.24%** for the next 90 days. Our supply monitor, which watches the published circulating count, reads **−1.22%** over the same 90 days. The gap is **0.00 percentage points** — well inside the 0.5-point tolerance — so no warning chip is shown and no deep walk was needed. Both readings agree because BNB's published supply is defined as the starting supply less everything sent to the burn address, and the burn address is exactly what the framework reads on-chain. BNB is a deflationary coin by structural burn: nothing is added, and a large, predictable amount is removed every quarter.

## Sell pressure: where new BNB comes from

Protocol inflation is **0 BNB**. BNB Smart Chain pays its validators only from the gas fees people pay; there is no block subsidy and no staking reward printed from nothing. We checked this directly: the published supply plus the balance of the burn address stayed the same across the window to within a few coins, which is only possible if nothing was minted.

Vesting unlocks are **0 BNB**. BNB's sale, founding-team and early-backer allocations finished vesting in 2021, no unlock tracker lists anything still to release, and the circulating count is equal to total supply, so there is no locked bucket left to open.

Foundation and unscheduled unlocks are **0 BNB**. The large balances that exist — the Auto-Burn reserve and the old bridge contract — are already inside the circulating count, and moving coins inside the float adds no new supply. They are covered below under overhang.

Long-term locked or bankruptcy supply is **0 BNB**. There is no court estate, no trustee schedule and no expiring lock-up releasing BNB. Listed companies that hold BNB, and the US BNB fund, bought their coins on the open market.

## Buy pressure: where new BNB goes

The quarterly Auto-Burn is the big one. On **Jul 15 2026** the 36th Auto-Burn destroyed **1,615,828 BNB**, sent from the Auto-Burn reserve to the burn address in a single transaction. The amount is not chosen by hand: a published calculation takes the number of blocks BNB Smart Chain produced in the quarter and the quarter's median BNB price, so more blocks and a lower price mean a bigger burn. For July to September the blocks and a median price of about **$608** point to about **1.65M BNB** for the 37th Auto-Burn, expected around **Oct 15 2026**.

The protocol fee burn removed **7,340 BNB** over the window. Under BNB Chain's real-time burn, a fixed share of the gas fees in each block goes to the burn address instead of to validators. The rate was about 53 BNB a day in early July and about 86 a day after mid-July, as the chain got busier. Because BNB Smart Chain keeps gas prices very low, this burn is small next to the Auto-Burn — about 0.5% of the total removed.

There is no programmatic buyback (**0 BNB**): the Auto-Burn spends coins a reserve already holds rather than buying them on the market. Foundation buying is **0 BNB**, with no treasury purchase announced or seen on-chain. New long-term locks are **0 BNB**: staked BNB still counts as circulating, so staking removes nothing from the float.

## Foundation and overhang

Two large balances are tracked on BNB Chain. The first is the Auto-Burn reserve, which held about **5.25M BNB** at the end of the window after paying for the July burn. It only ever sends coins to the burn address, so when it spends, supply falls rather than rises; after the October burn it should hold about 3.6M BNB. The second is the old bridge contract, which holds about **25.97M BNB** for users who have not yet moved balances over from BNB's retired original chain. About **8,949 BNB** left it this window as users claimed their coins.

Both balances are already inside the circulating count, and the published supply did not move when the bridge paid out, so neither adds sell pressure today. Exchange custody wallets and unlabelled large holders are left out on purpose — those coins belong to depositors, not to an identified group. We read both balances on-chain at every rebuild: if either one falls between refreshes in a way that sends coins anywhere other than the burn address, that outflow enters Sell #3 at the next refresh.

## How BNB compares to other exchange-chain tokens

Most large proof-of-stake coins pay validators with new coins and then try to offset that with a fee burn. Ethereum is the clearest case: on our own ledger it creates about 261K ETH in 90 days and burns only about 3.3K, so its supply grows about 0.21% a quarter. BNB works the other way round. It prints nothing for validators, so every burn is a real cut to supply, and its supply falls by more than 1% a quarter.

Among coins tied to an exchange, the common model is a buyback: the company spends part of its profit buying coins on the market and burning them, and the size depends on what it decides to spend. BNB's Auto-Burn is different because the amount comes from a public calculation based on blocks and price, not from a profit report, and it is paid from a reserve that already holds the coins. That makes the burn more predictable, but it also means it is not tied to how much the exchange earns.

Against hard-capped coins like Bitcoin, which still add new coins at a slowing pace until the cap, BNB is already past its peak supply of 200M and moving down toward a floor of 100M. At the current pace of about 1.6M BNB a quarter, the remaining 33M BNB to the floor is roughly five years of burns, though a higher BNB price makes each burn smaller.

## What to watch in the next 90 days

The 37th quarterly Auto-Burn, expected around **Oct 15 2026**, is the event that moves this reading; we book about **1.65M BNB** for it, and the final amount is set by the quarter's blocks and median price. The free-gas promotion for some stablecoin transfers ended on **Sep 30 2026**, which could change how much gas is paid and so the size of the real-time burn. The next network upgrade, Jenner, is listed in draft form with no date and no burn or reward change in it. Finally, the Auto-Burn reserve and the old bridge contract are read at every rebuild for any outflow that does not go to the burn address.

## Summary

BNB is deflationary: the MrNasdog Pressure Framework reads **−1.22%** over the last 90 days and projects **−1.24%** for the next 90, in line with our supply monitor. BNB Chain creates no new BNB, has no vesting left and no locked supply to release, so the only flows are the quarterly Auto-Burn — **1,615,828 BNB** in July, about **1.65M BNB** expected in October — and a small gas-fee burn of about **7,340 BNB** a quarter. The main risk to the reading is price: the Auto-Burn calculation burns fewer coins when BNB is more expensive. The burns stop when total supply reaches the **100M BNB** floor.

*MrNasdog Pressure Framework analysis of BNB, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 30 2026.*
