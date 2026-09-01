---
title:         "UNI Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description:   "Roughly flat: Uniswap burned 4.99M UNI out of swap fees in 90 days against a 5.00M UNI treasury growth budget. Net -0.02%, projected 0.00% for the next 90 days."
canonical_url: "https://mrnasdog.com/research/uni/inflation"
tags:          ["crypto", "uni", "uniswap", "defi"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/uni/inflation](https://mrnasdog.com/research/uni/inflation)*

# UNI Inflation Analysis · September 2026 · Mixed flows, supply roughly steady

Uniswap destroys UNI out of real swap fees, and the Uniswap DAO pays UNI out of its treasury, and the two are now almost exactly the same size. Over the 90 days to **Sep 1 2026** the Uniswap DAO released **5.00M UNI** of growth budget while the fee mechanism destroyed **4.99M UNI**, leaving the MrNasdog Pressure Framework reading UNI at **-0.02% net** supply and projecting a flat **0.00%** for the next 90 days. The important finding this time is about where the burn money comes from: it is funded by trading fees, not by the Uniswap treasury, and the chain proves it. UNI has never minted a single token — the supply still reads exactly **1,000,000,000** — but the mint switch is live, not dead.

## The verdict, in one paragraph

For the 90 days ending **Sep 1 2026**, the MrNasdog Pressure Framework reads **UNI at -0.02% net** — **5.00M UNI** of growth-budget release against **5.10M UNI** of absorption, on a tradable float of **623.21M UNI** — and projects **0.00%** for the next 90 days. Our supply monitor reads the same window at **+0.14%**, so the gap is **0.15 percentage points**, comfortably inside tolerance, and this build ships **no data-conflict flag**. That is itself a change worth naming: the previous read carried a large gap caused by a **Jun 1 2026** Uniswap governance vote that returned **12,500,001 UNI** from eight delegation contracts into the governance treasury — DAO-owned tokens that were never tradable float. This window opens after that date, so the artefact has aged out and the two readings now agree. The label for Uniswap today: **a fee-funded burn running dead level with a fixed treasury budget**.

## Sell pressure: where new UNI comes from

Not from minting. Sell #1, protocol inflation, is **zero**: reading the UNI contract on Ethereum at both ends of this window returned exactly **1,000,000,000 UNI**, the genesis number from **Sep 2020**, untouched. That is not the same as impossible. UNI carries a perpetual mint provision whose waiting period has already elapsed, whose ceiling is **2% a year**, and whose caller is the Uniswap governance timelock. A live mint with a non-zero cap and an expired waiting period is a dormant option, not a closed door, so the Pressure Framework keeps this row watched rather than retired — roughly **20M UNI** a year of capacity sits behind a single Uniswap governance vote.

Sell #2, vesting unlocks, is **zero** and this one really is finished. The original four-year distribution of UNI to the Uniswap team, investors and advisors completed in **2024**, and UNI is fully unlocked with no cliff calendar left to run. The chain confirms it from the other direction: every UNI that is not counted as circulating sits in one place, the Uniswap governance treasury, so there is no separate vesting escrow quietly releasing tokens.

The entire sell side is Sell #3, at **5.00M UNI**. The UNIfication upgrade created a growth budget of **20M UNI** a year, paid quarterly out of the Uniswap treasury to Uniswap Labs, starting **Jan 1 2026**. Three slices have now been paid, each exactly **5,000,000 UNI**: **Jan 5 2026**, **Apr 10 2026** and **Jul 14 2026**, about 95 days apart. One of those landed inside this window. Sell #4, bankruptcy or long-term locked supply, is **zero** — Uniswap has no estate, no trustee and no court-ordered distribution anywhere in its supply.

## Buy pressure: where new UNI goes

Buy #1, the programmatic buyback, is **4.99M UNI** and it carries the whole buy side. Under UNIfication a slice of every Uniswap swap fee accumulates in a vault that can only be emptied by buying UNI on the open market and destroying it. Over this window **4,990,000 UNI** reached the burn address, verified transfer by transfer: **1,980** separate burns from **23** different sender contracts, adding up to exactly that figure with nothing left over. Two details make this a genuine reading rather than a headline. First, the Uniswap supply counter never moved — the UNI contract has no burn function at all, so a build that watches total supply sees nothing and reports a wrong zero on the coin's largest mechanism. Second, and more important, the burn is not paid for by the Uniswap treasury. The treasury's only outgoing payment in this window was the **5.00M UNI** growth-budget slice, which went to a wallet that has since sent nothing onward; none of the 23 contracts feeding the burn address is the treasury. Uniswap's protocol fee income over the same 90 days would buy roughly **5.04M UNI** at current prices — within about 1% of what was actually destroyed, which is what confirms the burn is funded by trading.

Buy #2, a protocol fee burn, is **zero** — not because no UNI burns, but because that flow is already counted once above. No UNI is destroyed per swap; the fees arrive as pool assets, and it is the purchase-and-destroy step that removes UNI, so booking it twice would double the buy side. Buy #3, foundation buying, is **zero** with no public evidence of open-market purchases. Buy #4 is **0.11M UNI**: **113,138 UNI** came back into the Uniswap governance treasury on **Jul 30 2026**, and treasury-held UNI is not counted as circulating, so that return takes those tokens off the tradable float.

## Foundation and overhang

Four team-controlled overhangs are tracked. The largest is the Uniswap governance treasury itself at **267.2M UNI**, roughly **43%** of the tradable float, with no published release schedule beyond the quarterly growth budget. Next is the growth-budget wallet: it has received **15.0M UNI** from the treasury across the three quarterly slices, has ever released only **1.0M**, and has sent nothing at all in the last six months — it currently sits on **14.0M UNI**. Third, the original UNI distribution contract still holds **12.5M UNI** of unclaimed genesis allocation, draining about **31,000 UNI** across this window. Fourth is the dormant mint capacity, **2%** of supply a year, which is capacity rather than a holding but belongs on the same watch list. All four are read directly on Ethereum every rebuild, and the rule is simple: if any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How UNI compares to other fee-burning DeFi tokens

The mechanism comparison that matters is **fee-funded buy-and-burn** versus **emission-funded incentives**, and Uniswap sits at the extreme end of the first group. Uniswap's protocol family collects about **$102M** in fees over 30 days — the largest fee base of any asset the framework scores, ahead of the next-largest at roughly **$69M** — against a market capitalisation near **$3.3B**. Annualised, that is a fee base worth something like **38%** of the token's market value, which places UNI among the highest fee-to-capitalisation readings in the entire set. UNI is emphatically not a thin-fee token.

What separates the fee base from the token, though, is how much of it is allowed to reach UNI. Most of those fees still belong to Uniswap liquidity providers; the protocol's own share runs about **$8.8M** over 30 days, roughly **3%** of market capitalisation a year, and it is that slice — not the headline fee number — that funds the burn. Against exchange tokens that buy back on a quarterly schedule out of corporate profit, Uniswap's burn is more honest and more volatile at once: it is mechanical, permissionless and impossible to skip, but it rises and falls with swap volume rather than with a board decision. Against uncapped emission chains, UNI has the structural advantage of a supply that has genuinely never grown. Against a pure hard-cap asset, it has the disadvantage that the cap is a governance choice, not code.

## What to watch in the next 90 days

The next quarterly growth-budget slice of **5.00M UNI** is due around **Oct 17 2026** on the pattern observed so far, and it is the single largest scheduled supply event in the window. Swap volume is the other side of the scale: the burn ran **60,500 UNI** a day in June, **39,355** in July and **66,968** in August, so a sustained August-level pace would tip UNI clearly deflationary while a July-level pace would tip it the other way. Watch whether the growth-budget wallet, which has held **14.0M UNI** untouched for six months, begins releasing. Watch any Uniswap governance proposal that extends protocol fees to further pools or chains, which raises the burn without touching the budget. And watch the mint provision, dormant since **2020** but still callable once a year at **2%**.

## Summary

The MrNasdog Pressure Framework reads Uniswap as close to flat: **5.00M UNI** released against **5.10M UNI** absorbed over the 90 days to **Sep 1 2026**, a net of **-0.02%**, and a projected **0.00%** for the next 90 days. The mechanism is genuinely good — a permissionless, fee-funded buy-and-burn that has removed **109.9M UNI** in total and cannot be quietly switched off — but it is currently running level with a **20M UNI** a year treasury budget, so none of that shrinkage reaches the holder. The key risk is not inflation but concentration: **267.2M UNI** sits in the Uniswap treasury with no schedule attached, and the supply ceiling is a governance decision rather than protocol code, since the **2%** annual mint has never been used but has never been renounced either.

---

*MrNasdog Pressure Framework analysis of UNI, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 1 2026.*
