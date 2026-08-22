---
title: "PI Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description: "MrNasdog Pressure Framework read of Pi Network (PI): the mainnet total held at exactly 100,000,000,000 at five ledgers, yet 499.6M PI migrated into counted supply with no buyback and no burn. Net +4.50%."
canonical_url: "https://mrnasdog.com/research/pi/inflation"
tags: ["crypto", "pi", "pinetwork", "layer1"]
published: true
---

> Originally published at **[mrnasdog.com/research/pi/inflation](https://mrnasdog.com/research/pi/inflation)** by MrNasdog.

Pi Network (PI) is a mobile-mined coin on its own mainnet, and over the 90 days to **Aug 22 2026** the MrNasdog Pressure Framework reads sell pressure of **499.6M PI** against buy pressure of **zero** on a circulating base of **11,091,686,463 PI**, for a net of **+4.50%**. The Pi blockchain did not create a single coin in that window — the on-chain total read exactly **100,000,000,000** at five separate ledgers — because the entire cap was minted once at genesis. All 499.6M of the growth is mainnet migration: pre-made Pi crossing from the mining app into the counted supply. Against that there is **no buyback, no burn and no lock that absorbs anything**, which makes Pi Network **structurally inflationary with an empty buy side**.

## The verdict, in one paragraph

For the 90-day window ending **Aug 22 2026**, the Pressure Framework reads **PI at +4.50% net**: sell pressure of **499.6M PI**, buy pressure of **0**, on a circulating base of **11,091,686,463 PI**. The next 90 days read **+4.50%** as well, because mainnet migration is the only live mechanism and it is projected at the rate this window actually ran. Our supply monitor reads **+4.71%** for the same window, a gap of **0.21 percentage points**, comfortably inside the half-point tolerance, so no monitor-gap flag is raised on this build. That gap is almost entirely arithmetic rather than disagreement: the monitor divides the same flow by the supply as it stood 90 days ago and the framework divides it by the supply as it stands today, which alone accounts for **0.21** of it. The right label for Pi Network is **a fixed-cap chain that mints nothing and still inflates, because the supply counter is a migration queue**.

## Sell pressure: where new PI comes from

Sell #1, protocol inflation, is **499.6M PI**, and it is the only row on this page carrying a number. It is also not what the name usually means. The Pi blockchain is a Stellar-consensus chain whose entire **100,000,000,000 PI** cap was created in a single genesis batch, and the chain's own total supply read **100,000,000,000.0000000** — identical to seven decimals — at ledgers dated **May 24 2026**, **Jun 15 2026**, **Jul 9 2026**, **Aug 2 2026** and **Aug 22 2026**. Nothing was minted and nothing was burned. What grew is the number the market calls circulating supply, which for Pi Network is a running tally of mining rewards that have been migrated out of the mobile app and onto mainnet. That tally moved from **10,592,041,794 PI** to **11,091,686,463 PI** across the window, a rise of **499,644,669 PI**. Those coins were always going to exist; the window is when the market started counting them, and counting them is what makes them tradable.

Sell #2, vesting unlocks, is **0**, and this is the row where Pi Network is most widely misread. Trackers publish a monthly PI unlock calendar — roughly **775.8M PI** across July to December 2026, with **132.6M** in September, **138.2M** in October and **149.0M** in November. That calendar is not an escrow release schedule. It is the expiry schedule of the 6-month and 12-month lockups that individual pioneers elected for themselves at the moment they migrated, and those coins were counted on the day they migrated, not on the day they unlock. There is no lock contract paying anything into the supply, and that is proven rather than assumed: the chain's total supply did not move by a decimal on any of the dates in question. A published unlock table is not an escrow, and for Pi Network it is not even a supply event.

Sell #3, foundation and unscheduled unlocks, is **0** — capacity is not cadence, and no dated outflow was observed — but the overhang is enumerated rather than waved away, and it is enormous. The reported total supply of **17,064,133,020 PI** minus the circulating **11,091,686,463 PI** leaves **5,972,446,557 PI**, which is exactly **35%** of the total — precisely the core team's **20%**, the foundation's **10%** and the **5%** liquidity allocation, activated in proportion to migration rather than on any calendar. Behind that sits the far larger figure: **82,935,866,979 PI** of the 100B cap that has never been mined or migrated at all. Sell #4 is **0**: Pi Network has no bankruptcy estate, no trustee and no court-ordered distribution.

One extra row is carried explicitly, at **0**, because leaving it out would hide the number readers most want. About **419.8M PI** of pioneer lockups expire between September and November 2026. That is genuine pressure on what can be sold, and it belongs on a watch list — but it adds nothing to supply, because those coins are already inside the **11.09B**. Putting it in the ledger would count the same Pi twice.

## Buy pressure: where new PI goes

Nowhere. All four buy rows are **0**, and each one is zero for a reason that was checked this build rather than inherited. Buy #1, programmatic buyback, is **0** because no buyback exists. A sustained and well-publicised community campaign asked the Pi core team for an aggressive buyback-and-burn programme and was declined, on the stated grounds that Pi Network's tokenomics are built around inclusive distribution rather than scarcity. Buy #3, foundation buy, is **0** for the same reason: no open-market purchase by the Pi Foundation or the core team has ever been disclosed or observed.

Buy #2, protocol fee burn, is **0** because Pi Network has no burn at all. There is a real, one-way flow worth naming: transaction fees on this chain are not destroyed, they accumulate in a protocol fee pool that the network has no path to pay back out, and that pool grew from **8,263,357 PI** to **10,082,062 PI** across the window — **+1.82M PI**, rising at every one of the five ledgers read. It is still booked at zero, because Pi's circulating figure counts coins that have been migrated rather than coins people still hold, so spending Pi on gas never reduces it. Subtracting a balance-based flow from a migration counter would mix two different kinds of accounting, and at **0.016%** of supply the answer is immaterial either way.

Buy #4, new long-term lock, is **0**, and the lock pool was read at both ends of the window so the sign is settled instead of assumed. Locked PI stood at roughly **6.15B** on **May 20 2026** and at **6,178,732,387 PI** on **Aug 22 2026**, so fresh lockup elections slightly outran expiries over the full window. Mid-window the pool actually shrank, from **6,221,091,142 PI** on **Jun 15 2026** to **6,178,732,387 PI**, a fall of **42.4M** against a published calendar of roughly **231.6M** expiring in the same stretch — which is itself the evidence that new locks keep replacing the drained ones. Either way the row is zero, because the locked pool sits inside the counted supply: locking absorbs nothing and unlocking adds nothing.

## Foundation and overhang

Pi Network has three identified overhangs and no buyback wallet, no DAO treasury and no bankruptcy residual. The first is the non-mining allocation: **5,972,446,557 PI** covering the core team's **20%**, the Pi Foundation's **10%** and the **5%** liquidity share, read as the difference between the reported total and circulating figures and refreshed daily. It has no published release calendar; it simply scales into existence alongside migration.

The second is the un-mined remainder behind the ceiling: **82,935,866,979 PI** of the **100,000,000,000 PI** cap, released over years at a mining rate that follows a declining exponential curve. This is the structural reason Pi Network cannot be a low-inflation asset for a long time yet — the queue is more than seven times the entire counted supply. The third is the pioneer lockup pool at **6,178,732,387 PI**, which is unusual in that it is already inside the circulating figure and therefore drains into the tradable float without ever touching supply.

If any of those three balances falls between refreshes, the outflow enters Sell #3 at the next refresh — with one deliberate exception. Draining the pioneer lockup pool raises the tradable float but not the counted supply, because it is already inside it, so a fall there is surfaced as a float note rather than booked as a sell row.

## How PI compares to other fixed-cap chains

Pi Network shares one headline property with Bitcoin: a hard, protocol-level cap that no vote can raise. It shares almost nothing else. On a halving-model chain the cap is approached through issuance — coins are created block by block on a schedule everyone can compute, and the circulating figure and the minted figure are the same number. On Pi Network the cap was minted in full at genesis and the circulating figure is a migration counter, so the chain's own total supply is a constant while the market's supply figure climbs. The economic effect is identical to issuance — **499.6M PI** of newly tradable coin arrived this window — but every on-chain tool that watches total supply for inflation will report zero. That mismatch is the single most important thing to understand about PI.

Against uncapped continuous-emission layer-1s, Pi Network looks worse in the short run and better in the very long run. A staking chain issuing **4–7%** a year does so forever; Pi Network's **+4.50%** per 90 days is far heavier now, but it is drawn from a finite backlog of mined-but-unmigrated balances and a mining rate designed to decay. The catch is scale: with **82.94B PI** still behind the cap against **11.09B** counted, that backlog will not be exhausted on any timeframe an investor plans around.

Against exchange tokens with quarterly buyback-and-burn programmes, and against fee-burning smart-contract chains, the comparison is starkest and it is a comparison of absence. Those assets meet issuance with a mechanical, protocol-encoded bid or sink. Pi Network has neither, by choice: the fee pool is not burned, the core team declined a community buyback proposal, and the only lock in the system is one that never leaves the counted supply. All four buy rows read **0**, which is rare in this catalogue and is the whole reason PI scores where it does.

## What to watch in the next 90 days

First, the migration rate itself, which is the only number that moves this reading. It ran at **8.4M PI a day** in late May, fell to **3.2M** through mid-August, then jumped back to **6.5M** in the final week of the window — migration arrives in batches, so a slowdown needs more than one month of evidence before the forward projection should be cut.

Second, the pioneer lockup expiries of **132.6M PI** in September, **138.2M PI** in October and **149.0M PI** in November 2026. Watch what they do to price, not to supply — supply is unaffected.

Third, whether the locked pool keeps replacing itself. It stood at **6,178,732,387 PI** on **Aug 22 2026**; if it starts falling faster than the expiry calendar, pioneers have stopped re-locking and the tradable float is growing on two fronts at once.

Fourth, any reversal on buybacks or burns. The core team has declined so far, and a single announcement would be the first non-zero buy row Pi Network has ever had. Fifth, the Protocol 27 mainnet upgrade, expected late 2026 with no fixed date; Protocol 26, whose node deadline fell on **Aug 11 2026**, carried no supply mechanism, and Protocol 27 is currently described the same way.

## Summary

The MrNasdog Pressure Framework reads Pi Network at **+4.50%** net supply growth over the 90 days to **Aug 22 2026** and **+4.50%** for the next 90, driven entirely by **499.6M PI** of mainnet migration against an empty buy side. The structural mechanism is unusual and matters more than the number: the Pi blockchain minted nothing all window, its on-chain total held at exactly **100,000,000,000**, and the growth is pre-made Pi becoming counted as pioneers move balances out of the mining app. The key risk is that this is not a schedule anyone can bound — **82.94B PI** sits behind the cap against **11.09B** counted, with no buyback, no burn and no lock that removes anything. The ceiling is real and fixed at **100 billion PI**, but on the current run rate it constrains nothing an investor will live to see.

---

*MrNasdog Pressure Framework analysis of PI, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 22 2026.*
