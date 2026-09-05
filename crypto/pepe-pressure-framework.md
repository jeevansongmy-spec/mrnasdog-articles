---
title: "PEPE Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description: "A Pressure Framework read of Pepe (PEPE): no mint function in the bytecode, an empty owner slot, nothing vesting, and a 129.12M / 90D holder burn on a 420.69T float. Net 0.00%."
canonical_url: "https://mrnasdog.com/research/pepe/inflation"
tags: ["crypto", "pepe", "memecoin", "ethereum"]
published: true
---

> Originally published at **[mrnasdog.com/research/pepe/inflation](https://mrnasdog.com/research/pepe/inflation)** by MrNasdog.

Pepe cannot issue another coin — the deployed contract carries no mint function and its owner address reads empty — so all four sell rows in the Pressure Framework ledger are **0**. Against that, holders destroyed **129.12M PEPE** over the 90 days to **Sep 5 2026**, which is **0.00003%** of a **420.69 trillion** supply and worth roughly **$452**. Net 90-day supply pressure is **0.00%**. PEPE is not a deflationary token; it is a frozen one, and the burn is far too small to change that.

## The verdict, in one paragraph

The Pressure Framework reads PEPE at **0.00%** net supply pressure over the last 90 days and projects **0.00%** over the next 90. Sell pressure totals **0** PEPE, because no mechanism exists that could add one: there is no protocol inflation, no vesting unlock, no foundation release and no bankruptcy estate. Buy pressure totals **129.12M PEPE**, all of it voluntary holder burning. The internal inflation monitor independently reads **-0.0083%** for the same window, a gap of **0.008** percentage points against the framework's **-0.00003%** — comfortably inside tolerance, so no data-conflict warning ships on the overview page. Both readings say the same thing in different decimal places. The right label for PEPE is a **frozen supply**: not shrinking, not growing, structurally incapable of either at any scale a holder would notice.

## Sell pressure: where new PEPE comes from

Nowhere, and the reason is in the bytecode rather than in the marketing. Protocol inflation is **0** because the deployed PEPE contract on Ethereum contains no mint entrypoint at all — the standard mint and burn-from selectors are simply absent from its **4,517** bytes of code — and its owner address returns empty at both ends of the 90-day window, so the owner-only functions that do exist can never be called by anyone again. That is the difference between **cannot mint** and **has not minted**, and PEPE is the former.

Vesting unlocks are **0** because Pepe never had a vesting schedule to run down. The entire **420.69 trillion** supply was created in one transaction at launch in 2023 and distributed the same day: **93.10%** into a Uniswap pool whose liquidity receipt was destroyed, and **6.90%** — exactly **29.03 trillion** PEPE — into a launch multisig. Those two transfers sum to the genesis mint to the unit, with nothing held back. The public unlock calendar for PEPE shows **100.00%** unlocked with no event scheduled in any month through **Dec 2026**.

Foundation and unscheduled unlocks are **0** because every wallet that primary evidence ties to the Pepe launch holds nothing. The launch multisig that received the **6.90%** — traced this quarter directly from the genesis transaction rather than inferred from balance size — reads **0 PEPE** at both ends of the window, and so do the two other addresses associated with the 2023 launch and the 2023 community burn. Long-term locked or bankruptcy supply is **0**: Pepe was never custodied by a failed exchange or lender, so there is no creditor distribution queued behind it.

## Buy pressure: where new PEPE goes

Programmatic buyback is **0**. There is no treasury, no revenue stream and no operating entity behind PEPE, so there is nothing to fund a buyback and no contract that could execute one. Protocol fee burn is also **0**, and structurally so: the project's stated position is that PEPE charges no tax to transfer, the deployed code agrees, and with the owner address empty and no upgrade path there is no way to introduce a fee later. Foundation buying is **0** for the same reason the foundation sell row is — there is no foundation. New long-term locks are **0**; PEPE pays nothing for being held still, so no staking contract or vault removed any from circulation.

The one live mechanism is holder burning, carried as a separate ledger row rather than folded into the fee-burn line it does not belong to. Over the window it removed **129.12M PEPE**, and it was measured on two independent surfaces read at both window ends, because either one alone would have given a wrong answer. The unspendable dead address took in **129,118,743** PEPE while the token's own reported supply barely moved; the contract's public destroy function separately removed another **907** PEPE from that reported supply without touching the dead address. Those are genuinely two different routes — one can fire without the other — so both count, and together they come to **129,119,650** PEPE. It is a real, measured flow, and it is also **0.00003%** of the supply, which is why the net reading is flat rather than negative.

## Foundation and overhang

There is no foundation treasury to watch, and this quarter that claim was tested rather than assumed. The launch multisig at the end of the genesis transfer holds **0 PEPE** at both window ends, confirmed against three independent chain endpoints that agreed on every value. The Safe contract publicly associated with Pepe exchange listings holds **0**, and the address that executed the 2023 community burn holds **0**. A widely repeated third-party summary claiming the project multisig still holds around **2.12 trillion** PEPE was checked against the chain and does not survive it: the launch multisig is empty.

What does exist is two unattributed Safe contracts holding **2.95 trillion** and **2.12 trillion** PEPE respectively — **5.08 trillion** between them, or about **1.21%** of supply. Both are byte-identical at both ends of the window; neither moved a single coin all quarter. Their on-chain signer sets were read and share no address with the launch multisig's, and no Pepe disclosure claims either one, so they are surfaced and watched rather than booked as team-controlled supply. Both carry a value of **0** in the ledger, because holding coins is not the same as releasing them. If either balance falls between refreshes, the outflow enters the foundation and unscheduled-unlocks row at the next refresh.

## How PEPE compares to other fixed-supply memecoins

The memecoin class splits on one mechanical question: can anyone still create supply? Many memecoins on Solana and on newer launchpads keep a mint authority alive, a creator allocation on a vesting cliff, or a treasury that funds marketing by selling into the market — all of which show up as real sell rows. PEPE has none of those. Its supply question was settled permanently in a single 2023 transaction, and the framework can verify that from the contract's own code rather than from a promise. On the sell side PEPE is structurally as clean as an asset gets.

Where it differs from the deflationary memecoins it is often grouped with is the buy side. A token like SHIB burns through chain activity that produces a fee stream, and exchange tokens with quarterly buybacks destroy a fixed share of real revenue — those mechanisms scale with usage and can produce a genuinely shrinking supply. PEPE has no fee, no revenue and no buyback, so its only removal channel is holders choosing to destroy their own coins for nothing in return. That channel is voluntary, unfunded and tiny: **$452** worth in 90 days against a **$1.47 billion** market cap. A cumulative burn programme in the hundreds of millions of dollars is still repeated in price commentary, and the measured burn address says it has not executed.

Compared with a hard-capped proof-of-work chain like Bitcoin, PEPE is stricter on paper and weaker in mechanism. Bitcoin still issues new supply on a fixed halving schedule, so it is mildly inflationary by design; PEPE issues nothing at all. But Bitcoin's scarcity is enforced by an economically defended consensus, while PEPE's is enforced by an immutable contract nobody controls. Both are credible; only one of them is doing anything. The honest framing for PEPE is that supply is a solved and therefore uninteresting variable — the asset's outcome is decided entirely on the demand side.

## What to watch in the next 90 days

Four things could change this reading, and none of them is a supply mechanism turning on. First, the two static Safe contracts holding **5.08 trillion** PEPE between them: any outflow from either is the single largest available supply event on this ledger, and both are re-read at every refresh. Second, the burn rate itself — the row is carried forward at the measured rate, so a sustained increase of two orders of magnitude would be needed before the net reading moves off **0.00%**. Third, the spot PEPE ETF registration filed with the SEC on **Apr 8 2026**, whose review window runs to **December 2026**; approval would change access and demand, and would not change supply by a single coin. Fourth, any credible execution of the long-promised large burn programme, which the dead-address balance will show the moment it happens and has not shown yet.

There is deliberately no upcoming-events strip on the PEPE overview page. That is a measurement, not an omission: the unlock calendar publishes no event through **Dec 2026**, the contract has no scheduled burn, and there is no governance surface on which a supply decision could be taken.

## Summary

The MrNasdog Pressure Framework reads PEPE at **0.00%** net supply pressure for both the trailing and the forward 90-day window, and scores its Inflation metric a **3 out of 5** — flat, not deflationary. The structural mechanism is total supply finality: PEPE's Ethereum contract has no mint function in its deployed code and no owner able to add one, so all four sell rows are permanently **0**, and the only removal channel is voluntary holder burning that took out **129.12M PEPE**, or **0.00003%** of supply, in 90 days. The key risk is not dilution but attribution: **5.08 trillion** PEPE sits motionless in two unattributed Safe contracts, and an outflow from either would be the first real sell-side event this ledger has recorded. The ceiling is fixed and known — **420,690,000,000,000** PEPE, minted once, never to be added to.

---

*MrNasdog Pressure Framework analysis of PEPE, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 5 2026.*
