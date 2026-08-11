---
title: "ORCA Inflation Analysis · August 2026 · An empty sell ledger and a buyback tied to trading volume"
description: "A MrNasdog Pressure Framework read of Orca (ORCA): all four sell rows zero, vesting done since 2024, and a fee-funded buyback of 381.4K ORCA in 90 days. Framework −0.63% net; supply monitor −0.69%; forward −0.63%."
canonical_url: "https://mrnasdog.com/research/orca/inflation"
tags: ["crypto", "orca", "solana", "dex"]
published: true
---

> Originally published at **[mrnasdog.com/research/orca/inflation](https://mrnasdog.com/research/orca/inflation)** by MrNasdog.

Orca is one of the few tokens in this coverage whose sell ledger is genuinely empty. The ORCA supply on Solana is fixed at **75.0M**, every 2021 vesting schedule expired in 2024, and the single treasury account that holds the entire non-circulating balance has not transacted since **Mar 17 2026**. Against that, the Orca protocol's fee-funded buyback purchased **381.4K ORCA** on the open market over the 90 days to **Aug 11 2026** — a net of **−0.63%**, in line with our supply monitor at **−0.69%**.

## The verdict, in one paragraph

For the 90-day window ending **Aug 11 2026**, the Pressure Framework reads **ORCA at −0.63% net**. Sell pressure totals **zero ORCA** — all four sell rows are empty, which is rare — and buy pressure totals **381.4K ORCA** against a circulating base of **60.8M ORCA**. Our supply monitor reads the same window at **−0.69%**, a gap of **0.06 percentage points**, comfortably inside tolerance, so no monitor-gap flag ships with this page. The forward reading is also **−0.63%**, because the buyback mechanism is unchanged and the trailing measured rate carries forward. ORCA is best characterised as **deflationary by structural buyback, with the buying tied directly to trading volume**.

## Sell pressure: where new ORCA comes from

It does not come from anywhere, and that is the story of this page. Sell #1, protocol inflation, is **zero**. The ORCA mint on Solana returns a total supply of **74,999,546** tokens, identical at both ends of the window — the figure left after the Orca DAO destroyed **25.0M** of its own community treasury on **Apr 14 2025** and cut the ceiling from **100.0M** to **75.0M**. There is no block reward, no staking issuance and no rebase.

One honest caveat keeps this row tagged as checked rather than permanent: **the mint key has not been renounced**. It sits with the project's multisig — the same multisig that holds the treasury — and its only on-chain activity inside this window was routine wallet housekeeping, with no minting instruction and no ORCA moving at all. The capability exists, so we re-read it every rebuild.

Sell #2, vesting unlocks, is **zero** and permanently so. The 2021 Orca cap table — a token treasury at **55.85%**, team at **20%**, private sale at **9.6%**, and the grant, advisory, liquidity-provider and trader buckets making up the rest — ran linear release schedules that all completed in 2024. No unlock calendar for ORCA exists at any tracker, which removes the supply-cliff risk that dominates most tokens of this size. Sell #4, long-term locked or bankruptcy, is **zero** as well: Orca is a going concern with no estate, no trustee and no court-ordered distribution touching the token.

Sell #3, Foundation and unscheduled unlocks, is **zero** for the window — but it is the row that carries all of the latent risk. A single token account under the project's multisig holds **14.2M ORCA**, and that one balance is the entire arithmetic difference between the **75.0M** issued and the **60.8M** counted as tradable. It has no published release plan. Its last transaction of any kind is dated **Mar 17 2026**, nearly two months before this window opened, so nothing was released and the row books at zero under the framework's evidence test. If that balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## Buy pressure: where new ORCA goes

Buy #1, the programmatic buyback, is **381.4K ORCA** and it is the whole buy side of this ledger. The mechanism is unusually clean: a trader pays a pool fee, **12%** of that fee goes to the Orca protocol rather than the liquidity provider, and **40%** of the protocol share is spent buying ORCA on the open market. The share was **20%** until the Orca governance council doubled it on **Jan 13 2026** — before this window opened, so the full 90 days ran at the higher rate and no mid-window re-basing is needed. Execution is continuous rather than monthly: a keeper wallet routes small swaps out of the protocol's fee account many times an hour, spending a few hundred dollars at a time.

The framework measures the programme at its destination rather than trusting a dashboard. Every purchased ORCA is deposited into the xORCA staking vault, and because staking and unstaking are rate-neutral, the vault's redemption rate can only rise when a buyback adds ORCA without minting new xORCA. That rate moved from **1.4849** on **May 12 2026** to **1.5677** on **Aug 10 2026**, and integrating it against the xORCA supply across five checkpoints gives **381.4K ORCA** bought. Two independent angles agree: the protocol's own documented fee split applied to trailing 90-day protocol revenue implies roughly **400K**, and closing the vault's books from the other side — a total vault increase of **1.36M ORCA**, of which about **970K** is holders staking their own coins — leaves roughly **387K** for the buyback. One caveat belongs on the record: the pace is easing with trading volume, and the last three weeks of the window ran at about **3,040 ORCA** a day, which would be **274K** over a full quarter rather than **381.4K**.

Buy #2, protocol fee burn, is **zero**, and the distinction matters. **Orca does not burn.** The bought ORCA is parked in the staking vault where holders can still redeem it after a seven-day cooldown, so the float is locked rather than destroyed — and a supply count still treats those coins as circulating, which is exactly why the framework books this as a buyback and not as a burn. The only destruction event in this token's history was the one-off **25.0M** treasury burn of **Apr 14 2025**. Buy #3, Foundation buy, is **zero**: a proposal from **Feb 8 2026** would have redeployed **$4.8M** of idle climate-fund money into a months-long ORCA purchase, but it never found a sponsor and the council closed the thread on **Jul 28 2026** without submitting it. Buy #4, new long-term lock, is **zero**; the staking vault is an existing product, not a new lockup.

## Foundation and overhang

Three pools are tracked. The first is the **DAO treasury account** at **14.2M ORCA**, dormant since **Mar 17 2026** and read again on every update — it is the only identified team-controlled ORCA balance, and by construction it is also the entire non-circulating bucket. The second is the **xORCA staking vault** at **7.67M ORCA**, which is the destination of every coin the buyback has ever purchased; it is a tracked overhang rather than a burn, because a seven-day cooldown is the only thing standing between those coins and the market. The third is **holder staking**, which added roughly **970K ORCA** to that vault over the same 90 days — real float removal, but holder-elective and reversible, with no symmetric sell row for holders who unstake, so it is disclosed and deliberately not counted on the buy side. If any of these three balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How ORCA compares to other decentralised exchange tokens

The first comparison is issuance, and it is where ORCA separates from most of its peer group. A large share of decentralised exchange tokens still pay liquidity providers in their own token, which means the supply schedule is an ongoing cost of doing business and the ledger's sell side never empties. Orca does not do this: liquidity providers earn the trading fee itself, in the assets being traded, so there is no emission line at all. Add a vesting calendar that finished in 2024 and a hard ceiling cut to **75.0M** by the community's own burn on **Apr 14 2025**, and ORCA has the structural profile of a fully-issued asset rather than an emitting one.

The second comparison is what the fee revenue does with itself. Exchange tokens that run quarterly buybacks typically burn what they buy, which converts revenue into permanent supply reduction. Orca converts revenue into a staking claim instead: the **381.4K ORCA** bought this window sits in the xORCA vault, raising what each staked unit redeems for. Economically the purchase is real — the coins were bought on the open market from real sellers — but the reduction is reversible, and a supply count that treats vault balances as circulating will never register it. That is the honest asterisk on ORCA's deflation, and it is why the framework books this as a buyback with a tracked destination rather than a burn.

The third comparison is dependence. A halving-model chain's issuance is fixed no matter what happens to demand, and an uncapped proof-of-stake chain's issuance scales with its validator set — neither cares about usage. ORCA's entire supply story is usage: the buyback is **40%** of **12%** of whatever traders pay, so a quiet quarter mechanically shrinks the only positive force on the page. That is the trade a reader is making here. There is no downside supply risk to speak of, but the upside is a direct bet on Solana trading volume routing through Orca rather than through the competition.

## One caveat on the close agreement

The framework read and the monitor read land **0.06 percentage points** apart, which looks like a clean confirmation. It is worth being plain that the agreement is looser than it looks. The counted float here is on-chain supply minus that one dormant treasury account, and because the account did not move, the classified float was flat for the entire window. The monitor's daily prints swing around that constant — **−0.69%** on **Aug 11 2026** but **+0.29%** on **Aug 8 2026** — so today's close match is partly a coincidence of which day the window ends. The structural point stands either way: a supply count sees almost nothing here, because the vault holding the bought ORCA sits inside the counted float.

## What to watch in the next 90 days

First, protocol fee revenue: trailing 30-day revenue of about **$245K** annualises to a quarter's buyback near **274K ORCA** rather than **381.4K**, so a further slide in Solana trading share would visibly soften the only buy row on this page. Second, the dormant **14.2M ORCA** treasury account — its first transaction since **Mar 17 2026** would open Sell #3 and could outweigh several quarters of buying in a single transfer. Third, the climate-fund redeployment idea, dead as of the council's **Jul 28 2026** reply but revivable by any sponsor holding **500,000 ORCA**; if it passes it lands in Buy #3 as a one-off purchase. Fourth, any council update to the **40%** buyback share, which was itself doubled on **Jan 13 2026** and is the single lever that most changes this page. Fifth, the mint key: it has never been used, but it has never been renounced either, and a renouncement would move Sell #1 from checked to permanent.

## Summary

ORCA runs a one-sided supply ledger. Nothing mints, nothing vests, no estate distributes and the one team-controlled balance has been still since **Mar 17 2026**, so the entire framework reading for the 90 days to **Aug 11 2026** is a fee-funded buyback of **381.4K ORCA** — a net **−0.63%**, matched by our supply monitor at **−0.69%**. The structural mechanism is that **40%** of the protocol's **12%** fee share buys ORCA on the open market continuously and parks it in the xORCA staking vault rather than burning it. The key risk is not new supply but fading demand for the buyback's fuel: trading revenue has been easing, and the recent run rate points closer to **274K** a quarter. The ceiling is hard at **75.0M** tokens, with the caveat that the mint key still exists.

---

*MrNasdog Pressure Framework analysis of ORCA, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 11 2026.*
