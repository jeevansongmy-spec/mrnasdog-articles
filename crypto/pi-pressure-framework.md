---
title: "PI Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description: "MrNasdog Pressure Framework read of Pi Network (PI): the mainnet total held at exactly 100,000,000,000 at both window ends, yet 413.02M PI migrated into counted supply with no buyback and no burn. Net +3.71%."
canonical_url: "https://mrnasdog.com/research/pi/inflation"
tags: ["crypto", "pi", "pinetwork", "layer1"]
published: true
---

> Originally published at **[mrnasdog.com/research/pi/inflation](https://mrnasdog.com/research/pi/inflation)** by MrNasdog.

Pi Network minted no new PI in the last 90 days — the Pi mainnet ledger reported a total of exactly **100,000,000,000 PI** at both ends of the window — yet the MrNasdog Pressure Framework still reads PI at **+3.71% net**, because **413.02M PI** of already-mined, never-counted Pi crossed onto mainnet through migration on a circulating base of **11,141,680,597 PI**. Against that sell ledger the buy ledger is **0 PI**: Pi Network runs no buyback, no burn, and has no burn address on its chain at all. A supply monitor reads the same window at **+4.63%**, a gap of **0.93 percentage points** that the framework flags rather than hides.

## The verdict, in one paragraph

Over the last 90 days the MrNasdog Pressure Framework reads Pi Network at **+3.71% net**: a sell ledger of **413.02M PI** against a buy ledger of **0 PI** on a circulating base of **11,141,680,597 PI**. The supply monitor reads **+4.63%** for the same window, a gap of **0.93 percentage points**, which is outside tolerance and ships a data-conflict flag. Roughly four fifths of that gap is the eleven days between **Jun 4 2026** and **Jun 15 2026**, a stretch no primary Pi Network surface covers — the framework refuses to fill it with an estimate — and the rest is the arithmetic of measuring a percentage against a base that grew during the window. PI is best labelled a **zero-issuance chain with a structurally inflationary float**: no coin is created, and the counted supply rises anyway.

## Sell pressure: where new PI comes from

Sell #1 — protocol inflation — is **zero**, and this is the fact most readings of Pi Network get backwards. Pi mainnet is a Stellar-Consensus-Protocol fork, and the whole **100,000,000,000 PI** cap was created in two account-creation operations on **Dec 31 2020**: one for **19,999,999,800 PI** and one for **80,000,000,100 PI**. The chain has no issuance path for its native asset, and the ledger's own total read **100,000,000,000.0000000 PI** at both ends of the quarter, identical to seven decimal places. Mobile mining does not mint PI; it is an app-side entitlement against that single genesis batch, and a mined Pi becomes real, counted supply only at the moment its owner completes verification and migrates it onto mainnet.

Sell #2 — vesting unlocks — is **zero**, despite a widely republished monthly "PI unlock" calendar that says otherwise. Pi Network has no vesting escrow and no cliff schedule. What the calendar tracks is pioneer lockups: individual holders electing their own lock terms wallet by wallet, held on-chain as millions of separately dated lock entries. Those coins are already inside the number Pi Network publishes as circulating supply, so a lockup expiring moves Pi from locked to spendable without adding a single unit to the counted float. The evidence is in the direction of travel: across **Jun 15 2026** to **Sep 1 2026** the locked pool actually fell from **6,221,091,142 PI** to **6,172,685,902 PI**, a drop of **48.41M PI**, while counted supply rose regardless. The two numbers are independent, which is exactly why the unlock calendar is the wrong number to read.

Sell #3 — foundation and unscheduled unlocks — is **413.02M PI**, and it is the entire supply story of this asset. Pi Network's own supply endpoint publishes circulating supply as a cumulative count of migrated mining rewards, and the two fields are byte-identical at every reading. Measured directly at the origin, that counter ran **10,784,186,673 PI** on **Jun 15 2026**, **11,041,721,727 PI** on **Aug 14 2026** and **11,141,680,597 PI** on **Sep 1 2026** — an increase of **357.49M PI** across **77.9 days**, or **4.59M PI** a day, which is **413.02M PI** over a full quarter. There is no schedule, no cliff and no announcement behind it. Migration arrives in batches whenever the Pi Core Team processes another cohort of verified Pioneers, and it accelerated within the window: **4.31M PI** a day through mid-August, then **5.50M PI** a day into September.

Sell #4 — long-term locked or bankruptcy — is **zero**. No bankruptcy estate holds PI and no court-supervised trustee distributes it, so nothing arrives from that side.

## Buy pressure: where new PI goes

Buy #1 — programmatic buyback — is **zero**. Pi Network operates no buyback contract and publishes no buyback programme. A sustained community campaign for an aggressive buy-and-burn was publicly declined by the Pi Core Team, whose stated position is that Pi Network's tokenomics are built around inclusive distribution to as many people as possible rather than around engineered scarcity. That is a design choice, not an oversight, and it means the buy side of this ledger has never carried a number.

Buy #2 — protocol fee burn — is **zero**, and Pi Network is the rarer shape where there is no burn address to check. Both surfaces were read anyway. The chain's total never moved off **100,000,000,000 PI**, and Pi mainnet has no incinerator account. What exists instead is a protocol fee pool, which rose from **8,677,825 PI** to **10,318,648 PI** across the window — a collection of **1.64M PI** that left the wallets which paid it. Those coins were moved, not destroyed: the ledger total never fell, and Pi Network's circulating figure is a running migration tally rather than a sum of balances, so a fee sink cannot decrement it. The fee pool is therefore tracked as an overhang, never booked as a buy.

Buy #3 — foundation buy — is **zero**. There is no disclosed treasury bid for PI and no reserve programme buying on the open market. The two genesis distribution accounts were read directly this session and neither sent anything anywhere inside the window; their last outbound transfer of any size was **1,000 PI** in **Nov 2024**.

Buy #4 — new long-term lock — is **zero**, for the mirror image of the reason Sell #2 is zero. When a Pioneer elects a fresh lockup, the Pi moves inside the same counted pool it already sat in, so nothing is absorbed and the published circulating figure does not fall. Across this window the locked pool shrank rather than grew, so even a classifier that did count locks would find no buy pressure here.

## Foundation and overhang

Pi Network carries the largest team-controlled overhang of any asset the framework tracks, and it is enumerable exactly. The first and largest piece is the un-mined remainder behind the cap: **100,000,000,000 PI** exists on the ledger, Pi Network's effective total stands at **17,141,047,073 PI**, and the difference — **82,858,952,927 PI** — has never been mined or migrated. It has no release schedule; it enters only as mobile mining continues, at a rate the Pi Core Team controls.

The second piece is the non-mining allocation that activates alongside migration. Pi Network's effective total is defined as migrated mining rewards divided by **0.65** — the community-mining share — and that identity closed to zero residual at all three readings taken this session. The remaining **35%**, currently **5,999,366,475 PI**, is the core team, Foundation and liquidity share, and it scales up pro rata every time migration advances. It carries no published release calendar of its own. The third piece is the pioneer lockup pool at **6,172,685,902 PI**, which sits inside the counted float and therefore changes the tradable supply without changing the published one. The fourth is the protocol fee pool at **10,318,648 PI**, which no account can spend.

All four are refreshed from Pi Network's own supply endpoint and the Pi mainnet ledger on every rebuild. If the un-mined remainder or the non-mining allocation falls between refreshes, the outflow enters Sell #3 at the next refresh. The lockup pool is the deliberate exception: a fall there raises the tradable float without raising counted supply, so it is surfaced as a float note rather than booked as a sell row.

## How PI compares to other fixed-supply chains

Against a halving-model chain with a hard cap, Pi Network looks superficially similar and behaves nothing like it. Both have a fixed ceiling minted by protocol rule, but a halving chain issues its remaining supply on a published, immutable schedule that anyone can compute years ahead. Pi Network minted its entire cap on day one and releases it through mainnet migration — a process gated by identity verification and processed in batches at a cadence the Pi Core Team sets. The ceiling is just as hard; the path to it is discretionary rather than algorithmic, and that is the difference that matters to a supply reading.

Against an uncapped continuous-emission layer-1, the comparison inverts. Those chains mint real new units every block and often burn a share of fees back, so their net reading is a contest between two live protocol mechanisms. Pi Network has neither: the chain issues nothing and destroys nothing, and its entire net reading comes from reclassification — supply that already existed becoming supply the market counts. A staking chain paying **5%** a year with a fee burn can end a quarter deflationary. Pi Network cannot, because it has no burn to run and its migration counter only moves upward.

Against exchange tokens with quarterly buybacks, the gap is starkest. Those tokens fund repurchases from operating revenue and destroy the result, producing a reliable negative supply line every quarter. Pi Network has an active user base numbering in the tens of millions and no revenue mechanism pointed at its own token, and the community campaign to build one was declined. The comparison is mechanism, not sentiment: PI's buy side is structurally, not incidentally, zero.

## What to watch in the next 90 days

The first watch line is the migration rate itself, which accelerated inside this window from **4.31M PI** a day to **5.50M PI** a day — if that tail rate holds through the next quarter rather than reverting, Sell #3 lands nearer **495M PI** than **413M PI**. The second is any announcement of a further migration phase or a change to verification throughput, since that is the only lever that moves this ledger. The third is the Protocol 27 upgrade expected in late **2026** with no fixed date, which should be checked for a supply mechanism even though its predecessor, completed **Aug 26 2026**, carried none. The fourth is the buy side: a single announcement of a buyback or a burn programme would be the first non-zero buy row PI has ever had, and the ledger total would have to fall below **100,000,000,000 PI** for it to be real. The fifth is the pioneer lockup pool at **6,172,685,902 PI**, which changes the tradable float even when the published figure does not move.

## Summary

Pi Network reads **+3.71% net** over the last 90 days and **+3.71%** projected forward, against a supply monitor reading **+4.63%**. Structurally PI is a zero-issuance chain with a structurally inflationary float: its whole **100,000,000,000 PI** supply was minted once on **Dec 31 2020**, the ledger total has not changed by a stroop, and every unit of measured sell pressure is pre-existing Pi becoming counted through mainnet migration at **4.59M PI** a day. The key risk is that the release has no schedule to price in — it is set by how fast the Pi Core Team processes verified Pioneers, and **82,858,952,927 PI** still sits behind the cap unmined. The ceiling is genuinely hard at **100,000,000,000 PI**, but with no buyback, no burn and no burn address on the chain, there is nothing on the buy side to offset the climb toward it.

---

*MrNasdog Pressure Framework analysis of PI, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 2 2026.*
