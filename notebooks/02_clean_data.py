"""Week 3 — clean and normalize the raw financial, feature-matrix, and
review datasets collected in Week 2.

Input:  data/raw/{play_store_reviews.json, app_store_reviews.json,
                   cost_efficiency.csv, feature_matrix.csv}
Output: data/processed/{reviews_clean.csv, cost_efficiency_clean.csv,
                        feature_matrix_clean.csv}
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"


def clean_reviews():
    play = json.loads((RAW / "play_store_reviews.json").read_text(encoding="utf-8"))
    app = json.loads((RAW / "app_store_reviews.json").read_text(encoding="utf-8"))
    df = pd.concat([pd.DataFrame(play), pd.DataFrame(app)], ignore_index=True)

    df["text"] = df["text"].fillna("").astype(str).str.strip().str.replace(r"\s+", " ", regex=True)
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    df["date"] = pd.to_datetime(df["date"], errors="coerce", utc=True).dt.tz_localize(None)

    before = len(df)
    df = df[df["text"].str.len() > 0]
    df = df.dropna(subset=["rating"])
    df = df.drop_duplicates(subset=["entity", "platform", "text", "rating"])
    df["rating"] = df["rating"].astype(int)

    keep_cols = ["entity", "platform", "review_id", "rating", "text", "date", "app_version", "title"]
    for c in keep_cols:
        if c not in df.columns:
            df[c] = np.nan
    df = df[keep_cols].sort_values(["entity", "platform", "date"]).reset_index(drop=True)

    PROCESSED.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED / "reviews_clean.csv", index=False)
    print(f"reviews: {before} raw -> {len(df)} clean rows -> data/processed/reviews_clean.csv")
    return df


def clean_cost_efficiency():
    df = pd.read_csv(RAW / "cost_efficiency.csv")
    df["entity"] = df["entity"].str.strip()
    df["metric"] = df["metric"].str.strip()
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df["confidence"] = df["confidence"].str.strip().str.lower()
    df = df.drop_duplicates()
    df.to_csv(PROCESSED / "cost_efficiency_clean.csv", index=False)
    print(f"cost_efficiency: {len(df)} rows -> data/processed/cost_efficiency_clean.csv")
    return df


def clean_feature_matrix():
    df = pd.read_csv(RAW / "feature_matrix.csv")
    df["feature"] = df["feature"].str.strip()
    for col in ["jupiter", "hdfc_bank"]:
        df[col] = df[col].str.strip().str.title()
    df.to_csv(PROCESSED / "feature_matrix_clean.csv", index=False)
    print(f"feature_matrix: {len(df)} rows -> data/processed/feature_matrix_clean.csv")
    return df


if __name__ == "__main__":
    clean_reviews()
    clean_cost_efficiency()
    clean_feature_matrix()
