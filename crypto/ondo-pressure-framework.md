---
title:         "ONDO Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "ONDO supply is roughly steady: 0.00% net in 90 days, no mint, no unlock, and a 300M Foundation payout from coins already unlocked. Next cliff Jan 18 2027."
canonical_url: "https://mrnasdog.com/research/ondo/inflation"
tags:          ["crypto", "ondo", "rwa", "tokenunlocks"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/ondo/inflation](https://mrnasdog.com/research/ondo/inflation)*

# ONDO Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

ONDO supply is flat. Over the 90 days to **Sep 29 2026**, no new ONDO was created, no yearly unlock fell due and nothing was bought back or burned, so the MrNasdog Pressure Framework reads **0 ONDO** of sell pressure, **0 ONDO** of buy pressure and a net change of **0.00%** — the same for the next 90 days. The Ondo Foundation did pay out **300M ONDO**, but from coins that were already unlocked, and the next locked tranche does not open until **Jan 18 2027**.

## The verdict, in one paragraph

The framework reads ONDO at **0.00%** net over the last 90 days and **0.00%** for the next 90 days, on a circulating base of **4.87B ONDO** out of a fixed **10B** total. Our supply monitor, which tracks the market's circulating count day by day, reads **+0.01%** over the same window. The gap is **0.01 percentage points**, well inside our 0.5-point tolerance, so no warning flag is shown. In one line: **a quiet float between two yearly cliffs** — nothing new reaches the market until the Jan 18 2027 unlock.

## Sell pressure: where new ONDO comes from

**Protocol inflation is 0.** All 10B ONDO were created in one go in April 2022, and the on-chain total supply read exactly **10,000,000,000 ONDO** at both ends of the window. The ONDO contract does contain a mint function, but it only works for an address holding a special role, and a test call from an ordinary address is refused. No coins were minted this window and ONDO has no staking rewards, so there is no issuance to count. Because that mint function exists, we do not call the supply permanently fixed.

**Vesting unlocks are 0.** Locked ONDO opens once a year on **Jan 18**, a schedule that runs to **Jan 18 2029**. The last cliff was Jan 18 2026, when the circulating count jumped by about **1.71B ONDO** in a single day. The next cliff is **Jan 18 2027**: unlock trackers put it at about **1.94B ONDO**, while the last jump in the circulating count points to about 1.71B. Either way, it falls outside both 90-day windows, so it adds nothing here.

**Foundation and unscheduled unlocks are 0.** This is the row that looks busy but is not. The Ondo Foundation's main wallet sent out **150M ONDO on Aug 21 2026** and another **150M ONDO on Sep 23 2026**, and a payout wallet passed the coins on in lots of 9M to 26M. But at the start of the window the Foundation wallet held **348.5M ONDO more** than the entire locked supply, and the Foundation itself discloses only **4.42B ONDO** of that wallet as locked. So every payout came from coins the market already counts as circulating — a move inside the float, not new supply.

**Long-term locked or bankruptcy is 0.** ONDO has no bankruptcy estate and no court-run distribution. The founder, Nathan Allman, died in May 2026, and his estate — which includes an ONDO holding of undisclosed size — is part of a dispute over control of the company. No sale schedule for those coins has been published, so the row stays at zero and is watched.

## Buy pressure: where new ONDO goes

**Programmatic buyback is 0.** Ondo Finance earns fees on its tokenized Treasury funds and tokenized stocks, but none of that money buys ONDO today. A fee switch that could send revenue to ONDO holders or to buybacks has been discussed in the press for the second half of 2026, but no proposal exists on the Ondo DAO vote page, which has been paused since its last vote in early 2024.

**Protocol fee burn is 0.** The ONDO contract has no burn function. We checked both places a burn could show: total supply stayed at 10B, and the burn address held the same **7.59 ONDO** at both ends of the window. Posts in July 2026 about a vote to burn 100M ONDO did not match anything on-chain or on the vote page, so nothing is booked.

**Foundation buy is 0** — the Foundation pays ONDO out and received none from the market this window. **New long-term lock is 0** — ONDO has no staking or lock programme; it is a voting token only.

## Foundation and overhang

The Ondo Foundation's main wallet holds **5.18B ONDO**, more than half of all supply. The Foundation discloses **4.42B ONDO** of it as locked, which leaves about **757M ONDO** unlocked and ready to spend. Its payout wallet holds **125M ONDO** more. The pace of payouts has been steady: **125M** on Apr 22 2026, then **150M** each on May 11, Jun 22, Aug 21 and Sep 23 2026. At that pace, two or three more payouts in the next 90 days would still come out of the unlocked share, so they stay at zero in our ledger.

The market's circulating count treats **5.13B ONDO** as not yet circulating — about **708M ONDO** more than the Foundation says it holds locked. That extra locked amount sits outside the Foundation wallet, most likely with early investors and the team under the yearly schedule. A separate Foundation-linked wallet holding **100.2M ONDO** did not move this window. We read these wallets on-chain at every rebuild. If the Foundation wallet's balance falls below its disclosed locked amount, or any of these wallets sends coins that were counted as locked, that outflow enters the Foundation row at the next refresh.

## How ONDO compares to other RWA and DeFi governance tokens

ONDO sits in a group of governance tokens with a fixed supply and a large locked share that opens on a schedule. For these tokens, supply risk does not come from issuance — there is none — but from the calendar. ONDO's calendar is unusually lumpy: instead of monthly vesting, it releases one very large tranche each Jan 18, so the whole year's dilution lands in a single day. That makes ONDO look flat for eleven months and then jump, and it is why the 90-day reading today is zero while the one-year view carries about 1.71B to 1.94B ONDO.

The other difference is on the buy side. Some DeFi governance tokens, such as Aave and Sky, now use protocol revenue to buy their own token back, which gives them a steady buyer that offsets unlocks. ONDO has no such link: Ondo Finance's products earn fees, but the ONDO token captures none of them. Until a fee switch or buyback is voted in, ONDO has no structural buyer, and every future unlock has to be absorbed by market demand alone.

## What to watch in the next 90 days

**Foundation payouts:** the recent pace is about 150M ONDO every one to two months; watch whether the Foundation wallet drops toward its disclosed locked amount of 4.42B ONDO.

**A fee switch or buyback vote:** any real proposal on the Ondo DAO vote page would be the first buy-side mechanism ONDO has ever had.

**The founder's estate:** any court ruling or sale plan that moves the estate's ONDO would need to be checked against the locked count.

**The Jan 18 2027 cliff:** just after this window, about 1.71B to 1.94B ONDO unlocks — the largest single supply event of the coming year.

## Summary

ONDO is a fixed-supply governance token of Ondo Finance whose circulating count is flat: **0.00%** net over the last 90 days and **0.00%** projected for the next 90, with the supply monitor at **+0.01%**. The Ondo Foundation keeps paying out coins — **300M ONDO** this window — but only from its unlocked share, so the float does not grow. The main risk is the yearly unlock: about 1.71B to 1.94B ONDO opens on **Jan 18 2027**, with no buyback or burn on the other side. The ceiling is 10B ONDO in total, fully in circulation after the last cliff on Jan 18 2029 — a limit set by policy, since a role-gated mint function still exists in the contract.

---

*MrNasdog Pressure Framework analysis of ONDO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*
