---
title:         "FIL Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "FIL supply is growing: 16.84M vested, 11.61M collateral returned and 5.38M mined against a 585K burn gave +4.00% in 90 days, about +2.31% next as vesting ends."
canonical_url: "https://mrnasdog.com/research/fil/inflation"
tags:          ["crypto", "fil", "filecoin", "storage"]
published:     true
---

> Originally published at **[mrnasdog.com/research/fil/inflation](https://mrnasdog.com/research/fil/inflation)** by MrNasdog.

# FIL Inflation Analysis · September 2026 · Supply growing · projected to keep growing

Filecoin's FIL supply is growing fast, and the pace is about to fall. Over the last 90 days **33.83M FIL** reached the market — **16.84M** from the six-year launch vesting, **11.61M** from storage collateral coming back and **5.38M** from block rewards — while only **585.5K FIL** was burned, a net rise of **+4.00%**. The launch vesting ends on **Oct 14 2026**, so the next 90 days read about **+2.31%**; the monitor reads **+4.79%** for the last 90 days.

## The verdict, in one paragraph

The MrNasdog Pressure Framework puts FIL's net supply change at **+4.00%** over the last 90 days (Jul 1 to Sep 29 2026) and **+2.31%** for the next 90. The monitor, which reads a third-party circulating count, shows **+4.79%**, a gap of **0.79 percentage points**. That is above our 0.5-point line, so the page carries a ⚠ monitor gap note. We walked it down: the monitor's supply figure sits about 85M FIL below the chain's own count and caught up **4.8M FIL** of older supply during the window (0.60 points), and it divides by the smaller 90-day-old figure (0.19 points). The chain's own circulating supply rose **33.25M FIL**, which is exactly our sell rows less the burn. Filecoin is a **steadily inflationary storage network whose biggest unlock is about to end**.

## Sell pressure: where new FIL comes from

Three taps put FIL on the market, and the one people talk about most — mining — is the smallest. The largest is the **launch vesting**: 409.8M FIL set aside for Protocol Labs and the Filecoin Foundation at launch unlocks in a straight line over six years, about **187,100 FIL a day**. That added **16.84M FIL** in the last 90 days. The schedule is written into the chain's vesting multisigs and ends at epoch 6,456,088, on **Oct 14 2026**, so only about **2.89M FIL** is left to unlock. Protocol Labs' multisigs sent 14.8M FIL to its own wallets during the window; the Foundation's multisig did not move.

The second tap is **returned storage collateral**, which sits in our "long-term locked" row. Filecoin storage providers must lock FIL as collateral for every sector they store, and three quarters of each block reward is also locked for 180 days. When storage expires or is removed, that FIL comes back. The network shrank this window — raw storage power fell 18%, from 1.89 to 1.55 EiB — so far more collateral was returned than newly locked: the locked total fell from 75.54M to 63.93M FIL, releasing **11.61M FIL**. It came in bursts, with 4.2M FIL in the last ten days of July alone, and the next 90 days hold the same total because nothing in the protocol has changed.

The third tap is **protocol inflation**: block rewards paid from a reward pool that was minted at genesis. It paid out **5.38M FIL** in 90 days, about 59,700 a day. The reward per block shrinks by design and fell about 5% this window as storage power dropped, so the next 90 days use today's rate of about 58,350 a day, or **5.25M FIL**. There is no separate Foundation or treasury release — the mining reserve did not move — and there is no bankruptcy estate.

## Buy pressure: where new FIL goes

Very little FIL leaves the market. There is **no programmatic buyback**: no contract, treasury or company buys FIL back, and sites advertising an "official Filecoin buyback" are not project sites. The only real sink is the **protocol burn**: gas base fees, the fee each sector pays every day and penalties on failed or terminated storage go to the burn address. It took **585,488 FIL** in 90 days, about 6,500 a day, but 72% of that came in July when penalties spiked; the last ten days ran near 1,900 a day. Against 33.83M FIL coming in, the burn is about 58 times smaller.

There is **no Foundation buying** — the Foundation and Protocol Labs only send FIL out. And there is **no new long-term lock** on the buy side: new storage does lock fresh collateral, but this window less was locked than came back, so the net change is counted once, on the sell side.

## Foundation and overhang

The largest overhang is the **mining reserve**: **282.9M FIL** held by a protocol account with no release schedule. It can only be spent or burned by a network upgrade; a proposal to burn it has been debated since 2024 without being accepted, and the balance did not move this window. The **Filecoin Foundation** holds **7.55M FIL** in its launch multisig (0.70M of it still locked until Oct 14 2026) and about 10.0M FIL in the wallet that receives its withdrawals. **Protocol Labs**' four active genesis multisigs hold 5.35M FIL between them, and the wallet that receives their payouts holds about 19.6M FIL. Unlocked team coins already count as circulating, so moving or selling them adds nothing new to our count. We read these balances straight from the chain at every rebuild; if any of them falls, the outflow enters the Foundation row at the next refresh.

## How FIL compares to other decentralized storage chains

Filecoin's supply design is unusual among storage networks. Its 2B FIL cap was fully created at launch, but most of it sits in pools — the reward pool, the mining reserve and the vesting multisigs — that release on their own schedules. So FIL behaves like an uncapped, emitting chain even though the cap is fixed: circulating supply is still well under half of the 1.96B FIL total. Networks that pay storers from an endowment funded by upfront storage fees depend far less on new-coin rewards, and chains whose supply is already almost fully issued have little left to release.

The other difference is **collateral**. Filecoin makes storage providers lock FIL, which pulls coins off the market while the network grows and pushes them back when it shrinks. That makes FIL's supply swing with storage demand in a way that simple block-reward chains do not: in this window, falling storage power released more FIL than block rewards created. A network with a burn tied to real usage offsets new supply as usage grows; Filecoin's burn is small today, so it offsets almost nothing.

After Oct 14 2026 the comparison shifts. With launch vesting gone, FIL's new supply comes down to block rewards of about 21M FIL a year plus whatever collateral the network returns — much closer to a normal proof-of-storage chain with a modest reward stream.

## What to watch in the next 90 days

**Oct 14 2026 — launch vesting ends.** The last 2.89M FIL unlocks and the biggest source of new FIL stops; from then on the sell side is block rewards plus returned collateral.

**The Solstice upgrade (FIP-0118).** It went live on the Filecoin test network on Sep 28 2026 and has no main-network date yet. It would split block rewards between storage providers and paid services and burn the part not earned, and it would let storage providers upgrade existing storage in a way that locks more collateral. Its first quarter burns nothing, so it would not change our count right away.

**Storage power and collateral.** If storage power keeps falling, more collateral comes back to the market; if it stabilises, the 11.61M FIL release we project could shrink sharply — it was almost zero in late August.

**The mining reserve.** Any proposal to spend or burn the 282.9M FIL reserve would change the long-run picture; none is scheduled.

## Summary

FIL's supply grew **+4.00%** in the last 90 days: 16.84M FIL of launch vesting, 11.61M of returned storage collateral and 5.38M of block rewards, against a burn of only 585.5K FIL and no buyback. The launch vesting ends on Oct 14 2026, which brings the next 90 days down to about **+2.31%**. The key risk is collateral: a shrinking storage network keeps returning locked FIL to the market, and that release has been larger than block rewards. The 2B FIL cap is fixed, but with 282.9M FIL in the mining reserve and most of the reward pool still to pay out, FIL stays a net-emitting coin for years.

---

*MrNasdog Pressure Framework analysis of FIL, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*
