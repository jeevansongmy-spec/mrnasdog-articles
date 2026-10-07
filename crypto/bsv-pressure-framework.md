---
title: "BSV Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description: "BSV supply is roughly steady: mining issued 40,391 BSV in 90 days with no burn or buyback, +0.20% net, the same next. No vesting, no treasury, 21M hard cap."
canonical_url: "https://mrnasdog.com/research/bsv/inflation"
tags: ["crypto", "bsv", "bitcoin-sv", "proof-of-work"]
published: true
---

> Originally published at **[mrnasdog.com/research/bsv/inflation](https://mrnasdog.com/research/bsv/inflation)** by MrNasdog.

# BSV Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

BSV supply is roughly steady: over the last 90 days the Bitcoin SV network created **40,391 BSV** through the mining block subsidy and removed **0 BSV**, a net rise of **+0.20%** on a circulating supply of **20.09M BSV**. The monitor reads **+0.20%** too. BSV is a proof-of-work coin with a hard **21M** cap and a fixed halving schedule, no premine, no vesting, no buyback and no fee burn, so the 3.125 BSV paid for each new block is the whole story until the next halving around Apr 2028.

## The verdict, in one paragraph

The MrNasdog Pressure Framework puts BSV's 90-day net supply change at **+0.20%**, and the next 90 days at the same **+0.20%**, because the block subsidy and the block rate do not change before the next halving. Our inflation monitor, which reads circulating supply from market data, also shows about **+0.20%** over the same window — a gap of **0.00 percentage points**, well inside the 0.5-point line, so no data-conflict warning is shown. In one line: BSV is a **quiet halving-schedule chain** — a small, steady drip of new coins to miners, with nothing on the other side of the ledger.

## Sell pressure: where new BSV comes from

**Protocol inflation — 40,391 BSV.** Bitcoin SV pays miners a block subsidy that halves every 210,000 blocks. The chain is in its fourth era (blocks 840,000 to 1,049,999), where each block creates **3.125 BSV**. Between Jul 9 2026 and Oct 7 2026 miners found **12,925 blocks** (block 957,132 to block 970,057), about 143.6 a day, slightly fewer than the 144 a day the 10-minute target implies. That gives 12,925 × 3.125 = 40,391 new BSV. We checked the coinbase of 41 blocks spread across the window and every one claimed exactly 3.125 BSV plus its fees, so the BSV block subsidy is being paid in full. The previous 90 days held 12,912 blocks, so the pace is steady, and we carry the same 40,391 BSV forward.

**Vesting unlocks — 0.** BSV split from Bitcoin Cash on Nov 15 2018 and copied every existing balance one to one. There was no token sale, no team or investor allocation and no vesting contract, so there is no BSV unlock calendar and nothing that could open later.

**Foundation and unscheduled unlocks — 0.** The BSV Association, the Swiss non-profit that funds the node software, publishes no BSV treasury, and no team wallet is known. Only **300 BSV** sits outside the circulating count, so any large holder that moves coins is moving coins that are already counted as circulating.

**Long-term locked or bankruptcy — 0.** The Mt. Gox estate received a copy of its Bitcoin Cash when BSV split off — thought to be about **143K BSV**. Its repayment plan pays creditors in BTC, BCH or cash, not BSV, and any BSV it holds is already inside the circulating count, so even a sale would not add new BSV supply.

## Buy pressure: where new BSV goes

**Programmatic buyback — 0.** No contract, company or treasury buys BSV back on the open market.

**Protocol fee burn — 0.** Bitcoin SV burns no fees: every block's fees go to the miner in the coinbase, next to the 3.125 BSV subsidy. We also read the three best-known keyless BSV addresses, which nobody can ever spend from; together they received only **0.0057 BSV** in the 90 days, far too little to count as a burn.

**Foundation buy — 0.** No announcement or on-chain flow shows the BSV Association or any project treasury buying BSV in the window.

**New long-term lock — 0.** Bitcoin SV has no staking and no lock contract, so nothing pulls BSV out of the float. Buy pressure in total is **0 BSV**, which is why the whole 40,391 BSV of mining issuance shows up as net supply growth.

## Foundation and overhang

BSV has no foundation hoard in the usual sense. The only identified pile we track is the Mt. Gox estate's BSV, about 143K BSV by the one-to-one copy of its Bitcoin Cash at the 2018 split; the trustee has never published a BSV wallet, so we check it by a web walk every two weeks. The estate's last creditor deadline is Oct 31 2026, but its plan turns side coins into cash rather than paying them out. Beyond that, the early-mined coins from Bitcoin's first years exist on the BSV ledger too, but they belong to unknown holders, and the claims made in court about some of them were never tied to an address. All of these coins already count as circulating. If the estate's balance, or any newly identified team wallet, falls between refreshes, the outflow enters Sell #3 at the next refresh — and it would only count if those coins sat outside the circulating figure in the first place.

## How BSV compares to other proof-of-work chains

BSV shares Bitcoin's supply rules almost exactly: a **21M** hard cap, a 10-minute block target and a halving every 210,000 blocks. Bitcoin and Bitcoin Cash sit in the same fourth era, also at 3.125 coins per block, so all three print roughly 0.2% of supply per quarter. The difference is in the block count: BSV's hashrate is small and its difficulty adjusts block by block, so it runs a touch slow — 143.6 blocks a day here — which trims the real issuance a little below the round number.

Against Litecoin, which pays 6.25 LTC every 2.5 minutes on an 84M cap and issues about twice the share each quarter, BSV prints less of its supply. Against tail-emission coins such as Monero, which never stop minting, BSV's issuance keeps falling by half each era until it reaches zero near the 21M cap. And unlike Ethereum, BSV has no base-fee burn, so heavy network use never takes BSV out of supply; fees reward miners instead. That makes BSV a plain halving-model chain: issuance is set by the block subsidy, there is no offset, and the only real supply events are the halvings themselves.

## What to watch in the next 90 days

**Block rate.** If BSV hashrate drops and blocks slow further, the 90-day issuance falls a little below 40,391 BSV; a faster block rate would lift it slightly.

**Mt. Gox deadline, Oct 31 2026.** The creditor deadline could prompt the trustee to move or sell the estate's BSV; any sale would be coins already in the float, so it changes the price story, not the supply count.

**Teranode.** The new BSV node software is still being rolled out; it changes how blocks are processed, not the 3.125 BSV subsidy, but we re-check any release for monetary changes.

**Next halving.** Block 1,050,000 cuts the subsidy to 1.5625 BSV around Apr 2028 — outside this window, but the next big step down in BSV inflation.

## Summary

Bitcoin SV's supply grew **+0.20%** over the last 90 days and is set to grow the same over the next 90: **40,391 BSV** of new mining issuance against **0 BSV** of buybacks, burns or locks. The mechanism is a fixed proof-of-work halving schedule — 3.125 BSV per block until about Apr 2028 — with no vesting and no team reserve. The key risk is not new supply but existing holders, such as the Mt. Gox estate, selling coins that already circulate. The ceiling is the hard **21M BSV** cap, of which **20.09M** already exists.

---

*MrNasdog Pressure Framework analysis of BSV, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 8 2026.*
