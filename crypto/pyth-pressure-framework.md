---
title:         "PYTH Inflation Analysis · August 2026 · The annual unlock landed, forward flat"
description:   "PYTH's ~2.13B annual unlock landed May 19 2026 inside the trailing window; the framework reads +26.92% net last-90D and -0.06% forward, monitor +36.94%. Next cliff not until May 2027."
canonical_url: "https://mrnasdog.com/research/pyth/inflation"
tags:          ["crypto", "pyth", "pythnetwork", "oracle"]
published:     true
---

> Originally published at **[mrnasdog.com/research/pyth/inflation](https://mrnasdog.com/research/pyth/inflation)** by MrNasdog.

The MrNasdog Pressure Framework reads **PYTH at +26.92%** net supply over the last 90 days, but the entire figure is one event: the annual vesting cliff of about **2.13B PYTH** that landed on **May 19 2026**. PYTH is a fixed **10,000,000,000** token with no mint, so its only dilution is this once-a-year cliff — and the next one is not until **May 2027**. Against it, the DAO's PYTH Reserve bought back only about **5M PYTH**. Our supply monitor reads **+36.94%**, and the gap is entirely a denominator base, not a data conflict. Forward, with no unlock due, the framework reads **-0.06%** — a shade deflationary — with **~7.87B** of the **10B** cap now circulating.

## The verdict, in one paragraph

For the 90-day window from **May 8 2026** to **Aug 6 2026**, the framework reads **PYTH at +26.92% net**: sell pressure of about **2.13B PYTH** against buy pressure of about **5M PYTH** on a tradable base of **7.87B PYTH**. Our supply monitor reads **+36.94%** for the same period — a gap of about **10 percentage points**, well outside the framework's 0.5-point tolerance, so a monitor-gap note ships on the PYTH overview. That gap is not a disagreement about what happened; it is a denominator base. Both numbers measure the same one-time cliff: the monitor sizes the **2.13B** unlock against the pre-unlock float of about **5.75B** for **+36.94%**, while the framework sizes it against the current float of about **7.87B** for **+26.92%**. Same one-time cliff, different denominator. PYTH is best labelled a **fixed-cap token with a single annual dilution event** — inflationary only once a year, and quiet the rest of the time.

## Sell pressure: where new PYTH comes from

Sell #1 — protocol inflation — is **zero**, and it cannot turn on. PYTH is a Solana SPL token with a fixed **10,000,000,000** max supply, all minted at genesis in November 2023, and there is no mint function. The oracle-integrity-staking reward rate was set to zero, so staking pays out no new PYTH either; there is no emission curve of any kind. Staking and slashing stay live but distribute nothing. New supply reaches the market only when the vesting schedule releases already-minted coins, which is Sell #2.

Sell #2 — vesting unlocks — is about **2.13B PYTH**, and it is the whole story of this page. Eighty-five percent of PYTH was locked at launch and releases in four equal annual cliffs of roughly **2,125M** each at the six-, eighteen-, thirty- and forty-two-month marks. The thirty-month cliff unlocked into the float on **May 19 2026**, inside this window — the tradable supply stepped from about **5.75B** to about **7.87B** in a single move, a change of about **2.13B** that matches the scheduled quantum almost exactly, so there is no undrawn overhang to carry forward. Because these cliffs are annual and discrete, with no monthly drip between them, the forward 90 days carry a Sell #2 of exactly **zero**: the next and final cliff is not until **May 2027**.

Sell #3 — Foundation and unscheduled unlocks — is **zero**. About **2,125M PYTH** remains locked for that final 2027 cliff, the DAO holds ecosystem-growth PYTH released in past cliffs, and the buyback Reserve is accumulating — all tracked overhangs — but no discretionary sale beyond the scheduled cliff was observed in the window, so the row books zero and stays monitored. Sell #4 — long-term locked or bankruptcy — is **zero**: Pyth Network is a going concern and no estate or trustee schedule touches PYTH.

## Buy pressure: where new PYTH goes

Buy #1 — programmatic buyback — is about **5M PYTH**, the DAO's PYTH Reserve. Each month the DAO deploys roughly a third of its treasury balance to buy PYTH on the open market, funded by data-feed revenue, with the purchase executed fully on-chain. The DAO's own monthly purchase reports show **1,803,872 PYTH** bought in June 2026 and **1,144,629 PYTH** in July 2026, which with the May tranche is about **5M PYTH** across the window. Crucially the coins are held in the Reserve, not burned, so this is genuine buy pressure taken off the market — but at roughly **5M** against a **2.13B** unlock, it is a rounding error on the cliff, and it only becomes the dominant force once the unlock is out of the trailing window.

Buy #2 — protocol fee burn — is **zero**: PYTH has no automatic, fee-driven burn, only the discretionary Reserve buyback above. Buy #3 — Foundation buy — is **zero**, because the DAO buyback is the only entity purchase and is already counted in Buy #1. Buy #4 — new long-term lock — is **zero**: oracle-integrity staking exists but pays no reward and locks away no new supply, and no new lockup contract was created in the window. So the buy side is a single small on-chain buyback, and it does not pretend to offset an annual cliff.

## Foundation and overhang

PYTH carries a clean, well-defined overhang: the roughly **2,125M PYTH** that is still locked — the gap between the fixed **10B** cap and the circulating **7.87B** — which is the single final cliff scheduled for about **May 2027**, mostly ecosystem-growth allocation. On top of that, the DAO treasury holds ecosystem-growth PYTH from earlier cliffs and the growing PYTH Reserve of bought-back tokens. None of these is booked as sell pressure today, because the locked tranche releases on a known schedule rather than through discretionary sales, and the framework books the scheduled release under Sell #2 as it actually vests. If any of these DAO-controlled balances leaves through a discretionary sale between refreshes, the outflow enters Sell #3 at the next refresh. The date that matters is a long way off — the next cliff is May 2027 — so between now and then the supply picture is unusually quiet for a token still only about **79%** circulating.

## How PYTH compares to other fixed-cap governance tokens

PYTH's natural peers are fixed-cap, no-mint tokens whose only dilution is a vesting calendar — the model for most VC-backed launches of the last cycle. On that axis PYTH is unusually well-behaved: instead of a smooth monthly unlock that dilutes holders every single day, the network chose four discrete annual cliffs, so supply is flat for roughly eleven months and then steps once. That makes the framework read look violent in the month of the cliff and calm the rest of the year, which is exactly what the **+26.92%** trailing versus **-0.06%** forward split shows. Against a continuous-emission Layer 1 — a proof-of-stake chain that mints new coins every block — PYTH has no ongoing issuance at all; its staking rewards were switched off, so there is no tail inflation grinding away in the background.

Against exchange tokens and revenue-buyback-and-burn tokens, PYTH shares the buyback idea but not the burn: its PYTH Reserve holds the bought-back coins in the DAO rather than destroying them, so the buyback removes float today but leaves a DAO-controlled overhang that could return. And the scale is different — a mature exchange token burns a large quarterly quantum against a stable, fully-circulating float, while PYTH's **5M** buyback is tiny next to a **2.13B** annual cliff. So PYTH is neither a pure dilution story nor a deflation story: it is a fixed-cap oracle token whose supply is dominated by one calendar event a year, with a small and growing revenue buyback quietly working the other way in the gaps.

## What to watch in the next 90 days

First, and most importantly, there is no vesting cliff in this window — the next unlock is not until about **May 19 2027** — so the single biggest supply lever is simply absent, and the forward read is near flat. Second, the PYTH Reserve buyback rate: it is funded by data-feed revenue, and the paid Pyth Core data model went live on **Jul 31 2026**, so growing subscription revenue should lift the monthly buyback above the recent roughly **1.5M PYTH** pace. Third, any DAO governance move to deploy ecosystem-growth PYTH from the treasury, which would turn Sell #3 non-zero. Fourth, whether the DAO ever decides to burn rather than hold the Reserve, which would convert the buyback from a recoverable overhang into permanent deflation. Fifth, the circulating supply itself, which should sit flat near **7.87B** until the 2027 cliff.

## Summary

The MrNasdog Pressure Framework reads Pyth Network at **+26.92%** net supply over the last 90 days, in close agreement with our monitor's **+36.94%** once the denominator base is accounted for. PYTH is a fixed **10B** token with no mint and no burn, so its only dilution is a once-a-year vesting cliff — and the **2.13B** May 2026 unlock that drove this reading has already landed. The key point is timing: with the next cliff not due until **May 2027** and a small revenue-funded PYTH Reserve buyback of about **5M** running the other way, the forward 90 days read **-0.06%** — a shade deflationary. PYTH is inflationary for one month a year and quiet for the other eleven.

---

*MrNasdog Pressure Framework analysis of Pyth Network (PYTH), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 6 2026.*
