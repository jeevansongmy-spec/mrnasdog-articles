---
title: "ORCA Inflation Analysis · August 2026 · Supply shrinking, projected to keep shrinking"
description: "A MrNasdog Pressure Framework read of Orca (ORCA): zero issuance, vesting done since 2024, a ~0.43M/90D fee-funded buyback into the staking vault. Framework −0.7% net; monitor +0.20%; forward −0.5%."
canonical_url: "https://mrnasdog.com/research/orca/inflation"
tags: ["crypto", "orca", "solana", "dex"]
published: true
---

> Originally published at **[mrnasdog.com/research/orca/inflation](https://mrnasdog.com/research/orca/inflation)** by MrNasdog.

Orca is one of the rare tokens in our coverage where the whole supply story sits on the buy side. ORCA is fixed at about **75M** total, fully unlocked since 2024, with no mint and no vesting, so every sell row is **zero**. The only live mechanism is a buyback: **40% of Orca's protocol fees** automatically buy ORCA on the open market, roughly **0.43M ORCA** over the last 90 days. Against a circulating base of **60.8M**, that is **−0.7% net** — mildly deflationary — even though our supply monitor reads a near-flat **+0.20%**, a **0.9 percentage-point** gap the buyback itself explains.

## The verdict, in one paragraph

For the 90-day window ending **Aug 3 2026**, the MrNasdog Pressure Framework reads **ORCA at −0.7% net**. Sell pressure is **zero**, buy pressure is **0.43M ORCA**, against a circulating base of **60.8M ORCA**. Our supply monitor reads the realised change at **+0.20%**, a gap of **0.9 percentage points** — over tolerance, so a monitor-gap flag ships with this page. The gap is not an error: the buyback moves ORCA off the open market into the on-chain **xORCA staking vault**, which the monitor still counts as circulating, so the deflation the framework books does not show up in the monitored supply. The forward reading is also negative at **−0.5%** as protocol fees soften. ORCA is best characterised as a **fixed-supply exchange token that is deflationary by structural buyback, not by burn**.

## Sell pressure: where new ORCA comes from

There is none, and that is the honest headline. Sell #1, protocol inflation, is **zero** because Orca mints no ORCA. Orca is the governance token of a concentrated-liquidity exchange built on Solana; it is not a chain's native coin, so there is no block reward, no staking emission and no liquidity-mining curve. On-chain, the token's total supply held flat at **74,999,549** across the window — no issuance of any kind adds to the float.

Sell #2, vesting unlocks, is **zero** because every ORCA allocation — the token treasury, the team, the private sale, liquidity providers and trader rewards — finished vesting back in **2024**; nothing remains on a release schedule, so no locked supply cliffs into the market during the window.

Sell #3, Foundation and unscheduled unlocks, is also **zero** in flow, though the scope matters. About **14M ORCA** sits outside circulation — the difference between the **~75M** total and the **60.8M** circulating — held mostly by the Orca DAO and foundation. But the DAO's spendable treasury is denominated in **SOL and USDC**, not ORCA (its main treasury wallet holds zero ORCA), and no ORCA left a team wallet for the open market this quarter. Sell #4, long-term locked or bankruptcy, is **zero**: Orca has no estate, no trustee and no court-ordered distribution, and no long-term lock-up unwinds on a schedule. With no emission, no unlocks, no treasury sale and no estate, the sell side of the ledger is empty.

## Buy pressure: where new ORCA goes

Buy #1, programmatic buyback, is the entire story at **0.43M ORCA**. Orca directs **40% of its protocol fee revenue** — a rate raised from 20% on **Jan 13 2026** — into an automatic open-market purchase of ORCA. Over the 90 days the protocol earned about **$1.14M** in revenue, so roughly **$457K**, or about **0.43M ORCA**, was bought and added to the **xORCA staking vault**. On-chain, that vault now holds about **7.6M ORCA** backing **4.78M xORCA**, and because buyback ORCA is added without minting new xORCA, each xORCA steadily redeems for more ORCA. The forward column eases to about **0.32M** as recent fee revenue runs below the trailing window.

The other three buy rows are **zero**. Buy #2, protocol fee burn, is zero because no ORCA was burned in the window — the on-chain supply held flat, and although governance can burn repurchased ORCA, the default is to add it to the vault rather than destroy it. (A one-off 25% supply burn happened back in April 2025, long before this window.) Buy #3, Foundation buy, is zero because there is no discretionary purchase beyond the programmatic buyback; the DAO's roughly **55,000 SOL** treasury was staked to a validator for yield, not spent on ORCA, and no other open-market accumulation was disclosed. Buy #4, new long-term lock, is zero to avoid double-counting: xORCA staking does lock ORCA behind a 7-day cooldown, but the buyback already flows into that same vault and is counted in Buy #1.

## Foundation and overhang

The team-controlled overhang is modest and, for now, inert. Roughly **14M ORCA** sits outside circulation, dominated by the DAO and foundation treasury allocation left over from the original token distribution. The distinguishing feature is that Orca's working treasury does not hold ORCA to sell — it holds **SOL and USDC**, which is what funds the buyback and the validator stake, so the DAO is a net **buyer** of ORCA rather than a seller. The buyback accumulation itself is the growing pool to watch: bought-back ORCA lands in the on-chain xORCA vault, currently about **7.6M ORCA**, and is re-read every rebuild. If any team-controlled balance falls between refreshes — a treasury ORCA sale, or a governance decision to redistribute vault ORCA — the outflow enters Sell #3 at the next refresh.

## How ORCA compares to other DEX and buyback tokens

The comparison that matters is buyback-and-hold versus buyback-and-burn. Some exchange and DEX tokens route revenue into buybacks that are then **burned**, permanently cutting the on-chain supply — those show up as deflationary in any supply monitor because the total supply actually falls. Orca does something subtler: its buyback ORCA is added to the **xORCA vault** to back stakers, not burned, so the on-chain total stays fixed at **75M**. The framework still reads this as deflationary because the ORCA has left the tradable float, but a supply-only monitor that counts the vault as circulating does not — which is exactly the **0.9 percentage-point** gap on this page. Both approaches tighten the float today; only a burn is irreversible, and that distinction shows up in the overhang list, where the vault's ORCA is tracked rather than written off.

The second comparison is fixed-supply DEX tokens versus emission-driven ones. Many AMM and lending tokens still mint fresh supply through liquidity-mining rewards, so their float grows with usage and their inflation never truly ends. Orca retired emissions years ago and burned a quarter of its cap, so it has no issuance to fight — its net reading is set entirely by how much fee revenue the DEX earns and feeds back into the buyback. That makes ORCA's supply direction a clean function of protocol usage: more volume means more fees, more buyback and more deflation, with nothing on the sell side to offset it. A quiet quarter on Solana shrinks the bid automatically, but it can never turn the sell side positive.

## What to watch in the next 90 days

First, **Orca protocol fee revenue**: the buyback is 40% of it, so the single biggest driver of the reading is whether DEX volume holds — revenue softened from the trailing window, which is why the forward buyback eases to **0.32M**. Second, the **xORCA vault balance**, currently about **7.6M ORCA**, whose growth is the on-chain proof of the realised buyback. Third, any governance vote to change the buyback allocation again — it moved from 20% to 40% in January 2026, and a further change would re-rate the whole ledger. Fourth, whether the DAO decides to **burn** vault ORCA rather than hold it, which would convert the framework's float-based deflation into a supply cut the monitor also sees. Fifth, any deployment of the authorised **55,000 SOL** treasury buyback, which would add to Buy #1 on top of the fee-funded flow.

## Summary

Orca is a fixed-supply, fully-unlocked Solana DEX token with no mint, no vesting and no estate, so its entire supply story is a buyback: **40% of protocol fees** bought about **0.43M ORCA** over 90 days into the xORCA staking vault, against zero sell pressure and a circulating base of **60.8M**. That leaves the framework at **−0.7% net** — mildly deflationary — while our supply monitor reads a near-flat **+0.20%**, a **0.9-point** gap that exists only because the buyback holds ORCA in a vault the monitor still counts as circulating. The forward reading stays negative at **−0.5%** as fees ease. The key structural fact is that ORCA is deflationary by revenue, not by burn; the key risk is that the deflation is only as strong as Orca's fee income; and the key upside is that a governance vote to burn the vault would make the shrink permanent and visible everywhere.

---

*MrNasdog Pressure Framework analysis of Orca (ORCA), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated August 3 2026.*
