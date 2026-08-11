---
title:         "MNT Inflation Analysis · August 2026 · A flat ledger and one very large lever"
description:   "MNT total supply read 6,219,316,794.889999 byte-identically across 180 days — no mint, no burn. Every ledger row is 0. Framework net 0.00%, monitor +0.02%."
canonical_url: "https://mrnasdog.com/research/mnt/inflation"
tags:          ["crypto", "mnt", "mantle", "ethereum"]
published:     true
---

*Originally published at [mrnasdog.com/research/mnt/inflation](https://mrnasdog.com/research/mnt/inflation).*

# MNT Inflation Analysis · August 2026 · A flat ledger and one very large lever

Mantle issues no new MNT. The MNT total supply on Ethereum read **6,219,316,794** at both ends of the 90 days to **Aug 11 2026**, and the same figure six months earlier, so nothing was minted and nothing burned. Vesting for Mantle ended in **2023**, and the Mantle Treasury — the one pool that can change MNT's tradable float — held the identical **2,900,022,409 MNT** on its Ethereum wallet at both window ends. Every row of the MrNasdog Pressure Framework ledger is therefore zero: net supply **0.00%** against a supply-monitor reading of **+0.02%**, a gap of **0.02 percentage points**. MNT is a fixed-supply layer-2 gas token whose inflation is not an emission question at all — it is a governance question.

## The verdict, in one paragraph

For the 90-day window to **Aug 11 2026**, the framework reads **MNT at 0.00% net** on both the trailing and the forward window: sell pressure **0 MNT**, buy pressure **0 MNT**, against a circulating base of **3.30B MNT**. The supply monitor reads **+0.02%** for the same trailing window, so the gap is **0.02 percentage points** — comfortably inside the framework's 0.5-point tolerance, which is why the MNT overview carries no data-conflict chip. The two readings agree because there is nothing to disagree about: Mantle's own supply definition treats every token still inside the Mantle Treasury as non-circulating, and that treasury did not send a single MNT during the window. MNT is best characterised as **a fixed-supply layer-2 token with governance-controlled dilution** — flat today, with a very large lever that has not been pulled.

## Sell pressure: where new MNT comes from

Nowhere, for now. Sell #1, protocol inflation, is **zero**. Mantle is a layer-2 network settling on Ethereum: it pays no block rewards and runs no validator issuance in MNT. Reading the MNT token contract on Ethereum at the start of the window, at the end of it, and again at a block from February 2026 returns the same number every time — **6,219,316,794.889999 MNT** — which equals both the published total supply and the published maximum supply. MNT is also the gas token on Mantle, but the fees paid in it are kept as network revenue rather than reissued, so usage does not add supply either.

Sell #2, vesting unlocks, is **zero** and has been since 2023, when the release schedule inherited from the token's predecessor finished. MNT now reads as fully unlocked with no cliff of any size on the calendar, so there is no dated event in the next 90 days that mechanically adds supply.

Sell #3, foundation and unscheduled unlocks, is also **zero** — and this is the row that matters most on Mantle. The Mantle Treasury's Ethereum wallet held **2,900,022,409 MNT** on **Aug 11 2026**, an identical balance to the last decimal place to what it held on **May 12 2026** and again in February 2026. The treasury wallet on Mantle itself holds **2,000,000 MNT**, and roughly **15M MNT** sits across the smaller segregated treasury accounts. Nothing moved, and no budget proposal in the window authorised an MNT transfer. That is an observed flat balance, not an inferred one — the difference matters, because a treasury sized by subtraction can hide a transfer that a direct read cannot.

Sell #4, long-term locked or bankruptcy, is **zero**: the 2023 one-for-one conversion of the predecessor token is closed, the unconverted remainder was written off then, and no trustee schedule or wind-down contract feeds MNT back to the market.

## Buy pressure: where new MNT goes

The buy side is just as empty, which is the honest half of the story. Buy #1, programmatic buyback, is **zero**. Mantle operates no buyback contract and executed no purchases in the window. A phased treasury burn of **3–8%** of MNT supply over 12 to 24 months has circulated as a community discussion since **Feb 25 2026**, but it has never been submitted to a formal vote. The one adjacent governance item, the strategic credit facility approved on **May 8 2026**, commits **30,000 ETH** from the treasury — not MNT — and only earmarks the interest it earns toward possible future MNT burn initiatives. Earmarked interest is not a buyback, and the framework does not book intentions.

Buy #2, protocol fee burn, is **zero**. Mantle has no burn address in its design, and the flat on-chain total supply proves the point: a burn would show up as a falling total, and the total has not fallen by a single token in six months. Buy #3, foundation buy, is **zero** — no treasury open-market buying was disclosed, and the treasury balance neither rose nor fell, so it did not take MNT off the market. Buy #4, new long-term lock, is **zero** as well: there is no MNT staking or lock contract with an announced size that would pull tokens out of the tradable float.

## Foundation and overhang

One overhang dominates MNT, and it is enormous. The Mantle Treasury holds about **2.92B MNT** — roughly **47%** of every token that exists, and close to **88%** of the size of the tradable float. It is split across an Ethereum wallet holding **2,900,022,409 MNT**, a Mantle-native wallet holding **2,000,000 MNT**, and about **15M MNT** in smaller segregated accounts. There is no release schedule attached to any of it. Mantle's published supply definition is explicit — circulating supply is total supply minus treasury holdings — so a treasury transfer is not a bookkeeping event on Mantle, it is the arrival of new float.

There is no buyback accumulation wallet to watch, because there is no buyback, and no separate labs or founder pool beyond the treasury structure itself. That makes MNT unusually simple to monitor and unusually exposed to a single decision. If the treasury's balance falls between refreshes, the outflow enters Sell #3 at the next refresh — and because governance can authorise a large budget in one vote, the step from **0.00%** to a materially inflationary reading can happen in a single block rather than gradually.

## How MNT compares to other layer-2 network tokens

Most large layer-2 tokens are still working through investor and team vesting, releasing a fixed tranche every month whether the network needs the tokens or not. MNT is past that entirely: its unlock schedule closed in 2023, so the calendar-driven dilution that defines the rest of the class simply does not apply. On that axis MNT is one of the cleaner tokens in its sector.

On the other axis it is one of the least clean. Layer-2 tokens with a fee burn get a supply sink that grows with adoption. Mantle has none: MNT pays for gas, but the fees become revenue rather than ash, so usage does not tighten MNT the way it would on a burn-model chain. And where a hard-capped proof-of-work coin has its future issuance written into code, Mantle's **6.22B** ceiling is a governance convention rather than a code guarantee: the token sits behind an upgradeable proxy whose implementation still carries mint and burn functions, unused for at least 180 days but not removed. That is why the zeros on those rows are chain readings rather than permanent promises. Compared with exchange tokens that burn a fixed share of quarterly profit, MNT gives up automatic scarcity in exchange for a treasury the DAO can actually spend. The trade is deliberate: no forced dilution, no forced deflation, everything decided by vote.

## What to watch in the next 90 days

First, the Mantle Treasury balance itself: **2,900,022,409 MNT** on the Ethereum wallet as of **Aug 11 2026** is the single number that decides MNT's next reading, and any fall in it lands directly in Sell #3. Second, the phased treasury burn discussion first posted **Feb 25 2026** — if a formal proposal is submitted and passes, a burn of **3–8%** of supply would move MNT from a flat ledger to a genuinely deflationary one. Third, the credit facility approved **May 8 2026**: its interest is earmarked toward future burn initiatives, so the first realised burn from that stream would be the mechanism's proof of life. Fourth, any new budget cycle proposal, since budget authorisations are the standard route by which MNT leaves the treasury and becomes float. Fifth, the mint and burn functions on the token's upgradeable implementation — a change there would rewrite the whole supply picture rather than just a row of it.

## Summary

Mantle (MNT) is a fixed-supply layer-2 gas and governance token: total supply stood at **6,219,316,794** on Ethereum at both ends of the 90 days to **Aug 11 2026**, vesting closed in 2023, and no burn, buyback or lock removed anything. Every row of the framework ledger reads zero, for a net of **0.00%** of circulating supply against a supply-monitor reading of **+0.02%** — the two agree. The key risk is not emission but discretion: the Mantle Treasury holds about **2.92B MNT**, roughly 47% of the total and nearly as much again as the entire tradable float, with no published release schedule, and one governance vote can turn part of it into supply. The ceiling is **6.22B MNT**, and while it has held for years, it is enforced by governance rather than by code.

---

*MrNasdog Pressure Framework analysis of Mantle (MNT), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 11 2026.*
