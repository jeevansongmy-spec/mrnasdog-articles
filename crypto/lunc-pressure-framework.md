---
title: "LUNC Inflation Analysis · August 2026 · Mixed flows, supply roughly steady"
description: "A MrNasdog Pressure Framework read of Terra Classic (LUNC): the mint is switched off, and a 0.5% burn tax plus exchange burns removed ~7.5B LUNC in 90 days. Framework -0.14%, monitor +0.02%."
canonical_url: "https://mrnasdog.com/research/lunc/inflation"
tags: ["crypto", "lunc", "terra-classic", "burn"]
published: true
---

> Originally published at **[mrnasdog.com/research/lunc/inflation](https://mrnasdog.com/research/lunc/inflation)** by MrNasdog.

Terra Classic is a rare thing in this framework: a chain that cannot make more of its own token. The mint module reads **zero** on two independent nodes, so no new LUNC is issued at all. The only forces on supply are a **0.5%** on-chain burn tax and monthly exchange burns, which together destroyed about **7.5B LUNC** over the last 90 days, against a single **9.9M** governance spend on the sell side. Net that is **-0.14%** — genuinely deflationary — while our supply monitor reads **+0.02%**, a gap of just **0.15 percentage points** that ships no monitor-gap chip. Against a circulating base of **5.52T LUNC**, the burn is real but small, and cooling.

## The verdict, in one paragraph

For the 90-day window ending Aug 2 2026, the Pressure Framework reads **LUNC at -0.14% net**. Sell pressure is effectively **zero** — one **9.9M LUNC** community-pool spend — while buy-side burns removed about **7.5B LUNC**, against a circulating base of **5.52T LUNC**. Our supply monitor reads the realised change at **+0.02%**, a gap of **0.15 percentage points**, comfortably inside tolerance, so no monitor-gap chip ships. That agreement is itself the story: the previous build in July carried a warning chip because the monitor then read **+0.90%**, an aggregator reclassification of about 60B LUNC out of the non-circulating bucket that had stepped up in early May and sat just inside that window; the deep walk predicted it would age out, and it now has. Terra Classic is best characterised as **a burn-only chain with no issuance** — deflationary by mechanism, but slowly, because the burn tracks trading volume that has faded from its spring highs.

## Sell pressure: where new LUNC comes from

There is almost nowhere for new LUNC to come from, and that is the defining fact. Sell #1, protocol inflation, is **zero** because the mint module is switched off: reading the chain directly, the mint **inflation** parameter, both the **inflation_min** and **inflation_max** bounds, and **annual_provisions** all return zero, confirmed on two independent nodes. Terra Classic physically cannot issue a single new coin under its current parameters, and the supply arithmetic proves it — the original post-collapse supply of about **6.907T** minus every coin ever burned (**454.0B** cumulative) matches the live on-chain total of **6.453T** to within a rounding fraction, leaving no room for a mint term.

Sell #2, vesting unlocks, is **zero** because there is no unlock calendar left. The original team and investor allocations finished releasing years ago, and the trillions of LUNC created during the May 2022 depeg were minted straight into circulation rather than locked, so no schedule exists to release more. Sell #3, foundation and unscheduled unlocks, is a token **9.9M LUNC**: there is no foundation entity, and the only team-controlled pool is the DAO community pool, which moves only by a passed governance vote. In this window exactly one such spend passed — proposal **12222**, funding a cross-chain deployment — for about 9.9M LUNC, roughly **0.0002%** of supply. Sell #4, long-term locked or bankruptcy, is **zero**: the Terraform Labs Chapter 11 estate distributed nothing over the window, its dissolution deadline was extended to **Dec 31 2026**, and its stated intent is to burn its remaining LUNC rather than sell it.

## Buy pressure: where new LUNC goes

The entire net story lives on the buy side, and it is all burning. Buy #2, protocol fee burn, is about **5.70B LUNC**: a **0.5%** tax is charged on on-chain transfers, most of it sent to the burn address, and validators and community members send further LUNC to be destroyed on top of it. This burn is permanent — coins leave total supply entirely, and the on-chain total only ever falls. Buy #5, added as an extra row because it is a different mechanism, is about **1.80B LUNC** of exchange burns: the largest exchange destroys the LUNC it collects from trading fees once a month and announces it, roughly **600M** in each of June, July and August. Together the two burn mechanisms removed about **7.5B LUNC** over 90 days.

The remaining buy rows are all **zero**. Buy #1, programmatic buyback, is zero because the chain keeps no protocol revenue to fund open-market purchases and no DAO buyback has been deployed. Buy #3, foundation buy, is zero because no foundation or treasury entity exists to buy LUNC. Buy #4, new long-term lock, is zero and deserves a clarification, because about **905.4B LUNC** is staked and that can look like a lock. It is not one: staking here is standing delegation with a **21-day** unbonding period, a delay rather than a commitment, and every staked coin stays inside the circulating figure. No new lock contract exists or was announced.

## Foundation and overhang

Three team-controlled overhangs are tracked on Terra Classic. The first is the **DAO community pool**, a protocol treasury refilled by a share of gas fees that held about **8.46B LUNC** when read this session; it is unscheduled by design, releasing only by passed governance vote, and its one in-window spend was the 9.9M in Sell #3. The second is the **Terraform Labs Chapter 11 estate**, whose LUNC sits in exchange custody with no public address list — the community's own proposal to enumerate it was rejected — so it is monitored through estate reporting rather than a readable address; it distributed nothing over the window. The third is the **non-circulating classification bucket** of about **928.8B LUNC**, the difference between total and circulating supply, which has no published release schedule and is the one figure that can move without any chain event. All three are re-read on every rebuild, and if any balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How LUNC compares to other burn-model chains

The first comparison is mint versus no mint. Most proof-of-stake chains pay staking rewards from fresh issuance, so their sell side never stops; Terra Classic switched issuance off entirely and pays staking rewards purely from recycled fees and its tax split. That puts LUNC in a very small group — alongside fixed-supply tokens and fully-emitted assets — where the sell side of the ledger is structurally near-empty. The difference from a hard-capped coin is that LUNC has no maximum supply written into code; it simply has no active mint, which governance could in principle re-enable, so the zero is a policy state rather than a protocol guarantee.

The second comparison is burn versus no burn. Large fee-burning networks route a slice of every transaction fee to destruction, so a busy chain can print negative net supply; LUNC does the same through its **0.5%** tax, and layers discretionary exchange burns on top. The economic catch is that a burn this size only matters against the denominator it works on — **7.5B** destroyed is a large headline number, but against **5.52T** circulating it is a **0.14%** reduction over 90 days. A token whose supply is measured in trillions needs enormous absolute burns to move the percentage, which is why LUNC reads as quietly deflationary rather than sharply so.

The third comparison is float. LUNC does carry a heavy non-circulating bucket, about **928.8B** of the **6.45T** total, so its circulating figure is a classification rather than a chain read — the direct cause of the aggregator gap that the previous build flagged. That makes LUNC less transparent than a fully-circulating asset, but the risk is one-directional here: with no mint and no vesting, the bucket can only shrink into circulation slowly and by governance, never by scheduled unlock.

## What to watch in the next 90 days

First, proposal **12223**, which would raise the on-chain tax from **0.5%** to **1.5%** — it entered voting on **Jul 25 2026** and, if it passes, would roughly triple the on-chain component of the burn and is the single largest lever on this reading. Second, the burn rate itself, which has cooled from about **91M** a day in spring to nearer **50M** a day by late July as trading volume faded; because the burn tracks volume, a renewed rally would speed it up and a quiet quarter would slow it further. Third, the monthly exchange burn, the next of which lands around **Sep 1 2026** at roughly **600M LUNC**. Fourth, the Terraform Labs estate, whose dissolution deadline of **Dec 31 2026** and stated intent to burn rather than distribute would remove supply if executed. Fifth, any governance move to re-enable the mint, which remains the one thing that could turn the sell side back on.

## Summary

Terra Classic (LUNC) is a burn-only chain: its mint module reads **zero** on two independent nodes, so no new LUNC is issued, and the only supply forces are a **0.5%** on-chain burn tax and monthly exchange burns that together destroyed about **7.5B LUNC** over 90 days, against a single **9.9M** governance spend — a framework reading of **-0.14% net** against a monitor reading of **+0.02%**. The key constraint is the denominator: a **5.52T** circulating base means even large absolute burns register as a small percentage, so LUNC is deflationary but slowly. The main risk to the reading is not new issuance but the burn rate cooling with volume, while the main upside lever is the pending vote to triple the tax. There is no maximum supply, but there is also, for now, no way to make more.

---

*MrNasdog Pressure Framework analysis of LUNC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 2 2026.*
