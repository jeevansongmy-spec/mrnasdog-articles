---
title: "SEI Inflation Analysis · July 2026 · Supply growing · projected to keep growing"
description: "A MrNasdog Pressure Framework read of Sei (SEI): a 44.5M/90d reserve release plus 262.8M of team and investor vesting, no buyback or burn. Framework reads +4.56% net."
canonical_url: "https://mrnasdog.com/research/sei/inflation"
tags: ["crypto", "sei", "layer-1", "tokenomics"]
published: true
---

> Originally published at **[mrnasdog.com/research/sei/inflation](https://mrnasdog.com/research/sei/inflation)** by MrNasdog.

Sei hands out about **44.5M SEI** of reserve over 90 days on a fixed yearly release schedule, while team and private-investor vesting unlocks roughly **262.8M** more — about **307.3M SEI** reaching the market, against a buy side of exactly **zero**. The Pressure Framework reads **+4.56%** net for the last 90 days and **+4.52%** for the next. Our supply monitor reads **+0.03%** — a **4.53 percentage point** gap that ships a warning chip, because the circulating figure it tracks has been frozen at **6,733,333,333** for 87 straight days. SEI is **inflationary on the active float**: the 10B cap is real, but Sei is still only three years into handing its supply out.

## The verdict, in one paragraph

For the 90-day window ending **Jul 16 2026**, the MrNasdog Pressure Framework reads SEI at **+4.56%** net supply growth, and projects **+4.52%** for the next 90 days — sell pressure of **307.3M SEI** against a buy side of **0**. Our supply monitor reads the same trailing window at **+0.03%**, a gap of **4.53 percentage points**, which is far beyond tolerance and therefore ships a warning chip on the SEI overview. The gap is a measurement artifact, not a mechanism dispute. Sei's own mint module, read on-chain on **Jul 16 2026**, hands out **494,505 SEI** every single day, and the published team and private-sale vesting streams run to **Aug 15 2029** and **Aug 15 2027** respectively — none of which the frozen comparison figure registers. On an inflation lens, SEI is **inflationary on the active float**: new SEI arrives every day from two directions, and nothing burns or buys any of it back.

## Sell pressure: where new SEI comes from

Two mechanisms add SEI, and they are different in kind. Sell #1 — protocol inflation — is Sei's reserve release, worth about **44.5M SEI** over 90 days. Sei is a parallel-EVM, bonded proof-of-stake layer-1 with a genuine **10B** hard cap, and its genesis supply was **8.5B**. The remaining **1.5B** is not minted at will: the Sei chain's mint module carries a fixed ten-year release schedule that hands out **180M SEI** for the year to **Aug 14 2026**, then **165M**, then less each year, terminating in **2033** exactly at the cap. That works out to **494,505 SEI** a day, paid to stakers as rewards. The schedule is verifiable twice over: it predicts Sei's measured on-chain supply of **9,191,152,814 SEI** to six significant figures.

Sell #2 — vesting unlocks — is the larger flow at roughly **262.8M SEI** per 90 days, and it is what makes SEI inflationary rather than merely capped. Two genesis allocations are still vesting off a one-year cliff that lapsed on **Aug 15 2024**: the Sei team's **2B SEI**, releasing over five years to **Aug 15 2029**, and the private-sale investors' **2B SEI**, releasing over three years to **Aug 15 2027**. Together they hand out about **2.9M SEI** every day. Crucially these coins already exist on-chain — the lock is what expires — so this vesting does not raise Sei's total supply at all, but it lands directly on the tradable float, which is the only thing an inflation reading cares about.

Sell #3 — Foundation and unscheduled unlocks — is **0** for this window: no public evidence of a release was found, so the row stays at zero and the holdings are carried as watched overhang instead. Sell #4 — long-term locked or bankruptcy — is **0**, because no bankruptcy estate or court-ordered distribution applies to SEI. The supply-arithmetic check holds cleanly: only the reserve release is genuinely new supply, and circulating plus that release comes to **6,777.8M**, comfortably inside both the **10B** cap and the **3,266.7M** of headroom that remains.

## Buy pressure: where new SEI goes

Nowhere. The Sei buy ledger is empty on all four rows, and this is the single most important structural fact about SEI's inflation. Buy #1 — programmatic buyback — is **0**: Sei runs no protocol or treasury mechanism that spends revenue to buy SEI back off the open market, and none has been announced. Buy #2 — protocol fee burn — is **0**, and this is by design rather than omission: Sei's own EVM documentation states plainly that Sei does not implement base-fee burning, that there is no base-fee burn, and that all transaction fees accrue to validators. Unlike Ethereum after EIP-1559, no amount of activity on Sei destroys a single SEI.

Buy #3 — Foundation buy — is **0**: the Sei Foundation has never announced open-market buying, and none was observed in the window. Buy #4 — new long-term lock — is **0**: no new escrow or lockup contract was created, and staking does not count, because bonded SEI unbonds and returns to the float rather than being removed from it. With every offset row at zero, the full **307.3M SEI** of reserve release and vesting reaches holders completely unopposed. That is why the net figure and the gross figure for SEI are the same number.

## Foundation and overhang

Three team-controlled overhangs are tracked for SEI, none of which carries a value this window. The **Sei Foundation** treasury holds a **900M SEI** allocation — 9% of total supply — which finished unlocking on **Aug 15 2025** and is now entirely free to move at the Foundation's discretion; it is walked by hand on a recurring web check. The **Binance Launchpool** allocation of **300M SEI** was liquid from launch in August 2023 and is long dispersed, but is enumerated for completeness. The third is the not-yet-released remainder of the **ecosystem reserve**: roughly **808.8M SEI** of the 10B cap has still not been minted, and it is read directly from the Sei chain's mint module every rebuild.

The reserve remainder is the one overhang that is genuinely not discretionary — it is bound to a schedule encoded in the Sei chain itself, which is why it sits in Sell #1 rather than Sell #3, and why booking it in both would double-count it. The Foundation's 900M is the opposite: fully unlocked, entirely discretionary, and the single largest thing that could change this reading without warning. If the Foundation's balance falls between refreshes, that outflow enters Sell #3 at the next refresh, and the same trigger applies to every overhang listed here.

## How SEI compares to other capped proof-of-stake chains

SEI belongs to a specific class: capped layer-1 chains whose cap is real but whose float is still being built. The closest structural analogue is **Cardano**, which also has a hard cap — 45B ADA — and also never mints above it, releasing new ADA from a protocol reserve instead. The difference is maturity. Cardano's 2017 genesis allocations are long since fully distributed, so its reserve drip is essentially all of its sell pressure. Sei is only three years past its August 2023 launch, so its reserve release of **44.5M** is dwarfed by **262.8M** of team and investor vesting that Cardano no longer has. The cap tells you where SEI ends; it tells you nothing about the next three years.

Against uncapped continuous-emission chains the comparison inverts, and it flatters SEI on shape rather than on size. A chain with no cap can mint forever; Sei's emission is a finite **1.5B SEI** that steps down every year — **180M**, then **165M** from **Aug 15 2026**, then **135M** — and stops permanently in 2033. That is a genuinely better long-run shape than perpetual issuance. The gap that matters is against chains that burn. **Ethereum** and **BNB** both destroy supply as a function of use, so activity fights issuance; Sei routes every fee to validators, so activity does nothing to supply at all. Sei is closer to Cardano here — fees recycled, never destroyed — which means SEI's inflation is a pure function of its schedule, entirely indifferent to how successful the chain becomes.

The practical read: among capped chains, SEI's cap is credible and its emission curve is honest and declining, but it sits at the wrong point on that curve. It carries the dilution profile of an early chain with the marketing of a capped one. The framework scores the number, not the cap.

## What to watch in the next 90 days

Four things would move this reading. First, **Aug 15 2026**: the reserve release schedule steps down from **180M** to **165M** a year, cutting the hand-out from **494,505** to **453,297** SEI — a small, certain, dated improvement already booked into the next-90-day figure. Second, **Aug 15 2027** is the date the private-investor stream ends and roughly **55.6M SEI** a month stops permanently; it is outside this window but it is the single largest structural improvement on SEI's horizon. Third, any Sei Foundation transparency post or treasury movement touching the free **900M** allocation would open Sell #3. Fourth, watch Sei governance for any proposal introducing a fee burn or a buyback — the on-chain record through **Jul 9 2026** contains nothing of the kind, and until one passes, the buy side stays at zero.

## Summary

The MrNasdog Pressure Framework reads Sei (SEI) as **inflationary on the active float**, at **+4.56%** net over the last 90 days and **+4.52%** projected for the next. The mechanism is two-sided on the sell ledger and empty on the buy ledger: a fixed reserve release schedule hands out **44.5M SEI** per 90 days while team and private-investor vesting unlocks **262.8M** more, and neither a buyback nor a fee burn removes any of it, because Sei pays every transaction fee to validators rather than destroying it. The key risk is that this is the honest reading and the widely-quoted circulating figure is not — that number has sat frozen at **6,733,333,333** for 87 consecutive days and shows almost none of this dilution, which is why SEI ships with a data-conflict warning. The ceiling is genuine and worth stating: SEI cannot exceed **10B**, the emission is finite and declining, and it ends permanently in **2033** — but the investor stream runs to **Aug 15 2027** and the team's to **Aug 15 2029**, so the dilution has years left to run.

---

*MrNasdog Pressure Framework analysis of SEI, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 16 2026.*
