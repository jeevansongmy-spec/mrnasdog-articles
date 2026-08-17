---
title: "XLM Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description: "Stellar mints nothing since 2019, yet XLM float still grows +2.97% per 90 days as the Foundation releases ~1,025.8M XLM from its mandate wallets. Monitor +3.02%."
canonical_url: "https://mrnasdog.com/research/xlm/inflation"
tags: ["crypto", "xlm", "stellar", "payments"]
published: true
---

*Originally published at [https://mrnasdog.com/research/xlm/inflation](https://mrnasdog.com/research/xlm/inflation)*

# XLM Inflation Analysis · August 2026 · Supply growing, projected to keep growing

Stellar mints nothing. The XLM protocol inflation mechanism was disabled by a validator vote on Oct 28 2019 and total supply has been fixed near **50.00B XLM** ever since — yet the Pressure Framework still reads **+2.97%** net supply reaching the market over 90 days, closely matching the monitor's **+3.02%**. The reason is that every lumen entering circulation comes from one place: the Stellar Development Foundation releasing XLM out of its own mandate wallets, **~1,025.8M XLM** of it this window. Stellar is a fixed-supply network with a discretionary float, and the float is the part an investor actually holds.

## The verdict, in one paragraph

The framework books **~1,025.8M XLM** of sell pressure and **~0.6M XLM** of buy pressure against a circulating base of **~34,530.9M XLM**, for a net of **+2.97%** over the trailing 90 days and the same **+2.97%** projected for the next 90. The inflation monitor independently reads **+3.02%** for the same window, so the gap is just **0.05pp** — comfortably inside tolerance, no data-conflict chip, no deep walk required. The two numbers agree because they measure the same physical event from opposite ends: the monitor watches circulating supply rise, and the framework watches the Stellar Development Foundation wallets that supply it fall. The cite-able label for XLM is this — **a fixed-supply chain that is structurally inflationary on its active float**. The dilution is real and it runs close to 3% a quarter, but it is a treasury decision, not a protocol rule, and that distinction is the entire investment case either way.

## Sell pressure: where new XLM comes from

Sell #1, protocol inflation, is **0**. Stellar ran a 1% annual inflation mint for roughly five years, generating **5,443,902,087 XLM** before validators voted it off on Oct 28 2019; the following week the Stellar Development Foundation sent about **55.44B XLM** to a locked address, cutting total supply from ~105B to ~50B. Reading the Stellar ledger directly at both ends of this window returns an identical total-coins figure of **105,443,902,087 XLM**, and that figure is exactly the original 100B plus the frozen inflation total — so the mint is genuinely off, not slowed, off. It is worth being precise about the tag: the Core Advancement Proposal that turned inflation off states in its own text that it was designed so the mechanism could be turned back on later if needed. Because the switch lives in a consensus-upgradeable parameter rather than in immutable code, another validator vote could restore it, so the Pressure Framework keeps this row watched rather than permanently closed.

Sell #2, vesting unlocks, is **0**, and for an unusual reason. XLM was never sold to investors under a lock-up, so there is no vesting calendar, no cliff schedule, and — critically — no on-chain escrow contract holding vested-but-unclaimed lumens. Where a coin has a readable lock contract the framework ships the realised outflow rather than the calendar entitlement; on Stellar there is no calendar and no contract, so the question resolves trivially and every release is discretionary. Those discretionary releases are booked in Sell #3 instead, which is where the entire XLM supply story lives.

Sell #3, Foundation and unscheduled unlocks, is **~1,025.8M XLM** — effectively 100% of Stellar's sell pressure. The Stellar Development Foundation publishes 13 named mandate accounts across four buckets: Direct Development, Stellar Growth, Product and Innovation, and Assets and Liquidity. Reading all 13 accounts on-chain at both ends of the 90-day window shows the aggregate falling from **16,227.4M XLM** to **15,201.6M XLM**, a realised net release of **~1,025.8M XLM** into the float once internal foundation-to-foundation transfers cancel inside the perimeter. This is on-chain ground truth, not an estimate from a schedule, and it is confirmed twice over: the Stellar Development Foundation's own published mandate total agrees to within four lumens, and the monitor's independent circulating-supply rise of **+1,010.7M** lands within 1.5%. The pace ran about **11.4M XLM a day**, up from roughly **8.2M a day** averaged over the trailing twelve months — this window is a heavier stretch, not a lull.

Sell #4, long-term locked or bankruptcy, is **0**. No bankruptcy estate holds XLM and no trustee is under a court-ordered distribution schedule, so there is no forced-seller overhang of the kind that shapes the ledger on several other large-cap assets.

## Buy pressure: where new XLM goes

Buy #1, programmatic buyback, is **0**. The Stellar Development Foundation has never operated a buyback programme. It does not need one — it funds its operations out of the lumens it already holds, which is precisely why the sell side is so large. There is no buyback destination wallet to track on XLM because there are no bought-back tokens.

Buy #2, protocol fee burn, is **0**, and this is the detail most XLM commentary gets wrong. Stellar charges a base fee of **0.00001 XLM** per operation, and those fees are **not destroyed**. Historically the Stellar network pooled fees to fund the inflation distribution; when inflation was switched off in 2019 the pooling behaviour remained, so fees still accumulate rather than burn. Anyone modelling XLM as a fee-burn deflationary asset in the mould of a base-fee-burning smart-contract chain is modelling a mechanism Stellar does not have.

Buy #3, Foundation buy, is **0**. The Stellar Development Foundation is structurally a distributor of lumens, never a market buyer of them; its holdings originate from the original 2014 allocation.

Buy #4, new long-term lock, is **~0.6M XLM** — the one genuine buy-side entry on the page, and it is the fee pool. The pool belongs to no account, no one holds keys to it, and since inflation was retired there is no longer any mechanism that pays it out, so lumens that land there are permanently removed from circulation: economically a lock, not a burn, which is why the framework books it here rather than under Buy #2. Reading the Stellar ledger's fee-pool field at both ends of the window shows growth from **9.78M XLM** to **10.38M XLM**. It is a real offset, and it is precisely measured rather than rounded away — but the pool has accrued only about **10.4M XLM** in eleven years of network operation, so at roughly 1/1700th the size of the sell side it changes nothing about the verdict.

## Foundation and overhang

XLM has exactly one team-controlled overhang, and it is enormous. The Stellar Development Foundation's 13 mandate accounts still hold **~15,201.6M XLM** — roughly **30% of total supply** and about **44% of the current float** — split across Direct Development (~2,101.3M), Stellar Growth (~5,894.0M), Product and Innovation (~3,786.6M) and Assets and Liquidity (~3,419.7M). There is no published release calendar for any of it: the Stellar Development Foundation mandate describes purposes, not dates or quanta. At the realised rate of the last 90 days this overhang would take under four more years to exhaust, but nothing obliges the Stellar Development Foundation to move at that pace, in either direction. A second, much smaller non-circulating bucket exists — an upgrade reserve of about **258.9M XLM** — but it has been static for years and is not a discretionary treasury.

No other coordinated overhang is enumerable on XLM. There is no separate DAO treasury, no bankruptcy residual, no identified founder block, and no buyback accumulation wallet. Refresh cadence for the mandate accounts is a daily on-chain read, since all 13 addresses are public. The trigger is straightforward: if the balance of those mandate accounts falls between refreshes, the outflow enters Sell #3 at the next refresh, and because Sell #3 is currently the entire sell side of the XLM ledger, that single reading moves the headline number by itself.

## How XLM compares to other fixed-supply payment chains

The natural comparison for XLM is **XRP**, the other large cross-border payments asset with a fixed supply and a dominant foundational holder. The mechanisms differ in one decisive way. XRP's issuer-held reserve sits in on-chain escrows that release on a published monthly schedule, so the entitlement is knowable in advance and any unclaimed remainder is visible as a contract balance. Stellar has no escrow at all: the Stellar Development Foundation's lumens sit in ordinary accounts it can spend at will. XLM therefore trades less schedule risk for more discretion risk — you can read exactly what happened, but you cannot read what is coming.

Against hard-capped proof-of-work chains such as Bitcoin or Litecoin, the contrast is sharper still. Those assets carry a protocol-encoded issuance curve that no committee can alter, and their inflation falls mechanically at each halving. XLM has zero protocol issuance — strictly better on that axis — but its effective float inflation of nearly 3% a quarter is currently far above the issuance of most halving-model chains. A fixed cap tells you nothing about float dilution when 30% of the supply sits outside the float in one entity's wallets.

Against fee-burning smart-contract chains, XLM lacks the offsetting mechanism entirely. Chains with a base-fee burn convert network usage directly into supply reduction, so growing volume tightens supply. Stellar's equivalent flow is the fee pool, which locks lumens away permanently but at a scale three orders of magnitude too small to matter — **~0.6M XLM** against **~1,025.8M XLM**. Stellar's surging stablecoin payment volume and real-world-asset growth therefore do not tighten XLM supply the way comparable activity would on a burning chain.

## What to watch in the next 90 days

First, the balance of the 13 Stellar Development Foundation mandate accounts — the only number that materially moves the XLM ledger, and readable on-chain every day. At **+2.97%** the reading now sits right at the top of its band: a re-acceleration above roughly **11.5M XLM a day** pushes the next-90-day net past **+3%** and drops the inflation score a full band, and the current pace is **11.4M a day**. Second, Protocol 28 "Adapter", whose mainnet upgrade vote is scheduled for **Sep 16 2026**: its three Core Advancement Proposals cover faster consensus, atomic contract upgrades and contract schema migration, and none of them touch fees, the fee pool, the base reserve or supply — but the vote is the moment to re-read the parameter set. Third, the Stellar Development Foundation's next quarterly report, which restates the mandate balance and usually explains what the quarter's spending funded. Fourth, any future Core Advancement Proposal that converted pooled fees into burned fees — the single most consequential tokenomics change available to Stellar. Fifth, any validator move to restore the retired inflation mechanism: remote, but it is the reason Sell #1 stays watched rather than closed.

## Summary

The MrNasdog Pressure Framework reads XLM at **+2.97%** net supply to market over 90 days, projected flat at **+2.97%** for the next 90, against a monitor reading of **+3.02%** — a **0.05pp** gap and a clean verification. Stellar creates no new lumens; total supply has been fixed near **50.00B XLM** since the mint was voted off on Oct 28 2019. All of the dilution is the Stellar Development Foundation converting its mandate holdings into float, **~1,025.8M XLM** this window, offset only by **~0.6M XLM** accruing to a fee pool that no one can spend. The key risk is the remaining **~15,201.6M XLM** in those mandate accounts — about 30% of total supply, on no published schedule — and the ceiling is the hard 50B total that caps how much can ever reach the market. XLM is a hard-capped asset with a soft float, and the float is what an investor actually owns.

---

*MrNasdog Pressure Framework analysis of XLM, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 17 2026.*
