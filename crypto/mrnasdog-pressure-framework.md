---
title: "MrNasdog Pressure Framework"
description: "The MrNasdog Pressure Framework — a three-metric system for evaluating altcoins by sell pressure, buy pressure, and narrative, each scored 0 to 1 for a total out of 3."
canonical_url: "https://mrnasdog.com/research/pressure-framework/full"
tags: ["crypto", "investing", "framework", "altcoins"]
published: true
---

> Originally published at **[mrnasdog.com/research/pressure-framework/full](https://mrnasdog.com/research/pressure-framework/full)** by MrNasdog.

The **MrNasdog Pressure Framework** is a three-metric system for evaluating altcoins. It scores any coin on **sell pressure**, **buy pressure**, and **narrative** — each rated 0 to 1, for a total out of 3 — to judge how favorable a coin's *structural* conditions are. It is built by MrNasdog (Zhiyi Song).

## Why crypto needs its own framework

Why does no traditional financial framework work well for crypto? Why do most crypto analysts produce poor predictions? And what would a framework designed specifically for crypto actually look like?

This article answers those questions and presents a framework — the MrNasdog Pressure Framework — that emerges from the answers.

Traditional financial analysis doesn't work well in crypto for two structural reasons.

**Reason 1: Stock supply dynamics are regulated; crypto supply dynamics are wild.**

Public companies can't issue new shares whenever they want. Insider trading is illegal. Major insider sales must be disclosed. Regulators bound supply dynamics through legal mechanisms. As a result, supply mechanics don't dominate stock analysis — they're handled by regulation.

In crypto, none of this exists. Token unlocks aren't illegal — they're written into protocols. Teams can sell allocations whenever vesting allows. New supply can flood the market on schedules that aren't governed by anything outside the protocol itself. This means supply mechanics dominate crypto in ways they don't in stocks.

**Reason 2: Stock data is institutionally gated; crypto data is on-chain.**

In stocks, the information edge belongs to institutions. Real-time data, insider information, founder access — these are available to institutions but not retail investors. The information asymmetry between institutions and retail is what gives institutional finance its edge over time.

Crypto data is fundamentally different. Token balances are public. Unlock schedules are written into smart contracts. Burn rates are visible to anyone with a block explorer. The information asymmetry that protects institutional finance doesn't exist here. Transparent, trackable data makes everyone even.

**The combination matters.** Supply mechanics dominate crypto AND data is transparent. This means a systematic framework based on tracking supply pressure, structural buy pressure, and narrative position can work in crypto in a way it wouldn't work for stocks. The conditions specifically favor it.

## The framework

Three metrics, each scored 0 to 1, for a total out of 3.

**Sell pressure** measures the predictable selling baked into the coin's design.

**Buy pressure** measures the predictable buying baked into the coin's design.

**Narrative** measures whether the coin sits inside a developing story that will attract money during the next altcoin season.

The total score describes how favorable the structural conditions are for the coin's price to hold and potentially appreciate. It doesn't predict price. Price depends on the interaction between structural conditions and unpredictable demand. The framework addresses only the structural side.

## The precondition across Metric 1 and Metric 2: transparency

Before scoring sell pressure or buy pressure, one condition must be met: the underlying mechanism must be transparent.

Transparency means the mechanism is publicly documented, hard-coded into the protocol or operating under public rules, and verifiable from on-chain data or other public sources. Without transparency, neither metric is measurable. You can't track what you can't see. You can't predict what isn't documented.

A coin that fails the transparency precondition fails both Metric 1 and Metric 2 by default. Hidden allocations, opaque team holdings, off-chain agreements between insiders, undisclosed selling — these break the framework entirely. The framework is for coins where supply dynamics can actually be tracked.

This is why the framework works in crypto specifically. The transparency that comes from on-chain data and open-source protocols is what makes systematic measurement possible. In a market where transparency wasn't the default — like traditional stocks before mandatory disclosure rules — this kind of framework couldn't exist.

## Metric 1: Sell pressure

Sell pressure measures the predictable selling built into the coin's design.

**Sources of predictable sell pressure include:**

1. Protocol inflation — new tokens minted by the protocol on a fixed schedule
2. Vesting unlocks — team and investor allocations releasing on disclosed schedules
3. Treasury releases — DAO or foundation treasury distributions on schedule
4. Locked stake unlocks — staked tokens that become available to sell
5. Bankruptcy estate distributions — like the FTX estate releasing SOL into circulation
6. Large concentrated holdings — whales or groups whose intentions to sell are publicly known

This is not an exhaustive list. Any source of selling that's transparent and trackable counts as predictable sell pressure.

**Example: protocol inflation in Solana.**

To make this concrete, let me walk through one specific source — protocol inflation — and show how it gets tracked.

Solana's inflation schedule is fixed at the protocol level. The initial inflation rate was 8% per year at launch in 2020. The rate decreases by 15% each year until it reaches a long-term floor of 1.5% per year. This is not subject to discretion. It is hard-coded into the protocol.

Because the rule is fixed, the inflation rate for any given year is calculable in advance. The approximate yearly rates:

| Year | Approx. inflation rate |
|------|------------------------|
| 2020 | 8.0% |
| 2021 | 6.8% |
| 2022 | 5.8% |
| 2023 | 4.9% |
| 2024 | 4.2% |
| 2025 | 4.0% |
| 2026 | 3.84% |

*Hard-coded: −15% each year, toward a 1.5% long-term floor.*

If nothing changes in the protocol, the rate continues declining toward 1.5% on a known schedule.

This is what "trackable and predictable" means. The inflation rate isn't speculation about what Solana might do — it's a known consequence of a rule already written. Anyone with access to the protocol parameters can verify the rate today and project the rate forward.

For scoring purposes: a lower inflation rate scores higher. A coin with 1% inflation creates less sell pressure per year than a coin with 10% inflation. Bitcoin at sub-1% inflation is at the strong end. A high-emission memecoin at 30%+ annual inflation is at the weak end. Solana at 3.84% in 2026 sits in the middle.

**Why this works:** because the rule is transparent and fixed, the sell pressure from this source can be calculated, not guessed. Combined with the other sources of sell pressure (vesting unlocks, treasury releases, etc.), it gives a complete picture of how much new supply will hit the market.

**The logic:** coins with low and predictable sell pressure are structurally more durable. There's less new supply for buyers to absorb. Coins with high or unpredictable sell pressure require constant new demand just to maintain price.

## Metric 2: Buy pressure

Buy pressure measures the predictable buying built into the coin's design.

The same transparency precondition applies. The buying mechanism must be publicly documented, hard-coded or operating by public rule, and verifiable from on-chain data. Without transparency, the mechanism can't be scored.

**Sources of predictable buy pressure include:**

1. Revenue-backed buybacks — protocol uses fees or revenue to buy tokens off the market
2. Burn mechanisms — transactions destroy tokens, permanently reducing supply
3. Locked allocations — tokens removed from circulation through staking or other locks
4. Protocol-level demand mechanisms — required token holdings for ecosystem participation

This is not an exhaustive list. Any mechanism that creates transparent, rule-based buying or supply removal counts.

**Example: Solana's burn mechanism.**

To make this concrete, let me walk through Solana's burn mechanism.

Solana burns 50% of every transaction fee. The other 50% goes to validators. This rule is part of the protocol — it isn't subject to discretion, and it operates automatically with every transaction.

Because the rule is transparent and the data is on-chain, the burn rate is fully trackable. Anyone can pull the historical transaction fee data from a block explorer and calculate how much SOL has been burned over any time period.

As of May 2026, Solana burns approximately 87,800 SOL per 30 days. Annualized, this is roughly 1.05 million SOL per year. Compared to Solana's circulating supply of ~578 million, the burn removes about 0.18% of supply annually.

The same trackability that applies to inflation applies here. Historical burn data is on-chain. Future burn depends on transaction volume, which varies, but the mechanism is fully transparent — anyone watching the chain can see the burn happening in real time and project recent rates forward.

**The scoring question:** is the burn large enough to meaningfully offset sell pressure?

Solana's burn rate (0.18% of supply per year) compared to Solana's inflation rate (3.84% per year) means the burn covers only about 4.7% of new issuance. The mechanism exists and is real, but it's not large enough to meaningfully offset the sell pressure from inflation. For scoring purposes, this fails the metric. A burn that destroys 30-50% of new supply each year would pass. A burn that destroys 4.7% does not.

**Why this works:** because the burn rule is transparent and the data is on-chain, the buy pressure from this source can be calculated, not guessed. The framework can compare the predictable buy pressure against the predictable sell pressure and produce a meaningful score.

**The logic:** coins with significant, predictable buy pressure have a mechanical buyer baked into the protocol. There's a structural floor under the price that doesn't depend on retail sentiment. Coins without this pressure rely entirely on unpredictable demand to maintain price.

## Metric 3: Narrative

Narrative is qualitatively different from sell pressure and buy pressure. Sell and buy pressure are measurable from on-chain data — the transparency precondition makes them calculable. Narrative is about the future direction of demand, which can't be measured directly.

But narrative is also not random. Crypto narratives follow a historical pattern, and the pattern is what makes this metric scoreable.

### The historical pattern

Every major altcoin season in crypto history has been driven by narratives that were quietly developing for years before they became dominant. The pattern is consistent across multiple cycles.

**2017-2018 ICO boom.** The smart contract technology that powered the ICO boom existed since Ethereum's launch in 2015. The boom happened two to three years later, after enough infrastructure was built and enough projects had launched to make the narrative visible.

**2021 DeFi boom.** The protocols that drove DeFi summer 2020 and the DeFi boom of 2021 — Compound, Aave, Uniswap, Yearn — had been built and tested since 2019. The narrative was developing for two years before it became the dominant story.

**2021 NFT boom.** NFT infrastructure (ERC-721 standard, OpenSea, NFT projects) had existed for years before 2021. CryptoKitties was 2017. CryptoPunks was 2017. The boom came when the cumulative infrastructure plus celebrity adoption plus pandemic-era retail attention created the conditions for the narrative to take off.

**2023 Solana memecoin boom.** Solana's ecosystem — Phantom wallet, Jupiter, Raydium, the DEX infrastructure — had been built years before 2023. When retail attention shifted to memecoins, the infrastructure was already in place to support the boom.

The pattern across all of these: the strongest narratives come from things that have been developing for years. The narrative doesn't appear out of nowhere — it crystallizes around existing infrastructure that has been quietly maturing.

### What this means for prediction

If the strongest narratives always come from years of prior development, then the next major narratives are already developing now. They just aren't dominant yet. The question becomes: what's developing now that hasn't yet become the dominant story?

The framework identifies developing narratives by looking at two factors:

1. **Technology developments within existing crypto narratives.** What's being built and tested now that could become the next catalyst? Examples in 2026: AI x blockchain integration, account abstraction, restaking protocols, ZK-proof applications.
2. **Real-world changes that drive crypto adoption.** What's happening outside crypto that creates demand for specific crypto categories? Examples in 2026: the GENIUS Act and CLARITY Act creating regulatory clarity for RWA; institutional capital flows looking for tokenized real-world exposure; AI development creating demand for decentralized compute and data.

A narrative scores high in the framework when these two factors converge — when there's both internal crypto development and external real-world changes pointing in the same direction.

### Concrete example: RWA

RWA (Real World Assets) is the cleanest current example of a developing narrative the framework would score highly.

**Internal crypto development:** Tokenization infrastructure has been built and tested for years. Centrifuge, MakerDAO's RWA collateral, Ondo Finance, Maple Finance, and others have been operating since 2020-2022. The infrastructure exists. It's been stress-tested through multiple market cycles.

**External real-world change:** The GENIUS Act and CLARITY Act, both passed in the U.S. in 2025, created the regulatory clarity that institutional capital needs to deploy into tokenized assets at scale. Before these laws, institutional RWA was bounded by regulatory uncertainty. After, the path is open.

**The convergence:** Years of internal development meet a major external regulatory shift. This is the pattern that has produced every major altcoin season in crypto history. By the framework, RWA scores at the top of the narrative metric.

A coin scores 1.0 on narrative if it sits at the center of this kind of developing narrative. It scores 0.5 if it has tangential relevance. It scores 0 if it has no connection.

### Why this works

The pattern of years-of-development-before-dominant-narrative is consistent enough across crypto history to be predictive. Not certain — narratives can fail to materialize, regulatory shifts can reverse, technology developments can stall. But the base rate of new narratives emerging from nowhere with no prior development is very low. Narratives almost always come from something that has been quietly maturing.

This means the framework can score narrative position with reasonable confidence even though narrative itself isn't measurable from on-chain data. The historical pattern provides the structure that makes scoring possible.

### The underlying logic

Coins that sit at the center of developing narratives benefit when those narratives become dominant. They attract the demand that flows in during altcoin seasons. Coins with no narrative connection face the unpredictable demand alone, with no tailwind from a broader story.

Sell pressure and buy pressure tell you whether a coin's structural conditions are favorable. Narrative tells you whether the demand side is likely to provide the tailwind. The combination of all three is what the framework scores.

## Conclusion

The MrNasdog Pressure Framework exists because crypto is structurally different from stocks in two specific ways — supply mechanics matter more, and data is transparent. Those two facts make a systematic framework focused on sell pressure, buy pressure, and narrative position viable in crypto when it wouldn't work elsewhere.

The framework doesn't predict price. It identifies which coins have favorable structural conditions for price durability and upside, and which coins face headwinds.

Sell pressure measures the predictable selling baked into the coin's design. Buy pressure measures the predictable buying baked in. Narrative measures whether the coin sits inside a developing story that will attract future demand. Each metric scores 0 to 1, for a total out of 3.

The framework works because:

- Crypto supply dynamics are unregulated and dominant in ways stock supply dynamics aren't
- Crypto data is on-chain and verifiable in ways stock data isn't available to retail
- Crypto narratives follow a historical pattern of years-of-development-before-dominance that makes them partially predictable

Used as a filter — eliminating coins with bad structural conditions, identifying coins with favorable conditions for further analysis — and combined with separate judgment on demand-side dynamics and macro conditions, the framework provides a structural edge in evaluating which altcoins are worth holding through cycles.

In a market where most analysis is hype or chart-reading, having a systematic structure for evaluating supply mechanics, structural buy pressure, and narrative position is a small but durable advantage. Applied consistently over years, combined with public track record and willingness to be wrong publicly, it compounds.

## Limitations

**Limit 1: Supply-side bias.** The framework weights supply-side and structural buy-side dynamics. It doesn't capture demand-side drivers, which usually dominate short-term price action. The framework provides perhaps 30-40% of the picture; the rest is unpredictable.

**Limit 2: Narrative subjectivity.** Reasonable analysts disagree on which narratives matter and which coins are central versus peripheral. The framework provides structure but not objectivity on this metric.

**Limit 3: Trust assumption.** The framework assumes publicly stated supply mechanics will be honored. Teams that violate vesting commitments or operate with hidden allocations break this assumption. Higher risk for newer projects, lower risk for established ones.

**Limit 4: Market regime sensitivity.** The framework is calibrated for normal markets. In crisis events — regulatory crackdowns, major exchange failures, fundamental crypto-wide stress — structural metrics matter less than survival mechanics.

**Limit 5: Time horizon.** The framework is designed for multi-month to multi-year positioning. For short-term trading, the metrics move too slowly to be useful. Short-term traders need different tools.

**Limit 6: Score-outcome disconnect.** A 3/3 score is not a guarantee. A 0/3 score is not a death sentence. The score describes structural conditions, not outcomes. Outcomes depend on how structure interacts with unpredictable demand.

---

*This article describes the MrNasdog Pressure Framework. Data + explanation only. Not financial advice. Last updated May 2026. By MrNasdog (Zhiyi Song).*
