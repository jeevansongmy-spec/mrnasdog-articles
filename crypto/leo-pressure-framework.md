---
title: "LEO Inflation Analysis · August 2026 · Mixed flows, supply roughly steady"
description: "A MrNasdog Pressure Framework read of UNUS SED LEO: no mint, no vesting, only a chain-verifiable buyback-and-burn. Framework −0.07% net; the supply monitor reads −0.24%."
canonical_url: "https://mrnasdog.com/research/leo/inflation"
tags: ["crypto", "leo", "bitfinex", "exchange-token"]
published: true
---

> Originally published at **[mrnasdog.com/research/leo/inflation](https://mrnasdog.com/research/leo/inflation)** by MrNasdog.

UNUS SED LEO has no issuance at all: every one of the **1,000,000,000 LEO** was created and sold in **May 2019**, with no vesting calendar, and neither the Ethereum nor the Vaulta side has minted a token since. The only flow that moves LEO supply is iFinex buying LEO back and taking it off the market — **633,434 LEO** in the 90 days to **Aug 13 2026**, across **85** on-chain transfers. The Pressure Framework reads LEO at **−0.07% net** against a supply monitor at **−0.24%**, a gap of about **0.17 percentage points**, inside tolerance. LEO is a fixed-supply exchange token that shrinks slowly and verifiably.

## The verdict, in one paragraph

For the 90-day window ending **Aug 13 2026**, the MrNasdog Pressure Framework reads UNUS SED LEO at **−0.07% net** supply change, and projects the same **−0.07%** forward. Total sell pressure was **zero**; total buy pressure was **633,434 LEO**, against a circulating base of about **920M LEO**. Our supply monitor reads the same window at **−0.24%**, leaving a gap of about **0.17 percentage points** — inside the half-point tolerance, so no monitor-gap chip ships on the LEO overview. The residual is ordinary noise in a market-cap-over-price supply series, not a disagreement about mechanism: LEO's float is a pure function of chain state, and both readings agree the number is falling. The cite-able label for LEO is a **fixed-supply exchange token with a verifiable daily buyback-and-burn** — deflationary, but at a pace measured in hundredths of a percent per quarter, not in headlines.

## Sell pressure: where new LEO comes from

Nowhere, and that is the whole of it. Sell #1, protocol inflation, is **zero** because UNUS SED LEO is an exchange token rather than a chain: there is no consensus to pay for, no block reward denominated in LEO, and no staking emission. On Ethereum, the LEO ERC-20 reports a total supply of **660,000,000 LEO**, and it read exactly that at both ends of this window — the same figure it has carried since the 2019 issuance. On Vaulta, the chain formerly known as EOS, the LEO contract reports a supply of **307,653,658.9 LEO**, with no issue and no retire action anywhere in the account's indexed history.

Sell #2, vesting unlocks, is **zero**, and it is zero permanently. The May 2019 sale delivered every token at once, at one dollar each, with no discount tier and no lockup. There is no cliff calendar left to run, so no future date can add LEO to the float. This is unusual and worth stating plainly: most tokens carry a vesting overhang that decays over years, and LEO's decayed to nothing seven years ago.

Sell #3, Foundation and unscheduled unlocks, is **zero** for the window, because nothing left company hands. The size of what could leave is a different question, and it is the single largest fact about LEO: an Ethereum cold-storage safe holds **648,000,000 LEO** — about **98%** of the Ethereum-side supply, and roughly **70%** of the circulating figure the market quotes. It was funded in **2020** and topped up in **2023**, and it has never sent a token out. Sell #4, long-term locked or bankruptcy, is also **zero**: the 2016 breach restitution returns bitcoin to iFinex, not LEO, so no estate or trustee holds LEO to distribute.

## Buy pressure: where new LEO goes

Buy #1, the programmatic buyback, is the entire LEO ledger, and it is **633,434 LEO** over the window. iFinex committed to spend no less than **27%** of consolidated gross revenues repurchasing LEO on the open market and burning it, continuously, until none remain in commercial circulation. In practice this executes as roughly one transfer per day on Vaulta, from the operating account into the token issuer account, tagged with the memo **burn**. We counted **85** such transfers in the window at an average of about **7,038 LEO** each, and the pace was flat throughout: **121,663** from **May 15 2026**, **226,360** in **Jun 2026**, **200,839** in **Jul 2026** and **84,572** to **Aug 12 2026**.

The reason this burn is trustworthy rather than a claim is an accounting identity that closes exactly. The Ethereum supply of **660,000,000**, plus the Vaulta supply of **307,653,658.9**, minus the **47,659,925** LEO sitting in the burn account, equals **919,993,733.9** — the same circulating figure the wider market quotes for LEO, to the decimal. That proves the sink is excluded from circulating supply, so every LEO that lands in it leaves the float the instant the transfer confirms, whether or not the token is technically destroyed. The account has never sent a token back out. It also lets us test the louder claims: the story that **18,000,000 LEO** were burned in the first quarter of 2026 is false — the chain shows **781,820 LEO** for January, February and March combined, about **23** times smaller. So is the claim that **65%** of supply has been removed: the real cumulative removal is **80,006,266 LEO**, or about **8.0%** of the billion issued.

Buy #2, protocol fee burn, is **zero**, and it cannot be anything else — LEO is not the gas token of either chain it lives on, so no network fee is ever denominated in LEO and none can be destroyed that way. Buy #3, Foundation buy, is **zero** for now, though it is armed: iFinex pledged **80%** of net proceeds from the 2016 breach recovery and **95%** of any recovered Crypto Capital funds to additional LEO buybacks, and the seized bitcoin began moving in **Apr 2026**. Nothing has reached the burn stream yet — the daily pace shows no step up at all. Buy #4, new long-term lock, is **zero**: there is no staking contract to lock LEO into, and repurchased LEO is removed outright rather than parked for later release.

## Foundation and overhang

Three company-controlled holdings are worth tracking, and only one of them is small. First, the Ethereum cold-storage safe at **648,000,000 LEO** — dormant since **2023**, never a single outgoing transfer, and counted inside the circulating figure the market quotes. That last detail is the important one: the headline float of **920M LEO** is not what actually trades, because roughly **70%** of it sits in one safe that has never moved. Second, the Vaulta burn account itself, now holding **47,659,925 LEO** and rising by about **7,000** a day; it is an overhang only in the formal sense, since it is already excluded from circulating and has never had an outflow. Third, the Vaulta operating account at **2,198,884 LEO**, which drains only into the burn account.

The rule we apply to all three is the same: if any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh. Today none of them has, so every overhang row carries a value of zero — enumerated because we are watching it, not because it is moving.

## How LEO compares to other exchange tokens

Exchange tokens split into two mechanism families, and LEO sits at the far end of one of them. The first family issues on a chain of its own and then burns some of it back — the model where a token is simultaneously gas for a network and the subject of a quarterly buyback. Those tokens can show real deflation, but the burn has to outrun live issuance, and the issuance never stops. LEO has no issuance to outrun. Its supply was fixed in a single 2019 event, so every unit the buyback removes is a permanent reduction, and the direction of the supply curve cannot reverse without the issuer breaking its own commitment.

The second distinction is between a burn you can verify and a burn you are told about. Many exchange-token burn programmes are disclosed quarterly by the company, sized from revenue figures nobody outside can audit. LEO's is different in kind: the buyback lands as a dated on-chain transfer with a memo, into an account whose balance is arithmetically excluded from circulating supply. You can reconstruct the entire quarter from the chain without reading a single company statement.

Where LEO is weaker than its peers is concentration. A gas token's float is distributed across the users who need it to transact; LEO's is dominated by a single dormant safe holding roughly **70%** of the quoted supply. The deflation is real but small — a **0.07%** quarterly reduction is a rounding error next to a holding of that size, and a decision to move even a fraction of that safe would swamp several years of buyback in a single transaction.

## What to watch in the next 90 days

First, the daily burn transfer itself: any sustained move away from roughly **7,000 LEO** a day is the cleanest possible signal that iFinex revenue has changed, in either direction. Second, the 2016 breach restitution — the seized bitcoin began transferring in **Apr 2026**, and the pledge commits **80%** of net proceeds to LEO buybacks within eighteen months; if that lands, it arrives as a visible step up in the same daily stream, not as a separate announcement. Third, the Ethereum cold-storage safe: the first outgoing transfer it has ever made would be the single most important supply event in LEO's history, and it is watched on chain every refresh. Fourth, any change to the **27%** revenue commitment itself, which is the only lever that sets the burn rate. Fifth, whether any LEO ever leaves the Vaulta burn account — it never has, and it should not, but the identity that makes the float honest depends on it.

## Summary

UNUS SED LEO is one of the few tokens where the supply question has an arithmetic answer. Nothing mints LEO on either chain, no vesting remains, and the sole flow is a buyback that removed **633,434 LEO** in the 90 days to **Aug 13 2026** — a net of **−0.07%**, matched by a supply monitor at **−0.24%**. The structural mechanism is a revenue-funded, chain-verifiable daily burn against a supply that was fixed once, in 2019, and can never grow. The key risk is not inflation but concentration: **648,000,000 LEO** sit dormant in one safe inside the quoted float, roughly **70%** of it, and a single outgoing transfer there would matter more than years of buyback. The ceiling is absolute — **1,000,000,000 LEO** issued, about **8.0%** of it already removed, and no mechanism anywhere that can add one more.

---

*MrNasdog Pressure Framework analysis of LEO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 13 2026.*
