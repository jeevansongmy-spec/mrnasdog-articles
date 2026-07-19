---
title: "XLM Inflation Analysis · July 2026 · Supply growing, projected to keep growing"
description: "Stellar mints nothing since 2019, yet XLM float still grows +2.87% per 90 days as the Foundation releases ~979.9M XLM from its mandate wallets. Monitor +2.96%."
canonical_url: "https://mrnasdog.com/research/xlm/inflation"
tags: ["crypto", "xlm", "stellar", "payments"]
published: true
---

*Originally published at [https://mrnasdog.com/research/xlm/inflation](https://mrnasdog.com/research/xlm/inflation)*

# XLM Inflation Analysis · July 2026 · Supply growing, projected to keep growing

Stellar mints nothing. The XLM protocol inflation mechanism was retired by a validator vote on Oct 28 2019 and total supply has been fixed near **50.00B XLM** ever since — yet the Pressure Framework still reads **+2.87%** net supply reaching the market over 90 days, against the monitor's **+2.96%**, a gap of just **0.09pp**. The reason is that every lumen entering circulation comes from one place: the Stellar Development Foundation releasing XLM out of its own mandate wallets, **~979.9M XLM** of it this window. Stellar is a fixed-supply network with a discretionary float.

## The verdict, in one paragraph

The framework books **~979.9M XLM** of sell pressure and **~0.55M XLM** of buy pressure against a circulating base of **~34,157.2M XLM**, for a net of **+2.87%** over the trailing 90 days and the same **+2.87%** projected for the next 90. The inflation monitor independently reads **+2.96%** for the same window, so the gap is **0.09pp** — comfortably inside tolerance, no data-conflict chip, no deep walk required. The two numbers agree because they are measuring the same physical event from opposite ends: the monitor watches circulating supply rise, and the framework watches the Stellar Development Foundation wallets that supply it fall. The cite-able label for XLM is this — **a fixed-supply chain that is structurally inflationary on its active float**. The dilution is real and it is roughly 3% a quarter, but it is a treasury decision, not a protocol rule, and that distinction is the entire investment case either way.

## Sell pressure: where new XLM comes from

Sell #1, protocol inflation, is **0**. Stellar ran a 1% annual inflation mint for roughly five years, generating **5,443,902,087 XLM** before validators voted it off on Oct 28 2019; the following week the Stellar Development Foundation burned about **55.44B XLM**, cutting total supply from ~105B to ~50B. Reading the Stellar ledger directly at both ends of this window returns an identical total-coins figure, so the mint is genuinely off — not slowed, off. It is worth being precise about the tag: because inflation was disabled by a validator vote rather than removed by immutable code, another validator vote could in principle restore it, so the framework keeps this row watched rather than permanently closed.

Sell #2, vesting unlocks, is **0**, and for an unusual reason. XLM was never sold to investors under a lock-up, so there is no vesting calendar, no cliff schedule, and — critically — no on-chain escrow contract holding vested-but-unclaimed lumens. Where a coin has a readable lock contract the framework ships the realised outflow rather than the calendar entitlement; on Stellar there is no calendar and no contract, so the question resolves trivially and every release is discretionary. Those discretionary releases are booked in Sell #3 instead, which is where the entire XLM supply story lives.

Sell #3, Foundation and unscheduled unlocks, is **~979.9M XLM** — effectively 100% of Stellar's sell pressure. The Stellar Development Foundation publishes 13 named mandate accounts across four buckets: Direct Development, Stellar Growth, Product and Innovation, and Assets and Liquidity. Walking every native credit and debit on all 13 accounts across the 90-day window gives gross outflows of about **2,744.8M XLM** against gross inflows of about **1,764.9M XLM**, with internal foundation-to-foundation transfers cancelling inside the perimeter, for a net release of **~979.9M XLM** into the float. This is on-chain ground truth, not an estimate from a schedule.

Sell #4, long-term locked or bankruptcy, is **0**. No bankruptcy estate holds XLM and no trustee is under a court-ordered distribution schedule, so there is no forced-seller overhang of the kind that shapes the ledger on several other large-cap assets.

## Buy pressure: where new XLM goes

Buy #1, programmatic buyback, is **0**. The Stellar Development Foundation has never operated a buyback programme. It does not need one — it funds its operations out of the lumens it already holds, which is precisely why the sell side is so large. There is no buyback destination wallet to track on XLM because there are no bought-back tokens.

Buy #2, protocol fee burn, is **0**, and this is the detail most XLM commentary gets wrong. Stellar charges a base fee of 0.00001 XLM per operation, and those fees are **not destroyed**. Historically the network pooled fees to fund the inflation distribution; when inflation was switched off in 2019 the pooling behaviour remained, so fees still accumulate rather than burn. Anyone modelling XLM as a fee-burn deflationary asset in the mould of a base-fee-burning smart-contract chain is modelling a mechanism Stellar does not have.

Buy #3, Foundation buy, is **0**. The Stellar Development Foundation is structurally a distributor of lumens, never a market buyer of them; its holdings originate from the 2014 allocation.

Buy #4, new long-term lock, is **~0.55M XLM** — the one genuine buy-side entry on the page, and it is the fee pool. Because the pool belongs to no account and no one holds keys to it, lumens that land there are permanently removed from circulation: economically a lock, not a burn, which is why the framework books it here rather than under Buy #2. Reading the ledger's fee-pool field at both ends of the window shows growth from about **9.64M XLM** to about **10.19M XLM**. It is a real offset. It is also roughly 1/1800th the size of the sell side, so it changes nothing about the verdict.

## Foundation and overhang

XLM has exactly one team-controlled overhang, and it is enormous. The Stellar Development Foundation's 13 mandate accounts still hold about **15,575.6M XLM** — roughly **31% of total supply** and about **46% of the current float** — held in Direct Development, Stellar Growth, Product and Innovation, and Assets and Liquidity buckets. There is no published release calendar for any of it: the mandate describes purposes, not dates or quanta. At the realised rate of the last 90 days this overhang would take roughly four more years to exhaust, but nothing obliges the Stellar Development Foundation to move at that pace, in either direction.

No other coordinated overhang is enumerable on XLM. There is no separate DAO treasury, no bankruptcy residual, no identified founder block, and no buyback accumulation wallet. Refresh cadence for the mandate accounts is a daily on-chain read, since all 13 addresses are public. The trigger is straightforward: if the balance of those mandate accounts falls between refreshes, the outflow enters Sell #3 at the next refresh, and because Sell #3 is currently the entire sell side of the XLM ledger, that single reading moves the headline number by itself.

## How XLM compares to other fixed-supply payment chains

The natural comparison for XLM is **XRP**, the other large cross-border payments asset with a fixed supply and a dominant foundational holder. The mechanisms differ in one decisive way. XRP's Ripple-held reserve sits in on-chain escrows that release on a published monthly schedule, so the entitlement is knowable in advance and any unclaimed remainder is visible as a contract balance. Stellar has no escrow at all: the Stellar Development Foundation's lumens sit in ordinary multisig accounts it can spend at will. XLM therefore trades less schedule risk for more discretion risk — you can read exactly what happened, but you cannot read what is coming.

Against hard-capped proof-of-work chains such as Bitcoin or Litecoin, the contrast is sharper still. Those assets carry a protocol-encoded issuance curve that no committee can alter, and their inflation falls mechanically at each halving. XLM has zero protocol issuance — strictly better on that axis — but its effective float inflation of about 2.87% a quarter is currently higher than the issuance of most halving-model chains. A fixed cap tells you nothing about float dilution when a third of the supply sits outside the float in one entity's wallets.

Against fee-burning smart-contract chains, XLM lacks the offsetting mechanism entirely. Chains with a base-fee burn convert network usage directly into supply reduction, so growing volume tightens supply. Stellar's equivalent flow is the fee pool, which locks lumens away permanently but at a scale two to three orders of magnitude too small to matter — **~0.55M XLM** against **~979.9M XLM**. Stellar's surging stablecoin payment volume and real-world-asset growth therefore do not tighten XLM supply the way comparable activity would on a burning chain.

## What to watch in the next 90 days

First, the balance of the 13 Stellar Development Foundation mandate accounts — this is the only number that materially moves the XLM ledger, and it is readable on-chain every day. A sustained slowdown below the current pace would cut the framework's reading toward +2%; an acceleration would push it past +3% and drop the inflation score another band. Second, the Stellar Development Foundation's Q2 2026 quarterly report, expected in early August 2026, which restates the mandate balance and usually explains what the quarter's spending funded. Third, any protocol change that would create a fee burn: Protocol 27 "Zipper", voted on by validators on Jul 8 2026, added delegated authentication for smart-contract accounts and touched nothing about supply, fees, or the fee pool, but a future Core Advancement Proposal that converted pooled fees into burned fees would be the single most consequential tokenomics change available to Stellar. Fourth, any validator move to restore the retired inflation mechanism — remote, but it is the reason Sell #1 stays watched rather than closed.

## Summary

The MrNasdog Pressure Framework reads XLM at **+2.87%** net supply to market over 90 days, projected flat at **+2.87%** for the next 90, against a monitor reading of **+2.96%** — a **0.09pp** gap and a clean verification. Stellar creates no new lumens; total supply has been fixed near **50.00B XLM** since the mint was voted off on Oct 28 2019. All of the dilution is the Stellar Development Foundation converting its mandate holdings into float, **~979.9M XLM** this window, offset only by **~0.55M XLM** accruing to a fee pool that no one can spend. The key risk is the remaining **~15,575.6M XLM** in those mandate accounts — about 31% of total supply, on no published schedule — and the ceiling is the hard 50B total that caps how much can ever reach the market. XLM is a hard-capped asset with a soft float, and the float is what an investor actually owns.

---

*MrNasdog Pressure Framework analysis of XLM, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 19 2026.*
