"""Week 2/3 — pull raw app reviews for Jupiter and HDFC Bank.

Google Play via google-play-scraper; Apple App Store via the public
customer-reviews RSS/JSON feed (no extra dependency, avoids the
unmaintained app-store-scraper package's urllib3 pin).

Output: data/raw/play_store_reviews.json, data/raw/app_store_reviews.json
"""
import json
from pathlib import Path

import requests
from google_play_scraper import Sort, reviews

RAW_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"

PLAY_APPS = {
    "jupiter": "money.jupiter",
    "hdfc_bank": "com.snapwork.hdfc",
}

APP_STORE_APPS = {
    "jupiter": 1507748747,
    # id515891771 (HDFC Bank MobileBanking) from README/roadmap is stale/delisted;
    # current listing is "HDFC Bank App: Banking & Cards", track id 6504402552.
    "hdfc_bank": 6504402552,
}


def scrape_play_store(count=200):
    rows = []
    for entity, pkg in PLAY_APPS.items():
        result, _ = reviews(pkg, lang="en", country="in", sort=Sort.NEWEST, count=count)
        for r in result:
            rows.append({
                "entity": entity,
                "platform": "google_play",
                "review_id": r["reviewId"],
                "rating": r["score"],
                "text": r["content"],
                "date": r["at"].isoformat() if r["at"] else None,
                "app_version": r.get("appVersion"),
                "thumbs_up": r.get("thumbsUpCount"),
            })
        print(f"play_store/{entity}: {len(result)} reviews")
    return rows


def scrape_app_store(pages=10):
    rows = []
    for entity, app_id in APP_STORE_APPS.items():
        entity_count = 0
        for page in range(1, pages + 1):
            url = (
                f"https://itunes.apple.com/in/rss/customerreviews/"
                f"page={page}/id={app_id}/sortBy=mostRecent/json"
            )
            resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=20)
            if resp.status_code != 200:
                break
            entries = resp.json().get("feed", {}).get("entry", [])
            if not entries or (page == 1 and len(entries) == 1):
                break
            # first entry on page 1 is the app itself, not a review
            for e in entries:
                if "im:rating" not in e:
                    continue
                rows.append({
                    "entity": entity,
                    "platform": "app_store",
                    "review_id": e.get("id", {}).get("label"),
                    "rating": int(e["im:rating"]["label"]),
                    "text": e.get("content", {}).get("label", ""),
                    "date": e.get("updated", {}).get("label"),
                    "title": e.get("title", {}).get("label"),
                })
                entity_count += 1
        print(f"app_store/{entity}: {entity_count} reviews")
    return rows


if __name__ == "__main__":
    play_rows = scrape_play_store()
    (RAW_DIR / "play_store_reviews.json").write_text(
        json.dumps(play_rows, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    app_rows = scrape_app_store()
    (RAW_DIR / "app_store_reviews.json").write_text(
        json.dumps(app_rows, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"total: {len(play_rows)} play store + {len(app_rows)} app store reviews")
