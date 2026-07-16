---
title:         "LUNC Inflation Analysis · July 2026 · Mixed flows, supply roughly steady"
description:   "Terra Classic's mint module reads zero — it issues no LUNC at all. A 0.5% burn tax plus exchange burns remove ~9.4B/90d. Framework reads -0.16% net vs our monitor's +0.90%."
canonical_url: "https://mrnasdog.com/research/lunc/inflation"
tags:          ["crypto", "lunc", "terraclassic", "tokenomics"]
published:     true
---

*Originally published at [mrnasdog.com/research/lunc/inflation](https://mrnasdog.com/research/lunc/inflation)*

Terra Classic does not mint. The chain's mint module reads zero, so the only new LUNC reaching the market is about **389M** of community-pool spending over 90 days, against roughly **9.4B** destroyed by the **0.5%** burn tax and exchange burns. The Pressure Framework reads LUNC at **-0.16%** net — supply shrinking, but barely, because 9.4B is a rounding error against a **5.53 trillion** float. Our supply monitor reads **+0.90%**, a **1.07 percentage point** gap we could not close on-chain, so a **monitor-gap flag** ships with this read.

## The verdict, in one paragraph

For the 90-day window ending **Jul 16 2026**, the MrNasdog Pressure Framework reads **LUNC at -0.16% net**: about **389M LUNC** of sell pressure against about **9.4B LUNC** of buy pressure, on a circulating base of roughly **5.53 trillion LUNC**. Our supply monitor reads the realised last-90-day change at **+0.90%** — a gap of about **1.07 percentage points** in the opposite direction, which is over tolerance and triggers a **monitor-gap flag**. We walked it and kept our own read, for a reason that is not a judgement call: Terra Classic's mint module is switched off, and the chain's own arithmetic proves it. The original supply of **6.91 trillion LUNC** minus every coin ever burned equals the live total of **6.45 trillion** to within **0.000007%**. There is no room in that equation for a mint. Terra Classic is a **quiet chain with a slow, permanent leak downward** — it cannot issue, and it burns a little of everything that moves.

## Sell pressure: where new LUNC comes from

Sell #1, protocol inflation, is **zero** — and this is the single most important fact about Terra Classic's tokenomics. The chain's mint module reports an inflation rate of zero, with a zero floor, a zero ceiling and zero annual issuance. Terra Classic has not created a single new LUNC since 2022. This surprises people, because LUNC is a proof-of-stake chain and proof-of-stake chains normally mint. Terra Classic does not: staking rewards are funded out of transaction fees plus a **20%** slice of the burn tax routed to the oracle pool. That is existing LUNC changing hands, not new supply. Governance reinforced the position in April 2026 by passing a staking framework explicitly built on **no minting**.

Sell #2, vesting unlocks, is **zero**, and structurally so. Terra Classic launched in April 2019 and the original team and investor allocations finished their multi-year vesting years ago. The roughly **6.5 trillion LUNC** created during the May 2022 death spiral was issued straight to the market with no lock at all — the collapse was, in effect, the largest unlock in crypto history, and it already happened. There is no vesting contract, no cliff and no unlock calendar left. Unlock trackers that appear to cover Terra carry schedules for Terra 2.0 and its LUNA token, a different chain entirely; Terra Classic has none.

Sell #3, foundation and unscheduled unlocks, is about **389M LUNC** — the only sell-side line with a number on it. Terra Classic has no company and no foundation, but its DAO community pool is a genuine team-controlled overhang, and voters spent from it twice inside the window: about **379.1M LUNC** approved on **Apr 28 2026** to fund a core Cosmos SDK upgrade, and about **9.9M LUNC** on **Jul 1 2026** for cross-chain routing work. Both were on-chain votes with published amounts and recipients. Sell #4, long-term locked or bankruptcy, is **zero**: the Terraform Labs Chapter 11 estate had distributed **$0** to claim holders as of **Mar 31 2026**, and its stated intent for the LUNC it holds is to burn it rather than sell it.

## Buy pressure: where new LUNC goes

Buy #2, the protocol fee burn, is the mechanism that defines LUNC, and it removes about **5.7B LUNC** over 90 days. Every on-chain transaction pays a **0.5%** burn tax; **80%** of it is destroyed forever and the remaining **20%** funds staking rewards. Added to coins the community sends to the burn wallet by hand, that is the chain's only structural supply sink — and the reason Terra Classic's total supply is a one-way ratchet downward. Cumulatively, **453.15B LUNC** has now been burned since May 2022, about **6.56%** of the original supply.

Buy #5, exchange-led burns, adds roughly **3.7B LUNC** over 90 days. Major exchanges voluntarily destroy the LUNC they collect in trading fees and publish each burn: about **923M** on **May 1 2026**, about **2.2B** on **Jun 1 2026**, and **604M** on **Jul 1 2026**. This sits in its own row rather than under the protocol fee burn because it is a private commercial decision, not a protocol rule — an exchange can stop at any time, and the framework should not dress a voluntary act up as a structural one. The rest of the buy ledger is empty. Buy #1, programmatic buyback, is **zero** — no protocol revenue buys LUNC on the open market. Buy #3, foundation buy, is **zero**, because there is no foundation or treasury operator to do the buying. Buy #4, new long-term lock, is **zero**: about **902.2B LUNC** is bonded, but staking is an always-on mechanism with a 21-day exit, not a new escrow created inside the window.

## Foundation and overhang

Terra Classic has no foundation, so the overhang question is unusual — but it is not empty. The first tracked overhang is the **DAO community pool**, holding about **8.38B LUNC**, up from about **7.97B** at the start of the window. It is refilled continuously by **50%** of all gas fees, so spending from it does not deplete it; every release requires a public vote with a published amount, which makes this the most transparent overhang in the framework. The second is the **Terraform Labs bankruptcy estate**, whose remaining LUNC sits in exchange custody. The estate has paid out nothing, a community vote to force a final burn of those wallets was rejected in November 2025, and so the coins simply sit — neither burned nor distributed.

The third is the gap between the **6.45 trillion** total supply and the **5.53 trillion** circulating figure: roughly **925B LUNC** that the market's supply classification treats as not freely tradable. That bucket is the direct cause of the monitor gap discussed above, and it is the thing to watch most closely, because it is the one number here that can move without any coin being minted. If any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How LUNC compares to other uncapped proof-of-stake chains

On paper LUNC belongs to the uncapped continuous-emission Layer-1 class — the group that includes chains issuing new tokens to stakers every block, forever, with no ceiling. In practice LUNC has quietly left that class. An uncapped chain that mints nothing is not really uncapped in any way that matters: the cap only binds if issuance can approach it, and Terra Classic's issuance is zero. That makes LUNC structurally closer to a **fixed-supply chain with a fee burn** than to its nominal peers — the supply can only fall, never rise, which is the opposite of the class it is usually filed under.

Against fee-burn chains, though, the comparison flatters LUNC less. A burn only matters relative to the float it is burning against. Terra Classic destroys about **9.4B LUNC** a quarter, which sounds enormous until it is set against **5.53 trillion** circulating — **0.17%**. Chains that burn a base fee against a float measured in hundreds of millions can swing net supply by whole percentage points; LUNC cannot, because the 2022 collapse left it with a denominator so large that no realistic burn rate moves it. At the current pace, retiring even a tenth of the supply would take decades. That is the honest structural read, and it is why the burn narrative and the burn arithmetic point in the same direction but at wildly different magnitudes.

The comparison that does matter is with chains carrying a bankruptcy estate — the class where a court, not a protocol, controls the largest overhang. LUNC shares that shape, and like its peers the risk is binary and unscheduled rather than continuous. The difference is that here the estate's stated intent is to burn rather than sell, which if executed would be the single largest deflationary event available to this token — far larger than years of the tax.

## What to watch in the next 90 days

First, the **monthly exchange burns** on **Aug 1 2026**, **Sep 1 2026** and **Oct 1 2026**, each historically between **604M** and **2.2B LUNC**. Second, the **cooling burn rate**: burning tracks trading volume, and the pace has fallen from roughly **105-125M LUNC** a day in April 2026 to about **54M** a day over the last 30 days and about **25M** a day over the last 7. If that trend holds, the next quarter's burn will land below the **9.4B** this read carries, and the net will drift closer to flat. Third, any **governance proposal touching the burn tax rate or the 80/20 burn split** — both are on-chain parameters a single vote can change, in either direction. Fourth, any proposal that would **re-enable the mint module**, which is the one change that would break this entire read; nothing of the sort is currently proposed. Fifth, the **Terraform Labs estate**, where either a burn of its LUNC or a reversal toward distribution would dwarf every other line in this ledger.

## Summary

The MrNasdog Pressure Framework reads Terra Classic at **-0.16% net** supply over 90 days: about **389M LUNC** of community-pool spending against about **9.4B LUNC** burned by the **0.5%** transaction tax and voluntary exchange burns. The structural mechanism is unusual and widely misunderstood — LUNC's mint module is switched off, so despite being an uncapped proof-of-stake chain it issues nothing at all, and its supply can only fall. The key risk is not inflation but the **925B LUNC** sitting outside the circulating figure, including a bankruptcy estate whose coins can be reclassified into the float without a single new token being created — which is exactly what drives the **1.07 percentage point** gap against our monitor. The real ceiling on this asset is arithmetic, not policy: with **5.53 trillion** tokens outstanding, even an aggressive burn removes well under a percent a quarter.

---

*MrNasdog Pressure Framework analysis of LUNC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 16 2026.*
