---
title: "APT Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description: "A MrNasdog Pressure Framework read of Aptos (APT): 5.00M staking mint plus 33.93M of monthly unlocks per 90D vs a 0.62M gas burn. Framework +4.53%, monitor +4.74%."
canonical_url: "https://mrnasdog.com/research/apt/inflation"
tags: ["crypto", "apt", "aptos", "layer1"]
published: true
---

> Originally published at **[mrnasdog.com/research/apt/inflation](https://mrnasdog.com/research/apt/inflation)** by MrNasdog.

Aptos adds about **38.93M APT** to the market over the next 90 days — only **5.00M** of it newly minted by staking, the other **33.93M** released by the 2022 allocation calendar — against just **0.62M APT** of gas-fee burn and no buyback. The Pressure Framework reads **+4.53% net**, and the supply monitor reads **+4.74%** over the same window, a gap of about **0.21 percentage points** that stays inside tolerance. Aptos capped supply at **2.1 billion** and cut its staking emission to **2.60%** in early 2026, but the unlock calendar — not the mint — is the whole story until it runs out in October.

## The verdict, in one paragraph

Over the last 90 days the Pressure Framework reads Aptos at **+4.53% net**: about **38.93M APT** of new supply reaching the market against only **0.62M APT** of gas-fee burn, on a circulating base of **845.58M APT**. Our supply monitor reads the same trailing window at **+4.74%**, a gap of about **0.21 percentage points** — inside the framework's tolerance, so this build ships **no monitor-gap chip** and needs no reconciliation walk. The two agree because the monitor's circulating growth is dominated by the same three monthly unlocks the framework books directly. Looking forward, the framework reads **+4.53%** for the next 90 days as well. APT is best characterised as **structurally inflationary on its unlock calendar** — a newly hard-capped token whose protocol mint has been throttled to almost nothing, but whose four-year vesting schedule still floods the float faster than any burn can absorb.

## Sell pressure: where new APT comes from

Sell #2 — vesting unlocks — is the dominant stream, at about **33.93M APT** over the next 90 days. The 2022 genesis allocation for core contributors, private investors and the Foundation vests on a monthly calendar, releasing roughly **11.31M APT** — about **0.54%** of the 2.1B cap — on the 12th of each month. Three tranches fall inside the window: **Aug 12 2026**, **Sep 12 2026** and **Oct 12 2026**. That last date matters more than any other on Aptos: it is the final large monthly tranche of the four-year unlock that began at the October 2022 mainnet launch, after which the recurring unlock drops by roughly 60%. Until then, the calendar hands the market close to seven times more APT than the protocol itself mints.

Sell #1 — protocol inflation — is the staking-reward mint, and it is now small. In an early-2026 governance overhaul Aptos cut its staking-reward rate from **5.19%** to **2.60%**, the floor of its emission curve, so new APT is minted to stakers at that yearly rate — about every two hours — and on the roughly **810M APT** staked that works out to about **5.00M APT** over 90 days. Because APT is now capped at **2.1 billion** and only **1,206.64M** has ever been minted, this stream is genuinely finite: once supply reaches the cap, staking minting stops for good. For now it is real but modest — the mint is the minority of the sell pressure, not the majority.

Sell #3 — Foundation and unscheduled unlocks — is **zero** on this build, though the overhang behind it is large: about **361M APT** is minted but not yet circulating. The framework books nothing here because every one of those buckets releases through the same monthly calendar already counted in Sell #2, and no off-calendar Foundation distribution was observed in the window. Sell #4 — long-term locked or bankruptcy — is **zero** and structurally so: Aptos is a live project with no bankruptcy estate and no trustee distribution.

## Buy pressure: where new APT goes

Buy #2 — protocol fee burn — is the only non-zero buy row, and it is small: about **0.62M APT** over 90 days. The same early-2026 overhaul that capped supply also raised gas fees roughly **10x** and set **100%** of the base fee to be permanently burned — a genuine deflationary lever now built into the chain. On-chain that removed about **235,000 APT** in the last 30 days, one of the highest monthly burn rates the network has recorded, yet it still cancels only about **1.6%** of the supply arriving. The burn scales with network activity, so it is the row to watch: it is the mechanism through which Aptos could one day turn deflationary, but at today's usage it barely dents the unlock.

The other three buy rows are **zero**. Buy #1 — programmatic buyback — is zero because Aptos runs no buyback of any kind; no protocol or Foundation program repurchases APT on the open market. Buy #3 — Foundation buy — is zero because the Foundation discloses no open-market accumulation. Buy #4 — new long-term lock — is zero in-window: the Foundation did permanently lock and stake **210M APT** as part of the early-2026 overhaul, a large and real removal from the tradable float, but that was a one-off that executed before this window, so it books no in-window flow.

## Foundation and overhang

The team-controlled overhang on Aptos is roughly **361M APT** — the difference between the **1,206.64M APT** minted so far and the **845.58M APT** circulating. It splits across the genesis allocations still vesting: core contributors at about **19%** of the design, private investors at about **13.48%**, and the Foundation at about **16.50%**, all releasing on the monthly calendar counted in Sell #2. Inside that total sits the **210M APT** the Foundation locked and staked permanently in early 2026 — supply that is now committed rather than an overhang. Separately, about **893M APT** of headroom remains between today's minted supply and the 2.1B cap, reserved for future staking-reward minting and nothing else.

These balances are tracked against the published vesting schedule and the on-chain staking and supply reads at every rebuild. The monthly unlock is compared date by date against the calendar, which is how the framework knows the October 2026 tranche is the last large one. If any of these Foundation or contributor balances falls between refreshes faster than the published schedule allows, the excess outflow enters Sell #3 at the next refresh rather than being absorbed silently into the vesting row.

## How APT compares to other capped proof-of-stake chains

APT belongs to a specific structural class: the venture-funded proof-of-stake layer-1 whose hard cap is real but whose near-term supply is set by a vesting calendar rather than a block subsidy. Compared with a halving-model chain like Bitcoin, where the cap and the emission schedule are the same fact and the float converges on the cap, Aptos's new 2.1B cap tells you little about the next 90 days — what matters is that the four-year genesis unlock is still running. In that respect APT reads far more like Sui or Celestia than like Bitcoin: the dominant supply variable is an unlock schedule, and the block mint is the small part.

Against uncapped continuous-emission chains such as Solana or Cardano, Aptos has just moved the other way. Those networks mint genuinely new tokens every epoch with no ceiling, whereas Aptos capped supply and cut its emission to the **2.60%** floor, so its mint of about **5.00M APT** a quarter is already the minority of its sell pressure and shrinks toward zero as supply approaches the cap. The interesting comparison, though, is with fee-burn chains like Ethereum and BNB. Aptos now has the same class of lever — **100%** base-fee burn on **10x** gas — that lets Ethereum post negative net issuance in busy periods. The difference is entirely activity: Aptos burns about **0.62M APT** a quarter today, nowhere near the **33.93M** its calendar releases. The machinery for deflation is installed; the usage to power it is not yet there.

That makes the structural ceiling on APT's framework score clear and near-term. As long as the 2022 calendar runs, no realistic burn can offset it, so APT reads firmly inflationary. Once the calendar's large tranches end in October 2026, the arithmetic flips fast: the mint is tiny and shrinking, the burn is live, and the net figure could fall toward zero or below the moment unlocks stop dominating.

## What to watch in the next 90 days

The **Aug 12 2026** unlock adds about **11.3M APT** to the float, the **Sep 12 2026** unlock adds about the same, and the **Oct 12 2026** unlock — the final large monthly tranche of the four-year genesis vest — adds a last **11.3M APT** before the recurring release falls roughly 60%. That October date is the single most important supply event on Aptos: watch whether the framework's forward net drops sharply in the following build, because it should. Watch the gas-fee burn rate, currently about **0.62M APT** a quarter, since any sustained rise in network activity is the only path to a deflationary print. And watch for any new governance proposal that would alter the staking-reward floor or the burn split, the two levers that decide whether capped Aptos actually starts shrinking.

## Summary

The Pressure Framework reads Aptos as **structurally inflationary on its unlock calendar** at **+4.53% net** over the next 90 days, matched by the supply monitor at **+4.74%**. The mechanism is release-side: about **33.93M APT** of monthly allocation unlocks plus about **5.00M APT** of throttled staking mint, against just **0.62M APT** of gas-fee burn and no buyback. The key event is **Oct 12 2026**, when the four-year genesis calendar delivers its final large tranche and the dominant source of supply growth falls away. The ceiling — or in Aptos's case, the opportunity — is the newly installed **100%** base-fee burn under a hard **2.1 billion** cap: the machinery to turn APT deflationary exists, and only network usage stands between it and a shrinking supply.

---

*MrNasdog Pressure Framework analysis of Aptos (APT), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated August 4 2026.*
