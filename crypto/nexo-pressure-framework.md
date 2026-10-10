---
title:         "NEXO Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "NEXO supply is steady: 0.00% net over 90 days and the same next. A fixed 1B NEXO, no mint, no burn, vesting done in 2022; Nexo itself holds about 768M."
canonical_url: "https://mrnasdog.com/research/nexo/inflation"
tags:          ["crypto", "nexo", "cefi", "exchange-token"]
published:     true
---
> Originally published at **[mrnasdog.com/research/nexo/inflation](https://mrnasdog.com/research/nexo/inflation)** by MrNasdog.

<!-- main-page -->
Looking for the buy-or-sell answer? It is on the NEXO coin page, with demand and price drivers: [mrnasdog.com/research/nexo](https://mrnasdog.com/research/nexo)

# NEXO Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

NEXO supply was flat over the last 90 days and should stay flat over the next 90: the framework books **0 NEXO** of sell pressure against **0 NEXO** of buy pressure, a net change of **0.00%**, while the monitor reads **−0.06%**. The Nexo token contract minted all **1B NEXO** in April 2018 and has no function that can mint or burn, so the cap is real. What moves the market is not new NEXO but the roughly **768M NEXO** that Nexo the company keeps in its own wallets, which barely moved this window.

## The verdict, in one paragraph

Over the 90 days to Oct 7 2026 the NEXO ledger nets to **0.00%** of circulating supply, and the forward 90 days to early January 2027 also net to **0.00%**. The inflation monitor reads **−0.06%** for the same stretch, a gap of **0.06 percentage points** — well inside the 0.5-point tolerance, so no warning chip is shown. Total supply read exactly 1,000,000,000 NEXO at both ends of the window, and the small wobble on the monitor side is price-and-value rounding on a supply that cannot change. NEXO is a fixed-supply company token: no issuance, no burn, and a large company-held float.

## Sell pressure: where new NEXO comes from

Protocol inflation is **0 NEXO**. NEXO is an ERC-20 token on Ethereum, not its own chain, so there are no validators or miners to pay in new NEXO. The whole 1B NEXO supply was written into the contract on the day it launched, the verified Nexo token code sets total supply only once, at creation, and the contract carries no mint function, no burn function and no upgrade path. We read the supply value from contract storage at both ends of the window and it did not move.

Vesting unlocks are **0 NEXO**. The NEXO vesting schedule was built into the token contract itself: 525M for sale investors with no lock, 250M for a credit-line reserve released monthly after a five-month cliff, 112.5M for the team in 16 quarterly steps, 60M for the community and 52.5M for advisers. The team stream, the longest of them, finished in early 2022. No unlock is left on any calendar, and no unlock tracker lists a NEXO schedule.

Foundation and unscheduled unlocks are **0 NEXO**. Nexo holds a large pile of NEXO, set out in the overhang section below, but across the window only **2,000 NEXO** left the corporate treasury and every other company wallet sat still. Because all 1B NEXO already count as circulating, a Nexo wallet paying out or selling NEXO moves coins within the counted float; it does not add new supply.

Long-term locked or bankruptcy supply is **0 NEXO**. Nexo is an operating lending, exchange and card business, there is no estate or trustee distribution, and no lock contract holds NEXO with a dated release.

## Buy pressure: where new NEXO goes

Programmatic buyback is **0 NEXO**. Nexo ran three NEXO repurchase rounds — $12M announced in December 2020, $100M in November 2021 and $50M in August 2022 — and parked the bought NEXO in its Investor Protection Reserve wallet rather than burning it. That wallet holds **114.80M NEXO** today and has not changed in more than a year, and no new buyback round has been announced in 2025 or 2026.

Protocol fee burn is **0 NEXO**. The NEXO contract has no burn function, the Ethereum dead address held the same 10.71 NEXO at both ends of the window, and total supply never fell. Fees on the Nexo app are company revenue, not a burn.

Foundation buy is **0 NEXO**: no company wallet took in NEXO from the market this window. New long-term lock is also **0 NEXO**. The Nexo loyalty tiers reward users who keep NEXO in their account with better savings and borrowing rates, but those NEXO can be withdrawn at any time and sit in no lock contract, so they stay in the float.

## Foundation and overhang

Nexo the company controls about **768.03M NEXO**, or 76.8% of supply, across four places. The biggest is **353.85M NEXO** still parked in four release slots inside the token contract — coins that finished vesting years ago but were never taken out, and that only the contract owner can withdraw. Next come the corporate treasury at **213.23M NEXO**, the Investor Protection Reserve at **114.80M NEXO** and the contract owner wallet at **86.15M NEXO**. A further wallet with no public name holds exactly **100M NEXO** and has not moved in a year; we watch it but do not count it as Nexo until it is identified.

Two busy Nexo wallets that pay users and move coins to and from exchanges are left out of this list, because they behave like customer custody rather than a reserve. We read every listed balance from the chain at each rebuild. If any of these overhang balances falls between refreshes, the outflow is written into the Foundation and unscheduled unlocks row at the next refresh — counted as new sell pressure only if the coins were ever outside the counted float.

## How NEXO compares to other exchange and platform tokens

NEXO belongs to the family of tokens issued by a centralised crypto business rather than by a blockchain. In that family the usual supply levers are a company buyback, a burn and the release of a company-held reserve. Exchange tokens that burn coins on a schedule shrink their supply every quarter; NEXO did the opposite with its buybacks, holding the coins instead of destroying them, so its supply has stayed at exactly 1B since 2018.

Against a proof-of-stake or proof-of-work chain coin, NEXO has no issuance at all, which is why its 90-day net change is zero while most Layer 1 coins grow by a fraction of a percent each quarter. The trade-off is concentration: on a chain coin, new supply is spread across thousands of validators, whereas on NEXO the supply that could reach the market sits mostly with one company. That makes NEXO's supply story a question of company behaviour, not protocol math.

Compared with tokens that still have years of team and investor unlocks ahead, NEXO is past that phase entirely. Its vesting ended in 2022, and the remaining risk is a discretionary move by Nexo, which the ledger only books when it actually happens on-chain.

## What to watch in the next 90 days

First, the four release slots inside the NEXO contract: a withdrawal from the **353.85M NEXO** they hold would be the clearest sign Nexo is putting reserve coins to work.

Second, the corporate treasury and owner wallet balances, read at each rebuild; any outflow beyond small operating amounts would show up in the Foundation row.

Third, any new NEXO buyback round from Nexo, and whether bought coins would be held or, for the first time, burned — a burn would be the first real reduction in NEXO supply.

Fourth, the unnamed **100M NEXO** wallet: if it is identified as Nexo-controlled, it joins the overhang list. No dated NEXO supply event is scheduled before Jan 6 2027.

## Summary

NEXO supply is fixed at **1B NEXO**, and the framework reads **0.00%** net change for both the last and the next 90 days, against a monitor reading of **−0.06%**. The NEXO contract cannot mint or burn, vesting ended in 2022, and past Nexo buybacks were held in a reserve wallet rather than burned. The key risk is concentration: Nexo controls about **768M NEXO**, and while those coins barely moved this window, the company can release them whenever it chooses. The ceiling is hard — no more than 1B NEXO can ever exist.

---

*MrNasdog Pressure Framework analysis of NEXO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 8 2026.*
