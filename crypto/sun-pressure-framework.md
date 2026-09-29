---
title:         "SUN Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "SUN supply is roughly steady: no SUN can be minted, and a fee-funded buyback burned 9.03M SUN in 90 days, −0.05% net, with about 5.00M more due next quarter."
canonical_url: "https://mrnasdog.com/research/sun/inflation"
tags:                    ["crypto", "sun", "sunswap", "defi"]
published:     true
---

Originally published at [SUN Inflation Analysis · September 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/sun/inflation).

# SUN Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

**SUN supply is roughly steady, shrinking slightly.** No new SUN can ever be created — all **19.9B SUN** were made once, in 2021 — so the only thing that moves the SUN supply is the buyback-and-burn paid from SUN.io's fees. That burn removed **9.03M SUN** in the last 90 days, a net change of **−0.05%**, and about **5.00M SUN** (**−0.03%**) is expected in the next 90 days. The monitor reads **−0.11%**.

## The verdict, in one paragraph

Over the 90 days to Sep 29 2026, SUN's circulating supply of **19.22B SUN** shrank by **−0.05%**: nothing was added, and one quarterly buyback burn removed **9,025,027 SUN** on Jul 25 2026. For the next 90 days we expect one more burn of about **5.00M SUN**, or **−0.03%**. The monitor, which reads supply from market value and price, shows **−0.11%** for the same window. The gap is **0.07 percentage points**, well inside our 0.5-point tolerance, so no warning is raised. In one line: SUN is a **fixed-supply token with a small, steady fee-funded burn**.

## Sell pressure: where new SUN comes from

Protocol inflation is **0 SUN**, and it is permanent. The SUN token contract on TRON has only the standard transfer and allowance functions: no mint function, no owner and no upgrade path. The total supply reads exactly **19,900,730,000 SUN**, the number set when SUN was redenominated at 1 new SUN for 1,000 old in May 2021, and no function in the contract can raise it.

Vesting unlocks are **0 SUN**. SUN.io never sold SUN to private investors and kept no team share. The largest allocation, the SUN DAO's **47.16%**, was set to release over four years, but the circulating figure already counts every SUN except the burned ones — so any release from it moves coins that are already in the float.

Foundation and unscheduled unlocks are **0 SUN** for the same reason: the large reserve wallets are inside the circulating count, and none of them released coins to new owners outside it. Long-term locks and bankruptcy releases are **0 SUN**: there is no estate, no trustee and no unwinding lock holding SUN.

## Buy pressure: where new SUN goes

The programmatic buyback is the only live row: **9.03M SUN** burned in the last 90 days. The SUN buyback-and-burn is funded by four streams: 0.05% of every trade on SunSwap V2, one sixth of the fees from the TRX/USDT pool on SunSwap V3 (since May 2 2026), all protocol revenue from the SunPump meme launcher, and half of the net revenue from the SunX futures exchange. The fees buy SUN on the market into a pending-burn wallet, and the coins are sent to TRON's dead address every three months.

Round 51 of the burn, on Jul 25 2026, destroyed **9,025,027 SUN**: about **7.44M** from SunSwap V2 fees and **1.58M** from SunX, with nothing from SunPump this round. Since then the pending-burn wallet has bought another **2.93M SUN**. The buying inside the last 90 days cost about **$85,000**; at today's price of about $0.0171 the same spend buys about **5.00M SUN**, which is our figure for round 52, expected around Oct 25 2026. Since the first burn in December 2021, **678.5M SUN** — about 3.4% of all SUN ever made — has been destroyed.

The protocol fee burn is **0 SUN** as a separate row: the fee share already flows through the buyback, and the SUN contract has no burn function, so burned coins sit in the dead address while the total supply stays at 19.9B. A foundation buy is **0 SUN**: no treasury bought SUN outside the buyback. A new long-term lock is **0 SUN**: about **486.5M SUN** is locked for voting power (veSUN, up to four years), but locked SUN still counts as circulating.

## Foundation and overhang

SUN's supply is very concentrated. Eight large unlabelled wallets hold about **14.92B SUN**, three quarters of all SUN, most likely the SUN DAO reserve. Seven of them did not move a single SUN in the last 90 days; one sent out **1.2M SUN**. The veSUN vote-lock vault holds about **486.5M SUN**, released lock by lock as each one expires. The pending-burn wallet holds **2.93M SUN** waiting for the next burn; its owner can, in principle, withdraw coins before a burn, so we check that it empties into the dead address. We read all of these balances on-chain at every rebuild.

Because every one of these wallets is already counted as circulating, a sale from them would not add new supply to our ledger — but it would add selling to the market, which is why we list them. If any of these balances falls between our checks, the outflow enters Sell #3 at the next refresh.

## How SUN compares to other DEX and DeFi tokens

Most DEX tokens still pay liquidity providers in newly minted coins, so their burns first have to cancel out that new supply before the total can fall. SUN is different: its liquidity rewards come from coins that already exist, and the contract cannot mint. That makes SUN a pure fixed-cap token, like a coin with a finished emission schedule, with a burn on top.

The trade-off is size. SUN's burn is paid from a slice of fees, not from all of them, and SUN.io's fee income is smaller than a year ago. A burn of about **0.05%** of supply per quarter is steady but slow — much smaller, relative to supply, than tokens that send all their protocol revenue to buybacks. SUN also moved from a monthly burn to a quarterly one in 2026, which makes the supply fall in steps rather than in a smooth line.

Compared with governance tokens that still carry team and investor vesting, SUN has no unlock calendar at all. Its risk sits elsewhere: a very large share of the float sits in a few quiet wallets, and a move from them would be felt in the market even though it would not change the supply count.

## What to watch in the next 90 days

Round 52 of the SUN buyback-and-burn, expected around **Oct 25 2026** — we expect about **5.00M SUN**; a smaller burn, or a later date, would flatten the reading to near zero.

The pending-burn wallet, now at **2.93M SUN** — it should keep growing each month until the burn and then empty into the dead address.

The eight large reserve wallets holding about **14.92B SUN** — any outflow from them is the biggest market risk, even though it adds no new supply.

SunX and SunPump revenue — SunPump sent nothing to the last three burns, so the burn now leans on swap fees and the futures exchange.

## Summary

SUN is a fixed-supply TRON DeFi token: **19.9B SUN** were created once, the contract cannot mint more, and the circulating supply of **19.22B SUN** only shrinks, through a quarterly buyback-and-burn paid from SUN.io's fees. That burn removed **9.03M SUN** in the last 90 days (**−0.05%**) and is expected to remove about **5.00M SUN** (**−0.03%**) next, so supply is roughly steady. The key risk is not new supply but concentration: about 14.92B SUN sits in eight quiet wallets already counted as circulating.

---

*MrNasdog Pressure Framework analysis of SUN, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*
