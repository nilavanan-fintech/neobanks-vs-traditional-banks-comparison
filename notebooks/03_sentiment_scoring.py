"""Week 3 — VADER sentiment scoring on cleaned reviews.

Input:  data/processed/reviews_clean.csv
Output: data/processed/reviews_sentiment.csv (per-review scores)
        data/processed/sentiment_summary.csv (per-entity/platform rollup,
        feeds the Week 4 proxy-NPS calculation)
"""
from pathlib import Path

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

ROOT = Path(__file__).resolve().parent.parent
PROCESSED = ROOT / "data" / "processed"

analyzer = SentimentIntensityAnalyzer()


def score(text):
    s = analyzer.polarity_scores(text)
    return s["compound"], s["pos"], s["neu"], s["neg"]


def label(compound):
    if compound >= 0.05:
        return "positive"
    if compound <= -0.05:
        return "negative"
    return "neutral"


if __name__ == "__main__":
    df = pd.read_csv(PROCESSED / "reviews_clean.csv")

    scores = df["text"].apply(score)
    df[["compound", "pos", "neu", "neg"]] = pd.DataFrame(scores.tolist(), index=df.index)
    df["sentiment"] = df["compound"].apply(label)

    df.to_csv(PROCESSED / "reviews_sentiment.csv", index=False)
    print(f"scored {len(df)} reviews -> data/processed/reviews_sentiment.csv")

    summary = (
        df.groupby(["entity", "platform"])
        .agg(
            n_reviews=("text", "count"),
            avg_star_rating=("rating", "mean"),
            avg_compound=("compound", "mean"),
            pct_positive=("sentiment", lambda s: (s == "positive").mean() * 100),
            pct_negative=("sentiment", lambda s: (s == "negative").mean() * 100),
        )
        .round(3)
        .reset_index()
    )
    summary.to_csv(PROCESSED / "sentiment_summary.csv", index=False)
    print(summary.to_string(index=False))
    print("-> data/processed/sentiment_summary.csv")
