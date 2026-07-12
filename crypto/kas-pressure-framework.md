---
title: "KAS Inflation Analysis · July 2026 · Mining is the only supply, and it fades every month"
description: "A MrNasdog Pressure Framework read of Kaspa (KAS): ~178M / 90D of fair-launch proof-of-work mining and an empty buy ledger. Framework +0.65% net; monitor +0.735%, a near-exact match."
canonical_url: "https://mrnasdog.com/research/kas/inflation"
tags: ["crypto", "kas", "kaspa", "proof-of-work"]
published: true
---

> Originally published at **[mrnasdog.com/research/kas/inflation](https://mrnasdog.com/research/kas/inflation)** by MrNasdog.

Kaspa creates new **KAS** in only one way — proof-of-work mining — and the pace steps down about **5.6%** every month on its chromatic emission schedule. That adds roughly **178M KAS** over the next 90 days, against a completely **empty buy ledger** (no buyback, no burn), for a framework read of about **+0.65%** net. Our supply monitor reads **+0.735%** for the trailing window, a gap of about **0.03 percentage points**, so the two agree and no monitor-gap flag ships. With no premine, no vesting and no foundation, KAS is one of the cleanest inflation profiles in crypto: predictable, one-sided, and shrinking.

## The verdict, in one paragraph

For the next 90-day window, the MrNasdog Pressure Framework reads **KAS at about +0.65% net**, and for the trailing 90 days ending **Jul 13 2026** at about **+0.77%** — supply is growing, but slowly, and entirely from mining. Our supply monitor reads the realized last-90-day change at **+0.735%**, versus the framework's **+0.77%** for the same window — a gap of about **0.03 percentage points**, well inside tolerance, so **no monitor-gap chip ships**. The small difference is aggregator-side classification of already-mined coins, not a mining difference: the schedule minted roughly **211M KAS** in the last 90 days, and the monitor's realized circulating delta was about **200.7M**. KAS reads as **structurally low-inflation and steadily disinflating** — every month the new supply is smaller than the month before, and it is heading toward a fixed ceiling.

## Sell pressure: where new KAS comes from

Sell #1 — protocol inflation — is the entire story, at about **178M KAS** over the next 90 days. Kaspa is a proof-of-work BlockDAG that was fair-launched on **Nov 7 2021** with no premine and no allocation of any kind, so the only way new KAS enters existence is as a block reward paid to miners. That reward follows the **chromatic phase** schedule — the subsidy halves every twelve months, but instead of one abrupt yearly cut it is smoothed into a monthly step-down of about **5.6%**. Right now the network issues roughly **24.5 KAS** per second across its **10-blocks-per-second** cadence; a month ago it was closer to **26 KAS** per second, and by October it will be near **21 KAS**. The result is a mint that was about **211M KAS** last quarter and is about **178M** this one — visibly declining.

Every other sell row is **zero**, and structurally so. Sell #2 — vesting unlocks — is zero because there is nothing to vest: Kaspa had no premine, no team or investor tranche, and no tokens held back, so no unlock schedule has ever existed. Sell #3 — Foundation and unscheduled unlocks — is zero because there is no foundation, no company treasury and no premined reserve; there simply is no team-controlled KAS that could enter the market. Sell #4 — long-term locked or bankruptcy — is zero because no estate, escrow or court distribution applies to a coin that was mined into existence from block one. This is why KAS is unusual: the sell side has exactly one line, and it is a published, immutable schedule.

## Buy pressure: where new KAS goes

The buy ledger is empty — all four rows are **zero**. Buy #1 — programmatic buyback — is zero because Kaspa has no protocol treasury or revenue stream to fund one; there is no entity collecting fees to buy KAS back. Buy #2 — protocol fee burn — is zero because Kaspa does not burn anything: transaction fees are paid to miners as part of the coinbase, not destroyed, so network activity does not remove supply the way an **EIP-1559** base-fee burn would on other chains. Buy #3 — Foundation buy — is zero for the same reason Sell #3 is: there is no foundation doing open-market buying. Buy #4 — new long-term lock — is zero because a pure proof-of-work chain has no staking or lock-up contract that could sequester supply. Nothing on the network offsets the mining emission, so the net reading is simply the mint itself.

## Foundation and overhang

Kaspa has **no team-controlled overhang at all** — and that is the point. There is no foundation wallet, no company treasury, no premined reserve, no investor unlock schedule and no bankruptcy estate, because none of those were ever created. The project was fair-launched with the code public and mining open to everyone from the first block, so the entire supply that exists today reached the market the same way: it was mined. That removes the single largest source of uncertainty on most other tokens — the discretionary decision of an entity sitting on a large idle balance. The only overhang KAS has is the **~1.1B KAS** still to be mined over the coming decades under a schedule that is fixed in protocol and cannot be changed by any vote. If that schedule ever changed, it would enter Sell #1 at the next refresh — but it is immutable, so in practice the forward supply is fully known.

## How KAS compares to other proof-of-work chains

KAS belongs to the **capped, halving-model proof-of-work** family — the same structural class as **Bitcoin** and **Litecoin**. Like Bitcoin, Kaspa has a hard ceiling (about **28.7B KAS**) and a subsidy that halves on a fixed schedule, so its inflation only ever falls. The difference is cadence and shape: Bitcoin halves in one step every four years, which creates a sharp discontinuity, while Kaspa's chromatic schedule spreads the same decay across smooth monthly steps, so its disinflation is gradual rather than lumpy. At about **96% mined**, KAS is much further along its emission curve than most young proof-of-work coins, which is why its annualized inflation is already low and heading lower.

Against the uncapped side of proof-of-work — chains like **Monero** and its tail-emission descendants — the contrast is sharper. Monero shares Kaspa's fair-launch, no-premine ethic, but it deliberately never stops issuing: a fixed tail subsidy keeps miners paid forever, so its supply grows in perpetuity. Kaspa instead approaches a fixed cap, so its emission trends toward zero. And unlike exchange tokens or fee-burning smart-contract chains that can push their supply net-deflationary through buybacks or an **EIP-1559** burn, Kaspa has no burn and no buyback — it will never be deflationary, but its inflation is small and falling. The honest label is **disinflationary hard-capped mining**: one-sided supply, no offsets, no surprises.

## What to watch in the next 90 days

The one recurring dated event is the monthly emission step-down — the next one lands around **Aug 5 2026**, when the block reward drops from about **2.45 KAS** to about **2.31 KAS** per block, followed by similar cuts in early September and early October. Each step lowers the mint, so forward inflation only eases. Watch the **95%-mined milestone** crossed in July 2026 as a narrative marker for shrinking miner sell-pressure. Watch whether the **Toccata hard fork** (activated **Jun 30 2026**, adding native assets, covenants and ZK verification) drives new on-chain activity — it does not change KAS emission, but heavier usage would raise miner fee revenue without adding to supply. And watch for any governance or roadmap proposal touching the block rate: a future change would adjust the per-block reward to keep per-second emission on the same curve, so the schedule itself should stay intact.

## Summary

KAS has one of the simplest inflation profiles in crypto: mining is the only source of new supply, and it is falling every month. Kaspa mints about 178M KAS over the next 90 days on a chromatic schedule that steps emission down about 5.6% monthly, against a completely empty buy ledger — no buyback, no burn — for a framework read of about +0.65% net. Our supply monitor reads +0.735% realized, and the two agree within about 0.03 percentage points, so no monitor-gap flag ships. The key features are structural: no premine, no vesting and no foundation means no discretionary overhang, and a fixed ~28.7B cap that is roughly 96% mined means the inflation can only keep shrinking toward zero.

---

*MrNasdog Pressure Framework analysis of Kaspa (KAS), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 13 2026.*
