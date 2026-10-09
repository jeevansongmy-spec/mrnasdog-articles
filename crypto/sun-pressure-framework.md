---
title:         "SUN Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "SUN supply is roughly steady: no SUN can be minted, and a revenue buyback burned 9.03M SUN in 90 days, −0.05% net, with about 8.27M more due around Oct 25 2026."
canonical_url: "https://mrnasdog.com/research/sun/inflation"
tags:                    ["crypto", "sun", "sunswap", "defi"]
published:     true
---

Originally published at [SUN Inflation Analysis · October 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/sun/inflation).

# SUN Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

SUN supply is roughly steady and edging down: no new SUN can ever be created, and the SUN.io revenue buyback burned **9,025,027 SUN** in the last 90 days, a net change of **−0.05%**. The next quarterly burn, due around **Oct 25 2026**, should remove about **8.27M SUN**, or **−0.04%** over the next 90 days. Our inflation monitor reads **−0.05%** as well, so the two readings agree. The supply is fixed at **19.90B SUN**, and the real risk is not new coins but the very large reserve wallets that already count as circulating.

## The verdict, in one paragraph

Over the 90 days to Oct 9 2026, SUN had **0 SUN** of new supply and **9.03M SUN** burned, so the circulating supply of **19.22B SUN** fell by **0.05%**. The inflation monitor, which reads the circulating supply day by day, shows **−0.05%** for the same 90 days. The gap is **0.00 percentage points**, well inside our 0.5-point tolerance, so no data-conflict warning is needed. For the next 90 days we expect one burn of about **8.27M SUN** and no new coins, a net of **−0.04%**. In one line: SUN is a fixed-supply DeFi token with a small, steady buyback-and-burn.

## Sell pressure: where new SUN comes from

Protocol inflation is **0 SUN**, and it can stay at zero for good. All 19,900,730,000 SUN were created in one go when the token was relaunched on TRON in 2021, after a 1-for-1,000 split of the original SUN. We read the token contract itself: it carries only the standard transfer, approval and balance functions, with no mint function, no owner and no way to upgrade the code. Total supply read exactly **19,900,730,000** at both ends of the window, and nothing in the contract can change it.

Vesting unlocks are **0 SUN**. SUN never had a private sale or a team cliff, and there is no locked pile left that the market does not already count. The only coins treated as outside circulating supply are the **678.55M SUN** sitting at the TRON dead address — coins that are gone for good. Everything else, including the old SUN DAO allocation, is already part of the 19.22B SUN circulating supply, so nothing can be "unlocked" into it.

Foundation and unscheduled unlocks are **0 SUN** for the same reason: the big reserve wallets already count as circulating, so a move or a sale from them shifts existing coins rather than adding new ones. Long-term locks and bankruptcy estates are also **0 SUN** — no court case, trustee or estate holds SUN, and no lock is paying coins out on a schedule.

## Buy pressure: where new SUN goes

The programmatic buyback is the only active row, at **9,025,027 SUN** over the last 90 days. SUN.io sends part of its revenue into it: **0.05%** of every SunSwap V2 trade, one sixth of the fees from a busy SunSwap V3 pool since May 2 2026, **100%** of SunPump launchpad revenue, and **50%** of SunX net revenue after costs. That money buys SUN on the market, the SUN waits in a pending-burn wallet, and once a quarter the whole balance goes to the TRON dead address. Round 51 did exactly that on **Jul 25 2026**, and it was the only burn inside the window. The monitor's supply line fell by almost the same amount, about 9.03M SUN, which confirms it.

For the next 90 days we book one burn, round 52, of about **8.27M SUN**. That is what the last 90 days of purchases into the pending-burn wallet are worth at today's price; **6.06M SUN** of it is already sitting in that wallet waiting. The buyback is set in dollars of revenue, so a falling SUN price buys more coins and a rising price buys fewer. The burn is small next to the supply: about one twentieth of one percent per quarter.

There is no separate protocol fee burn (**0 SUN**): the fee share SUN.io sets aside already flows into the buyback, and the token has no burn function of its own. No reserve wallet bought SUN on the open market this window, so the foundation buy is **0 SUN**. The new long-term lock row is also **0 SUN**: holders can lock SUN for 26 weeks up to 4 years to vote and earn more, and the lock vault holds **478.4M SUN**, but locked SUN still counts as circulating, so locking removes nothing from the float.

## Foundation and overhang

SUN's overhang is concentrated. One group of six linked wallets holds about **11.22B SUN** — more than half of all SUN — after one wallet split its balance across five others in April 2025; none of them has moved a coin since May 2025. A second large wallet holds **2.52B SUN** and pays out small amounts every couple of months, only **1.2M SUN** in this window. A third holds **1.19B SUN**, much of it received from the lock vault in November 2025. None of these wallets carries a public label, but their size and history fit the old SUN DAO reserve.

Two smaller pools sit beside them: the lock vault with **478.4M SUN**, whose locks run out one holder at a time, and the pending-burn wallet with **6.06M SUN**. The pending-burn wallet has an owner who could, in principle, pull coins back out before a burn, which is why we only book SUN once it reaches the dead address. All of these coins already count as circulating, so a sale from them adds no new supply, but it would add real selling. We read every one of these balances each rebuild: if one falls between refreshes, the outflow shows up in the foundation-and-unscheduled row at the next refresh.

## How SUN compares to other DeFi exchange tokens

SUN sits in the group of DEX and DeFi tokens that turn platform revenue into buybacks. What sets it apart is the supply side: many exchange tokens still pay new coins to liquidity providers or stakers, so their buyback first has to cancel fresh emissions before supply can fall. SUN has no emission left at all, so every coin bought and burned is a real net cut. That puts SUN closer to a fixed-cap token with a burn than to an emission-funded farm token.

The trade-off is size. A buyback funded by a slice of revenue is only as big as the revenue: here it removes about **0.05%** of supply a quarter, far less than tokens that send most or all of their fees to buybacks, and far less than the reserve wallets could put on the market in a single day. Compared with its sister TRON tokens, which also run quarterly buyback-and-burn rounds, SUN's round is funded by four products — a swap exchange, a launchpad, a futures venue and one V3 pool — rather than mainly by lending revenue.

Against a hard-capped chain like Bitcoin, SUN has the cap without the issuance: there are no block rewards to absorb. Against an uncapped smart-contract chain, SUN has no staking inflation at all. Its supply story is simple — fixed, slowly burned — and its risk lives in custody rather than in code.

## What to watch in the next 90 days

Round 52 of the SUN buyback-and-burn is due around **Oct 25 2026**; we expect about **8.27M SUN**, and the 6.06M SUN already waiting is the floor if nothing is pulled back.

The size of round 52 against round 51's 9.03M SUN will show whether SunPump, SunSwap and SunX revenue is still shrinking or has found a floor.

TRON's 60-day DeFi rewards season that started on **Oct 4 2026** includes SUN deposits on a lending market; it moves no supply, but it can draw SUN out of exchange wallets into deposits until it ends around **Dec 3 2026**.

Any movement from the six-wallet reserve group holding 11.22B SUN would be the single biggest change to the SUN picture, since it has been still for about 17 months.

Round 53 would fall around **Jan 25 2027**, just after this 90-day window closes on Jan 7 2027.

## Summary

SUN supply is roughly steady and slowly shrinking: **0 SUN** of new supply against **9.03M SUN** burned in 90 days, a net **−0.05%**, matched by the monitor, with about **8.27M SUN** more due in the round-52 burn around Oct 25 2026. The SUN token cannot mint, so the 19.90B supply is a true ceiling and every SUN.io buyback is a permanent cut. The key risk is not inflation but concentration: reserve wallets holding about 14.9B SUN already count as circulating and could be sold at any time.

*MrNasdog Pressure Framework analysis of SUN, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 9 2026.*
