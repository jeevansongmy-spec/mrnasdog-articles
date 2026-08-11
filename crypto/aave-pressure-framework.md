---
title:         "AAVE Inflation Analysis · August 2026 · The buyback and the reward stream cancelled out"
description:   "AAVE is capped at 16M with no mint and no burn. The DAO reserve released 20.6K AAVE while the buyback bought and kept 20.2K. Framework 0.00% net; monitor +1.55%."
canonical_url: "https://mrnasdog.com/research/aave/inflation"
tags:          ["crypto", "aave", "aavenomics", "defi"]
published:     true
---

*Originally published at [mrnasdog.com/research/aave/inflation](https://mrnasdog.com/research/aave/inflation)*

Aave is one of the very few coins in this coverage where the sell side and the buy side actually cancel. AAVE is capped at **16,000,000** and was fully minted in the 2020 migration, so nothing can be created and nothing is ever burned; the tradable float is simply sixteen million minus whatever the Aave DAO Ecosystem Reserve still holds. Over the last 90 days that reserve released **20.6K AAVE** of Safety Module staking rewards, while the DAO's revenue-funded buyback bought and kept **20.2K AAVE** — a net of **0.00%**, against our supply monitor at **+1.55%**.

## The verdict, in one paragraph

For the 90-day window ending **Aug 11 2026**, the Pressure Framework reads **AAVE at 0.00% net**. Sell pressure totals **20.6K AAVE**, buy pressure totals **20.2K AAVE**, against a circulating base of **15.42M AAVE**. Our supply monitor reads the same window at **+1.55%**, a gap of **1.55 percentage points**, so a monitor-gap chip ships on the overview page: the monitor's figure comes from a single-day supply-count restatement of **236.4K AAVE** on **Jul 19 2026** that no chain event matches, not from coins reaching the market. The forward reading is **+0.09%**, because the Safety Module keeps paying while the buyback has not shown up on chain since **Jun 29 2026**. AAVE is best characterised as a **hard-capped coin whose entire inflation question is one reserve balance**.

## Sell pressure: where new AAVE comes from

Sell #1, protocol inflation, is **20.6K AAVE**, and the label needs a caveat because Aave has no protocol inflation in the usual sense — no block reward, no mint function anyone can call. On-chain the AAVE total supply read exactly **16,000,000** at both ends of the window. What behaves like emission is the **Aave DAO Ecosystem Reserve**, the single non-circulating pool, paying **Safety Module** staking rewards to stkAAVE holders. Reading that reserve directly, its balance fell from **598,048** to **577,424** over the 90 days — the **20.6K AAVE** that stakers actually claimed and could actually sell. The framework books the realised drawdown rather than the accrual, because the reserve is a readable escrow and unclaimed rewards are not float.

The forward number is lower, and for a documented reason. Aave governance executed **AIP 491** on **Jun 13 2026**, cutting the stkAAVE emission rate from **220 AAVE per day** to **150 AAVE per day** to target a lower staking yield. That step is visible in the staking contract's own emission parameter, not just in the forum thread, and it landed inside this window — so the trailing average blends a retired rate with the live one. The next-90-day column is re-based on the post-cut rate at **13.5K AAVE**. A second reward stream, the AAVE incentive on staked GHO, has already run to zero, so the Safety Module is now the reserve's only outlet.

Sell #2, vesting unlocks, is **zero**: every AAVE was created at once in the LEND migration and there is no vesting contract, no cliff and no calendar left to run. The old migration contract emptied its final **302,384 AAVE** into the DAO reserve on **May 9 2026**, before this window opened, which closed the last loose end. Sell #4, long-term locked or bankruptcy, is **zero**: there is no Aave estate, no trustee and no court-ordered distribution. Sell #3, Foundation and unscheduled unlocks, is also **zero** for the window — no public evidence of a discretionary release — but it is the row with the largest latent capacity, and it is covered below.

## Buy pressure: where new AAVE goes

Buy #1, the programmatic buyback, is **20.2K AAVE** and it is the reason this quarter nets to nothing. The Aave DAO buys AAVE on the open market with protocol revenue, executed by a four-member finance committee multisig, and the acquired coins are **held, never burned** — the committee parks its stack by supplying it into the Aave lending market, where the balance is readable. That stack grew from **220,308** to **240,502** over the window. Weekly sampling puts every unit of the increase between **Jun 15 2026** and **Jun 29 2026**: the buyback had been paused since **Apr 19 2026** after a collateral incident, restarted mid-June, and then went quiet on chain again.

This is worth stating plainly, because it is easy to read the buyback as circulating-neutral and conclude nothing was bought. The committee does not hold raw AAVE — it holds the interest-bearing receipt token from supplying that AAVE into the lending market. Look only at raw AAVE balances in DAO wallets and the buyback appears to have done nothing; read the receipt-token balance and the purchase is right there, **+20,194 AAVE bought and kept**.

The forward column ships that row at **zero**, which needs explaining. **Aavenomics 3.0** went live on **Jun 27 2026**, replacing the committee's discretionary schedule with an automated engine and routing all Aave protocol and GHO revenue to the DAO treasury; the annual buyback budget had already been trimmed from about **$50M** to about **$30M** in March 2026. The programme is live and funded. But in the **43 days** since **Jun 29 2026**, no AAVE has landed in any Aave DAO wallet — not the committee safe, not the swapper, not the collector, not the reserve — and a scan of the largest holders over the same period turns up no DAO-controlled address accumulating. The framework projects from what it can observe after a dated mechanism change, so the row is carried at zero and monitored rather than credited forward on a rate nobody can see.

Buy #2, protocol fee burn, is **zero** because AAVE has no burn at all: supply has been fixed at **16,000,000** since 2020 and not one coin has ever been destroyed. This matters more than it sounds. A buyback that burns shrinks supply permanently; a buyback that holds only moves coins into custody, where a future governance vote can send them back out. Buy #3, Foundation buy, is **zero** because the DAO's only market purchases are the buyback above and counting them twice would overstate the buy side. Buy #4, new long-term lock, is **zero**: Safety Module staking grew by roughly **409K AAVE** over the window, but staked AAVE still counts as circulating and exits after a short cooldown, so it is a holder preference, not supply taken off the market.

## Foundation and overhang

Three team-controlled pools are tracked. The **Aave DAO Ecosystem Reserve** holds **577.4K AAVE** — the entire non-circulating bucket, drawn down only by the staking-reward stream, with no published release schedule for the rest. The **buyback stack** holds **240.5K AAVE** supplied into the lending market by the finance committee; those coins already count as circulating, so if the DAO ever sold them the market would feel it even though the headline supply figure would not move. Third, a reported exchange transaction — **250,000 AAVE** plus equity for **35,000 ETH**, reported **Jun 25 2026** — has never been put to a DAO vote or executed, so it stays a watch item at zero. Each balance is re-read every rebuild, and if any of the three falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How AAVE compares to other DeFi governance tokens

The first comparison is cap versus emission. Uncapped lending and DEX tokens mint fresh supply through liquidity-mining curves, so their inflation scales with usage and never really ends. AAVE cannot mint at all — the 16M ceiling was set once and the supply has been complete for six years — so its worst case is bounded by the **577.4K AAVE** still sitting in the reserve, about **3.7%** of supply. That is a genuinely small ceiling by the standards of this coverage, and it is why AAVE reads near flat even in a quarter when the buyback goes quiet.

The second comparison is buy-and-burn versus buy-and-hold, and it is where AAVE differs from the exchange tokens it is often grouped with. Exchange tokens that run quarterly buybacks usually send the coins to a burn address, which removes them permanently and shows up as an outright supply decline. Aave buys with real revenue but keeps the coins in DAO custody for governance-approved programmes. Economically the purchase is still a bid; in supply terms it is not deflation, because nothing is destroyed and the treasury can redeploy the stack. The result is a token that looks flat rather than shrinking: over this window the buyback matched the reward stream almost exactly, which produces a net of zero rather than a negative.

## What to watch in the next 90 days

First, whether the automated buyback reappears on chain — nothing has entered DAO custody since **Jun 29 2026**, and a resumption would flip the forward reading from **+0.09%** back toward zero or below. Second, the reserve drawdown at the new **150 AAVE per day** rate, which is now the only source of new float and sets the entire sell side. Third, any governance move to point bought AAVE at a burn address instead of the treasury, which would turn the buyback from price support into genuine supply reduction. Fourth, the reported exchange transaction: if it goes to a vote, **250,000 AAVE** from the DAO would be the largest single supply event in years. Fifth, whether the reward rate is cut again — the same proposal track that produced the **Jun 13 2026** reduction remains open.

## Summary

The MrNasdog Pressure Framework reads AAVE at **0.00% net** over the last 90 days and **+0.09%** over the next 90. The structural mechanism is unusually simple: a hard cap of **16,000,000** that was fully minted in 2020, no mint and no burn, and a tradable float that is just sixteen million minus the **577.4K AAVE** the DAO reserve still holds. The key risk is that the buyback holds rather than burns, so the offset can stop at any time — as it appears to have done since **Jun 29 2026** — and the stack it has built can be redeployed by a vote. The ceiling is the comfort: even if the reserve emptied completely, AAVE's float could only grow by about **3.7%**, and there is no mechanism anywhere that can take it past sixteen million.

---

*MrNasdog Pressure Framework analysis of AAVE, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 11 2026.*
