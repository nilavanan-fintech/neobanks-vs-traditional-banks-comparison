# App Store Ratings — Proxy NPS Inputs

Observed 2026-07-10. Direct WebFetch of the live Google Play / App Store listing pages returned JS-rendered shells (blocked for simple fetchers) — figures below come from secondary aggregators (MWM.ai, JustUseApp, Kimola, AppGrooves-derived search snippets), which disagreed across sources. **Treat as directionally indicative, not verified precise counts.** Recommend a human manually open each listing on a phone/browser during Week 2 and log the exact figure — canonical URLs:

- Jupiter: https://play.google.com/store/apps/details?id=money.jupiter · https://apps.apple.com/in/app/jupiter-cards-upi-banking/id1507748747
- HDFC Bank: https://play.google.com/store/apps/details?id=com.snapwork.hdfc · https://apps.apple.com/in/app/hdfc-bank-mobilebanking/id515891771

## Ratings snapshot

| App | Platform | Rating | Review count | Source type | Confidence |
|---|---|---|---|---|---|
| Jupiter | Google Play | ~4.7/5 | 1M+ downloads (review count unconfirmed) | search aggregation | unverified |
| Jupiter | Apple App Store | 4.6–4.7/5 | ~327 to ~54.5K (sources disagree) | Kimola, MWM.ai | unverified |
| HDFC Bank MobileBanking | Google Play | ~3.4–3.9/5 | ~982K+ | AppGrooves, MWM.ai | unverified |
| HDFC Bank MobileBanking | Apple App Store | conflicting: 1.9/5 (17K reviews) vs 3.4/5 | 17,000+ | MWM.ai vs. general aggregation | unverified, needs manual check |

## Review themes (for sentiment/NLP seeding in Week 3)

**Jupiter — positive:** clean/modern UI, good UPI experience, rewards ("Jewels")/cashback, easy account tracking.
**Jupiter — negative:** unresponsive customer support (bot-heavy, no phone helpline), stuck-at-OTP/login freezes on iOS, misleading cashback/reward claims, slow refund resolution.

**HDFC MobileBanking — positive:** fast transaction processing in newer app versions, biometric/security features, wide transaction coverage (150+ services), trusted "large bank" reputation.
**HDFC MobileBanking — negative:** frequent login/authentication failures, app heaviness (requires Wi-Fi), missing RBI-mandated 2FA step for FD breaking, NRI friction (Indian-number-only OTP), intrusive in-app ad banners during transactions.
