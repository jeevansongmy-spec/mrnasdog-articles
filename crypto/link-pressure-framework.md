---
title: "LINK Inflation Analysis · September 2026 · Mixed last 90D · projected to grow"
description: "LINK supply was flat for 90 days, but Chainlink's reserve releases of 18.75M and 11.25M LINK are due next: about +4.01% in 90 days. Fixed 1B supply, no mint, no burn."
canonical_url: "https://mrnasdog.com/research/link/inflation"
tags: ["crypto", "link", "chainlink", "oracles"]
published: true
---

> Originally published at **[mrnasdog.com/research/link/inflation](https://mrnasdog.com/research/link/inflation)** by MrNasdog.

# LINK Inflation Analysis · September 2026 · Mixed last 90D · projected to grow

**Chainlink (LINK)** added **no new coins** to the market in the last 90 days, but about **30.0M LINK** is due to leave the project’s reserve wallets in the next 90 — a net rise of about **+4.01%** of circulating supply. LINK has a fixed supply of **1B** and no mint; all new selling pressure comes from Chainlink releasing its own reserve, about **7%** of total supply a year, in fixed steps. Our monitor reads **−0.03%** for the same 90 days, so the two readings agree.

## The verdict, in one paragraph

Over the 90 days to **Sep 29 2026**, LINK’s net supply change was **0.00%**: no LINK left the reserve, none was burned, and nothing was minted. The monitor measured **−0.03%** over the same window, a gap of **0.03 percentage points** — well inside our 0.5-point tolerance, so no warning chip is shown. The flat reading is a pause, not a new trend: the next 90 days are projected at **+4.01%**, because two scheduled reserve releases, **18.75M** and **11.25M LINK**, both fall inside the window. In one line: **LINK is a fixed-supply token whose float grows in quarterly steps from a team-held reserve.**

## Sell pressure: where new LINK comes from

**Protocol inflation is zero, permanently.** All 1B LINK were created when the Chainlink token launched in 2017. We read the token contract’s code this build: it has no mint function, no owner and no upgrade path, so no one can create more LINK. Node operators and stakers are paid from LINK that already exists.

**Vesting unlocks are zero.** LINK has no vesting calendar left. The 2017 token sale is long spent, and unlock trackers list Chainlink as fully unlocked. The coins not yet in the market are not vesting to anyone — they sit in Chainlink’s own reserve wallets and move only when the project releases them.

**Foundation and unscheduled unlocks are the whole story: 0 LINK in the last 90 days, 30.0M LINK projected for the next 90.** Chainlink publishes a list of 33 non-circulating wallets. Together they hold **251.9M LINK**, and 1B minus that figure equals the circulating count of **748.10M LINK** to the last unit. We read all 33 at both ends of the window, and their total did not move. The last release was **21M LINK on Jun 19 2026**, twelve days before the window opened; most of it went to an exchange deposit address and the rest to a team payout wallet.

The releases follow a fixed turn. Since mid-2023 Chainlink has let out **21M**, then **18.75M**, then **11.25M**, then **19M** LINK, and started over — **70M LINK** per cycle, which is the **7% of total supply per year** the project states. The autumn 18.75M came on Sep 15 2023, Sep 20 2024 and Oct 10 2025; this year it has not come yet, so it lands in the next 90 days. The December 11.25M came on Dec 15 2023, Dec 20 2024 and Dec 19 2025 — the third Friday each time — which puts the next one on **Dec 18 2026**. Together that is **30.0M LINK**. If the December release slips into the new year, the next-90-day figure falls to 18.75M LINK, or about +2.51%.

**Long-term locked or bankruptcy supply is zero.** There is no bankruptcy estate, trustee schedule or unwinding lock that holds LINK. Funds and listed companies that hold LINK bought it in the market, so those coins were already counted.

## Buy pressure: where new LINK goes

**The programmatic buyback books 0 LINK, even though it is real.** The Chainlink Reserve buys LINK every week with fees paid for Chainlink services — including fees paid in stablecoins or other tokens, which are swapped into LINK — and keeps it. In the last 90 days it bought **1.54M LINK** in 13 weekly deposits and took nothing out; it now holds **6.05M LINK**. Chainlink says it does not expect to withdraw from the Reserve for years. But the Reserve wallet is not one of the 33 non-circulating wallets, so its LINK is counted as circulating. Buying into it moves coins from one circulating wallet to another, and our ledger books that as zero. If Chainlink ever moves the Reserve outside the circulating count, the same buying would start to count here.

**The protocol fee burn is zero.** Chainlink does not burn fees. Total supply read exactly 1B LINK at both ends of the window, the token has no burn function, and the common dead address gained less than 1 LINK of stray sends.

**Foundation buying is zero.** Outside the Reserve, no team or treasury purchase of LINK was announced or seen on-chain in the window.

**New long-term locks are zero.** Chainlink staking is full: the community pool holds its cap of **40.88M LINK**, and node operators stake about **1.65M LINK** more. Staked LINK stays in the circulating count, and the pool cap did not change, so staking removed nothing new from the market this window.

## Foundation and overhang

The main overhang is the reserve itself: **251.9M LINK** across Chainlink’s 33 listed non-circulating wallets, about a quarter of all LINK. At 70M LINK a year, it would last a little over three and a half years. Most of it sits in seven wallets of 30M LINK each and one of 22M; about 20M sits in smaller wallets that have funded recent releases. We read these balances from the chain at every rebuild.

Three more team-linked wallets are tracked even though they already count as circulating. The Chainlink Reserve holds **6.05M LINK** and sent nothing out this window. A team payout wallet that takes a slice of each release fell from **11.06M** to **9.56M LINK** this window as it paid out. The staking reward vault holds **2.75M LINK** and pays stakers from it. Moves out of these three wallets add nothing new to the market count. If the reserve wallets’ balance falls between our refreshes, the outflow enters the foundation-and-unlocks row at the next refresh; if the Reserve ever sends LINK out, that outflow is tracked the same way.

## How LINK compares to other oracle tokens

Among oracle and data-network tokens, LINK sits in the fixed-supply, reserve-release group. Its supply cannot grow past 1B, and the only question is how fast the team lets the reserve out. That is different from a token that pays its network with continuous new issuance, such as The Graph’s GRT, where supply grows a little every day and a small fee burn works against it. LINK issues nothing day to day; its float grows in four steps a year and stands still in between.

It is also different from a token with a large cliff schedule, such as Pyth’s PYTH, where big blocks of locked tokens open on fixed yearly dates set at launch. LINK’s releases are smaller — about 1.1% to 2.1% of total supply each time — and they follow a stated yearly rate, not a contract lock, so the team could change the pace. The one mechanism on the buy side, the Chainlink Reserve, is a fee-funded accumulator rather than a burn: it takes LINK off exchanges but keeps it inside the circulating count, where a fee burn like Ethereum’s would destroy it.

Against a hard-capped coin like Bitcoin, LINK is similar in one way — a fixed ceiling — and different in another: Bitcoin’s remaining supply comes out on a code-set schedule, while LINK’s comes out when Chainlink decides, at a pace it has kept for three years.

## What to watch in the next 90 days

**The autumn release of 18.75M LINK**, due now; it came on Oct 10 last year. It will show as a drop in the 33 reserve wallets and a deposit at an exchange.

**The December release of 11.25M LINK**, expected on Dec 18 2026, the third Friday of December, as in each of the last three years.

**The Chainlink Reserve**: it now adds roughly 90,000 to 100,000 LINK a week. Any withdrawal, or any change in whether it counts as circulating, would change the buy side.

**Staking changes**: a bigger staking cap or a new staking pool would lock more LINK, but staked LINK still counts as circulating, so it would not change this ledger unless that changes too.

## Summary

Chainlink’s LINK has a fixed supply of 1B and no mint, so its circulating supply grows only when Chainlink releases LINK from its own reserve — **251.9M LINK** in 33 listed wallets, let out at about 7% of total supply a year. The last 90 days were flat at **0.00%**, in line with the monitor’s **−0.03%**, but two releases totalling **30.0M LINK** are due by the end of December, for about **+4.01%**. The Chainlink Reserve keeps buying LINK with fees and now holds 6.05M, but it counts as circulating and does not offset the releases. The ceiling is firm: at the current pace, the reserve runs out in a little over three and a half years.

---

*MrNasdog Pressure Framework analysis of LINK, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*
