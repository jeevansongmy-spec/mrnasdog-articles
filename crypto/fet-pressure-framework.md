---
title:         "FET Inflation Analysis · August 2026 · Supply was growing, trend cooling"
description:   "FET reads +0.64% net supply to market per 90 days. The Ethereum token is capped at 2.71B and minted nothing, but the uncapped Fetch chain paid stakers 10.65M new FET."
canonical_url: "https://mrnasdog.com/research/fet/inflation"
tags:          ["crypto", "fet", "fetchai", "tokenomics"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/fet/inflation](https://mrnasdog.com/research/fet/inflation)*

# FET Inflation Analysis · August 2026 · Supply was growing, trend cooling

FET, the token of the **Artificial Superintelligence Alliance**, is usually described as hard-capped and fully minted. Half of that is true. The Ethereum FET contract is capped at **2,714,384,546** and we read it identical at both ends of this window, to the last decimal — but the native **Fetch chain** has no cap at all, and its mint module paid stakers **10.65M** brand-new FET over the 90 days to **Aug 18 2026**. Add the merger migration tail and one treasury payment and sell pressure is **14.37M FET** against **zero** on the buy side, a net **+0.64%** of circulating supply. Our supply monitor reads **-1.25%**, a gap of **1.89** percentage points that turns out to be a bridge, not a burn.

## The verdict, in one paragraph

For the 90-day window ending **Aug 18 2026**, the Pressure Framework reads **FET at +0.64% net**. Sell pressure is **14.37M FET**, buy pressure is **0**, and the circulating base is **2.23B FET**. Our supply monitor reads **-1.25%**, so the gap is **1.89** percentage points and a monitor-gap note ships on the FET overview. The gap closes on arithmetic. The Fetch bridge contract on Ethereum held **266.997M** FET on **May 20 2026** and **294.650M** on **Aug 18 2026**; that **27.653M** increase is FET leaving the Ethereum ledger to become native FET, and the monitor books it as a supply drop. Net of the **0.369M** drawn out of the migration escrows, it explains **27.284M** of the monitor's **28.256M** fall, with the remainder inside the monitor's own day-to-day spread. FET is best described as **a capped token on one chain and an uncapped staking-inflation chain on the other, with nothing on the buy side yet**.

## Sell pressure: where new FET comes from

Sell #1, protocol inflation, is **10.65M FET**, and it is the row a one-chain reading of FET always misses. The Fetch chain runs a fixed **3%** annual inflation and pays every unit of it to stakers. We did not take that from a parameter page — we measured the chain. The mint pays **7.888792** FET per block, read directly from bank supply across four heights, and the window contained **1,350,220** blocks at a measured **5.75** seconds each, not the **5.0** seconds the chain's own year-length setting implies. Multiply and the Fetch chain issued **10,651,076** FET, an annual run rate near **43.3M**. A second angle agrees: **43.3M** a year spread over the **605M** FET currently bonded is a **7.1%** staking return, which is what custodial staking desks advertise for FET.

Sell #2, vesting unlocks, is **0.37M FET**, and it is far smaller than any unlock calendar suggests. The AGIX and OCEAN merger left two conversion contracts on Ethereum holding FET for holders who never swapped. We read both at each end of the window: together they fell from **14.88M** to **14.51M**. The published migration calendar lists a release on **Aug 28 2026** and one roughly every month before it, but the escrow is what actually moves, and claimants are drawing it down slowly — **1.29M** in the previous quarter and only **0.37M** in this one. Booking the calendar figure instead of the realised one would have invented sell pressure that never reached a wallet.

Sell #3, foundation and unscheduled unlocks, is **3.35M FET** — a single firing. The SingularityNET treasury held **10.951M** FET on **May 20 2026** and **7.601M** a month later, and has not moved since. It is the only identified team wallet that paid anything out in the window, and because it is one event in twelve months with no published schedule, it carries forward at **zero**. Sell #4, long-term locked or bankruptcy, is **zero**: the Alliance has no insolvency estate, no trustee and no long-dated lock contract unwinding into the float.

## Buy pressure: where new FET goes

Every buy row is **zero**, and the most interesting of them is Buy #1. The Alliance has announced an Earn and Burn programme that routes a slice of ecosystem revenue into buying FET and destroying it, with a stated first-year target near **35M** FET. An announced target is not a realised flow, so we checked the ledger the burn would have to touch. The Ethereum FET contract does cut its own total supply when tokens are destroyed — we watched it fall by **0.109M** in the winter of **2025** — and across this window it read **2,714,384,546.672** on both dates, unchanged. Both burn addresses hold nothing. So the mechanism exists, it has fired before, and it did not fire in these 90 days.

Buy #2, protocol fee burn, is **zero** by design on both ledgers. Fetch chain fees are paid to validators and stakers rather than burned, so network usage never removes a FET; the Ethereum token has no fee mechanism at all. Buy #3, foundation buy, is **zero** — no treasury purchase has been disclosed or seen on chain, and every identified safe is a payer, not a buyer. Buy #4, new long-term lock, is **zero** as well, and this is the row where FET is often flattered: staking **605M** FET is not a lock, because it unbonds back into the float and the market counts it as circulating the entire time. The Ethereum staking contract that holds **80.616M** FET did not change by a single token across the window.

## Foundation and overhang

What the Alliance controls is large and, this quarter, almost entirely still. The biggest identified safe holds **277.55M** FET and has not moved since late **2025**, though it did release **246.9M** before that, so it is capacity with a history. The Fetch.ai Foundation safe holds **26.69M**, two further group safes hold **81.21M** and **32.20M**, and the SingularityNET treasury holds **7.60M** after its **3.35M** payment. The two merger conversion contracts hold a further **14.51M** that belongs to unclaimed AGIX and OCEAN holders. Separately, the Ethereum bridge lockbox holds **294.65M**, but that is location rather than overhang — every FET in it is already live as native FET on the Fetch chain.

All of these balances are read fresh at every refresh, and the rule is simple: if any of these wallets' balances falls between refreshes, the outflow enters Sell #3 at the next refresh. The staking pool sits outside that perimeter deliberately, because unbonding returns tokens the market already counts.

## How FET compares to other multi-chain staking tokens

FET looks like a capped asset and behaves like a Cosmos one. A token such as WLD is capped and pre-minted, so its only supply pressure is a release calendar, and when the calendar slows the pressure slows with it. FET has that mechanism too, in the merger migration tail, but the tail is now trivial. Its real issuance is the Cosmos staking model — ATOM, INJ, TIA and every other chain paying validators in freshly minted units — where supply grows as long as the chain produces blocks, no matter what the token contract on another chain says.

The comparison that matters most is with the exchange-token model, where a quarterly buyback and burn is the whole thesis. FET has announced that shape of mechanism and has burned before, but for this window the buy side is empty, so nothing offsets the staking issuance. Against BNB or OKB, which remove supply on a fixed quarterly schedule, FET sits on the other side of the ledger until Earn and Burn fires at a size that shows up on chain. And against a single-chain token generally, FET carries a reading hazard the others do not: the bridge makes the Ethereum float fall while total FET rises, so a one-chain view of FET reports deflation during a quarter of real growth.

## What to watch in the next 90 days

Watch the Ethereum token's own total supply — it is the one number that proves an Earn and Burn burn actually happened, because the contract cuts it directly rather than parking tokens in a dead address. Watch the merger migration release dated **Aug 28 2026**, and specifically whether the conversion escrows actually drain rather than simply re-dating a calendar entry. Watch the bridge lockbox: it added **27.65M** FET in two months after being flat for two, and a reversal would push the supply monitor the other way just as sharply. Watch the SingularityNET treasury, which has paid out once in twelve months and would change the Sell #3 forward reading if it fired twice. And watch the Fetch chain's own inflation setting, currently **3%**, which is the single largest lever on this reading and is governable.

## Summary

The Pressure Framework reads FET at **+0.64%** net supply to market over the 90 days to **Aug 18 2026**, easing to **+0.49%** as the one-off treasury payment drops out. The structural mechanism is a split personality: an Ethereum token hard-capped at **2,714,384,546** that minted nothing, and an uncapped Fetch chain paying **3%** a year to stakers, which is where all **10.65M** of the quarter's new FET came from. The key risk is that the buy side is entirely empty: the Earn and Burn programme is announced and has fired before, but it did not fire in this window, so nothing offsets issuance. The ceiling everyone quotes is real, but it belongs to one contract on one chain — it is not a cap on how much FET can exist.

---

*MrNasdog Pressure Framework analysis of FET, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 18 2026.*
