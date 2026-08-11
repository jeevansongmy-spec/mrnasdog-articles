---
title:         "JASMY Inflation Analysis · August 2026 · The code can neither create a token nor destroy one"
description:   "JasmyCoin is a fixed 50B ERC-20 whose deployed contract has no mint, no owner and no burn. All eight ledger rows read zero, the framework reads 0.00% net, and our monitor agrees at −0.04%."
canonical_url: "https://mrnasdog.com/research/jasmy/inflation"
tags:          ["crypto", "jasmy", "jasmycoin", "erc20"]
published:     true
---

*Originally published at [mrnasdog.com/research/jasmy/inflation](https://mrnasdog.com/research/jasmy/inflation)*

JasmyCoin is an Ethereum **ERC-20** whose deployed contract can neither mint a new token nor burn an existing one — the code exposes only transfers and approvals, with **no mint path, no owner and no burn function**. Total supply read exactly **50,000,000,000 JASMY** on-chain, the genesis figure, and **49.44B** of it already circulates. Every row of the Pressure Framework ledger for JASMY, sell and buy, is **zero**, so the framework reads **0.00% net** across both the trailing and the forward 90-day window. Our independent supply monitor reads **−0.04%** over the same window — a gap of about **0.04 percentage points**, far inside tolerance, so **no monitor-gap chip** is attached to the JASMY page.

## The verdict, in one paragraph

For the 90-day window ending **Aug 11 2026**, the MrNasdog Pressure Framework reads **JasmyCoin at 0.00% net**, and the forward view is identical at **0.00%**: a JASMY sell ledger of **zero** against a JASMY buy ledger of **zero**. Our supply monitor reads **−0.04%** for the same trailing window, a gap of roughly **0.04 percentage points** — well within the framework's half-point tolerance, so no **monitor gap** chip is warranted. That residual is not a supply event: it is estimation noise in a market-cap-over-price supply figure bouncing either side of a constant **49.44B**. JasmyCoin is the rare asset that is **flat by construction rather than flat by coincidence** — a fixed-cap ERC-20 with no issuance mechanism and no destruction mechanism.

## Sell pressure: where new JASMY comes from

It does not come from anywhere, and the reason is written into the contract. Sell #1, protocol inflation, is **zero**: the deployed JasmyCoin bytecode reaches only the eleven standard ERC-20 entry points — name, symbol, decimals, total supply, balance, transfer, transfer-from, approve, allowance and the two allowance adjusters. There is no mint selector, no owner, no ownership transfer and no minter role anywhere in it, so issuance is not merely unused, it is unreachable. Total supply read exactly **50,000,000,000 JASMY** this session, the same number minted once at genesis in **Dec 2020**. Sell #2, vesting unlocks, is **zero** because JasmyCoin never used a vesting or escrow contract: the genesis distribution ran as plain wallet transfers, in weekly tranches that ended in **Nov 2023**, followed by two isolated releases and nothing at all since **Jan 16 2025**. There is no calendar left to fire.

Sell #3, Foundation and unscheduled unlocks, is **zero** for the window, though this is the one row worth watching on JASMY. A single genesis reserve wallet still holds **555,000,322.41 JASMY** — and that balance is exactly the difference between the **50B** cap and the **49.44B** classified as circulating, so it is the entire non-circulating position in the asset. It has capacity but no release pattern: its last outflow was **Jan 16 2025**, roughly nineteen months ago, and the forwarding wallet it used to route those tranches holds nothing and last moved **Mar 8 2025**. A reserve that has been still for more than a year gives the framework nothing to project, so the row stays at zero and the balance is carried as a tracked overhang instead. Sell #4, long-term locked or bankruptcy, is **zero**: JASMY was issued by an operating Japanese company, not an insolvent exchange, so there is no estate, trustee schedule or court distribution feeding tokens to the market.

## Buy pressure: where new JASMY goes

The buy ledger is just as empty, and that symmetry is what makes the JASMY reading a true flat rather than a small negative. Buy #1, programmatic buyback, is **zero**: there is no buyback contract and no repurchase programme disclosed by the issuer, and no protocol revenue is routed into bidding for JASMY. Buy #2, protocol fee burn, is **zero** for the strongest possible reason: the JasmyCoin contract has no burn function, so the token cannot be destroyed by its own code. The standard dead address holds a cumulative **315 JASMY** across the token's entire history, and the null address holds none; JASMY is a token on Ethereum, not a base layer burning its own fees.

Buy #3, Foundation buy, is **zero**: the issuer has disclosed no open-market purchase of JASMY, and the reserve wallet has only ever sent tokens outward — nothing has flowed back into it from an exchange. Buy #4, new long-term lock, is **zero** as well. No new lockup contract was deployed in the window, and there is no staking product taking JASMY out of circulation. The one nuance is JasmyChain, the project's own layer-2, which completed its mainnet migration on **Jan 17 2026** and uses JASMY as its gas token: units bridged to that network are held in a gateway contract on Ethereum. That is a custody move, not a removal — the tokens still belong to their holders and can return — so bridging does not earn a buy-side row.

## Two claims we checked and discarded

Both of the stories that would push JASMY off zero fail on primary evidence, and it is worth being explicit about why, because both are widely repeated.

The first is a "buyback and burn program" for JASMY. It is published by a social account that is not the issuer's — the issuer publishes elsewhere — and the contract it points readers at is a different token on a different chain entirely. It is not a JasmyCoin mechanism, it does not touch the Ethereum ERC-20 that defines circulating supply, and the framework does not count it. Buy #1 stays at zero.

The second is a claim that ecosystem burns have already cut JASMY's circulating supply by around **1.2%**. The chain refutes it directly. Total supply is unchanged at exactly **50,000,000,000 JASMY**, and the standard dead address holds **315 JASMY** for the token's entire lifetime — six ten-millionths of one percent of the cap. The figure behind the claim is a small creation fee charged on the project's own layer-2; it is an activity cost on that network, not a destruction of the Ethereum token. A 1.2% reduction in circulating supply would be roughly 593 million JASMY. Nothing close to that has ever been burned, and with no burn function in the code it could only ever happen by hand.

## Foundation and overhang

JasmyCoin has exactly one team-controlled overhang, which makes it unusually easy to police. The genesis reserve wallet holds **555,000,322.41 JASMY**, about **1.1%** of the **50B** cap, and it is an ordinary wallet rather than a lock contract — the tokens are unscheduled, not vested. It is read directly from the chain on every rebuild. Everything else in the top of the holder list is excluded on principle: the largest balances belong to exchange hot and cold wallets holding customer deposits, which are not project-controlled supply. There is no separate foundation multisig, no DAO treasury and no identified founder allocation beyond the reserve, because JASMY is corporate-issued and has no governance surface able to change its supply.

The trigger is simple to state and simple to test. If the reserve wallet's balance falls between refreshes, that outflow enters Sell #3 at the next refresh — and because this one wallet is the whole non-circulating bucket, any movement out of it is the only way JasmyCoin's float can grow. Until it moves, the framework treats capacity as capacity and not as pressure.

## How JASMY compares to other fixed-cap ERC-20 tokens

JasmyCoin belongs to the class of **pre-mined, fixed-cap ERC-20 tokens whose issuance is finished** — a shape that looks like Bitcoin's hard cap from the outside but arrives at it by a completely different route. Bitcoin is capped yet still issuing: a shrinking block subsidy keeps adding coins until roughly 2140, so its framework reading is a small positive number that halves on a schedule. JASMY was minted once, in full, at genesis, so its issuance curve is not shrinking — it does not exist. On that single axis JASMY is quieter than any proof-of-work chain, and quieter still than an uncapped continuous-emission layer-1, where staking rewards mint new units every block and the sell ledger carries a real figure every window.

The sharper comparison is with the other fixed-supply ERC-20 tokens JASMY sits beside. Many of them pair a fixed cap with an active burn: a large memecoin routing ecosystem activity into recurring destruction, or an exchange token buying back and burning a slice of quarterly profit, will read mildly **deflationary** in this framework because its buy ledger carries a number. JasmyCoin cannot join that group — its contract has no burn function, so a burn would require sending tokens to a dead address by hand, and the **315 JASMY** parked there over five years shows nobody does. It also cannot join the other common group, the still-vesting launch tokens whose monthly investor tranches dilute the float, because its distribution completed and the residue is unscheduled. What is left is the flattest possible position: a **50B** cap, **49.44B** circulating — **98.9%** of the total — with no mint, no burn, no buyback and no unlock calendar. On the inflation metric alone that is a strength, because there is no dilution to price in, but it is a genuine **0.00%**, not a shrinking supply, and the framework scores it as such.

## What to watch in the next 90 days

First, the reserve wallet: any outflow from the **555.0M** genesis balance is the single event that could push JasmyCoin's reading off zero, and it is checked on-chain at each rebuild — a full release would add roughly **1.1%** to the float. Second, watch for any JasmyChain announcement that ties layer-2 gas to a destruction of Ethereum-side JASMY; today the gas token model moves value without touching the ERC-20 supply, and a change there would give the buy ledger its first real number. Third, watch the dead address, which has held the same trivial balance for years — a deliberate corporate burn would have to appear there, since the contract itself cannot destroy tokens. Fourth, watch for any first-ever disclosure of a buyback programme from the issuer; none exists today, and the offers circulating under unofficial accounts are not it. Absent all four, the next-90-day JASMY read stays flat through **Nov 2026**.

## Summary

The MrNasdog Pressure Framework reads JasmyCoin at **0.00% net** over the next 90 days, from a sell ledger and a buy ledger that are both entirely empty. The structural mechanism is a **one-time genesis mint under a fixed 50B cap, in a contract with no mint path and no burn function** — no emission, no vesting left, no fee burn and no buyback, with our monitor agreeing at **−0.04%**. The key risk is not dilution from issuance, which is impossible, but the one dormant reserve wallet holding **555,000,322.41 JASMY**: it is the entire non-circulating balance, it is unscheduled, and it has not moved since **Jan 16 2025**. The ceiling is hard and permanent at **50,000,000,000 JASMY**, of which **49.44B** already trades.

---

*MrNasdog Pressure Framework analysis of JASMY, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 11 2026.*
