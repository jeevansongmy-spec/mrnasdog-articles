---
title:         "WLD Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description:   "World reads +5.90% net supply to market per 90 days: a fixed 10B-cap token that cannot mint or burn, so all pressure is the release of pre-minted WLD, cut 43% on Jul 24 2026."
canonical_url: "https://mrnasdog.com/research/wld/inflation"
tags:          ["crypto", "wld", "worldcoin", "tokenomics"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/wld/inflation](https://mrnasdog.com/research/wld/inflation)*

# WLD Inflation Analysis · August 2026 · Supply growing, projected to keep growing

World (WLD) is the heaviest unlocker in our coverage, and the strange part is that its contract **cannot mint a single new token**. WLD is hard-capped at **10 billion**, every one of them created at launch, so supply pressure is never issuance — it is the speed at which World hands the pre-minted pile out. Over the 90 days to **Aug 16 2026** we measured **256.9M WLD** leaving World's lock, treasury and custody wallets, against **44.4M** that went straight back into new lock contracts, for a net **+5.90%** of circulating supply. Our supply monitor reads **+6.25%**, a gap of **0.35** percentage points, which is inside tolerance and needs no warning note. The release rate was cut **43%** on **Jul 24 2026**, which drops the forward reading to **+4.62%** — lighter, and still heavy.

## The verdict, in one paragraph

For the 90-day window ending **Aug 16 2026**, the Pressure Framework reads **WLD at +5.90% net**. Sell pressure is **256.9M WLD**, buy pressure is **44.4M WLD**, and the circulating base is **3.60B WLD**. Our supply monitor reads **+6.25%**, so the gap is **0.35** percentage points — under the half-point line, so no monitor-gap note ships on the WLD overview. The two readings are closer than that number suggests: the monitor implies **211.8M** WLD of net flow and we measured **212.5M**, a difference of three-tenths of one percent, with the small residual coming from the monitor dividing by the float of 90 days ago while we divide by today's. World is best described as **a fixed-cap token that is inflationary purely by release schedule, with nothing on the buy side to slow it**.

## Sell pressure: where new WLD comes from

Sell #1, protocol inflation, is **zero**, and that is the defining fact about WLD. All **10 billion** tokens were created at genesis on **Jul 24 2023**. We read total supply directly on the Ethereum token contract at both ends of this window and it was **10,000,000,000** on both dates, unchanged to the last decimal. There is no block reward, no staking emission and no live mint path. Governance cannot add supply at all before **Jul 24 2038**, and even then only up to **1.5%** a year. Nothing the market experiences as WLD inflation is new minting.

Sell #2, vesting unlocks, carries **193.2M WLD** and is the engine of the whole reading. The single largest event was **Jul 24 2026**, when **157.4M WLD** left World's release safe in one batch and landed in twelve team, investor and ecosystem wallets. A second, quieter stream runs alongside it: the eight custody contracts that have held team and investor tokens since the first unlock cliff in **Jul 2024** paid out another **35.8M WLD** across the window. That second stream is the flow a single-chain reading misses, and finding it is what closed the gap against our supply monitor this build. On the published schedule, the team and investor release rate was cut from **1.9M** to **1.3M** WLD a day on the same July date — a **32%** reduction.

Sell #3, foundation and unscheduled unlocks, carries **63.7M WLD**. World's operating treasury safe spent **36.9M** over the window, and the grant wallets on World Chain that pay verified users sent out a further **26.8M**. That grant stream is winding down: from **Jun 1 2026** World stopped creating and renewing yearly grant cycles, so anyone who verifies their World ID from that date forward receives no WLD at all, and existing cycles simply run out. The wallet that pays recurring user grants shows it plainly — it fell from **16.0M** to **7.4M** WLD, and most of that drain happened before the July cut.

Sell #4, long-term locked or bankruptcy, is **zero**. World has never been through an insolvency, there is no estate and no trustee selling a recovered position into the market. Nothing enters the WLD float from that direction, now or later.

## Buy pressure: where new WLD goes

Buy #1, programmatic buyback, is **zero**. World has never repurchased WLD, and no buyback contract exists that could be switched on. Buy #2, protocol fee burn, is also **zero**, and it cannot be anything else: World Chain charges gas in ETH, not in WLD, so no amount of network usage destroys a token. The WLD contract has no burn path in use, which means the **10 billion** cap is also a floor — the supply can never shrink. Buy #3, foundation buy, is **zero** as well; the World Foundation funds the network by selling its own allocation, and no purchase has ever been disclosed or seen on chain.

Buy #4, new long-term lock, is the one non-zero entry on this side at **44.4M WLD**, and it deserves a careful reading because it is not demand. Of the **157.4M** released on **Jul 24 2026**, four recipients did not receive tokens they could sell. Their share went into four freshly deployed lock contracts, and we read those contracts directly: each has a start date of **Jul 24 2027** and a vesting length of zero, which is a hard cliff. Not one of those **44.4M** WLD can move for another year. That is real removal of supply from the tradable float for this window, so it is booked as a buy-side offset — but it is deferral, not absorption, and it comes back as sell pressure on a known date.

## Foundation and overhang

What World still controls dwarfs what it has released. Three community lock contracts on Ethereum hold **3.50B WLD** between them: **1.75B** in the tranche that began releasing on **Jul 24 2026** and runs three years, plus **875M** that starts in 2029 and **875M** that starts in 2032. The tranche now running gives the clearest confirmation of the July cut we have: **1.75B** spread over **1,096** days is **1.597M** WLD a day, which is exactly the **1.6M** community rate World announced.

On top of the lock contracts, World's release safe held **1,398M WLD** at the end of this window, up from **956M**, because the matured first tranche emptied **674.6M** into it on **Aug 11 2026**. The operating treasury safe holds **69.7M**, the grant and campaign wallets on World Chain hold **131M**, the eight team and investor custody contracts hold **940M**, and the four new cliff contracts hold **44.4M** until **Jul 24 2027**. Add it up and roughly **6.08B WLD** sits outside the market in identified, watchable wallets. Every one of those balances is read fresh at each refresh, and if any of them falls between refreshes the outflow enters Sell #3 at the next refresh.

## How WLD compares to other fixed-cap unlock-driven tokens

WLD sits in an unusual corner. Its cap behaves like Bitcoin's — a fixed **10 billion** that governance cannot raise for another twelve years — but the resemblance stops there. Bitcoin's supply grows because miners are paid new coins, and that rate halves on a schedule nobody controls. WLD's supply does not grow at all; what grows is the tradable share of a pile that was complete on day one. That distinction matters for anyone reading a supply chart: a Bitcoin holder waits out a halving, while a WLD holder waits out a distribution calendar that runs to **2038**.

Against uncapped continuous-emission chains, WLD is both better and worse. A proof-of-stake L1 that issues **5%** a year issues it forever, but a large share is paid to stakers who compound rather than sell, and fee burning can claw some of it back. WLD has neither. There is no staking sink, no fee burn, and no buyback, so **every** WLD that leaves a lock contract lands somewhere it can be sold. Exchange tokens with quarterly buybacks are the opposite pole: their unlocks are offset by a purchase programme funded by revenue, so their net reading can be negative. WLD's net can only ever be zero or positive.

The closest structural analogues are other large airdrop-and-vest launches — tokens with a small day-one float, a multi-year distribution calendar and no destruction path. What separates World is scale and duration: a fifteen-year calendar and a float that is still only **36%** of the cap. Even after the **43%** cut, roughly **2.9M** WLD unlocks every day. The July cut is a genuine improvement in the reading, but it changes the slope, not the direction.

## What to watch in the next 90 days

First, whether the release safe stays full. It held **1,398M WLD** after the **Aug 11 2026** transfer, and that is now the single biggest discretionary pool in WLD; a large outflow from it would move Sell #3 immediately. Second, the grant wallets on World Chain — with new cycles stopped since **Jun 1 2026**, the recurring wallet should keep draining and then flatten, and a flat line there is the clearest sign the user-grant era has ended. Third, the eight custody contracts, which paid out **35.8M** this window at a visibly slower rate after the July cut. Fourth, the operating treasury safe, which spent **36.9M** before **Jul 24 2026** and nothing since; it fires in lumps with no published calendar, so it is the largest single source of surprise in the forward number. Fifth, the four cliff contracts that unseal **44.4M WLD** on **Jul 24 2027** — outside this window, but the date is already fixed.

## Summary

World (WLD) is a hard-capped **10 billion** token that cannot mint and cannot burn, so its inflation is entirely a distribution schedule rather than issuance. Over the 90 days to **Aug 16 2026**, **256.9M WLD** left World's lock, treasury and custody wallets while **44.4M** was re-locked until **Jul 24 2027**, a net **+5.90%** of circulating supply against a supply monitor at **+6.25%**. The **43%** release cut on **Jul 24 2026** and the end of new grant cycles on **Jun 1 2026** both lighten the forward reading to about **+4.62%**. The risk is not that new WLD appears — it never will — but that roughly **6.08B WLD** still sits outside the market with a calendar that runs to **2038**, and with no buyback, no burn and no staking sink, the only thing standing between that pile and the float is time.

---

*MrNasdog Pressure Framework analysis of WLD, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 17 2026.*
