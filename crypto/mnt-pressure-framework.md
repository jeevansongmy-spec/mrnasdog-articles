---
title:         "MNT Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description:   "Mantle reads 0.00% net: no issuance, no vesting since 2023, no fee burn, and a 2,917.02M MNT treasury that did not move a single wei across the quarter."
canonical_url: "https://mrnasdog.com/research/mnt/inflation"
tags:          ["crypto", "mnt", "mantle", "ethereum"]
published:     true
---

*Originally published at [mrnasdog.com/research/mnt/inflation](https://mrnasdog.com/research/mnt/inflation).*

# MNT Inflation Analysis · September 2026 · Mixed flows, supply roughly steady

Mantle created no new MNT in the last 90 days, destroyed none, and released none from the Mantle Treasury, so the MrNasdog Pressure Framework reads MNT at **0.00% net** on a circulating base of **3,302,294,382 MNT**. Total supply held at **6,219,316,794.89 MNT** at both ends of the window and the token's governed mint cap parameter reads **zero** — the mint exists, it is simply switched off. Everything still outside the tradable float sits in the Mantle Treasury, **2,917,022,412 MNT** across eleven published wallets on two networks, and every one of them held an identical balance on **Jun 4 2026** and on **Sep 2 2026**. Against a supply-monitor reading of **+0.03%**, the gap is **0.03 percentage points** and the framework ships no data-conflict flag.

## The verdict, in one paragraph

Over the last 90 days the MrNasdog Pressure Framework reads Mantle at **0.00% net**: a sell ledger of **0 MNT** against a buy ledger of **0 MNT** on a circulating base of **3,302,294,382 MNT**. The supply monitor reads the same window at **+0.03%** — a gap of **0.03 percentage points**, far inside tolerance, so no data-conflict flag is raised. That small positive is not issuance; it is the arithmetic noise of deriving supply from market capitalisation divided by price, around a published circulating figure that did not change by a single wei. Mantle is a **frozen float with a governance-sized overhang**: MNT has no emission, no vesting and no burn, so the only mechanism on the whole chain that can move the tradable supply of MNT is a Mantle DAO vote releasing treasury MNT — and no vote was held inside the window.

## Sell pressure: where new MNT comes from

Sell #1 — protocol inflation — is **zero**, and the contract settles it rather than the marketing. Mantle is an Ethereum layer-2 with a sequencer, not a proof-of-stake chain with validators, so there is no block subsidy, no staking emission and no fee-sharing mint paying out MNT. Total supply read **6,219,316,794.889999 MNT** at both window ends. The interesting part is what sits behind that flat number: the MNT token is an upgradeable proxy, and its implementation genuinely carries a mint function guarded by a governed cap. Read live at both ends, the cap numerator is **0** against a denominator of **10,000**, so the maximum mintable amount computes to zero and any mint call reverts. The time gate is already open — it elapsed in **Jun 2024** — and the owning account is a live multisig, not the null address. Mantle's mint is switched off, not renounced, which is why this page awards no permanence to MNT's supply finality and why the widely quoted 6.22B "max supply" is an aggregator convention rather than a protocol-encoded cap.

Sell #2 — vesting unlocks — is **zero** because Mantle has nothing left to unlock. The MNT release calendar completed in **2023** and the unlock trackers read MNT as fully unlocked with no remaining vests and no future dates. There is no cliff inside the 90-day window because there are no cliffs at all. This is the structural feature that separates Mantle from most large layer-2 tokens: MNT's dilution schedule is finished, so the token carries no calendar risk whatsoever.

Sell #3 — foundation and unscheduled unlocks — is **zero**, and this is the row that carries all of MNT's real supply risk. The Mantle Treasury holds **2,917,022,412.35 MNT**, roughly **47%** of every MNT that exists and about **88%** of the tradable float again, making it one of the largest single-protocol treasuries in crypto. Mantle publishes all eleven of its treasury addresses, and each one was read directly on its own chain at both window ends: the main Ethereum safe at **2,900,022,409.21 MNT**, a second Ethereum safe at **10,000,000 MNT**, four Mantle-network wallets summing to **7,000,003.15 MNT**, and five published wallets holding nothing. Every balance was identical to the last decimal on **Jun 4 2026** and **Sep 2 2026**, so the treasury delta across the quarter is exactly **zero**. A treasury this large is capacity, not a plan — it releases only on a passing Budget Proposal, and Mantle's governance recorded no proposal of any kind inside the window.

Sell #4 — long-term locked or bankruptcy — is **zero**. No bankruptcy estate holds MNT and no court-supervised trustee distributes it on a schedule, so nothing arrives from that side.

## Buy pressure: where new MNT goes

Buy #1 — programmatic buyback — is **zero**. Mantle operates no buyback contract and publishes no buyback programme. A phase-based proposal to burn **3–8%** of the treasury's MNT over twelve to twenty-four months has been sitting in the pre-proposal discussion stage since **Feb 25 2026** and has never advanced to a temperature check, a formal proposal or a vote. It is worth noting what would happen if it ever did: because the Mantle Treasury sits outside the circulating count by Mantle's own definition, destroying treasury MNT would genuinely shrink the tradable float rather than merely relabel it. The mechanism would be real. It simply has not been enacted.

Buy #2 — protocol fee burn — is **zero**, and Mantle is precisely the shape of chain where that answer is easy to get wrong. MNT is the gas token of the Mantle network, so every transaction on the chain consumes MNT, which invites the assumption of a fee burn. There is none. Both surfaces were read on both chains: total supply never moved off **6,219,316,794.89 MNT**, the Ethereum burn address took in exactly **1 MNT** across the whole quarter, and the Mantle-side null addresses held **65.62 MNT** and **8,394,908.88 MNT** unchanged at both ends. The gas actually goes into three protocol fee accounts, which rose together from **160,155.07 MNT** to **201,186.88 MNT**, a collection of **41,031.81 MNT** over the window. Those coins were moved, not destroyed — they remain inside the counted float and are tracked as an overhang, not booked as a buy.

Buy #3 — foundation buy — is **zero**. Mantle disclosed no open-market MNT accumulation during the window, and no treasury wallet's MNT balance rose.

Buy #4 — new long-term lock — is **zero**, and it moved the wrong way. Mantle's opt-in Rewards Station lets holders lock MNT voluntarily; those two lock contracts fell from **7,163,730.48 MNT** to **7,073,921.59 MNT**, a net release of **89,808.88 MNT**. The one balance that grew is not a lock at all: a Chainlink bridge pool went from **0** to **5,545,326 MNT** after Mantle migrated its Super Portal in **Jul 2026** and extended it in **Aug 2026**. That MNT is collateral backing MNT issued on other networks. Reading it as a lock would have manufactured a buy row out of a plumbing change.

## Foundation and overhang

The Mantle Treasury is the whole overhang, and unusually for a treasury this size, none of it is opaque. Mantle publishes every address, so the entire **2,917,022,412 MNT** is readable on-chain: the dominant Ethereum safe holding **2,900,022,409 MNT**, a second Ethereum safe holding **10,000,000 MNT**, four Mantle-network wallets holding **7,000,003 MNT** between them, and five published-but-empty wallets tracked so that a refill would be visible immediately. None carries a schedule, so there is no date to plan around; all of them are read straight from the chain. Two smaller pools sit alongside: the protocol fee accounts at **201,186.88 MNT**, growing slowly as the chain is used, and the bridge collateral at **5,545,326 MNT**. If any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

One clarification matters for reading Mantle correctly: mETH and cmETH are separate liquid-staking tokens with their own contracts and their own supplies, and Mantle's total value locked is a deposit figure denominated in other assets. None of them is an MNT quantity, and none of them appears anywhere in this ledger. Every number on this page is either an MNT balance read from a chain or the MNT supply itself.

## How MNT compares to other layer-2 tokens

Against the other large Ethereum layer-2 tokens, Mantle is the one that has already finished diluting. The rollup tokens that dominate the sector still run multi-year unlock calendars, releasing team and investor allocations on fixed monthly dates that arrive whether or not anybody wants them — that is calendar-driven sell pressure with a published schedule. MNT has none: its release calendar closed in **2023**, so there is no date on which supply mechanically appears. Structurally, Mantle trades scheduled dilution for discretionary dilution, and that is a genuinely different risk. A calendar is predictable and priced in; a **2,917,022,412 MNT** treasury released by vote is unpredictable in timing and potentially far larger in size.

Against the layer-2s that burn, the contrast is sharper still. The rollup design that pays its gas in the base asset destroys part of every fee, so heavy usage makes the token deflationary by design. Mantle takes gas in MNT — which sounds like the same thing and is not. Mantle's fees accumulate in protocol accounts rather than a burn address, so usage moves MNT from users to the protocol without removing a single coin from the count. This quarter that difference was worth **41,031.81 MNT** collected and zero destroyed. A chain with a real fee burn would have shown that amount leaving the supply; Mantle shows it changing hands.

Against the exchange tokens that run quarterly buybacks and burns, Mantle has the treasury capacity but not the mechanism. An exchange token funds repurchases from operating revenue on a fixed quarterly schedule and destroys the result, producing a reliable negative supply line every quarter. Mantle holds a treasury larger than most of those programmes will ever deploy and has burned none of it, because the proposal to do so has not passed. The comparison is mechanism, not size: Mantle's buy side is currently zero, and the difference between zero and deflationary here is one governance vote.

## What to watch in the next 90 days

The first watch line is the phase-based treasury MNT burn discussion, unmoved since **Feb 25 2026**: a temperature check or a formal proposal appearing would be the single largest possible change to this page, converting Buy #1 from zero into a real deflationary row. The second is the Mantle DAO's vote portal generally — the most recent proposal of any kind closed on **May 8 2026**, so any new Budget Proposal would be the first supply-relevant governance event in more than a quarter. The third is the main treasury safe holding **2,900,022,409 MNT**; any outflow from it books straight into Sell #3. The fourth is the token's mint cap parameter, currently **0** with its time gate already elapsed — a change there, or an upgrade of the token implementation behind its proxy, would reopen issuance. The fifth is the bridge collateral pool at **5,545,326 MNT**, which should keep tracking MNT issued on other networks rather than diverging from it.

## Summary

Mantle's MNT reads **0.00% net** over the last 90 days and **0.00%** projected forward, against a supply-monitor reading of **+0.03%**. Structurally MNT is a finished distribution: no emission, no vesting since **2023**, a mint function whose cap parameter reads zero, and a gas model that parks fees in protocol accounts instead of burning them. The key risk is not dilution by schedule but dilution by decision — the Mantle Treasury holds **2,917,022,412 MNT**, about **47%** of all MNT, and a single passing vote could move any part of it into the float. The ceiling is not a hard cap either: total supply sits at **6,219,316,794.89 MNT** because a governed parameter says so, not because the protocol forbids more. Flat, not shrinking, and entirely dependent on governance staying quiet.

---

*MrNasdog Pressure Framework analysis of MNT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 2 2026.*
