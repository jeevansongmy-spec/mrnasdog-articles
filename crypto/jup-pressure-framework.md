---
title:         "JUP Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "JUP supply is roughly steady: no mint, frozen reserves and a 948K JUP fee burn cut supply 0.03% in 90 days, while the Litterbox buyback holds its 173M JUP."
canonical_url: "https://mrnasdog.com/research/jup/inflation"
tags:          ["crypto", "jup", "jupiter", "defi"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/jup/inflation](https://mrnasdog.com/research/jup/inflation)*

# JUP Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

JUP supply was roughly steady over the last 90 days and is set to stay that way. No new JUP can be created, nothing new was released, and a batch burn of verification fees destroyed **948,317 JUP**, so the circulating supply of **3.32B JUP** shrank by **0.03%**. The monitor reads **−0.02%**. The one big question is the **3.54B JUP** in locked reserves: they did not move, and a community vote keeps team vesting paused.

## The verdict, in one paragraph

Over the 90 days from Jul 1 to Sep 29 2026, JUP supply fell by **0.03%** of the circulating float: **0 JUP** of sell pressure against **948,317 JUP** of buy pressure, all of it burned. For the next 90 days the ledger projects **0 JUP** of new supply against about **4,554 JUP** of small burns, which rounds to **0.00%**. The monitor, which measures the circulating count directly, reads **−0.02%** over the same 90 days — a gap of under **0.01 percentage points**, well inside our tolerance, so no warning chip applies. In one line: Jupiter is a fixed-supply token whose reserves are frozen for now, with a buyback that buys and holds rather than burns.

## Sell pressure: where new JUP comes from

Protocol inflation is **0 JUP**. JUP is a standard Solana token whose mint authority is empty, and an empty mint authority can never be set again, so no new JUP can ever be created. Every change to total supply from here is a burn, which can only make it smaller. Total supply now sits at **6.86B JUP**, down from 10B at launch after a 3B burn in January 2025 and a burn of the Litterbox holdings in November 2025.

Vesting unlocks are **0 JUP**. The team reserve used to send **116.67M JUP** to the team every three months, and its last payment went out on Jan 31 2026. Then the community passed the Net-Zero Emissions vote in February 2026, which paused team vesting, postponed the 2026 Jupuary airdrop and promised that Jupiter would buy back what the old Mercurial investors sell. The team cold wallet has not moved since. The Mercurial investor streams still release about **0.91M JUP** a quarter until Dec 23 2026, but those coins are already counted as circulating, so they add nothing new.

Foundation and unscheduled unlocks are **0 JUP**. The three reserves that sit outside the circulating count — the community cold wallet with **1.70B JUP**, the team cold wallet with **1.68B JUP** and one more reserve with **159.89M JUP** — had no transactions in the window. Other Jupiter wallets were busy: the community hot wallet paid a **47.9M JUP** staking-reward round on Jul 7 2026, and a team wallet sent out **72M JUP** in July and August. Those coins were already inside the circulating count, and the count did not move when they left, so they are moves within the market, not new supply.

Long-term locks and bankruptcy releases are **0 JUP**. There is no estate or trustee holding JUP, and the team members' own locks open from Jan 31 2027, after this window.

## Buy pressure: where new JUP goes

The programmatic buyback books **0 JUP**, even though it is the biggest flow on the page. Half of Jupiter's on-chain revenue buys JUP on the market for the Litterbox Trust. The Trust bought **28.75M JUP** in the 90 days, taking its balance from **144.31M** to **173.06M JUP**, and sold nothing. But it holds what it buys. Those coins are still counted as circulating, so for supply the buyback is a transfer from sellers to a Jupiter wallet, not a removal. It would count the day the Trust burns them, as the community voted to do with the first 130M in November 2025.

The fee burn is **948,317 JUP**. Projects that want a fast token check on Jupiter pay 1,000 JUP, and Jupiter burns those fees in batches from a multisig. One batch destroyed **943,764 JUP** on Sep 10 2026, and holders burned about **4,554 JUP** more on their own. The previous batch, about 1.55M JUP, was burned in late April 2026. Since the next batch has no date, only the small burns are carried into the next 90 days; about **194K JUP** of fees is already waiting in the burn wallet.

Foundation buying is **0 JUP**: when Jupiter buys back JUP sold by its team or by Mercurial investors, the coins move from one holder to another inside the market. New long-term locks are also **0 JUP**: staked JUP and the founders' self-locks stay in the circulating count.

## Foundation and overhang

We track six Jupiter-controlled piles. Outside the circulating count: the community cold wallet (**1.70B JUP**, which also holds the postponed 700M Jupuary airdrop), the team cold wallet (**1.68B JUP**, paused by the February 2026 vote) and a third reserve (**159.89M JUP**, untouched since Feb 9 2026). Together they explain the whole gap between total and circulating supply to within 0.47M JUP. Inside the count: the Litterbox Trust (**173.06M JUP**), the community hot wallet that pays staking rewards (**223.40M JUP**) and the team distribution wallet (**191.57M JUP**). We read all six on-chain at every rebuild. If any of the three outside wallets falls between refreshes, that outflow enters the ledger as a Foundation unlock at the next refresh — and a revived Jupuary would be the largest such event.

## How JUP compares to other DeFi app tokens

Among DeFi app tokens, JUP sits with the fixed-supply group. Tokens that still stream emissions to liquidity providers or stakers grow every day, and their buybacks have to outrun that stream just to hold supply flat. JUP has no emission at all, so the only question is whether its reserves open. That makes it closer to a token with a hard cap and a large treasury than to an emissions-funded exchange token.

The buyback is where JUP differs from the buy-and-burn model some perpetual-exchange tokens use. There, revenue buys the token and destroys it or locks it for good, so supply falls every day. Jupiter's Litterbox buys and holds, which supports demand but leaves the coins one vote away from the market. JUP's actual burns come from a small fee and from one-off community votes, like the 3B supply cut in January 2025 and the Litterbox burn in November 2025.

Against tokens still in their vesting years, JUP's position is unusual: less than half of total supply circulates, yet nothing is scheduled to unlock, because the team and airdrop reserves were frozen by vote rather than by a calendar. A calendar is easy to model; a vote can be reversed by another vote.

## What to watch in the next 90 days

The third-quarter staking-reward round, about 50M JUP, should pay out in early October 2026 from the community hot wallet; it moves coins already in the market and does not change supply. The next verification-fee burn has no date — about 194K JUP was waiting on Sep 29 2026. Forum proposals to raise the Litterbox share from 50% to 70% and to burn what it buys have not reached a vote; a burn vote would turn the **173.06M JUP** it holds into real buy pressure. A new vote on the postponed Jupuary airdrop would do the opposite, releasing up to 700M JUP from the community cold wallet. The last Mercurial investor streams end on Dec 23 2026.

## Summary

JUP supply was roughly steady over the 90 days to Sep 29 2026, down **0.03%**, because no new JUP can be created, team vesting is paused and a **948,317 JUP** fee burn was the only change. The Litterbox buyback bought **28.75M JUP** but holds it, so it does not shrink supply yet. The key risk is the **3.54B JUP** held in three locked reserves, which a future community vote could release. The ceiling is fixed: total supply is **6.86B JUP** and can only go down.

---

*MrNasdog Pressure Framework analysis of JUP, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 30 2026.*
