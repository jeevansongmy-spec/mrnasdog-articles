---
title:         "JUP Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "Supply growing: JUP can't be minted, but 53.69M JUP of reserve payouts beat a 31.46M Litterbox buyback — +0.72% net over 90 days and +0.64% projected next."
canonical_url: "https://mrnasdog.com/research/jup/inflation"
tags:          ["crypto", "jup", "jupiter", "defi"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/jup/inflation](https://mrnasdog.com/research/jup/inflation)*

# JUP Inflation Analysis · September 2026 · Supply growing · projected to keep growing

JUP, the token of Jupiter on Solana, cannot be minted — the JUP mint authority is empty and a test mint failed against the token program — yet the JUP float still grows. Jupiter's reserves paid **53.69M JUP** to holders over the last 90 days, mostly through the quarterly Active Staking Rewards round, and JUP vesting escrows released **1.51M JUP** more. Against that, the Litterbox Trust bought **31.46M JUP** on the open market and sold none. The MrNasdog Pressure Framework reads JUP at **+0.72% net** over the last 90 days and **+0.64%** over the next 90, against a supply-monitor reading of **−0.41%** — a gap of **1.12 percentage points** that ships with a data-conflict flag.

## The verdict, in one paragraph

For the 90-day window ending **Sep 13 2026**, the Pressure Framework reads **JUP at +0.72% net**: **55.20M JUP** reached holders from Jupiter's reserves and vesting escrows, while the Litterbox buyback took **31.46M JUP** back off the market, on a circulating supply of **3.32B JUP**. The independent supply monitor reads the realised 90-day change at **−0.41%**. The gap is **1.12 percentage points**, more than twice the framework's half-point tolerance, so a five-class deep walk was run. It found the cause rather than an error: the monitor's circulating series held flat near **3.32B** for the whole window, so it cannot see JUP moving from Jupiter's community reserve into holders' hands. The primary reading stands and JUP ships with the **monitor-gap flag**. The forward column reads **+0.64%** because one more staking-rewards round lands inside the next 90 days. The label for JUP is **fixed supply, rising float**: a token that can never be minted, whose float still grows because a buyback smaller than the reserve payouts is the only thing leaning against them.

## Sell pressure: where new JUP comes from

Sell #1, protocol inflation, is **zero**, and it is zero by code rather than by promise. The JUP mint on Solana has no mint authority and no freeze authority, and a simulated mint of a single JUP was rejected by the token program with its own fixed-supply error. The JUP total supply of **6.86B** can stay where it is or fall, never rise.

Sell #2, vesting unlocks, is **1.51M JUP**. Jupiter team vesting was paused by the February 2026 net-zero emissions vote, and the quarterly team tranche that used to move from the team cold wallet has not run since **Jan 31 2026**. What still vests is a set of contributor schedules held in on-chain lock contracts: holders claimed **1,170,574 JUP** from a monthly contributor tranche and **340,049 JUP** from roughly 6,600 small schedules that end on **Dec 23 2026**. JUP that vested but was not claimed stays inside the escrow and is not counted, because it has not reached anyone who can sell it.

Sell #3, foundation and unscheduled unlocks, is the largest JUP row at **53.69M JUP**. Active Staking Rewards pay JUP stakers **50M JUP** a quarter from the community reserve, funded from airdrop tokens that went unclaimed. On **Jul 7 2026** the Jupiter community hot wallet funded the April-to-June claim contract with **47,904,313 JUP**; stakers claimed **47,412,091 JUP** before Jupiter pulled the remainder back on **Aug 25 2026**. Late claims on the January-to-March round added **4,305,256 JUP**, and rewards paid outside the contract, a small support payout and monthly contributor pay added **1,974,843 JUP**. Every move between Jupiter's own wallets was traced and netted out. The largest of those was **90M JUP** that the team distribution vault moved into nine new staking vaults between Jun 15 and Aug 5; those vaults are run by the same signer as the vault that funded them, so the JUP never left Jupiter's control and is not booked. Sell #4, long-term locked or bankruptcy supply, is **zero**: JUP has no estate and no trustee schedule.

## Buy pressure: where new JUP goes

Buy #1, the programmatic buyback, is **31.46M JUP**. Half of Jupiter's protocol revenue buys JUP on the open market and sends it to the Litterbox Trust wallet. Every one of the **14,881** Litterbox purchases in the window was summed and checked against the wallet balance at both ends: it rose from **137.28M** to **168.73M JUP**, the two agree exactly, and there was not a single outgoing transfer. The JUP buyback also accelerated inside the window, from **6.53M JUP** in the second half of June to **11.85M JUP** in August, as Jupiter revenue rose. The forward column holds the trailing 90-day amount, because no rule changed.

Buy #2, the protocol fee burn, is **zero**: JUP supply was flat across the build and the burn addresses received nothing. The last JUP burn was the Litterbox balance, destroyed by DAO vote in November 2025. Buy #3, foundation buying, is **zero** — no Jupiter wallet other than the Litterbox Trust took JUP from the market. Buy #4, new long-term locks, is **zero**. Staked JUP can be withdrawn after a **7-day** wait and stays inside circulating supply, and the Litterbox purchases are already counted once in Buy #1, so nothing is booked twice.

## Foundation and overhang

Jupiter controls a large JUP overhang, and all of it is on-chain and read on every rebuild. The community cold wallet holds **1.70B JUP** and the team cold wallet **1.68B JUP**; neither moved in the window. The community hot wallet that funds the staking rewards holds **223.40M JUP**, the team distribution vault **191.57M JUP**, and the team hot wallet **126.38M JUP**. About **124M JUP** sits staked in vaults Jupiter itself runs. The Litterbox Trust, now **168.73M JUP**, is the buyback destination: its three-year hold is a stated policy rather than a lock written into code. None of these reserves has a published release date. If any of those balances falls between refreshes and the JUP does not land in another Jupiter wallet, the outflow enters Sell #3 at the next refresh.

## How JUP compares to other DeFi exchange tokens

JUP sits in an unusual spot among exchange and DeFi tokens. Most proof-of-stake chain tokens grow their supply by minting new coins for validators; JUP cannot mint at all, so its supply ceiling is fixed at **6.86B**. The float grows anyway because roughly half of that fixed supply was created up front and parked in Jupiter reserves, and the reserves pay out over time. For JUP the question is never how fast the chain inflates; it is how fast the reserves drain and whether the buyback keeps up.

Against DeFi tokens that burn what they buy back, the JUP buyback is a hold, not a burn. Burning removes coins for good, while the Litterbox Trust keeps them in a wallet that governance has already emptied once, by burning it. Against perps-exchange tokens that send nearly all fees into buybacks with no large reserve left to hand out, JUP carries the opposite shape: a buyback funded by half of revenue running into a reserve payout that is larger. That is why JUP shows a steady market bid and a rising float at the same time — the bid is real, and on this window the payouts were about **1.75 times** as large.

## What to watch in the next 90 days

First, the July-to-September Active Staking Rewards round, expected to open for claims around **Oct 8 2026** at **50M JUP**; it is the single event that decides the forward JUP reading. Second, a **489,893 JUP** contributor vesting tranche due on **Sep 15 2026**. Third, the Litterbox buyback rate, which ran at **11.85M JUP** in August — a stronger revenue quarter would push Buy #1 past its booked **31.46M**. Fourth, the Jupiter governance forum, where open proposals would raise the buyback share of revenue to 70% and burn the purchases; none has gone to a vote. Fifth, the Jupiter reserves themselves: a move of the paused team allocation or the community cold wallet would open a new sell row.

## Summary

The MrNasdog Pressure Framework reads Jupiter's JUP at **+0.72% net** over the trailing 90 days and **+0.64%** over the next 90. The structural mechanism is a fixed-supply token with no mint whose float grows as Jupiter reserves pay out quarterly staking rewards, partly offset by a revenue-funded buyback that holds, rather than burns, the **31.46M JUP** it bought. The key risk is the size of the reserves behind those payouts — more than **3.9B JUP** in Jupiter wallets with no published release dates. The ceiling is hard: the JUP mint cannot create a single coin, so total supply cannot exceed **6.86B JUP**.

*MrNasdog Pressure Framework analysis of JUP, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 13 2026.*
