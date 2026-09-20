---
title:         "PONS Inflation Analysis · September 2026 · Supply shrinking · projected to keep shrinking"
description:   "PONS supply shrank 45.80% in 90 days: 0 verified additions against 314.1M tokens destroyed by fee-funded buybacks. Pressure Framework ledger and mint-path proof."
canonical_url: "https://mrnasdog.com/research/pons/inflation"
tags:          ["crypto", "pons", "launchpad", "tokenburn"]
published:     true
---

Originally published at [PONS Inflation Analysis · September 2026 · Supply shrinking · projected to keep shrinking](https://mrnasdog.com/research/pons/inflation).

# PONS Inflation Analysis · September 2026 · Supply shrinking · projected to keep shrinking

PONS supply is shrinking and is projected to keep shrinking. The Pressure Framework records **0** verified additions against **314.1M PONS** destroyed, a net of **−45.80%** over the last 90 days and **−16.05%** projected forward. Pons is a token launchpad on Robinhood Chain whose trading-fee revenue buys PONS on the open market and sends it to an unspendable address. The token contract carries no way to create another PONS, so the entire ledger is one-directional — but the share of fees pointed at the buyback is a team setting, not a protocol rule.

## The verdict, in one paragraph

On a circulating denominator of **685.9M PONS**, the Pressure Framework reads **−45.80%** over the trailing 90 days and **−16.05%** projected over the next 90. There is no monitor cross-check to compare against: the inflation monitor has only carried PONS since **Jul 22 2026**, its 90-day column is empty for every snapshot, and a coin younger than the window cannot produce one. That means no gap and no warning chip on the overview, and it also means this reading stands on primary evidence alone. Every figure here comes from the token contract and a complete sweep of its transfer log on the public chain. PONS is deflationary by revenue-funded buyback on a fixed, non-mintable supply.

## Sell pressure: where new PONS comes from

Protocol inflation is **0**, and this is the strongest zero on the page. A read of the PONS token contract's runtime code returned **30** external functions: the nine standard token calls plus twenty-one view-only getters for launch metadata. There is no mint function, no owner, no role check and no upgrade path, and the code contains no instruction that can call or deploy another contract. Exactly one issuance event exists in the whole history of the chain — **1,000M PONS** created in a single transfer on **Jul 13 2026** — and the supply figure has read **1,000M PONS** at every check since. That figure is not a compiled-in constant either: the value is absent from the bytecode, so it lives in writable storage and its flatness is a genuine measurement.

Vesting unlocks contribute **0**. The whole supply was handed out in that single issuance, and the wallet that received it now holds effectively nothing. No vesting contract, team tranche or investor cliff exists for PONS, and none can be created later, because no further token can be issued. Foundation and unscheduled unlocks are **0** for a structural reason worth stating plainly: the counted float for PONS is defined as the full **1,000M** less whatever has been destroyed, which means every PONS that still exists is already counted. No wallet sits outside the float, so no transfer — by the team, the creator or anyone else — can add a single token to it. Long-term locked or bankruptcy releases are **0** as well: no estate, trustee or court-directed distribution exists for this token.

## Buy pressure: where new PONS goes

The programmatic buyback is the whole story, and it removed **215.9M PONS** over the window. Pons takes a share of the trading fee charged on every token launched through the platform, spends most of that revenue buying PONS on the open market, and sends what it buys to an address nobody holds the key to. Since **Sep 2 2026** the buying has run through an on-chain contract that executes in thousands of small slices rather than one large purchase; before that date an operator wallet carried it out by hand. A separate row records the launch phase: in the six days after launch, the launch pool, a launch fee wallet and the creator's own wallet sent a combined **98.3M PONS** to the same unspendable address. The last of those fired on **Jul 18 2026** and none has fired since, so that row projects nothing forward.

Protocol fee burn is **0**. Robinhood Chain charges gas in ETH, not in PONS, so the token is never consumed by network activity and there is no burn at the network level to add. Both destruction surfaces were read, and they disagree exactly as the mechanism predicts: the supply figure never falls, because a PONS burn is a transfer to an unspendable address rather than a call that cancels the token, while the balance at that address rose to **314.1M PONS**. Reading the supply figure alone would have booked the entire buy side of this page at zero. Foundation buying is **0** because the project's only market purchases are the buyback already counted, and counting them twice would double the row. New long-term lock is **0**: nothing about PONS is locked, staked or escrowed — what leaves the float here is destroyed outright.

## Foundation and overhang

The overhang question has an unusually clean answer for PONS, and the arithmetic is what settles it. Total supply and circulating supply are the same number, **685.9M PONS**, which leaves a non-circulating bucket of exactly zero. There is therefore no reserve, treasury or unscheduled allocation that could enter the market, because there is nowhere outside the market for a PONS to sit. Every project-side balance is already inside the counted float.

For completeness, those balances are enumerated and watched. The launch contract holds **6.1M PONS**, a launch fee wallet holds **3.1M PONS**, the launch pool retains **0.1M PONS**, and the retired burn operator wallet is down to roughly **1.0K PONS**. The automated burn contract holds nothing — it destroys what it receives in the same transaction. The token creator's own wallet reads **0**. Together those identified balances are about **9.3M PONS**, or roughly **1.4%** of the float, and they are read on-chain at every rebuild. If any of them falls between refreshes, the outflow still enters no sell row, because it is a move inside the float rather than an addition to it; what it would change is the overhang note itself. The one balance whose movement matters is the unspendable address: if it stops rising, the buy side of this page stops with it.

## How PONS compares to other fee-funded buyback tokens

PONS belongs to the launchpad-token class — a protocol that earns a cut of speculative trading volume and routes that revenue back into its own token. Measured against a capped proof-of-work coin, the difference is directional. A halving-schedule chain issues less over time but never less than zero; PONS issues nothing at all and removes what already exists, which is why its reading sits deep in negative territory rather than merely near flat. Measured against an uncapped staking chain with a continuous emission, PONS has no reward stream to finance and therefore no structural dilution to offset.

The closer analogue is an exchange token running a revenue-funded quarterly burn. Both destroy supply out of earnings, but the shapes differ. A quarterly burn lands as one dated event that a reader can put on a calendar; the PONS buyback runs continuously in small slices, which makes the flow smoother to estimate but ties it directly to whatever the launchpad earned that week. The mechanism is also less binding. An exchange token's burn is usually written into a published schedule; the PONS split between buyback and treasury is a team setting that the project itself describes as not yet permanent. A fee burn encoded in protocol rules cannot be switched off by a decision, and this one can.

The last comparison is to the rest of its own class. Launchpad revenue is the most volatile revenue in crypto, and the PONS record already shows it: the token-denominated burn rate has fallen steadily since launch, partly because volume cooled and partly because the same dollar of fee revenue buys far fewer PONS at a higher price. A reader should treat the forward number as a function of launchpad activity, not as a protocol constant.

## What to watch in the next 90 days

Through **Dec 19 2026**, the single most informative number is the balance at the unspendable address, currently **314.1M PONS** — if it keeps climbing at the rate seen since **Sep 2 2026**, the projected **−16.05%** holds. Watch for the announced move to make the fee split permanent and fully automated; until that ships, the buyback share remains changeable and the buy side of this ledger is a policy, not a rule. Watch the launchpad's own fee revenue, since the buyback is funded entirely from it and the burn rate has already declined through August and September. Watch for any second burn route appearing alongside the current contract, which would need to be separated rather than added. And watch the supply figure itself: it has read **1,000M PONS** since **Jul 13 2026**, and any movement in it would mean a mint path this review did not find.

## Summary

The Pressure Framework reads PONS at **−45.80%** over the trailing 90 days and **−16.05%** projected forward, on a float of **685.9M PONS**. Nothing is minted, nothing vests and nothing sits outside the counted float, so verified additions are **0**, while trading-fee revenue bought and destroyed **314.1M PONS** inside the window. The structural strength is the token contract itself, which carries no mint, no owner and no upgrade path, making the supply ceiling of **1,000M PONS** a permanent one. The structural risk is that the buy side is discretionary: the share of fees pointed at the buyback is a team setting the project has not yet made permanent, and the revenue behind it depends on launchpad volume that has already cooled since **Jul 13 2026**.

MrNasdog Pressure Framework analysis of PONS, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 20 2026.
