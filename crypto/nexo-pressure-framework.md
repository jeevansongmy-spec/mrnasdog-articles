---
title:         "NEXO Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "NEXO supply is flat: 0.00% net over 90 days and the same next. 1B NEXO fixed in code, no burn, vesting over since 2022 — and Nexo holds 768M of the coins."
canonical_url: "https://mrnasdog.com/research/nexo/inflation"
tags:          ["crypto", "nexo", "cefi", "exchange-token"]
published:     true
---

> Originally published at **[mrnasdog.com/research/nexo/inflation](https://mrnasdog.com/research/nexo/inflation)** by MrNasdog.

# NEXO Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

NEXO supply is flat. Over the 90 days to **Sep 29 2026** the Nexo token added **0 NEXO** and removed **0 NEXO**, so the net change is **0.00%**, and the next 90 days read the same. All **1B NEXO** were created in 2018, the token code has no way to make more or burn any, and the built-in release schedule ended in 2022. The one thing that matters is who holds the coins: Nexo itself controls about **768.03M NEXO**, or **76.8%** of the supply.

## The verdict, in one paragraph

The MrNasdog Pressure Framework reads NEXO at **0.00%** net supply change over the last 90 days and **0.00%** for the next 90 days. Our supply monitor reads **+0.05%**, a gap of **0.05 percentage points** — well inside the 0.5-point line, so there is no warning chip. The monitor's small wobble comes from dividing market value by price around a total that is fixed at 1B; the token contract itself read exactly 1,000,000,000 NEXO at both ends of the window. NEXO is a **fixed-supply company token with a large company-held float**: nothing new is printed, nothing is burned, and the only real supply question is what Nexo does with its own coins.

## Sell pressure: where new NEXO comes from

**Protocol inflation is 0 NEXO.** NEXO is an ERC-20 token on Ethereum, not its own blockchain, so there are no validators or miners to pay. The Nexo token contract sets its total supply once, in the step that created it in April 2018, and no function in the code can raise it. We checked this on-chain: the total sits in a normal storage slot, it read 1B at both ends of the window, and the verified NEXO source has no mint and no burn function. So this zero is permanent.

**Vesting unlocks are 0 NEXO.** The NEXO token has its own release schedule written into the code: 525M for the first investors with no wait, 250M of loan reserves released monthly after a five-month cliff, 112.5M for the team over four years, 60M for the community and 52.5M for advisers. The last stream, the team's, ran out in early 2022. There is no vesting cliff, no unlock and nothing left on a calendar for the next 90 days.

**Foundation and unscheduled unlocks are 0 NEXO.** This is the row to watch, even at zero. Nexo holds about 768.03M NEXO across its own wallets, and part of it — about 353.85M NEXO released under the old schedule but never withdrawn — can be taken out by the token's owner at any time. None of it has a schedule, and almost none of it moved: the corporate treasury went down by just 2,000 NEXO in the window. Because every one of these coins is already counted as circulating, moving them would not add to the count. It would, of course, still be real selling if it ever happened.

**Long-term locked or bankruptcy is 0 NEXO.** Nexo is a working company, not in bankruptcy, and no estate, trustee or court order holds NEXO for later release.

## Buy pressure: where new NEXO goes

**Programmatic buyback is 0 NEXO this window.** Nexo has run NEXO buybacks before: a $12M round in December 2020, a $100M round from November 2021 and a $50M round from August 2022. Those repurchased coins went into the Investor Protection Reserve, which now holds **114.80M NEXO**. They were held, not burned. The reserve read the same at both ends of the window and a year earlier, and no new buyback round has been announced, so nothing is booked.

**Protocol fee burn is 0 NEXO.** The NEXO token has no burn function and Nexo runs no burn. The dead address held 10.71 NEXO at both ends of the window, and the total supply did not fall. This zero is also permanent — the code cannot shrink the supply.

**Foundation buy is 0 NEXO.** No Nexo wallet took in NEXO in the window. When customers choose to earn interest in NEXO, Nexo pays them from coins it already holds, which moves coins around inside the float rather than taking any off the market.

**New long-term lock is 0 NEXO.** Holding NEXO in the Nexo app lifts a customer's loyalty tier, but those coins can be withdrawn at any time and stay in the circulating count. We found no lock contract with a fixed term.

## Foundation and overhang

Nexo has no foundation or DAO; the company itself is the holder. We track four groups of company-held NEXO. The four release addresses from the original schedule hold **353.85M NEXO** — 208.33M of loan reserve, 98.44M of team tokens, 33.33M of community tokens and 13.75M of adviser tokens — and they have not moved in at least two years. The wallet labelled as Nexo's corporate treasury holds **213.23M NEXO**, down 2,000 in the window. The token's owner wallet holds **86.15M NEXO**, unchanged. The Investor Protection Reserve, where past buybacks landed, holds **114.80M NEXO**, unchanged.

Together that is about **768.03M NEXO, 76.8% of all NEXO**. Wallets that hold customer deposits are left out, because those coins belong to depositors. We read every one of these balances on-chain at each rebuild. If any of them falls between rebuilds, the outflow goes into the Foundation and unscheduled unlocks row at the next refresh.

## How NEXO compares to other exchange and platform tokens

NEXO belongs to the family of tokens issued by a crypto company for its own platform, alongside BNB, OKB, LEO and CRO. The big difference between them is whether the company takes coins out of the market. BNB runs a quarterly auto-burn that destroys coins on a set schedule, and LEO's issuer buys back and burns tokens from its revenue. On those tokens the buy side is a real, repeating flow. NEXO has neither: Nexo's past buybacks were held in a reserve, not burned, and there has been no round since 2022.

The other difference is the size of the company-held float. On most of these tokens the issuer holds a share of supply, but on NEXO it is about three quarters, and a large part of it is counted as circulating even though it has not moved in years. That makes the NEXO supply number very stable — nothing in the code can change it — but it also means the real float trading on exchanges is much smaller than the 1B headline, and the NEXO supply story depends on one company's decisions rather than on a burn or an emission curve.

## What to watch in the next 90 days

There is no dated NEXO supply event between **Sep 29 2026** and **Dec 28 2026**. First, watch the four release addresses and the owner wallet: a withdrawal from the 353.85M there would be the first movement in years and the clearest sign Nexo plans to use them. Second, watch the corporate treasury and the Investor Protection Reserve for outflows to exchanges. Third, watch for a new buyback announcement, which would be the first since 2022; whether the coins are burned or held decides whether it changes the count. Fourth, the possible Coinbase listing of NEXO, on that exchange's roadmap since May 2026, is a demand event that does not change supply.

## Summary

NEXO is a fixed-supply Nexo token: the MrNasdog Pressure Framework reads **0.00%** net supply change over the last 90 days and **0.00%** for the next 90, with the monitor at **+0.05%**. The code holds the supply at 1B NEXO forever — no minting, no burning — and the vesting schedule ended in 2022. The key risk is concentration: Nexo controls about 768.03M NEXO, 76.8% of the supply, and could sell it at any time without breaking any rule. The ceiling is hard and the buy side is idle, so what Nexo does with its own wallets is the whole NEXO supply story.

---

*MrNasdog Pressure Framework analysis of NEXO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*
