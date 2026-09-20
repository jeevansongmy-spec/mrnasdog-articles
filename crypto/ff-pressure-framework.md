---
title:         "FF Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "FF supply grows 7.17% over 90 days as locked treasuries release 225M tokens. Read the Pressure Framework ledger, burn checks and the Sep 29 team cliff."
canonical_url: "https://mrnasdog.com/research/ff/inflation"
tags:          ["crypto", "ff", "falconfinance", "defi"]
published:     true
---

Originally published at [FF Inflation Analysis · September 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/ff/inflation).

# FF Inflation Analysis · September 2026 · Supply growing · projected to keep growing

Falcon Finance supply is growing and is projected to keep growing. The Pressure Framework records **225.0M FF** released from locked treasuries and **0** verified removals, giving **+7.17%** over the last 90 days and **+7.17%** projected forward, while the monitor reads **+9.39%**. Falcon Finance has never minted a single FF beyond its original **10,000.0M FF**; the dilution comes entirely from an unlock schedule that still has **6,860.0M FF** to deliver.

## The verdict, in one paragraph

On the **3,140.0M FF** circulating denominator, the Falcon Finance vesting schedule produces **+7.17%** net supply pressure over 90 days, and the same rate is projected forward. The monitor reports **+9.39%**, leaving a **2.23 percentage-point** difference and a warning on the overview. A full walk of the FF token contract, the four locked treasury wallets, the unlock aggregators, the Falcon Finance announcement feed and the governance surface found no additional release. The difference is fully explained: **40.8M FF** of it is catch-up the monitor was still carrying from the **Jun 3 2026** release, **4.3M FF** is price-derived rounding, and the rest is the monitor dividing by the smaller supply at the start of the window. FF is a non-minting token that is inflationary by its own unlock calendar rather than by issuance.

## Sell pressure: where new FF comes from

Protocol inflation is **0**. The entire FF supply — **10,000.0M FF** — was issued in one transaction at launch in September 2025 and the token has created nothing since. The supply field read **10,000.0M FF** at both ends of the window, and the field is live, writable storage rather than a number baked into the contract code, so that flat reading is a real measurement and not an artefact. Falcon Finance does not fund staking rewards by minting FF; the sFF staking product pays in the protocol's synthetic dollar or in FF the treasury already holds.

Vesting unlocks contribute **225.0M FF**, and they are the whole of the sell side. The Falcon Finance ecosystem treasury released **75.0M FF** a month in three transfers, on **Jul 6 2026**, **Aug 5 2026** and **Sep 2 2026**. Each of those is a genuine crossing: the treasury sits outside the classified float and the receiving wallet sits inside it, so the coins are counted once, at the moment they cross. The treasury's own balance fell from **2,475.0M FF** to **2,250.0M FF**, matching the transfers to the token. An independently published unlock model puts the same stream at **77.14M FF** a month, within three percent of the measured figure.

Foundation and unscheduled unlocks contribute **0**. The Falcon Finance foundation treasury, the core team allocation and the investor allocation all sit in separate multisig wallets outside the float, and all three read exactly the same balance at both ends of the window — **2,160.0M FF**, **2,000.0M FF** and **450.0M FF**. The team and investor wallets have never moved a single token since they were funded at launch. Long-term locked or bankruptcy releases are also **0**: there is no estate, trustee or court-directed distribution anywhere in the FF cap table.

## Buy pressure: where new FF goes

Programmatic buyback is **0**. Falcon Finance publishes a policy under which a fifth of platform fees may be used to buy FF on the open market and burn it, or be paid to sFF stakers instead. That policy is real, but nothing in this window shows it removing FF from the float: no treasury wallet received tokens, no destruction was recorded, and the policy itself allows the protocol to route the same fees to stakers rather than to a burn.

Protocol fee burn is **0**, and it was verified on both surfaces because either one alone can be misleading. The unspendable address held **0.1 FF** at the start of the window and **0.1 FF** at the end — dust from launch, never added to. Total supply held **10,000.0M FF** at both ends. A buyback that burns by transfer would have moved the first surface; one that burns by reducing supply would have moved the second. Neither moved, so nothing was destroyed. Foundation buying is **0** for the same reason: the foundation wallet received nothing. New long-term lock is **0** — staked FF sits in contracts far smaller than the non-circulating bucket and already inside the classified float, so staking rearranges FF without removing any.

## Foundation and overhang

Four wallets hold everything Falcon Finance has not yet released, and together they hold **6,860.0M FF** — exactly the difference between the **10,000.0M FF** total and the **3,140.0M FF** float. That exact match is what makes this ledger measurable: the boundary between locked and circulating is not an estimate, it is four readable balances. The ecosystem treasury holds **2,250.0M FF** and is the only one currently paying out, at **75.0M FF** a month. The foundation treasury holds **2,160.0M FF**, the core team allocation **2,000.0M FF** and the investor allocation **450.0M FF**.

The team and investor wallets carry the single largest dated risk in this page. Falcon Finance applied a one-year cliff to both, and that cliff falls on **Sep 29 2026**, inside the forecast window. Neither wallet has released anything, and Falcon Finance has not published the size of the first post-cliff release, so the framework books it at **0** and carries it as a watched overhang rather than inventing a number. All four wallets are readable on chain and are refreshed at every rebuild. If any of these balances falls between refreshes, the outflow enters the Foundation row at the next refresh. No buyback accumulation wallet and no bankruptcy residual exist.

## How FF compares to other collateral-protocol tokens

Falcon Finance belongs to a class of protocols whose governance token is deliberately separated from the product. The synthetic dollar USDf and its staked form are collateral instruments with their own supply, and none of that supply touches this ledger. FF is only the governance and fee-share token, and its supply behaves like a venture cap table rather than like a monetary asset. That is the opposite of a fee-burn token such as an EIP-1559 chain's native unit, where usage mechanically destroys supply; on FF, usage only creates a discretionary buyback the protocol may choose not to perform.

Against a halving-model coin with a hard cap, FF looks superficially similar — a fixed **10,000.0M FF** ceiling, no minting, no issuance curve. The difference is that a halving chain's float is already most of its cap, while only **31.4%** of FF is circulating. A fixed total tells a holder nothing about dilution when two thirds of that total is still sitting in four wallets with a release calendar running to 2029. Against an exchange token that runs a quarterly buyback and burn, FF has the policy written down but not the executed burns: the comparison the framework makes is between a stated mechanism and an observed one, and only the observed one changes a ledger.

Among tokens launched in the same 2025 cohort with one-year cliffs, FF is now at the point in its life where the cliff arrives. That is the structural event that separates tokens whose float grows smoothly from tokens whose float steps. FF's float has grown smoothly so far, at roughly **75.0M FF** a month; whether it continues to is decided on **Sep 29 2026**.

## What to watch in the next 90 days

The one date that matters is **Sep 29 2026**, when the one-year cliff on the **2,000.0M FF** core team allocation and the **450.0M FF** investor allocation expires; watch both wallets for their first outflow and for any Falcon Finance disclosure of the post-cliff release size. Second, check whether the ecosystem treasury keeps paying **75.0M FF** in early October, early November and early December 2026, or changes its pattern as it did on **Jun 3 2026** when it pushed out **523.0M FF** in one transfer. Third, watch the unspendable address for its first real increase above **0.1 FF**, which would be the first evidence that the buyback-and-burn policy has actually executed. Fourth, watch total supply independently for any reduction below **10,000.0M FF**. Fifth, watch for the first FF governance vote with a supply consequence — the FF Foundation currently administers unlocks without a public vote portal, so a change in that arrangement would itself be material.

## Summary

The Pressure Framework reads Falcon Finance at **+7.17%** over the trailing 90 days and **+7.17%** projected forward. FF creates no new tokens — the supply has read **10,000.0M FF** since launch — but its locked treasuries release **75.0M FF** a month into the float while the stated buyback and burn has destroyed nothing measurable. The principal risk is the **6,860.0M FF** still locked, and specifically the team and investor cliff on **Sep 29 2026**, whose size Falcon Finance has not published. The monitor difference stays visible and is fully explained by its base and by catch-up from the **Jun 3 2026** release.

MrNasdog Pressure Framework analysis of FF, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 20 2026.
