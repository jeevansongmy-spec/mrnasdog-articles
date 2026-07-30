---
title:         "GNO Inflation Analysis · July 2026 · Mixed flows, supply roughly steady"
description:   "GNO is hard-capped at 3M, on-chain supply held flat all quarter, and the GIP-151 treasury redemption burn has drawn nothing yet. Framework +0.00% net, monitor -0.01%."
canonical_url: "https://mrnasdog.com/research/gno/inflation"
tags:          ["crypto", "gno", "gnosis", "inflation"]
published:     true
---

*Originally published at [mrnasdog.com/research/gno/inflation](https://mrnasdog.com/research/gno/inflation)*

Gnosis is one of the flattest supply stories the framework tracks. GNO is hard-capped at **3,000,000** and its on-chain total supply read **byte-identical** at both ends of this 90-day window — nothing was minted, sold, or burned into the market. Validators earn GNO rewards but re-stake them, there is no vesting calendar and no buyback, so both the sell and buy ledgers total **0 GNO** against a **2.64M** circulating base. The framework reads **+0.00% net** versus our supply monitor at **-0.01%** — the same flat picture. The one force that would change this is the **GIP-151** treasury redemption burn, which passed in June but has drawn no supply yet.

## The verdict, in one paragraph

For the 90-day window ending Jul 31 2026, the Pressure Framework reads **GNO at +0.00% net**. Sell pressure totals **0 GNO** and buy pressure totals **0 GNO**, against a circulating base of **2.64M GNO**. Our supply monitor reads the realised change at **-0.01%**, a gap of about **0.01 percentage points**, comfortably within tolerance, so no monitor-gap chip ships on the GNO overview. The flatness is not an assumption: reading the GNO contract on Ethereum and its Gnosis Chain representation directly, total supply was **10,000,000** and **1,435,214** respectively at both the current block and a block roughly 90 days earlier — identical to the last decimal. GNO is best characterised as a **hard-capped token with no live emission reaching the float**, whose next real supply event is a burn, not a mint.

## Sell pressure: where new GNO comes from

Sell #1, protocol inflation, is **0**, and the reason is structural. Gnosis Chain is proof-of-stake: each validator stakes **1 GNO** and earns GNO consensus rewards, and there are hundreds of thousands of validators. That sounds inflationary, but the rewards are drawn against the fixed **3M cap** and overwhelmingly re-stake rather than reach the tradable float. The proof is on-chain — GNO total supply did not move at all across the window, and the circulating figure held flat around **2.64M**, oscillating only inside a narrow price-driven noise band. The framework measures supply reaching the market, and that was zero.

Sell #2, vesting unlocks, is **0** because Gnosis has no live unlock calendar. The original eight-year vesting contract that began in 2020 is exactly the supply the community chose to destroy: a governance mandate cut the cap from **10M to 3M**, burning roughly 70% of the token out of that vesting contract over several tranches. What would have been a multi-year drip of early-holder and team GNO was removed instead. Sell #3, Foundation and unscheduled unlocks, is **0** — two team-controlled overhangs are tracked but neither sold in the window. Sell #4, long-term locked or bankruptcy, is **0**: there is no Gnosis estate, trustee or court-ordered distribution.

## Buy pressure: where new GNO goes

The buy ledger is as quiet as the sell ledger. Buy #1, programmatic buyback, is **0** — there is no live protocol buyback spending revenue to acquire GNO on the open market. Buy #2, protocol fee burn, is **0** because Gnosis Chain gas is paid in **xDAI**, a stable gas token, not in GNO, so ordinary network activity never removes GNO from supply the way a base-fee burn does on some other chains. Buy #3, Foundation buy, is **0**: the DAO disclosed no open-market GNO purchase in the window.

Buy #4, new long-term lock, is **0** — validator staking is stable, and the re-staking that keeps Sell #1 at zero is the same flow, so counting it again as a lock would double-count. The row that matters is the extra one: Buy #5, the **treasury redemption burn**, also **0** today but the dominant force ahead. GnosisDAO passed **GIP-151** on Snapshot on **Jun 26 2026** with 97.53% in favor and 161,740 GNO voting, authorising a one-time, pro-rata redemption in which holders hand back GNO for a share of the roughly **$223M** liquid treasury and the returned GNO is permanently burned. The claim window opens only after a 30-day audit period, and no GNO has been redeemed or burned on-chain yet — which is exactly why the supply reads flat. The framework holds the forward column at zero until a real burn lands, rather than guessing how many holders will opt to cash out.

## Foundation and overhang

Two team-controlled overhangs sit behind the flat float. The first is the **GnosisDAO treasury**, which holds GNO alongside about **$223M** of liquid assets — the same treasury now earmarked for the GIP-151 redemption, so it is set to shrink as holders redeem rather than grow into the market. The second is the **un-emitted reserve**: **360.4K GNO** that exists under the 3M cap but is not yet circulating, released only slowly through validator rewards with no fixed schedule. Neither overhang moved into the market during the window. Each is re-read on every rebuild, and if either balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How GNO compares to other capped staking tokens

The mechanism comparison that matters is cap plus custody of the mint. Many proof-of-stake tokens are uncapped and mint continuously, so their sell side scales with the validator set forever. GNO is the opposite: the ceiling is a hard **3M**, and because rewards re-stake, the circulating float barely moves. That makes it behave less like an emission token and more like a fixed-supply asset, with only **360.4K GNO** of headroom left between today's float and the cap.

The second comparison is burn source. Chains that burn supply usually do it through a base-fee burn tied to usage, so the deflation is continuous and small. GNO does not burn gas at all — its deflation is **discretionary and event-driven**, coming from governance-approved treasury operations rather than from network throughput. The historic cut from 10M to 3M was one such event; the GIP-151 redemption is the next. That gives GNO a lumpier supply profile than a fee-burn token: long flat stretches punctuated by large, vote-driven burns. It also ties the token's supply to treasury policy rather than to on-chain activity, which is unusual among staking assets.

## What to watch in the next 90 days

First and above all, the **GIP-151** redemption claim window: once the audit completes and the portal opens, every GNO redeemed is burned, and a meaningful take-up would swing this reading from flat to clearly deflationary. Second, the total GNO actually redeemed versus the amount eligible — the framework will book the real on-chain burn into Buy #5 as it happens, not the theoretical maximum. Third, any follow-on governance that changes the redemption price or extends the window. Fourth, the un-emitted reserve, which is the only channel that could add float and only does so slowly through staking rewards. Fifth, whether validator re-staking behaviour shifts, since a large wave of reward claims reaching the market is the only way Sell #1 leaves zero.

## Summary

Gnosis is a hard-capped token whose supply is genuinely flat: GNO total supply read identical on-chain at both ends of the quarter, there is no vesting, no buyback and no fee burn, and validator rewards re-stake rather than reach the market, so both ledgers total zero and the framework reads +0.00% net against a monitor at -0.01%. The structural fact is the 3M cap with only 360.4K GNO of headroom left; the key event is GIP-151, a governance-approved treasury redemption that permanently burns any GNO handed back but has drawn no supply yet. The risk to the flat reading is therefore one-directional and deflationary: the next real move in GNO supply is a burn, whose size depends entirely on how many holders choose to redeem.

---

*MrNasdog Pressure Framework analysis of Gnosis (GNO), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 31 2026.*
