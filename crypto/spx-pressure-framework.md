---
title:         "SPX Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "SPX6900 supply is flat: no mint path, no vesting, and only 5.72K SPX burned in 90 days. Net 0.00% in both windows. Read the Pressure Framework ledger."
canonical_url: "https://mrnasdog.com/research/spx/inflation"
tags:           ["crypto", "spx", "spx6900", "memecoin"]
published:     true
---

Originally published at [SPX Inflation Analysis · September 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/spx/inflation).

# SPX Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

SPX6900 supply is flat and will stay flat: the Pressure Framework books **0** SPX of sell pressure and **5.72K SPX** of buy pressure over the last 90 days, a net of **0.00%** in both windows, while the monitor reads **+0.23%**. The SPX6900 contract on Ethereum has no mint function, no owner and no upgrade path, so no new SPX can ever be created. The only thing that moves is the burn address, fed mostly by a launchpad that destroys every SPX it earns in fees.

## The verdict, in one paragraph

Against a circulating base of **930.99M SPX**, the framework books **0** SPX of sell pressure and **5.72K SPX** of buy pressure over the 90 days to **Sep 22 2026**, a net of **−0.0006%**, which shows as **0.00%**. The next 90 days project the same **0.00%**. The inflation monitor reads **+0.23%** for the same window, a gap of **0.23 percentage points**. That is inside the framework's 0.5-point tolerance, so no monitor-gap warning ships on the overview. The monitor estimates supply from market value divided by price, and that estimate swung from **−0.10%** to **+0.23%** in a single day while the chain moved by a few thousand SPX. The label for SPX6900 is **a sealed supply with a slow outside burn**.

## Sell pressure: where new SPX comes from

Nowhere. Sell #1, protocol inflation, is **0**, and it is a proven zero rather than an observed one. The number the SPX6900 contract reports as its total supply is a fixed value written into the code, so it would read **1,000M SPX** even if a mint happened. A flat reading therefore proves nothing on its own. The proof comes from the code itself: the verified source matches the deployed Ethereum contract exactly, and its **24** public functions include no mint, no burn, no upgrade and no way to hand over ownership. The contract contains no delegate call, no self-destruct and no contract creation. Coin balances change only by transfer, and the owner key was given up at launch. SPX also lives on Solana, Base and Avalanche, but those copies are created only when the same amount of SPX is locked on Ethereum. The Solana and Base copies are issued by a bridge that holds **109.09M SPX** on Ethereum, and the Avalanche copy's **61.4K SPX** matches its Ethereum lock exactly.

Sell #2, vesting unlocks, is **0**. SPX6900 was fair-launched in August 2023 with the whole **1,000M SPX** made at once and sold through the market. There was no team, investor or advisor share, and with no mint there is no way to create one later. Sell #3, foundation and unscheduled unlocks, is **0**: SPX6900 has no foundation, no lab and no DAO treasury. Sell #4, long-term locked or bankruptcy, is **0**, because no bankruptcy estate or trustee holds SPX.

One check decides every sell row. The published circulating figure equals **1,000M SPX** minus the burn address balance, to the last decimal. So the burn address is the only balance outside the float, and nothing can leave it. Any other SPX transfer, however large, is a move between wallets that already count as tradable.

## Buy pressure: where new SPX goes

Buy #1, programmatic buyback, is **0**. SPX6900 has no revenue and no treasury, and no plan to buy SPX was announced or run in the window. Buy #2, protocol fee burn, is also **0**, and it can never change: the trading tax is set to zero, the owner key that could raise it is gone, and the contract has no code that sends SPX to the burn address. Buy #3, foundation buy, is **0** because no foundation exists. Buy #4, new long-term lock, is **0**, because SPX has no staking or lock-up at all.

The one real flow is Buy #5, burns sent to the dead address, at **5.72K SPX**. We read both burn surfaces at both ends of the window. The burn address rose from **69.0071M SPX** to **69.0128M SPX**. The supply figure cannot move, as shown above, so the burn address is the only place a burn can appear. A sweep of every transfer into the burn address found **31** transfers and none out, and their sum matches the balance change to within a hundred-millionth of a coin. **28** of those came from a launchpad contract live since **Jul 27 2026**, whose code burns **100%** of the SPX it earns in trading fees; its own burn counter matches its transfers exactly. The other three came from one savings contract. The next 90 days assume the same pace.

## Foundation and overhang

SPX6900 has no team-controlled overhang in the usual sense. There is no foundation, no reserve and no unscheduled allocation. Two balances are still worth watching. The first is the SPX6900 token contract itself, which holds **0.062M SPX** sent to it over time. The launch fee wallet can swap that balance for ETH at any time, even with ownership given up. It never has, and those coins already count as tradable, so a swap would add nothing to the float.

The second is the pair of bridge vaults on Ethereum, holding **109.2M SPX** between them. They back the Solana, Base and Avalanche copies one for one, and they fell over the window as holders moved SPX back to Ethereum. Both balances are read on-chain at every rebuild. If either falls by more than the bridged copies can explain, the outflow enters Sell #3 at the next refresh.

## How SPX compares to other fixed-supply memecoins

Most memecoins say they have a fixed supply. Fewer can prove it. Many keep a mint function behind an owner key, or sit behind an upgradeable proxy whose code can be swapped. SPX6900 has neither: no mint, no proxy and no owner. Its supply claim rests on code that cannot change, not on a promise. That puts it in a stricter class than tokens whose supply is capped only by policy.

Compared with a halving-model chain like Bitcoin, SPX6900 mints nothing at all, so its issuance reading is a flat zero rather than a small, shrinking number. Compared with exchange tokens that run large quarterly buybacks and burns, SPX6900 has no revenue to fund one. Its burns come from outside groups, such as the launchpad that burns its SPX fees, and they remove a few thousand SPX a quarter against a float of **930.99M**. For a burn to move this reading by even one tenth of a percent, it would need to destroy about **0.93M SPX** in a quarter.

So SPX sits at the far end of the supply spectrum: nothing added, almost nothing removed. Its price is set by demand alone.

## What to watch in the next 90 days

First, the launchpad burn: it burned SPX in late July, early August and early September, and a busier launchpad through **Dec 22 2026** would raise Buy #5, though not enough to move the net off **0.00%**. Second, the burn address at **69.0128M SPX**, which is read at every rebuild. Third, the **0.062M SPX** held in the token contract, the one balance a single wallet can move. Fourth, the bridge vaults at **109.2M SPX**, which should keep matching the copies on other chains. No dated supply event falls in the window.

## Summary

The MrNasdog Pressure Framework reads SPX6900 at **0.00%** over the trailing 90 days and **0.00%** projected forward: mixed flows, supply roughly steady. The mechanism is a sealed Ethereum contract with no mint, no owner and no upgrade path, and its copies on other chains are backed by locked SPX. The only flow is a small outside burn of **5.72K SPX** a quarter. The key risk is on the demand side, not the supply side, and the hard ceiling is the **1,000M SPX** made at launch, of which **69.0128M** is already burned.

MrNasdog Pressure Framework analysis of SPX, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.
