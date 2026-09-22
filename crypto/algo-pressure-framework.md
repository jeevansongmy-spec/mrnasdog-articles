---
title:         "ALGO Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "ALGO supply grows 1.34% in 90 days: Algorand mints nothing, but Foundation wallets released 102.5M ALGO and staking rewards 18.9M. Full ledger and risks."
canonical_url: "https://mrnasdog.com/research/algo/inflation"
tags:                    ["crypto", "algo", "algorand", "layer1"]
published:     true
---

Originally published at [ALGO Inflation Analysis · September 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/algo/inflation).

# ALGO Inflation Analysis · September 2026 · Supply growing · projected to keep growing

ALGO supply is growing and is projected to keep growing, even though Algorand mints nothing: all **10,000M ALGO** were created at launch. The Pressure Framework reads **+1.34%** over the last 90 days and **+0.86%** for the next 90, because Algorand Foundation wallets released **102.47M ALGO** to outside accounts and staking rewards paid from a Foundation-funded fee pot added **18.91M**, against only **0.12M** of fees taken back off the market. The monitor reads **+1.41%**. The ceiling is the Foundation's remaining **931.4M ALGO**.

## The verdict, in one paragraph

Against a circulating base of **9,042.8M ALGO**, the framework books **121.38M ALGO** of sell pressure and **0.12M ALGO** of buy pressure over the trailing 90 days, a net of **+1.34%**, and projects **+0.86%** for the next 90 days. The inflation monitor reads **+1.41%** for the same window, a gap of **0.07 percentage points**, which sits inside the framework's 0.5-point tolerance, so the overview carries no warning chip. The label for ALGO is a **fully minted chain whose float grows by Foundation release**: the protocol cannot print ALGO today, but the Algorand Foundation's reserve reaches the market every week.

## Sell pressure: where new ALGO comes from

Sell #1, protocol inflation, is **18.91M ALGO**, and it is not minting. Since early 2025 every Algorand block pays the account that proposed it a bonus plus half of the block's fees. That payment comes out of the fee sink, an account that sits outside the float, and the Algorand Foundation keeps it full: it sent **10.3M ALGO** into the fee sink on **Jul 10 2026** and **9.0M ALGO** on **Aug 19 2026**. Across the window the fee sink paid out **19.54M ALGO**, of which **0.63M** went to a Foundation node and stayed outside the float, leaving **18.91M ALGO** that reached outside stakers. We checked that no coin is created along the way: over a run of 21 blocks, the change in Algorand's counted money equalled the payouts minus the fees to the last micro-ALGO. The bonus fell from **8.51** to **8.26 ALGO** per block across the window, because it drops 1% every million blocks, so the next 90 days should bring about **18.38M ALGO**.

Sell #2, vesting unlocks, is **0**. Algorand's launch vesting schedule for the public sale, node grants, team and investors finished in 2024, and no tranche is left to unlock.

Sell #3, Foundation and unscheduled unlocks, is the main story at **102.47M ALGO**. We read every one of the Algorand Foundation's published wallets, 74 current and 230 legacy, and traced every payment that left them for an outside account. **48.28M ALGO** went to the account that receives the Foundation's structured selling, in tranches of 3M to 5M from Jun 29 to Aug 26 2026. **30.00M ALGO** left in a single payment on **Jul 17 2026** to an account that has since passed it all on. **12.63M ALGO** left in a single payment on **Sep 22 2026**. The remaining **11.56M ALGO** went out as xGov awards, grants and operating payments. For the next 90 days the framework keeps the repeating streams, **59.84M ALGO**, and leaves out the two one-off payments, which have no schedule. Sell #4, long-term locked or bankruptcy, is **0**: ALGO has no bankruptcy estate, trustee or court-ordered distribution.

## Buy pressure: where new ALGO goes

Almost nowhere. Buy #1, programmatic buyback, is **0**: the Algorand Foundation runs no buyback, and not one ALGO flowed from outside accounts into its wallets during the window. Buy #2, protocol fee burn, is **0**. Algorand fees are not destroyed; they go to the fee sink and are paid back out to block proposers. We checked both places a burn could show. The all-zero address held **39,465 ALGO** at both ends and received nothing, and the **10,000M ALGO** created at launch are all still in existence, because Algorand has no burn operation for its native coin.

Buy #3, Foundation buy, is **0**; the Foundation only sent coins out. Buy #4, new long-term lock, is **0**. Algorand staking has no bond and no unbonding period, so the roughly **2,000M ALGO** online stays spendable and inside the float. The one real removal is Buy #5, fees paid into the fee sink, at about **0.12M ALGO** over 90 days. Those coins leave the float when they are paid and come back when the fee sink pays its next rewards, which is why the framework books them separately and never nets them twice.

## Foundation and overhang

The overhang on ALGO is the Algorand Foundation itself. Its published wallets held **931.4M ALGO** outside the fee sink at the end of the window. The largest single wallet holds **140.6M ALGO**, and a legacy wallet still holds **29.5M**. The fee sink holds a further **13.0M ALGO**. Together these balances make up the whole gap between the **10,000M** created and the ALGO counted as circulating: our wallet-by-wallet total matched the Foundation's own non-circulating figure to within about **1,500 ALGO**, which is a few minutes of staking payouts.

The Foundation's Q2 2026 transparency report put its holdings at **1,035.6M ALGO** on **Jun 30 2026**, with **10.6M** of structured selling in that quarter. The pace since then is several times faster. None of this reserve is on a published release calendar; the Foundation decides each month what to sell, grant, invest and send to the fee sink. Every wallet is read from the chain at each rebuild, and if any Foundation balance falls between refreshes, that outflow enters Sell #3 at the next refresh.

## How ALGO compares to other fully minted proof-of-stake chains

ALGO sits in a small group: proof-of-stake chains whose whole supply was created at launch and that pay staking rewards out of existing coins rather than new ones. On the issuance axis that is stricter than an uncapped continuous-emission chain, where a staking reward of several percent a year is minted and the total supply rises with it. Algorand's 10,000M total has not moved.

The float is a different matter. A hard total protects holders from new coins, not from a large reserve held by one organisation. ALGO's reading of **+1.34%** a quarter is closer to a young token still working through a treasury than to a mature capped chain like Bitcoin, where the only new supply is a shrinking block subsidy. The difference from a typical vesting token is that the Algorand Foundation's release is discretionary, not scheduled, so the pace can speed up or pause without notice.

Compared with exchange tokens that burn coins with a share of revenue, Algorand has no removal mechanism of any size. Its fees are recycled to stakers, so network use does not shrink supply; at about **0.12M ALGO** a quarter, fees would need to grow several hundred times to offset the Foundation's releases.

## What to watch in the next 90 days

First, the Algorand Foundation's structured selling: its last tranche to the selling account was on **Aug 26 2026**, and whether it resumes decides most of the forward number. Second, the staking bonus steps down 1% at about **Oct 15 2026**, **Nov 16 2026** and **Dec 18 2026**, trimming Sell #1 slightly. Third, the Foundation's Q3 2026 transparency report, due around the end of October, which should explain the **30.00M** Jul 17 payment and the **12.63M** Sep 22 payment. Fourth, the King Safety paper on how to pay stakers once the Foundation bonus ends; on **Jul 1 2026** the Foundation said the bonus now runs to 2028, and the options it is studying include new-coin rewards, which would need 90% of online stake to approve. Fifth, the fee sink balance of **13.0M ALGO** and the next Foundation refill.

## Summary

The MrNasdog Pressure Framework reads ALGO at **+1.34%** over the trailing 90 days and **+0.86%** projected forward: supply growing, projected to keep growing. Algorand mints nothing and burns nothing; the float grows because the Algorand Foundation released **102.47M ALGO** from its reserve and funded **18.91M ALGO** of staking rewards through the fee sink. The key risk is that this release is discretionary and large, with **931.4M ALGO** still in Foundation wallets. The ceiling is firm: Algorand's **10,000M ALGO** total has not changed since launch, and changing it would take a protocol upgrade approved by 90% of online stake.

MrNasdog Pressure Framework analysis of ALGO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.
