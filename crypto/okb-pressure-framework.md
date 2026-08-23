---
title: "OKB Inflation Analysis · August 2026 · Mixed flows, supply roughly steady"
description: "A MrNasdog Pressure Framework read of OKB: fixed at 21M with mint and burn removed from the token contract. Framework 0.00% net; the supply monitor agrees at +0.04%."
canonical_url: "https://mrnasdog.com/research/okb/inflation"
tags: ["crypto", "okb", "okx", "exchange-token"]
published: true
---

> Originally published at **[mrnasdog.com/research/okb/inflation](https://mrnasdog.com/research/okb/inflation)** by MrNasdog.

OKB, the OKX exchange token and the mandatory gas token of X Layer, has no mint path, no vesting calendar and no active burn — all three were settled in **August 2025**, when OKX fixed the total supply at **21 million** and upgraded the token contract to remove both minting and burning. Over the 90 days to **Aug 23 2026** nothing was issued and nothing was retired, so the MrNasdog Pressure Framework reads OKB at **0.00% net** on a **21M** float. Our independent supply monitor reads **+0.04%** across the same window — a gap of **0.04 percentage points**, which is agreement, not conflict.

## The verdict, in one paragraph

For the 90-day window ending **Aug 23 2026**, the Pressure Framework reads OKB at **0.00% net**: every sell row and every buy row in the OKB ledger is zero. Nothing mints OKB, no vesting remains, no reserve is being released, and — since the **Aug 18 2025** contract upgrade removed the burn function — nothing is being retired either. The supply monitor reads the realised change at **+0.04%** over the same window, so the gap between the two readings is **0.04 percentage points**, well inside the framework's half-point tolerance; OKB therefore ships with **no monitor-gap flag**. The label for OKB is **fixed by contract**: a hard 21 million cap that no longer grows and no longer shrinks. That is a Bitcoin-style scarcity story with one asterisk, covered below.

## Sell pressure: where new OKB comes from

It does not come from anywhere, and that is the defining fact about OKB today. Sell #1, protocol inflation, is **zero**. OKB is not a blockchain — it is a token issued by the OKX exchange — so there are no block rewards, no staking emissions and no security budget denominated in OKB. Even the theoretical route to new supply is closed. We re-read the live token code this session rather than trusting the announcement: the implementation the OKB contract points at exposes sixteen public functions — name, symbol, decimals, total supply, balances, transfers, approvals, a set of address getters and one dormant bridge entry — and not one of them is a mint. The supply figure the contract returned at the opening block of the window and at the closing block was byte-for-byte identical on two independent readers.

Sell #2, vesting unlocks, is **zero** for a structural reason and is the one row the framework marks permanent: the original OKB allocation finished vesting in **2018**, all 21 million is already unlocked, and there is no team, seed or treasury release calendar left to run down. Three independent supply registries agree that circulating, total and maximum supply are the same **21 million** number. Sell #3, foundation and unscheduled unlocks, is **zero** because there is nothing left to unschedule: the OKX reserve and the accumulated buyback OKB that would normally be an exchange token's largest overhang were not parked, they were destroyed in the **Aug 15 2025** burn of **65,256,712 OKB**. Sell #4 is **zero** because no bankruptcy estate holds OKB and no trustee distribution schedule exists.

## Buy pressure: where new OKB goes

The buy side is symmetrically empty, which is the part most readers get wrong about OKB. Buy #1, programmatic buyback, is **zero**. The quarterly buyback-and-burn that defined OKB for years is retired, and it cannot quietly restart in its old form because the burn function was removed from the token code in the same **Aug 18 2025** upgrade that removed minting. The cumulative burn totals still quoted around OKB are lifetime figures from the pre-2025 era; they are not a flow inside this window, and the framework does not book them.

Buy #2, protocol fee burn, is **zero**, and this is worth being precise about because OKB genuinely is a gas token. X Layer runs one-second blocks at a base fee near **0.02 gwei** — gas is close to free by design — and we measured the whole fee economy this session rather than carrying a number forward. Across five sample points spanning the window the chain took in roughly **3 to 7 OKB per day** in fees, about **$350 to $760 a day**, or a few hundred thousand dollars a year against a market capitalisation near **$2.29B**. More importantly, that gas is not destroyed: it accrues to the sequencer and base-fee accounts, and both of those balances were **larger** at the end of the window than at the start. Less than **one whole OKB** drifted into unrecoverable addresses across the entire 90 days.

Buy #3, foundation buy, is **zero**: OKX runs no open-market accumulation programme, because buying was the input to a burn engine that no longer exists. Buy #4, new long-term lock, is the one row that changed character this quarter. On **May 26 2026** — inside this window — X Layer launched Exchange OS, which makes OKB the collateral for deploying a trading venue: a deployer must stake OKB into the chain's staking contract, where it sits locked and slashable. That is a real lock mechanism and OKB did not have one before. But the whitepaper publishes no required amount and no contract address, so there is no quantum to book. The row stays at **zero** and the mechanism is tracked.

## Foundation and overhang

OKB is the rare token where the overhang list is genuinely short. There is no foundation treasury, no DAO treasury and no unscheduled-unlock pool, because circulating, total and maximum supply are all the same **21 million** — there is no non-circulating bucket for anything to sit in. The reserve that would ordinarily be enumerated here was burned rather than shelved. OKX's exchange wallets hold enormous quantities of OKB, but those are customer deposits, not project-controlled supply, and the framework excludes custodial balances by rule.

One control point remains, and it is the asterisk on the scarcity story. The OKB token is an upgradeable proxy, and its owner slot is still populated by a live, ordinary wallet with the upgrade function available. "Mint and burn removed" is therefore the state of the code that is installed today, not a mathematical impossibility — the owner could install different code. That is why the framework tags OKB's contract-dependent rows as checked rather than permanent, and re-verifies the code from bytecode on every rebuild. If the implementation the proxy points at ever changes, or if the Exchange OS staking contract is published with a disclosed balance, the outflow or the lock enters the ledger at the next refresh.

## How OKB compares to other exchange tokens

The exchange-token class is normally defined by a buyback-and-burn engine: the venue earns fees, spends part of them retiring its own token, and the token is deflationary in proportion to exchange revenue. BNB works this way through an automatic quarterly burn plus a real-time fee burn on BNB Chain, and LEO works this way through a discretionary repurchase funded from Bitfinex revenue. Both are structurally deflationary while the revenue holds, and both are structurally exposed if it stops — the scarcity is a function of a business, re-earned every quarter.

OKB has stepped out of that class entirely. Rather than burning slowly forever, OKX burned once, enormously, and then removed the machinery. The mechanism is no longer "fees fund scarcity"; it is "the number is 21 million." That makes OKB a closer structural analogue to a hard-capped proof-of-work coin than to its exchange-token peers — except that Bitcoin is still issuing new coins under a halving schedule and OKB is not issuing at all, and Bitcoin's cap is enforced by a distributed consensus while OKB's is enforced by an upgradeable contract. Against BNB and LEO the trade is legible: OKB gives up the ongoing deflation those tokens still deliver, and gets in exchange a supply that cannot surprise you upward. In the framework's scoring that is a ceiling, not a floor — a supply that is fixed but not shrinking cannot score above the flat band, because no coins are actually being removed.

## What to watch in the next 90 days

First, the token contract's implementation address. It is the single fact the whole reading rests on; if the proxy is pointed at new code, minting or burning could return in one transaction. Second, Exchange OS adoption: if OKX publishes the X Layer staking contract or a total staked figure, Buy #4 gains a real quantum for the first time and the ledger stops being symmetrically empty. Third, X Layer's fee economy — at roughly **3 to 7 OKB a day** it is currently too small to matter to supply, but a fee-burn policy change would move Buy #2 off zero. Fourth, any OKX announcement reinstating a repurchase programme, which would have to be paired with a new burn route to affect supply at all. Fifth, the possibility that OKX completes the Ethereum phase-out of the residual **429,065 OKB** still sitting on the old contract; that is a venue migration rather than a supply change, but it is the kind of event that makes third-party supply trackers wobble.

## Summary

OKB is a fixed-supply exchange token whose supply neither grows nor shrinks: OKX burned it down to a hard **21 million** cap in **August 2025** and upgraded the contract to remove both minting and burning, the vesting finished in 2018, and X Layer gas is collected by the sequencer rather than destroyed. Over the 90 days to **Aug 23 2026** the framework reads **0.00% net**, matched by the supply monitor at **+0.04%**. The structural strength is a hard cap with no live issuance path anywhere in the code; the structural risk is that the cap is enforced by an upgradeable contract whose owner slot is still populated, so the guarantee is a policy written in code rather than true immutability. The ceiling on the story is simple arithmetic: with nothing minting and nothing burning, 21 million is where OKB stays.

---

*MrNasdog Pressure Framework analysis of OKB, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 23 2026.*
