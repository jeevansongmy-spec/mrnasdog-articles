---
title:         "QNT Inflation Analysis · August 2026 · Supply flat, projected to stay flat"
description:   "Quant has minted no new QNT since 2018, vesting is long expired, and Overledger licence fees lock QNT in treasury rather than burning it. Framework reads a flat 0.00% net, monitor -0.01%."
canonical_url: "https://mrnasdog.com/research/qnt/inflation"
tags:          ["crypto", "qnt", "quant", "interoperability"]
published:     true
---

> Originally published at **[mrnasdog.com/research/qnt/inflation](https://mrnasdog.com/research/qnt/inflation)** by MrNasdog.

# QNT Inflation Analysis · August 2026 · Supply flat, projected to stay flat

Quant's QNT is a fixed-supply ERC-20. The on-chain supply reads a static **45,467,000 QNT** from a single 2018 sale, with no mint and no burn, so the framework reads **0.00% net** over the trailing 90 days against the **14.54M** the market recognizes as circulating. Every ledger row is zero: no protocol inflation, no vesting, no bankruptcy release, no buyback and no fee burn. The only live supply mechanic is the treasury and the Overledger licence-lock — both discretionary and quiet this window. Our supply monitor agrees, reading about **-0.01%**, a gap of well under a tenth of a percentage point, so no monitor-gap chip ships.

## The verdict, in one paragraph

For the 90-day window ending **Aug 5 2026**, the Pressure Framework reads **QNT at 0.00% net**. Sell pressure is **zero** across all four rows and buy pressure is **zero** across all four rows, against a circulating base of **14.54M QNT**. Our supply monitor reads the realised change at about **-0.01%**, a gap of roughly **0.006 percentage points**, comfortably inside tolerance, so no chip ships. The two readings agree because there is nothing to disagree about: QNT's on-chain supply is a fixed **45,467,000** constant that has not moved, and the circulating figure barely wobbles day to day. QNT is best characterised as **a fixed-supply utility token whose float is flat, gated by discretionary treasury activity rather than any protocol emission**.

## Sell pressure: where new QNT comes from

There is no new QNT. Sell #1, protocol inflation, is **zero**: the token contract read on-chain returns a static total supply of **45,467,000**, all issued at the 2018 sale, with no mint function in use, no staking issuance and no emission curve. The mintable path on the contract reverts when called, so there is no way for the protocol to create fresh QNT. This row can only be zero.

Sell #2, vesting unlocks, is **zero**: the 2018 sale lockups expired years ago, and there is no live vesting calendar or cliff in this window. There are no remaining founder or advisor streams to model for the next 90 days or beyond.

Sell #3, Foundation and unscheduled unlocks, is **zero** as a flow, but it carries the one thing worth watching — a large off-market overhang of about **30.85M QNT** that sits outside the recognized supply (company reserve and treasury), plus a further ~68K between recognized total and circulating. That reserve is the pool the treasury draws on to service Overledger licence conversions. No dated release from it was observed over the window, so the row books nothing, but it is enumerated and monitored.

Sell #4, long-term locked or bankruptcy, is **zero**: there is no QNT estate, no trustee and no court-ordered distribution attached to the token. The whole sell side, in short, is empty this period.

## Buy pressure: where new QNT goes

Buy #1, programmatic buyback, is **zero**: Quant runs no protocol-encoded buyback contract. The treasury does buy QNT over-the-counter from exchanges to fulfil fiat-to-QNT licence conversions, but that is a discretionary operational purchase with no published rate, and no dated quantum was observed in the window.

Buy #2, protocol fee burn, is **zero**, and this is the load-bearing structural fact about QNT's tokenomics. Overledger licence fees are paid in fiat, and any portion settled in QNT is **held in the treasury — locked and later reused, not destroyed**. Nothing is sent to a burn address. So there is no deflationary burn flow, despite QNT often being marketed as a scarce, deflationary asset. This row can only be zero.

Buy #3, Foundation buy, is **zero**: the only open-market QNT buying is the treasury's discretionary licence-conversion activity already noted in Buy #1, and counting it twice would double it.

Buy #4, new long-term lock, is **zero** this period but is QNT's real deflationary lever: enterprises lock QNT to licence Overledger, and staked QNT backs network operations, so an adoption surge would remove float. No net new lock was booked over the window and circulating stayed flat, so it reads zero — but it is the row to watch.

## Foundation and overhang

The team-controlled overhang is large in raw terms and quiet in behaviour. Beyond the **14.54M** circulating and the ~14.61M the market recognizes as total, about **30.85M QNT** from the original on-chain mint is held off-market by Quant-controlled reserve and treasury wallets, which is why the on-chain total supply of **45.47M** is more than three times the recognized supply. This reserve is the pool the treasury draws on to service Overledger licence conversions, and it is where any future supply expansion would originate, but it operates on no published schedule and released nothing measurable over the last 90 days. It is re-read every rebuild; if the reserve's balance falls between refreshes — through a large OTC sale or a distribution to holders — that outflow enters Sell #3 as real sell pressure at the next refresh. Today there is nothing of the sort: the reserve is static.

## How QNT compares to other fixed-supply utility tokens

The comparison that matters is fixed-and-minted versus emitting. Most smart-contract-platform tokens still issue new supply through staking rewards or inflation, so their sell side scales with network activity and their float grows every year. QNT does not: the **45.47M** on-chain supply is fully minted and static, nothing new is created, and the sell rows are all zero — closer to a capped, fully-distributed asset than to an emitting layer-1. In that sense it behaves like the quiet end of the capped-supply spectrum, where the inflation question is settled and the only variable left is how much of the float is held off-market.

The sharper contrast is lock versus burn. Deflationary tokens route revenue into a buyback that ends in a burn address, so supply irreversibly shrinks and the supply feed books a permanent reduction. QNT's Overledger model does the opposite of both minting and burning: licence fees and enterprise usage **lock** QNT in the treasury rather than destroying it, so the tokens are removed from float only while a licence is live and can return when it lapses. That makes QNT's deflation conditional and reversible rather than structural — the float tightens when adoption rises and loosens when it falls, but the total never changes. The framework's reading captures exactly that: with adoption quiet this window, neither the lock nor the reserve moved, so the net is flat.

## What to watch in the next 90 days

First, the treasury reserve: a large OTC sale or a disclosed distribution to holders or stakers would be a real, one-time supply event to book in Sell #3, and it is the single cleanest signal of float change. Second, Overledger enterprise adoption — the bank integrations and tokenized-deposit work expected through the year — because rising licence demand locks more QNT and tightens the float via Buy #4. Third, any move by Quant to introduce a formal staking or burn mechanism, which would turn a discretionary lock into a structural one and change the reading. Fourth, the recognized circulating figure itself: if the classification of the off-market reserve shifts, the denominator moves even when no tokens trade. Fifth, the monitor gap, which should stay near zero as long as the fixed supply holds.

## Summary

Quant's QNT is a fixed-supply ERC-20 with a static on-chain supply of 45,467,000, no mint and no burn, so every ledger row reads zero and the framework nets 0.00% over 90 days against a recognized float of 14.54M — a genuinely flat token. The supply monitor agrees at about -0.01%, so no gap is flagged. The structural mechanism is a treasury-and-licence-lock model: QNT is removed from float when enterprises licence Overledger and returned when licences lapse, making its deflation conditional and reversible rather than a structural burn. The key risk is not inflation but the large off-market reserve — roughly 30.85M QNT the company controls — whose discretionary release is the one thing that could move a supply that is otherwise fixed.

*MrNasdog Pressure Framework analysis of Quant (QNT), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated August 5 2026.*
