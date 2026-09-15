---
title: "BTT Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description: "Mixed flows, supply roughly steady: BTT reads 0.00% over 90 days. BitTorrent cannot mint or burn, and its staking payouts only move coins already in the float."
canonical_url: "https://mrnasdog.com/research/btt/inflation"
tags: ["crypto", "btt", "bittorrent", "tron"]
published: true
---

> Originally published at **[mrnasdog.com/research/btt/inflation](https://mrnasdog.com/research/btt/inflation)** by MrNasdog.

BitTorrent cannot create or destroy a single BTT — the token contract on TRON has no mint function and no burn function — and the Pressure Framework reads BTT at **0.00%** over the trailing 90 days and **0.00%** over the next 90. Coins did move: **399.9B BTT** of BitTorrent Chain staking rewards were claimed and a wallet public reporting ties to TRON's founder sent **212B BTT** to an exchange. But both came from wallets already counted as circulating, so neither added to the float. Sell pressure is **0**, buy pressure is **0**, and the ceiling is a fixed **990,000B BTT** that no function in the contract can raise.

## The verdict, in one paragraph

Against a circulating base of **987,038B BTT**, the framework books **0** of sell pressure and **0** of buy pressure over the trailing 90 days — a net of **0.00%** — and projects **0.00%** for the next 90 days. The inflation monitor reads **-0.33%** for the same window, a gap of **0.33 percentage points**, which is inside the framework's 0.5pp tolerance, so no monitor-gap warning ships on the overview page. The monitor rebuilds supply from market value divided by price, which carries day-to-day pricing noise on a token priced in fractions of a millionth of a dollar; the counted circulating figure itself did not change by a single BTT across the window. The label for BTT is **a frozen supply with a large, unscheduled insider overhang and a buyback that has not started**.

## Sell pressure: where new BTT comes from

It does not come from minting. The BTT contract on TRON exposes eleven functions — the standard transfer, approval and balance calls — and the deployed bytecode contains no selector for minting, burning or changing ownership. Its supply reads **990,000B BTT**, and no code path can ever move that number. Of that, **987,038B** is counted as circulating, which leaves only about **2,962B BTT** outside the float in total. That small figure decides every sell row, because a coin only adds to the float when it leaves a wallet outside that **2,962B** bucket.

Sell #1, protocol inflation, is **0**. BitTorrent Chain keeps all BTT staking in a contract on TRON, and rewards are paid out of it: over these 90 days delegators claimed **374.7B BTT** and validators **25.2B BTT**, every claim matched to its token transfer and confirmed on a second data provider. But that staking contract holds **23,607B BTT** — eight times the entire non-circulating bucket — so it is necessarily counted as circulating already. Paying stakers out of it moves coins inside the float; it does not add to it. The counted circulating figure did not step on any claim date.

Sell #2, vesting unlocks, is **0**. Every original BTT allocation — team, TRON Foundation, seed, private and public sales, ecosystem, partnerships and both airdrops — has already reached the end of its release schedule, and the monthly airdrop to TRX holders was stopped in **June 2020**. No cliff falls in either window.

Sell #3, foundation and unscheduled unlocks, is **0** for the same reason. On **Aug 19 2026** a wallet that public reporting describes as controlled by TRON's founder sent **212B BTT** to an exchange deposit address. Before that transfer it held about **52,675B BTT**, seventeen times the whole non-circulating bucket, so it was inside the float and the sale changed owners rather than supply. Sell #4, long-term locked or bankruptcy, is **0**: no bankruptcy estate, trustee or court-ordered distribution is attached to BTT.

## Buy pressure: where new BTT goes

Nowhere yet. Buy #1, programmatic buyback, is **0** — but it is the row most likely to change. On **Jul 6 2026** BitTorrent announced that **100%** of revenue from its decentralized services will buy BTT on the open market every quarter, with the coins destroyed and the amount, share of supply and transaction published after each round. The first burn is due in **mid-October 2026**. No buying wallet, revenue figure or target size has been disclosed, so there is nothing to project.

Buy #2, protocol fee burn, is **0**, and it is a measured zero. Because the BTT contract has no burn function, the count of BTT in existence can never fall; a burn on BTT can only be a transfer to an address nobody controls. The TRON null address, which holds **7.9B BTT** from past burns, received nothing in these 90 days — its last arrival was **Dec 5 2025** — and two other unspendable addresses were silent as well. BitTorrent Chain blocks carry no base fee, so the chain destroys nothing either.

Buy #3, foundation buy, is **0**: no team or foundation wallet bought BTT on the market. Buy #4, new long-term lock, is **0**. Staking did grow — a net **3,102B BTT** moved into the staking contract over the window — but staked BTT can be withdrawn after a short wait and is already counted as circulating, so it removes nothing from this reading.

## Foundation and overhang

The BTT overhang is large, concentrated and entirely unscheduled — and almost all of it is already counted as circulating, which is why none of it shows in the number. The biggest identified item is a pair of wallets that public reporting links to TRON's founder: the one that sold on Aug 19 2026 still holds **52,463B BTT**, and a second holds **112,604B BTT** and has not moved since **July 2025**. The staking contract holds **23,607B BTT** of stakers' funds and pays the rewards. All three are read from the chain at every rebuild.

The newest item came from the closure of the BitTorrent Chain bridge. Deposits closed on **Jun 13 2026**, and on **Jul 7 2026** the bridge contract on TRON was upgraded and its remaining **8,896B BTT** was withdrawn into a brand-new wallet that made the call itself. That balance is three times the non-circulating bucket, so it is already counted as circulating. There is a separate wrinkle: those coins used to back BTT still sitting on BitTorrent Chain, and that copy still exists, so a sale from this wallet would put coins on the market twice over. Only the roughly **2,962B BTT** outside the float could ever enter this reading. If it shrinks between refreshes, that outflow enters Sell #3 at the next refresh.

## How BTT compares to other fixed-supply tokens

BTT sits in the strictest supply class there is: a token whose contract simply has no mint and no burn function. That is harder than a halving schedule. Bitcoin still mints on every block at a shrinking rate, so its reading is positive on a known clock. BTT mints nothing, ever — and it cannot burn either, which is the less-noticed half. Tokens with a burn function can shrink their recorded supply; BTT can only park coins at dead addresses, and those addresses have received less than **0.001%** of supply in their whole history.

Proof-of-stake chains usually pay stakers with freshly minted coins, so their inflation shows up in the supply figure every quarter. BitTorrent Chain pays stakers from BTT that already exists and is already counted as circulating, so its staking costs holders nothing in dilution. The trade-off is concentration: with **99.7%** of supply already classed as circulating, BTT's risk is not new coins but who holds the old ones, and how much of that sits with a handful of insider wallets.

The last comparison is to exchange-linked tokens that burn from revenue every quarter. Those can read genuinely negative because the burn scales with usage. BTT has now adopted the same design on paper, funded by storage, file-sharing and AI-compute revenue. Because nothing is being added, any burn at all would turn BTT's reading negative — the open question is whether the revenue is large enough to show at a **990,000B** supply.

## What to watch in the next 90 days

First, the first quarterly buyback burn in **mid-October 2026**: any burn turns BTT from flat to shrinking, and the burn address it uses will be read at every rebuild. Second, the **8,896B BTT** swept out of the closed bridge on **Jul 7 2026** — a sale would not change this reading, but it would put coins on the market while the BitTorrent Chain copies they once backed still exist. Third, the founder-linked wallets holding **52,463B** and **112,604B BTT**, whose exits have no calendar. Fourth, the roughly **2,962B BTT** classed as not circulating — the only pot whose release would register here. Fifth, the staking contract at **23,607B BTT**, whose reward payouts run continuously.

## Summary

The MrNasdog Pressure Framework reads BTT at **0.00%** over the trailing 90 days and **0.00%** projected forward: mixed flows, supply roughly steady. BitTorrent's token cannot be minted or burned, nothing reached a dead address in 90 days, and the **399.9B BTT** of staking rewards and **212B BTT** founder-linked sale both came from wallets already counted as circulating. The key risk is concentration rather than issuance: wallets linked to TRON's founder and a team wallet holding the swept bridge reserve control more than **173,000B BTT** with no release schedule. The ceiling is the genuine comfort — **990,000B BTT**, fixed in code — and the October buyback burn is the first chance for the reading to turn negative.

---

*MrNasdog Pressure Framework analysis of BTT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 15 2026.*
