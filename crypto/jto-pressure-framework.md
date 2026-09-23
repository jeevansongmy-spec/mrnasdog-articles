---
title:         "JTO Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "JTO supply grows 6.78% in 90 days and 5.02% next as team and investor tokens unlock every day to Dec 7 2026. Jito cannot mint JTO; its JTX burn is still small."
canonical_url: "https://mrnasdog.com/research/jto/inflation"
tags:          ["crypto", "jito", "solana", "jto"]
published:     true
---

Originally published at [JTO Inflation Analysis · September 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/jto/inflation).

# JTO Inflation Analysis · September 2026 · Supply growing · projected to keep growing

JTO supply is growing and is projected to keep growing until the team and investor vesting ends on **Dec 7 2026**. The Pressure Framework books **35.86M JTO** of sell pressure against **0.34M JTO** of buy pressure over the last 90 days, a net of **+6.78%**, and **+5.02%** for the next 90 days; the inflation monitor reads **+8.25%**. Jito can never mint another JTO, because the token's mint authority is gone, so every point of this comes from tokens that already exist becoming tradable.

## The verdict, in one paragraph

Against a circulating base of **524.1M JTO**, the framework reads **+6.78%** over the trailing 90 days and **+5.02%** forward. The monitor reads **+8.25%**, a gap of **1.47 percentage points**, which is over the framework's 0.5-point tolerance, so the JTO overview carries a monitor-gap warning. Most of that gap is explained: **0.63 points** is the monitor dividing by the smaller supply of 90 days ago, **0.37 points** is **1.95M JTO** that vested inside Jito's on-chain vesting program but was never withdrawn, and **0.12 points** is the monitor's own supply estimate running slightly above the counted float. The last **0.35 points** was not traced to any wallet, so the framework keeps its own number. The label for JTO: **a fixed-supply token in the last quarter of its insider unlock**.

## Sell pressure: where new JTO comes from

Protocol inflation is **0**, and it is 0 for good. JTO is a standard Solana SPL token whose mint authority was removed, which means the token program rejects every attempt to create new JTO and no Jito DAO vote can switch minting back on. The JTO supply can only go down: **986.5M JTO** exist today against **1,000M** at launch, after **13.48M JTO** were burned by buybacks before this window.

Vesting unlocks are the whole story, at **31.52M JTO**. At launch on **Dec 7 2023**, **245M JTO** went to core contributors and **162.1M JTO** to investors, on a three-year plan with a one-year cliff. Jito's own on-chain vesting program spells the terms out exactly: one third unlocked on **Dec 7 2024**, and the other two thirds unlock in **730** equal slices, one per day, that end on **Dec 7 2026**. Most of the team and investor JTO was paid into ordinary wallets, so for that part the calendar decides, at about **0.34M JTO a day**, or **30.45M JTO** over 90 days. A smaller slice of **36.6M JTO** sits inside the vesting program itself, and there the framework counts only what holders actually withdrew: **1.06M JTO** this window, against **3.01M** that the calendar made available. Nothing here is new supply. It is existing JTO turning from locked into tradable.

Foundation and unscheduled unlocks add **4.34M JTO**. The Jito Foundation's liquidity wallet sent **4.0M JTO** on **Jul 13 2026**, the day before the JTX trading app opened, to an actively trading outside wallet, and paid **0.34M JTO** of monthly liquidity rewards on **Jul 7**, **Aug 6** and **Sep 2 2026**. Long-term locked or bankruptcy releases are **0**: JTO has no bankruptcy estate and no court-ordered payout.

## Buy pressure: where new JTO goes

Programmatic buyback is **0.34M JTO**. The Jito DAO passed JIP-38 on **Jul 13 2026**: **80%** of JTX platform fees go to the DAO, and all of that is committed to buying and burning JTO until late 2027. When a JTX fee is paid in JTO, it lands directly in the Jito DAO treasury, which sits outside the circulating supply, and **0.34M JTO** arrived that way this window. None of it has been burned yet; it is waiting in the treasury.

Protocol fee burn is **0**, and both burn surfaces were read. The JTO supply moved by only a few thousand tokens in 90 days, all from users burning dust as they close empty accounts, and the known burn addresses hold under **1 JTO** between them. Foundation buy is **0**: JIP-37 told the DAO's cryptoeconomics subDAO to buy JTO at par with protocol revenue from **Jul 1** to **Sep 30 2026**, but no fills and no wallet were published, so nothing is credited. New long-term lock is **0**: the **21.2M JTO** deposited for voting and about **5.2M JTO** staked can both be withdrawn at any time.

## Foundation and overhang

The biggest JTO holding is the Jito DAO treasury at **209.8M JTO**. It rose over the window, from **209.42M** to **209.77M**, on JTX fees alone, and it has no release calendar; any spend needs a DAO vote. Next come Foundation-linked wallets holding about **90M JTO**, including a new wallet that received **15M JTO** from the Foundation on **Jul 7 2026** and has not moved since. The vesting program still holds **7.6M JTO**, of which about **5.1M** is already vested but not withdrawn. Jito Labs has also said some later employee grants vest on their own three- to four-year clocks, with dates it does not publish. All of these balances are read on-chain at every rebuild. If any of them falls between refreshes by more than the calendar explains, that outflow enters the Foundation row at the next refresh.

## How JTO compares to other fixed-supply governance tokens

JTO belongs to the class of tokens whose supply is fixed in code and can only shrink. That is a stronger promise than a halving chain like Bitcoin, which still mints on every block, and far stronger than an uncapped proof-of-stake chain that pays stakers with new coins every epoch. On the issuance axis alone, JTO scores as well as a token can.

And yet JTO reads **+6.78%** a quarter, far above a mid-cycle Bitcoin. The reason is the difference between total supply and tradable float. A fixed cap stops new tokens; it does not stop old tokens from unlocking. JTO looks less like a mature capped coin and more like any venture-backed token near the end of a three-year insider vest. What sets it apart is the shape: a straight line, day after day, with no monthly cliff to trade around, and a hard end date.

The other comparison is with exchange tokens that buy back and burn from fee revenue, where the burn can outrun issuance and push supply down. Jito now has that machine on paper, through JIP-38 and JTX. For now it is small: **0.34M JTO** of fees against **35.86M JTO** of unlocks. The comparison flips only after Dec 7 2026, when the unlock stops and the fee burn becomes the only moving part.

## What to watch in the next 90 days

First, the vesting calendar: about **25.4M JTO** unlocks for wallet-held team and investor tokens between now and the final day, **Dec 7 2026**, after which the published calendar is empty. Second, **Sep 30 2026**, when the JIP-37 buyback mandate and the current BAM subsidy period end and the DAO decides where protocol revenue goes next; a vote routing it to buybacks would add a real buy row. Third, the first JIP-38 burn: the DAO treasury holds the JTX fees but has burned none, and a burn would show up as a drop in total supply. Fourth, the Foundation-linked wallet that took **15M JTO** on **Jul 7 2026**; if it starts sending, that is new sell pressure. Fifth, the monthly liquidity rewards of about **0.1M JTO**.

## Summary

The MrNasdog Pressure Framework reads JTO at **+6.78%** over the trailing 90 days and **+5.02%** projected forward: supply growing, projected to keep growing. The mechanism is unlock, not inflation: Jito cannot mint JTO, and **31.52M** of the **35.86M JTO** sell pressure is the three-year team and investor vest paying out a slice every day. The key risk is that this continues every day until **Dec 7 2026** regardless of price, while the JTX buy-and-burn has taken in only **0.34M JTO** and burned none. The ceiling is the comfort: **986.5M JTO** exist, and that number can only fall.

MrNasdog Pressure Framework analysis of JTO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.
