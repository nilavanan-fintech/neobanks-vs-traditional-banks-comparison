"""Week 3 — score the qualitative product feature matrix numerically
so Week 4 can fold it into the composite comparison index.

Yes = 1.0, Partial = 0.5, No = 0.0

Input:  data/processed/feature_matrix_clean.csv
Output: data/processed/feature_matrix_scored.csv
"""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
PROCESSED = ROOT / "data" / "processed"

SCORE_MAP = {"Yes": 1.0, "Partial": 0.5, "No": 0.0}

if __name__ == "__main__":
    df = pd.read_csv(PROCESSED / "feature_matrix_clean.csv")

    for col in ["jupiter", "hdfc_bank"]:
        df[f"{col}_score"] = df[col].map(SCORE_MAP)

    totals = pd.DataFrame({
        "feature": ["TOTAL / product-depth score"],
        "jupiter": [""],
        "hdfc_bank": [""],
        "notes_source": [""],
        "jupiter_score": [df["jupiter_score"].sum()],
        "hdfc_bank_score": [df["hdfc_bank_score"].sum()],
    })
    out = pd.concat([df, totals], ignore_index=True)

    out.to_csv(PROCESSED / "feature_matrix_scored.csv", index=False)
    print(out[["feature", "jupiter_score", "hdfc_bank_score"]].to_string(index=False))
    print("-> data/processed/feature_matrix_scored.csv")
