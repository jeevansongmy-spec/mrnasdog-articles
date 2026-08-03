---
title: "ETC Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description: "Proof-of-work issuance, no burn and no buyback: Ethereum Classic minted ~1.15M ETC in 90 days for +0.73% net. The Jul 22 2026 reward cut eases the forward read to +0.60%. Monitor +0.65%."
canonical_url: "https://mrnasdog.com/research/etc/inflation"
tags: ["crypto", "etc", "ethereum-classic", "proof-of-work"]
published: true
---

> Originally published at **[mrnasdog.com/research/etc/inflation](https://mrnasdog.com/research/etc/inflation)** by MrNasdog.

Ethereum Classic minted **1.15M ETC** over the last 90 days — 574,913 proof-of-work blocks, most of them before the reward dropped from **2.048** to **1.6384 ETC** at the Jul 22 2026 reduction — and absorbed none of it, because ETC has no buyback, no fee burn and no treasury. The framework reads **+0.73% net** on a **157.7M** circulating base against a **~210.7M** ceiling, easing to **+0.60%** at the lower reward. The supply monitor reads **+0.65%** — a 0.07-point agreement, comfortably inside tolerance.

## The verdict, in one paragraph

For the 90-day window from May 5 2026 to Aug 3 2026, the framework reads **Ethereum Classic at +0.73% net inflation**: mining emission of **1.15M ETC** against exactly zero on the buy side. Because the reward cut landed inside the window, the forward reading re-bases to the post-cut rate and eases to **+0.60%**. The supply monitor reads **+0.65%**, leaving a gap of about **0.07 percentage points** — comfortably inside tolerance, so no monitor-gap flag ships with this page. Ethereum Classic is a **quiet, capped proof-of-work chain**: every ETC in existence traces to the 2014 genesis allocation or a coinbase output, the issuance curve is fixed in protocol, and nothing on the chain can vote a new coin into being.

## Sell pressure: where new ETC comes from

There is exactly one source, and it is the block reward. Sell #1, protocol inflation, booked **1.15M ETC** — and that figure is a count, not an estimate. Reading the chain end to end for this window gives **574,913 blocks** between height 24,502,791 and height 25,077,704, or about **6,390 blocks per day** against Ethereum Classic's roughly 13-second target. The subtlety is that the reward changed mid-window. Under the "5M20" monetary policy, the block reward falls **20% every 5,000,000 blocks**, and block **25,000,000** was mined on **Jul 22 2026**, cutting the reward from **2.048 ETC** to **1.6384 ETC**. So the window splits: 497,209 blocks at the old reward and 77,704 at the new one, for a blended **1.15M ETC**. Because the cut is inside the window, the framework projects the next quarter off the post-cut rate rather than the blend, which is why the forward figure is the lower **0.94M ETC**.

Every other sell row is zero, and each is zero for a structural reason. Sell #2, vesting unlocks, is **0** and always will be: Ethereum Classic inherited the Ethereum state at the Jul 2016 fork, and the roughly **72M** genesis supply was the original 2014 Ethereum crowdsale allocation, distributed at genesis with no team lockup, no investor cliff and therefore no vesting contract to unlock. Sell #3, Foundation and unscheduled unlocks, is **0** because Ethereum Classic has no protocol-level foundation allocation and no diversion out of the coinbase; the ETC Cooperative that supports development is donation-funded and holds no protocol reserve. Sell #4, long-term locked or bankruptcy, is **0** because no bankruptcy estate or locked protocol allocation is associated with the coin.

## Buy pressure: where new ETC goes

Nowhere. All four buy rows are **0**, and Ethereum Classic is unusually clean about it. Buy #1, programmatic buyback, is **0** because there is no protocol revenue and no treasury — the chain collects nothing and holds nothing, so there is no cash flow that could be pointed at the market. Buy #2, protocol fee burn, is **0**, and this is the point most often gotten wrong about Ethereum Classic: it never adopted the base-fee burn that Ethereum runs, so transaction fees are paid to miners and no ETC is destroyed. The chain tip carries no base fee at all. Buy #3, Foundation buy, is **0** because no foundation entity holds a protocol allocation or runs an accumulation programme. Buy #4, new long-term lock, is **0** because Ethereum Classic is pure proof-of-work: there is no staking contract, no bonding curve and no lockup to take coins off the float.

The result is that Ethereum Classic prints its inflation at face value. On a chain with a buyback or a fee burn, the headline emission number overstates what actually reaches the market. Here it does not. The **1.15M ETC** mined in the window is **1.15M ETC** of new float, and the net is simply the gross. The one change on the horizon — the Olympia upgrade, with a fee-market redesign — is worth naming precisely, because it does not add buy pressure: Ethereum Classic's design redirects the base fee to an on-chain treasury rather than burning it, and Olympia is live only on a test network, targeting mainnet late 2026.

## Foundation and overhang

Ethereum Classic has no team-controlled overhang in the usual sense. There is no foundation treasury, no labs multisig, no unscheduled allocation and no buyback accumulation wallet, because there was never a protocol allocation to create one from. The genesis supply was distributed at the 2014 crowdsale and the 2016 fork carried that ledger over one coin for one coin, so the coins that exist are already on the market. The ETC Cooperative funds client teams from donations, not from a reserve of ETC it could release.

The only forward-looking item is the **Olympia Treasury**, which would begin accumulating the redirected base fee once Olympia activates on mainnet. It does not exist on mainnet today, holds nothing, and would be an on-chain, readable contract when it does — so it is a future Sell-side watch item, not a current overhang. If and when that treasury goes live and its balance begins to move, the outflow enters Sell #3 at the next refresh.

## How ETC compares to other capped proof-of-work chains

Ethereum Classic belongs to the family of hard-ceiling proof-of-work chains whose entire supply schedule is a stepped-down emission curve: Bitcoin, Bitcoin Cash and Litecoin on the halving model, and Ethereum Classic on its own **5M20** variant. The mechanism is the same idea — periodic, protocol-encoded reward reductions toward a fixed ceiling — and only the timing differs. Bitcoin halves the reward every four years; Ethereum Classic cuts it **20%** every five million blocks, roughly every two and a half years, which produces a gentler curve of more frequent, smaller steps. The Jul 2026 cut is the fifth such step, and at **157.7M** of a **~210.7M** ceiling the chain still has meaningful issuance ahead, which is why its quarterly reading is a clear positive **+0.6%** rather than the near-zero prints of chains that are 95%-plus mined.

The sharper contrast is against chains that have a buy side at all. Its closest sibling, Ethereum, adopted a base-fee burn and can run negative net supply in a busy quarter because the burn scales with usage. Ethereum Classic deliberately kept the older gas market, so it has no such lever: its net can never go below zero from fees. An exchange token with a quarterly buyback removes float on a schedule regardless of usage; Ethereum Classic has no treasury to fund one. Its floor is the emission curve, and the best reading it can produce is a small positive number that steps lower at each reduction — predictable, but never deflationary.

The third comparison worth drawing is governance surface. A chain with a live treasury, a DAO or a vesting cliff carries a standing risk that a vote changes the supply picture. Ethereum Classic carries almost none of that today, precisely because Olympia's treasury and DAO are not yet on mainnet. Its monetary policy has been fixed and unedited since the 5M20 rule was set, and for this metric the absence of a discretionary lever is the finding.

## What to watch in the next 90 days

First, the Olympia upgrade. It is targeting mainnet activation in **late 2026**; the item to check is not a burn — Ethereum Classic redirects its base fee to a treasury rather than destroying it — but the first appearance of that treasury contract, which would become the chain's first Sell-side overhang. Second, the observed block rate. This window ran at about **6,390 blocks per day**; because Ethereum Classic and Ethereum-style GPU miners share hardware, a sustained hashrate shift would move the emission figure by a couple of percent in either direction, the only real variable in the ledger now that the reward is fixed at **1.6384 ETC**. Third, the next reduction, at block height **30,000,000** — roughly 4.9 million blocks out, expected around 2028 — which is the event that steps this page's headline number lower again. Fourth, any first appearance of a corporate treasury or buyback programme denominated in ETC; none exists today, and a search of the last 90 days found none.

## Summary

Ethereum Classic is a fair-launch, hard-ceiling proof-of-work chain whose only supply mechanism is the block subsidy, and the framework reads it at **+0.73% net** over the last 90 days — **1.15M ETC** mined across 574,913 observed blocks, with nothing absorbed on the buy side because no buyback, burn, treasury or staking lock exists. The reward cut on **Jul 22 2026** dropped issuance to **1.6384 ETC** per block, easing the forward reading to **+0.60%**, and the supply monitor's **+0.65%** sits a 0.07-point gap away, inside tolerance. The structural mechanism is one of the cleanest in the catalog: no premine vesting, no foundation allocation, no fee burn, and no live governance lever over issuance. The key risk is not protocol issuance but the pending Olympia upgrade, whose on-chain treasury — fed by a redirected base fee, not a burn — would be the first discretionary supply mechanism Ethereum Classic has ever carried.

---

*MrNasdog Pressure Framework analysis of ETC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 4 2026.*
