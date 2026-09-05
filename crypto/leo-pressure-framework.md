---
title: "LEO Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description: "A MrNasdog Pressure Framework read of UNUS SED LEO: no issuance, no vesting, and a revenue-funded buyback that parks 601,043 LEO rather than burning any. Framework −0.07% net; supply monitor −0.04%."
canonical_url: "https://mrnasdog.com/research/leo/inflation"
tags: ["crypto", "leo", "bitfinex", "exchange-token"]
published: true
---

> Originally published at **[mrnasdog.com/research/leo/inflation](https://mrnasdog.com/research/leo/inflation)** by MrNasdog.

UNUS SED LEO adds no supply at all: every one of the **1,000,000,000 LEO** was created and sold in **May 2019**, there is no vesting calendar, and neither the Ethereum nor the Vaulta issuance minted a token in this window. The one flow that moves LEO is the iFinex buyback — **601,043 LEO** in the 90 days to **Sep 5 2026**, across **82** on-chain moves. But those tokens are **parked, not burned**: they sit in the token contract's own issuer account, no destroy call was made, and both chains' supply figures are unchanged. The Pressure Framework reads LEO at **−0.07% net** against a supply monitor at **−0.04%**, a gap of about **0.03 percentage points**, well inside tolerance.

## The verdict, in one paragraph

For the 90-day window ending **Sep 5 2026**, the MrNasdog Pressure Framework reads UNUS SED LEO at **−0.07% net** supply change and projects the same **−0.07%** forward. Total sell pressure was **zero**; total buy pressure was **601,043 LEO** of buyback accumulation, against a circulating base of **919,857,851.9 LEO**. The supply monitor reads the same window at **−0.04%**, a gap of about **0.03 percentage points** — inside the half-point tolerance, so no monitor-gap chip ships on the LEO overview. The residual is ordinary rounding in a market-cap-over-price supply series, not a disagreement about mechanism. The cite-able label for LEO is an **exchange token with no issuance and a revenue-funded buyback that accumulates rather than destroys** — the float shrinks, but by hundredths of a percent per quarter, and by a mechanism that one transfer could reverse.

## Sell pressure: where new LEO comes from

Nowhere, and that is the whole of it. Sell #1, protocol inflation, is **zero** because UNUS SED LEO is an exchange token rather than a chain: there is no consensus to pay for, no block reward denominated in LEO, and no staking emission. The Ethereum LEO contract reports a total supply of **660,000,000 LEO** and read exactly that at both ends of this window — and at ten historical checkpoints stretching back to 2019. The Vaulta issuance, on the chain formerly called EOS, reports **307,653,658.9 LEO**, with zero issue, retire and create actions across the whole indexed history back to **Mar 19 2023**. Neither number moved.

A flat supply number only means something if the number is capable of moving, so both were checked. The Ethereum LEO token is a MiniMe contract whose deployed code carries a working mint function and a working destroy function, and whose controller address is live rather than null. The Vaulta contract exposes issue and retire, and its retire path has demonstrably fired before: the Vaulta share was **340,000,000 LEO** at issuance and reads **307,653,658.9** today, so **32,346,341 LEO** really were destroyed on that chain at some point before the index begins. These are measurements, not dead fields. The direct consequence is that LEO cannot be described as a fixed supply: nobody has given up the ability to mint on either chain, and no row on the LEO ledger carries a permanence marker.

Sell #2, vesting unlocks, is **zero** because the May 2019 private sale delivered every token at once, with no lockups and no release calendar to drain. Sell #3, Foundation and unscheduled unlocks, is **zero** because none of the four identified issuer pots sent anything toward the market in the window. Sell #4, long-term locked or bankruptcy, is **zero** because no estate, trustee or court-supervised schedule holds LEO — the 2016 Bitfinex breach restitution points the other way, funding purchases rather than distributions.

## Buy pressure: where new LEO goes

Buy #1, the programmatic buyback, is the only live mechanism on the page and it is worth reading precisely. iFinex commits at least **27%** of its consolidated gross monthly revenue — Bitfinex trading fees, lending, and its other products, gross revenue rather than net profit — to repurchasing LEO on the open market. The purchases settle on Vaulta as roughly one transfer a day, **82** of them over the window, carrying **601,043 LEO** in total. Every one of those transfers is labelled a burn. None of them is one.

The destination is **bitfinexleo1**, which is the LEO token contract's own issuer account. On a Vaulta-style token, sending units to the issuer does not reduce supply; only a retire call does, and there have been none. Both destruction surfaces were read at both ends of the window on both chains: the Ethereum dead addresses hold **zero LEO**, the Ethereum supply is unchanged, and the Vaulta supply is unchanged. The buyback tokens are parked in a live account, and one transfer would put them back on the market. The Pressure Framework still books them as buy pressure, because that account has never sent a token out across its whole indexed history and the market's own circulating-supply classification excludes its balance — but it books them as accumulation, not as destruction, and the distinction is the single most important fact on this page.

Buy #2, protocol fee burn, is **zero**: LEO pays no network fees on either chain, so there is no fee stream that could be destroyed. Buy #3, Foundation buy, is **zero**: the 2016 breach restitution earmarks **80%** of net proceeds for LEO repurchases over roughly 18 months, on top of the standing revenue commitment, but no tranche has reached the chain and the daily stream shows no acceleration. Buy #4, new long-term lock, is **zero**: there is no staking contract, no lock-up programme and no announced escrow for LEO.

## Foundation and overhang

Four issuer-controlled pots are enumerated and watched, all refreshed daily from chain state. The largest is a Bitfinex company cold account on Vaulta holding **257,791,296 LEO**, which has had no activity inside this window and only three balance writes on record, all on **Sep 15 2025**. Next is a single Ethereum custody block of **648,000,000 LEO**. Then the buyback accumulation sink, holding **47,795,807 LEO**, which has received **7,511** transfers and sent **zero** across its whole indexed history. Last is the account that funds the daily buyback moves, holding **2,063,002 LEO** and drawn down by exactly the window's buyback total. If any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

The Ethereum block deserves its own note, because the custody-versus-treasury line is genuinely hard when the issuer is itself an exchange. That address holds **98.18%** of the Ethereum issuance and about **70%** of the circulating figure, and has not moved across this window or the trailing year. It was funded straight from Bitfinex's cold wallet and sits beside tens of thousands of ETH and assorted third-party tokens, which reads like exchange custody holding depositors' assets; but an exactly round **648,000,000** held immobile for years reads like a company reserve. The framework enumerates it rather than dropping it, at a value of zero, and says plainly that the call is uncertain. The wider point stands either way: three of these four pots are counted inside the circulating figure, so the LEO that actually changes hands is a far smaller number than the headline float.

One more reconciliation belongs here, because it is widely misread. The commonly quoted figure of roughly **80 million LEO** burned to date is arithmetically **32,346,341** genuinely retired on Vaulta before 2023 plus **47,795,807** parked in the live issuer account. About **60%** of the number has never been destroyed.

## How LEO compares to other exchange tokens

Against the rest of the exchange-token class, LEO is unusual in two mechanical ways and ordinary in a third. The unusual parts: it has no issuance whatsoever, where most exchange tokens still carry a reserve, a team tranche or an ecosystem allocation with a release calendar attached; and its removal mechanism is funded by a disclosed share of gross revenue rather than by a discretionary quarterly decision. That combination is why the sell side of this ledger is a clean row of zeros while comparable tokens usually have at least one live unlock line.

The ordinary part is the one the marketing hides. Exchange tokens that run genuine auto-burns call a supply-reducing function, and their published supply falls quarter after quarter — you can watch the number drop. LEO's published supply on both chains has not moved for years. The economics of a park and a burn look identical while the tokens sit still, but they are not the same commitment: a burn is irreversible and a park is a transfer away from being undone. Compared with a Layer-1 running continuous validator emission, LEO is the quieter shape — there is no issuance to outrun. Compared with a chain running a base-fee burn, LEO's removal is a corporate policy rather than protocol code, which means it can be slowed, paused or reversed by the same company that writes it, and it depends on that company's revenue rather than on network usage.

## What to watch in the next 90 days

First, the 2016 breach restitution. A US court has cleared the return of roughly **94,643 BTC** to Bitfinex, and iFinex has said **80%** of net proceeds will fund LEO repurchases over about 18 months. Nothing from it has touched the chain yet; the first tranche would be visible as a step change in the daily transfer size. Second, whether any retire call ever fires — a single one would convert this page's largest caveat into a genuine burn row. Third, the pace itself: the daily moves ran a little under **7,000 LEO** each through the window, and that pace is a direct read on iFinex revenue. Fourth, the buyback sink's first outgoing transfer, which would move **47,795,807 LEO** from watched overhang to realised sell pressure. Fifth, any change to the **27%** commitment itself, which is a corporate policy and not protocol code.

## Summary

UNUS SED LEO is an exchange token with no issuance and a revenue-funded buyback, reading **−0.07% net** supply change over the 90 days to **Sep 5 2026** and projected at the same rate forward, against a supply monitor at **−0.04%**. The sell side is a clean row of zeros: no emission, no vesting, no estate, no observed issuer outflow. The buy side is **601,043 LEO** of buyback that leaves the tradable float and accumulates in the issuer's own account rather than being destroyed. The key risk is exactly that reversibility — **47,795,807 LEO** now sit in an account one transfer from the market, on a token whose mint function is live on both chains and whose supply ceiling is therefore a matter of policy, not of code.

---

*MrNasdog Pressure Framework analysis of LEO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 5 2026.*
