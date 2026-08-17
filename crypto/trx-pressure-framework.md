---
title: "TRX Inflation Analysis · August 2026 · Mixed flows, supply roughly steady"
description: "TRON minted 352.4M TRX and burned 245.7M in fees over 90 days. The framework reads +0.11% net — barely inflationary, and the burn is slipping."
canonical_url: "https://mrnasdog.com/research/trx/inflation"
tags: ["crypto", "tron", "trx", "fee-burn"]
published: true
---

> Originally published at **[mrnasdog.com/research/trx/inflation](https://mrnasdog.com/research/trx/inflation)** by MrNasdog.

TRON has both an issuance engine and a burn engine running at full speed, and they very nearly cancel. Over the 90 days to **Aug 17 2026** TRON block rewards minted **352.4M TRX** while transaction-fee burning destroyed **245.7M TRX**, leaving **+0.11% net** supply growth against a supply monitor reading **+0.10%** — a gap of about **0.01 percentage points**. TRX is uncapped, so the ceiling is behavioural, not coded: TRON stays close to flat only for as long as fee burning keeps pace with a fixed **136 TRX** per block, and right now the burn is the side that is slipping.

## The verdict, in one paragraph

For the 90-day window ending **Aug 17 2026**, the MrNasdog Pressure Framework reads TRX at **+0.11% net** supply growth and projects **+0.11%** forward. Total sell pressure was **352.4M TRX** of block-reward issuance; total buy pressure was **245.7M TRX** of fee burn, and every other row on both ledgers is zero. Our supply monitor reads the same window at **+0.10%**, a gap of roughly **0.01 percentage points** — far inside the half-point tolerance, so no monitor-gap chip ships on the TRX overview. The two agree because TRON is effectively fully circulating: its total supply and its circulating supply differ by less than **5M TRX** out of **94.9B**, so there is no reserve bucket for the two readings to disagree about. The cite-able label for TRX is a **high-throughput settlement chain whose fee burn no longer quite covers its block rewards** — inflationary by a hair, for the third quarter running.

## Sell pressure: where new TRX comes from

Sell #1, protocol inflation, is the only live sell row on TRON and it is pure protocol arithmetic. Every TRON block pays **8 TRX** to the Super Representative that produced it and **128 TRX** to the voters spread across the top 127 Super Representatives and partners — **136 TRX** per block, fixed, with no halving and no decay curve. Because TRON block times drift slightly above the nominal three seconds, this build counted the blocks rather than assuming them: the chain moved from block **82,829,692** to block **85,420,813** across the window, **2,591,121** blocks at an average of **3.0010** seconds. That gives **352.4M TRX** of gross issuance, or about **3.92M TRX** a day. TRON governance cut this rate once, in **Jun 2025**, from **176 TRX** per block; no proposal has touched it since, and no supply-affecting proposal was approved inside this window at all, so the trailing rate is also the forward rate.

Sell #2, vesting unlocks, is **zero**. TRON launched in 2018, its founding allocations finished releasing years ago, and the project publishes no live vesting calendar — there is no dated cliff for this window or any window ahead. Aggregator pages that show a TRX unlock schedule are describing a different asset; on TRON there is nothing left to unlock.

Sell #3, Foundation and unscheduled unlocks, is **zero** for the window: no identified TRON treasury sold into the market, and no wallet with a public identity showed an outflow that qualifies as a release. Sell #4, long-term locked or bankruptcy, is **zero** as well — no bankruptcy estate or court-appointed trustee holds TRX, so there is no forced distribution schedule to track. The practical consequence is that TRX inflation is almost pure protocol arithmetic: one row, one rate, no discretionary surprises.

## Buy pressure: where new TRX goes

Buy #2, protocol fee burn, is the load-bearing row on the whole TRX ledger. TRON destroys transaction fees rather than paying them to block producers: bandwidth costs **1,000** sun per byte and energy costs **100** sun per unit, and when a sender has not staked TRX for those resources the network burns TRX to cover the shortfall. Because TRON exposes no historical burn counter, this build measured the burn directly, sampling **4,000** blocks spread evenly across the window and summing the fee destroyed in every transaction. The result is **94.8 TRX** burned per block, or **245.7M TRX** over 90 days — about **2.73M TRX** a day. Two independent readings corroborate it: an external quarterly series puts the Apr to Jun 2026 burn near **2.96M TRX** a day, and TRON's own quarterly report put the Jan to Mar 2026 burn at **281.8M TRX**. All three agree on both the size and, more importantly, the direction — the burn is falling.

Why it is falling is the single most important thing to understand about TRX supply. Burning is the fallback, not the default: a TRON user who stakes TRX for energy and bandwidth, or who rents energy from a lending market, pays nothing to the burn at all. As the energy-rental market matured, more of TRON's record throughput started running on staked and rented resources instead of burned TRX, so activity and burn decoupled. Inside this window alone the burn dropped from **96.5 TRX** per block in the first half to **92.3 TRX** in the second. TRON can process a record quarter of stablecoin volume and still burn less TRX than the quarter before.

The rest of the buy ledger is empty. Buy #1, programmatic buyback, is **zero** — TRON operates no protocol buyback contract. Buy #3, Foundation buy, is **zero**, and this row deserves a note because a headline number sits behind it: the Nasdaq-listed TRX treasury company keeps growing its stack at about **$50,000** a day. Its own quarterly filing, published **Aug 11 2026**, shows the mechanism is a token purchase agreement dated **Jan 6 2026** under which a related party delivers that TRX every day for 360 days against **$18.0M** paid up front — an off-market delivery from an affiliate's existing coins, not an open-market bid, so it absorbs no float and books zero. Buy #4, new long-term lock, is **zero** too: staked TRX still counts as circulating and unwinds in 14 days, and the staked share actually fell across the window to about **48.2%** of supply.

## Foundation and overhang

TRON has no locked foundation allocation left, so its overhang is corporate rather than protocol. The largest identified holder is the Nasdaq-listed TRX treasury company, which held more than **709.4M TRX** as of **Aug 12 2026** — roughly **0.75%** of circulating supply — with nearly all of it staked through a lending protocol and therefore subject to a 14-day unwind before any of it could reach an exchange. Sitting behind it is roughly **30M TRX** still owed to that company under the standing delivery contract, which runs into **Jan 2027**; that flow moves coins between private holders rather than adding supply. The third tracked overhang is the reserve backing TRON's own dollar-pegged token, which holds TRX among its collateral.

None of the three fires in this window, so all three sit at zero. If any of these balances falls between refreshes, that outflow enters Sell #3 at the next refresh. The treasury company's **Aug 13 2026** announcement that it intends to seek Super Representative status cuts the other way — a block producer needs its stake in place, which makes an unwind less likely, not more.

## How TRX compares to other uncapped settlement chains

The obvious comparison is Ethereum, because both chains burn fees. Ethereum burns a base fee that scales with congestion and pays issuance to stakers, so its net supply flips between shrinking and growing depending on demand for blockspace. TRON burns fees at fixed unit prices and pays a fixed **136 TRX** per block regardless of activity, which makes TRX far more predictable and far less responsive: a busy TRON quarter cannot mint less, and the burn only rises if users choose to pay in burned TRX rather than staked or rented resources. That resource-rental escape valve has no clean Ethereum analogue, and it is why TRON's burn can fall while its volume sets records.

Against capped chains, TRX is a different asset class of supply. Bitcoin's issuance falls on a known schedule toward a hard ceiling; TRON's issuance is a flat line with no ceiling at all, and the only thing standing between TRX and open-ended growth is a burn that governance can change but cannot guarantee. Against exchange tokens that run quarterly buybacks funded by business revenue, TRX again lacks the mechanism. The fairest label is that TRX behaves like a low-inflation utility coin — under **0.5%** a year at the current pace — rather than a deflationary one, and the marketing framing of TRON as a deflationary chain has been out of date since the fee cut of **Aug 2025** made the network cheap enough that burning stopped keeping up.

## What to watch in the next 90 days

First, the staked share of TRX. It slipped to about **48.2%** across this window after six quarters of growth, and staking and burning are substitutes — a rebound in staking suppresses the burn further and pushes net inflation up. Second, the close of the third quarter on **Sep 30 2026** and the quarterly supply report that follows it, which will show whether the burn's slide from **96.5** to **92.3 TRX** per block continued. Third, any TRON governance proposal touching the energy price or the block reward: the last two such votes, in **Jun 2025** and **Aug 2025**, each moved TRX supply more than a year of ordinary activity. Fourth, the listed treasury company's Super Representative bid, expected to be voted through **Sep 2026**. Fifth, the standing delivery contract running into **Jan 2027**, which quietly concentrates roughly **30M TRX** more into a single treasury.

## Summary

TRX is an uncapped coin held near flat by an unusually even contest: TRON mints **136 TRX** every block, or **352.4M TRX** across the 90 days to **Aug 17 2026**, and burns transaction fees worth **245.7M TRX** over the same window, for **+0.11% net** supply growth against a supply monitor at **+0.10%**. The key risk is structural rather than dramatic: the burn side is optional for users and the mint side is not, so as staking and energy rental absorb more of TRON's throughput, the network can grow busier and more inflationary at the same time. There is no cap to fall back on and no buyback to lean on, which leaves TRON governance — the same body that cut the block reward in **Jun 2025** and cut fees in **Aug 2025** — as the only lever that can turn TRX deflationary again. For now TRX is best read as very slightly inflationary and highly predictable, with a supply path decided by user behaviour rather than by code.

---

*MrNasdog Pressure Framework analysis of TRX, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 17 2026.*
