---
title: "ICP Inflation Analysis · July 2026 · Mixed flows, supply roughly steady"
description: "A MrNasdog Pressure Framework read of Internet Computer (ICP): ~2.43M / 90D of reward minting vs a ~0.24M cycle burn. Framework +0.40% net; monitor +0.46% (0.06pp gap)."
canonical_url: "https://mrnasdog.com/research/icp/inflation"
tags: ["crypto", "icp", "internet-computer", "compute"]
published: true
---

> Originally published at **[mrnasdog.com/research/icp/inflation](https://mrnasdog.com/research/icp/inflation)** by MrNasdog.

The Internet Computer mints about **2.43M ICP** over 90 days as network rewards — almost all node-provider pay — while the cycle burn destroys only about **0.24M ICP** as users buy compute. The mint outweighs the burn, so the Pressure Framework reads about **+0.40%** net, mildly inflationary. Our supply monitor reads **+0.46%** realized over the same window; the gap of **0.06 percentage points** is inside tolerance, so no data-conflict flag. ICP is an uncapped mint-and-burn token where the mint still wins, but Mission 70 is narrowing the margin.

## The verdict, in one paragraph

For the 90-day window ending July 14 2026, the framework reads **ICP at about +0.40% net** on the last-90-day view and about **+0.32%** looking forward, driven by protocol minting that the cycle burn only partly offsets. Our supply monitor reads the realized last-90-day change at **+0.46%**, against the framework's **+0.40%** for the same window — a gap of just **0.06 percentage points**, well under the half-point tolerance, so **no monitor-gap chip ships**. The small residual is the NNS voting-reward maturity that is minted but not captured in the node-provider figure. ICP is **mildly inflationary on an uncapped supply** — a mint-and-burn token where issuance still exceeds destruction, but by a shrinking amount as the Mission 70 reforms take effect.

## Sell pressure: where new ICP comes from

Sell #1 — protocol inflation — is the whole sell story, at about **2.43M ICP** minted over the last 90 days. The Internet Computer mints new ICP as network rewards through two channels: pay to node providers who run the physical machines, and voting rewards to neurons that stake ICP and vote in the Network Nervous System. Node-provider pay is the dominant realized mint — three monthly distributions inside the window added roughly **2.43M ICP** — while most voting rewards accrue as neuron maturity that compounds rather than being minted immediately, so their realized minting is small. There is **no supply cap**; ICP is uncapped by design. Governance has already cut the node-provider reward under Mission 70, so the forward view runs closer to **2.05M** over the next 90 days.

Sell #2 — vesting unlocks — is **zero** as a source of new supply: the 2021 genesis allocations were minted at launch and are already counted in the 554.41M circulating figure, and while seed, team and early-contributor tokens dissolve out of eight-year neurons, that is already-issued ICP, not new coins. Sell #3 — Foundation and unscheduled unlocks — is also zero as a flow; the DFINITY Foundation endowment, team neurons and the NNS community-fund maturity are governance-controlled balances with no dated release. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court distribution applies to ICP, and staked ICP in neurons is already part of total supply rather than a pending cliff.

## Buy pressure: where new ICP goes

The buy ledger has exactly one live line, and it is not a buyback. Buy #1 — programmatic buyback — is **zero**: ICP network rewards are paid from new issuance, not by purchasing ICP back from the market. Buy #2 — protocol fee burn — is the real offset, at about **0.24M ICP** destroyed over the last 90 days. ICP is burned whenever it is converted into cycles, the units that pay for on-chain computation and storage; the more the network is used, the more ICP is burned. But at current usage the burn is far smaller than the mint, so it only softens the dilution rather than reversing it. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no discretionary open-market buying and no new escrow announced in the window. With the burn at roughly a tenth of the mint, ICP stays a net issuer.

## Foundation and overhang

ICP has no classic unlock cliff — total supply equals circulating supply, and genesis vesting resolves through dissolving neurons rather than a dated release. The team-controlled balances worth naming are the **DFINITY Foundation** endowment and team neurons, and the NNS community-fund maturity of about **5.57M ICP**, which the governance system accrues and can deploy only through a passing on-chain proposal. None of these is a stockpile waiting to dump: deployments are vote-gated and infrequent. The framework books no discretionary release beyond protocol minting and re-checks the on-chain mint, burn rate and community-fund balance on a roughly bi-weekly walk; if any of these governance-controlled balances falls between refreshes, that outflow enters Sell #3 at the next refresh.

## How ICP compares to other uncapped mint-and-burn chains

ICP belongs to the class of **uncapped chains that both mint and burn** — closer to Ethereum's issuance-versus-EIP-1559-burn balance than to a hard-capped, halving coin like Bitcoin. Unlike Bitcoin, ICP has no ceiling and no halving schedule; unlike Cosmos, which mints staking rewards with no burn at all, ICP does destroy ICP through its cycle burn. The distinguishing feature is direction: at today's usage the ICP mint clearly outruns the burn, so the chain sits on the inflationary side of the mint-and-burn family, whereas Ethereum can flip net-deflationary when block space is in heavy demand.

The number that decides ICP's side of the ledger is network usage, because usage is what drives the cycle burn. The Mission 70 program, approved by the Network Nervous System on April 7 2026, is engineered to move both levers at once: cut minting on the supply side and raise the ICP burn on the demand side by increasing compute prices. DFINITY's stated aim is to lower raw annual inflation from about **9.72%** at the start of 2026 toward roughly **2.92%** by year-end. For an inflation lens specifically, ICP today reads as mildly inflationary and cooling — the mint still wins, but the gap between mint and burn is the smallest it has been.

## What to watch in the next 90 days

Watch the monthly node-provider reward, the single largest mint line — each further Mission 70 step lowers it, and a lower figure pulls Sell #1 down directly. Watch the cycle burn rate: rising network usage or higher compute prices would lift the burn toward the mint and could push ICP toward flat or even net-deflationary. Watch the Mission 70 rollout for any additional ratified parameter change through 2026, since the program is phased rather than a single switch. Watch the NNS community-fund balance of about **5.57M ICP**, the main governance-controlled pool that could reach the market through a spend vote. And watch total supply itself, the clean on-chain check on whether mint is still beating burn.

## Summary

ICP is an uncapped mint-and-burn token: the Internet Computer mints about 2.43M ICP over 90 days as node-provider and staking rewards, while the cycle burn destroys only about 0.24M ICP as users pay for computation, leaving the framework at about +0.40% net. Our supply monitor reads +0.46% realized, a gap of just 0.06 points, so the two agree and no flag is raised. The structural mechanism is issuance that exceeds a real but smaller burn, and the key risk to the reading is usage: a burn that grows faster than the mint would flip ICP toward flat. With no supply cap, the ceiling is set by governance rather than code — and Mission 70 is deliberately steering minting down and the burn up through the rest of 2026.

---

*MrNasdog Pressure Framework analysis of Internet Computer (ICP), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 14 2026.*
