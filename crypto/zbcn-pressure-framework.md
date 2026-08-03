---
title:         "ZBCN Inflation Analysis · August 2026 · Supply growing slowly, projected to keep growing"
description:   "Zebec's mint key is destroyed and vesting ended in March 2026, yet a project reserve wallet paid out ~703M ZBCN in 90 days. Framework +0.72%, monitor flat."
canonical_url: "https://mrnasdog.com/research/zbcn/inflation"
tags:          ["crypto", "zbcn", "zebec", "payments"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/zbcn/inflation](https://mrnasdog.com/research/zbcn/inflation)*

# ZBCN Inflation Analysis · August 2026 · Supply growing slowly, projected to keep growing

Zebec Network cannot mint a single new ZBCN — the mint key is destroyed on-chain and the full **100,000,000,000 ZBCN** supply sits flat at its hard cap — yet ZBCN is still mildly inflationary, because a project reserve wallet keeps paying already-minted coins out to the market. About **703.1M ZBCN** reached the market over the trailing 90 days from that distribution wallet, against a buy side of **0**. That puts the framework at **+0.72%** net for the trailing window and **+0.58%** forward. Our supply monitor reads roughly **flat**, a gap that traces to the reserve wallet already being counted as circulating supply.

## The verdict, in one paragraph

For the 90-day window opening **Aug 3 2026**, the MrNasdog Pressure Framework reads **ZBCN at +0.58% net** forward, close to the **+0.72%** it measured over the trailing 90 days — the reserve drawdown is a steady stream and the wallet still holds enough to keep paying. Our supply monitor reads roughly **-0.01%** for the trailing window, a gap of about **0.73 percentage points** that ships a monitor-gap chip on the ZBCN overview. The deep walk reconciled it: read straight off the chain, the project distribution wallet **71LxiE4P…** paid out **703.1M ZBCN** in 11 dated transfers between May 13 and July 26 2026, and the two hubs downstream received exactly that amount. The monitor stays flat because the upstream supply method counts an unlocked project wallet as already circulating, so paying out of it cannot move the reading. The framework counts supply reaching third-party hands. ZBCN is best characterised as **a hard-capped, zero-mint token that dilutes slowly by drawing down a pre-minted reserve rather than issuing new coin**.

## Sell pressure: where new ZBCN comes from

Sell #1 — protocol inflation — is **zero**, and it is zero permanently. Zebec Network destroyed the ZBCN mint key: on-chain, mint authority is null and freeze authority is null, so no new ZBCN can ever be created. The whole **100,000,000,000 ZBCN** was issued years ago and the on-chain supply reads flat below the cap, with only about **1.22M** ever retired. There is no emission, no staking-reward issuance, and no governance switch that can turn one on.

Sell #2 — vesting unlocks — is **zero** because the vesting is finished. Zebec's final scheduled unlock landed on **Mar 17 2026**, before this window opened, and every unlock tracker now reads fully unlocked with nothing due between May and August 2026. Just as important, no vesting contract paid the distribution wallet inside the window — its inflow was zero all 90 days — so both the scheduled figure and the realised figure agree at zero.

Sell #3 — foundation and unscheduled unlocks — is the only live row, at about **703.1M ZBCN**. This is a discretionary drawdown of already-minted reserve: the project distribution wallet **71LxiE4P…** paid out **703.1M ZBCN** across 11 dated transfers from **May 13 2026** to **Jul 26 2026**, read directly from the chain. The two hubs downstream received exactly **371.5M** and **331.6M** — **703.1M** in total, an exact match at the second hop. Because these are coins that already existed rather than freshly minted ones, the framework books the realised outflow as a reserve drawdown, not as new issuance. The wallet still holds about **571.4M ZBCN**, and because its refill source has been idle since March 2026, that remaining balance caps the forward projection at roughly **571.4M**. Sell #4 — long-term locked or bankruptcy — is **zero**: no bankruptcy estate or court-ordered distribution holds ZBCN.

## Buy pressure: where new ZBCN goes

Buy #1 — programmatic buyback — is **zero** on the framework, and this is the row that most understates Zebec's real economics. Zebec does run a genuine buyback: revenue from payroll, Zebec Card and partner contracts is used to buy ZBCN on the market, and roughly **504.7M** has been repurchased cumulatively as of July 2026. But two things keep it at zero here. First, a 2024 governance vote — ZIP-4 — **paused the token burn** while keeping the buyback, so the bought-back coins **accumulate** in a treasury wallet rather than being destroyed; the on-chain supply still sits at the cap less about 1.22M, confirming nothing has been burned. Second, no on-chain buyback address and no dated in-window quantum are published, so there is no single verifiable amount to book this window. Because the mechanism holds rather than removes supply, and no measurable flow can be triangulated, Buy #1 books zero and is monitored.

Buy #2 — protocol fee burn — is **zero** because the burn was paused by that same ZIP-4 vote, and network fees on Zebec are paid in the host chain's coin rather than routed through an on-chain ZBCN burn. Buy #3 — foundation buy — is **zero** as a separate line: the distribution wallet only sent coins out this window and took none in. Buy #4 — new long-term lock — is **zero** as well; the staking vault holds about **4.6B ZBCN**, but it is withdrawable rather than a new dated lock, and no fresh lockup contract was announced in the window.

## Foundation and overhang

The team-controlled overhang on ZBCN is large and easy to size because the supply is fixed at a hard cap. The most active piece is the project distribution wallet **71LxiE4P…**, which still holds about **571.4M ZBCN** — the balance feeding Sell #3, currently draining into the market. Alongside it, a separate project pool holds about **6.0B ZBCN** with no published release schedule, the single largest unscheduled overhang; a staking vault holds about **4.6B ZBCN** that is withdrawable rather than locked; and the buyback treasury accumulates repurchased ZBCN at an undisclosed on-chain address. These balances are read every rebuild. If any of them moves out to third-party wallets between refreshes, the outflow enters Sell #3 at the next refresh.

## How ZBCN compares to other capped payment tokens

ZBCN belongs to the hard-capped, mint-renounced class — tokens where the supply ceiling is not a policy choice but a destroyed mint key. On that measure it is cleaner than an uncapped Layer 1 whose validators earn genuinely new coins forever: Zebec will never create a hundred-billion-and-first ZBCN, and its dilution has a hard ceiling. What it shares with the wider payments-token class is the quiet catch that a capped supply is not the same as a fixed float. A pre-minted reserve leaving a project wallet to reach the market weighs on price exactly as a freshly minted coin would, even though the accounting calls it a reserve transfer rather than issuance.

The sharper comparison is to an exchange token that buys and burns every quarter. Zebec has the same raw ingredient — real product revenue from payroll, cards and partner contracts — and it spends that revenue buying ZBCN back. The difference is what happens next: an exchange token destroys the coins it buys, permanently shrinking supply, while Zebec's 2024 vote paused its burn, so the bought-back ZBCN piles up in a treasury instead of leaving supply. That single governance choice is the whole reason the buy side reads zero here: the buying is real, but a held coin is not a removed coin, and a treasury that accumulates is itself an overhang.

Against its own class on timing, ZBCN is past the hard part. Its vesting is finished, its mint is dead, and the only live supply force is a discretionary reserve drawdown that is knowable transfer-by-transfer on-chain. The honest reading is that ZBCN's inflation profile is small, fully visible and slowly positive — the entire question is whether Zebec resumes burning its buybacks, which would flip the buy side from zero to a genuine structural force pulling ZBCN out of supply.

## What to watch in the next 90 days

Watch the distribution wallet **71LxiE4P…** and its remaining **571.4M ZBCN**: as long as it keeps paying out at the current pace it will empty inside the forward window, and the moment it is refilled from the **6.0B** project pool the forward reading jumps. Watch for any move to resume the paused token burn — a governance vote that un-pauses ZIP-4 would turn the real, ongoing buyback into a genuine deflationary force and move Buy #1 off zero. Watch the buyback treasury for a published on-chain address or a dated repurchase amount, which is the missing piece that would let the framework credit the buy side. And watch the staking vault of about **4.6B ZBCN** — being withdrawable, a large unstake could add float even though it is not new supply.

## Summary

Zebec Network is a hard-capped, zero-mint payments token whose float still grows slowly because a pre-minted reserve keeps leaving the project distribution wallet. About **703.1M ZBCN** reached the market over the trailing 90 days and about **571.4M** is projected forward, against a buy side of **zero**, leaving the framework at **+0.72%** net trailing and **+0.58%** forward. Our supply monitor reads roughly **flat**, a gap that reconciles cleanly: the reserve wallet is already counted as circulating, so paying out of it does not move the monitor, while the framework counts the coins reaching third-party hands. The key variable is the buy side — Zebec earns real revenue and already buys ZBCN back, but its burn is paused, so those coins accumulate instead of shrinking supply; un-pausing the burn is the one change that would turn ZBCN deflationary.

---

*MrNasdog Pressure Framework analysis of Zebec Network (ZBCN), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated August 3, 2026.*
