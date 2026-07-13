---
title: "AVAX Inflation Analysis · July 2026 · The staking mint now outruns a shrunken fee burn"
description: "A MrNasdog Pressure Framework read of Avalanche (AVAX): ~3.4M/90d staking mint plus a 1.67M Foundation cliff against only ~0.11M fee burn. Net +1.15% under a 720M hard cap."
canonical_url: "https://mrnasdog.com/research/avax/inflation"
tags: ["crypto", "avax", "avalanche", "proof-of-stake"]
published: true
---

> Originally published at **[mrnasdog.com/research/avax/inflation](https://mrnasdog.com/research/avax/inflation)** by MrNasdog.

Avalanche is a hard-capped proof-of-stake chain — **720M AVAX** maximum, with **~431.8M circulating**. The protocol mints new AVAX as staking rewards, about **3.4M** over 90 days, and a quarterly **Foundation vesting cliff** adds another **1.67M** on Aug 10 2026. On the other side, every C-Chain fee is burned — but after the ACP-125 base-fee cut, that burn is only about **0.11M** over 90 days, a fraction of the mint. The Pressure Framework reads net supply at **+1.15%**. Our supply monitor reads **+0.031%**, a gap of about **1.1 percentage points** — a circulating-classification effect — so a monitor-gap flag is raised.

## The verdict, in one paragraph

For the 90-day window beginning July 13 2026, the MrNasdog Pressure Framework reads **Avalanche at about +1.15% net supply growth** — roughly **5.07M AVAX** of new supply from staking emission and the Foundation vesting cliff, offset by only about **0.11M** of fee burn. Our supply monitor reads the realized last-90-day change at **+0.031%**, essentially flat, a gap of about **1.1 percentage points**, which **does raise a monitor-gap flag**. The gap is structural, not an error: the monitor's circulating-supply base held AVAX near-flat at ~431.8M because newly-minted staking rewards are classified as staked or non-float and the Foundation cliff lands in custody, while the framework counts the real on-chain mint toward the 720M cap. Both readings agree on direction once you look at total minted supply — Avalanche is inflating. The right label is **structurally inflationary on the staking mint, with a fee burn too small to offset it**.

## Sell pressure: where new AVAX comes from

The dominant sell force is **protocol inflation** — the staking mint — about **3.4M AVAX** over the next 90 days. On Avalanche, all validator income is newly minted: transaction fees are burned rather than paid to validators, so the entire staking reward is fresh supply issued toward the **720M hard cap**. With roughly **201.9M AVAX staked** — a **46.76%** staking ratio — earning about **6.8%** a year, the protocol mints on the order of 3.4M AVAX a quarter. The second sell force is **vesting unlocks**: the Foundation allocation (9.26% of supply, about **66.67M AVAX**) vests on a quarterly schedule of **1.67M AVAX** per cliff, and the next cliff lands **Aug 10 2026**, inside this window.

The other two sell rows are **zero**. Sell #3 — Foundation and unscheduled unlocks — is zero as discretionary market flow: the quarterly Foundation cliff is already counted above and unlocks into custody, and no discretionary Foundation sale was observed on-chain in the window. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court-ordered distribution applies to AVAX.

## Buy pressure: where new AVAX goes

The buy side is thin. Buy #1 — programmatic buyback — is **zero**: Avalanche runs no buyback, because validator income comes from newly minted rewards plus burned fees, not from a treasury buying AVAX on the market. Buy #2 — protocol fee burn — is real but small at about **0.11M AVAX** over 90 days. Every C-Chain base fee, and the priority fee too, is permanently burned under Avalanche's **EIP-1559-style** dynamic fee, but the **ACP-125** upgrade cut the minimum base fee from **25 nAVAX to 1 nAVAX**, so at current activity the network burns only about 1,000 to 1,300 AVAX a day — far below the ~3.4M staking mint (cumulative lifetime burn is about **5.4M AVAX**). Buy #3, a Foundation buy, is **zero** — there is no open-market buying of AVAX — and Buy #4, a new long-term lock, is **zero**, because AVAX staking locks are structural to consensus, not a new lockup event created in the window.

## Foundation and overhang

The team-controlled overhang is the Avalanche Foundation. Its allocation is about **66.67M AVAX** (9.26% of supply), of which roughly **38.34M** is unlocked and about **28.34M** remains on the quarterly vesting schedule that releases **1.67M** per cliff. Separately, about **31.67M AVAX** is minted but not yet circulating — the gap between the ~463.4M total minted and the ~431.8M circulating — held across staking and reserve buckets. The Foundation's cliffs unlock into custody for ecosystem use rather than straight onto the market, which is why the discretionary Sell #3 row is carried at zero. The trigger is simple: if the Foundation's balance falls between refreshes — an on-chain outflow beyond the scheduled cliff — that outflow enters Sell #3 at the next refresh.

## How AVAX compares to other capped proof-of-stake chains

AVAX sits between two structural classes. Like **Bitcoin**, it has a **hard cap** — 720M — so its issuance is bounded and, unlike an uncapped chain such as **Ethereum** or **Solana**, AVAX can never mint beyond that ceiling. But unlike Bitcoin's fixed halving schedule, Avalanche's issuance is a **staking-reward curve**: new AVAX is minted continuously to validators toward the cap, so at ~463.4M minted of 720M there is still years of issuance ahead. That makes AVAX **capped but still meaningfully inflationary** today, closer to a mid-life proof-of-stake chain than to a near-terminal-issuance asset.

The comparison that matters most is the **fee burn**. Avalanche and Ethereum both burn base fees under an EIP-1559 design — and Avalanche burns the priority fee too — so both chains can, in principle, offset issuance with burn during high activity. Ethereum has periodically burned enough to go net deflationary; Avalanche did so during 2025 activity spikes. But after the **ACP-125** base-fee cut, AVAX's burn at current volume is a rounding error against the staking mint, so the offset that makes the mechanism interesting is dormant. AVAX is therefore a **capped chain whose burn is real but currently too small to cancel issuance** — the mint sets the direction until either activity (and burn) rises sharply or issuance decays further toward the cap.

## What to watch in the next 90 days

Watch the **C-Chain burn rate** — it is the only force that can offset the mint, and a sustained rise in network activity (the kind that briefly turned AVAX deflationary in 2025) would close the gap fast. Keep the **Aug 10 2026** Foundation vesting cliff on the calendar — 1.67M AVAX into custody — and watch whether any of it moves on-chain toward exchanges, which would push the Sell #3 row above zero. Watch the **staking ratio**: if more AVAX is staked, the effective network issuance rises; if stakers unstake, it falls. And watch for any **ACP** governance proposal that changes the base-fee floor or the staking-reward curve, either of which would reset the mint-versus-burn balance directly.

## Summary

Avalanche's AVAX is a hard-capped (720M) proof-of-stake token whose supply is still growing: about 5.07M AVAX over 90 days from a 3.4M staking mint plus a 1.67M quarterly Foundation cliff, against only about 0.11M of fee burn — net roughly +1.15%. The defining mechanism is that all validator income is newly minted while fees are burned, and after the ACP-125 base-fee cut the burn is now far too small to cancel the mint. Our monitor reads +0.031%, essentially flat, because its circulating base does not capture the staked, non-float mint or the custody cliff — a structural classification gap, not a data error. The key point is that AVAX is capped but not yet near terminal issuance: until burn rises with activity or issuance decays toward the cap, the staking mint keeps supply growing.

---

*MrNasdog Pressure Framework analysis of AVAX, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 13 2026.*
