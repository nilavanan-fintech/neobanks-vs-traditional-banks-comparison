# Neobanks vs Traditional Banks: A Financial Performance & Customer Experience Comparison

A comparative analytics project benchmarking a digital-first neobank (**Jupiter** or **Fi Money**) against a traditional bank (e.g. **HDFC Bank**, **ICICI Bank**) on four pillars: **cost efficiency**, **customer acquisition cost (CAC)**, **Net Promoter Score (NPS)**, and **product offerings**.

> See `guide.html` for the full illustrated walkthrough. This README is the quick-reference version.

## 1. Thesis

Neobanks compete on experience and product velocity; traditional banks compete on scale, trust, and balance-sheet economics. This project quantifies that trade-off across the four pillars above, using one neobank and one traditional bank as a clean head-to-head.

**Reality check:** most Indian neobanks (Jupiter, Fi Money, Open) don't disclose an official NPS or full audited financials the way listed banks do. Several figures here are proxy-derived from app-store reviews, funding disclosures, and sector reports — this project is explicit about which numbers are official vs. modelled.

## 2. Roadmap (5–6 weeks)

| Week | Phase | Output |
|---|---|---|
| 1 | Scope & framework | KPI rubric, entity selection |
| 2 | Data collection | Raw financials, reviews, survey responses |
| 3 | Cleaning & NLP | Clean dataset, sentiment-scored reviews |
| 4 | Analysis | Cost-to-income, CAC, proxy-NPS, product-depth scores |
| 5 | Visualization & story | Dashboard, findings narrative |
| 6 | Polish | README, demo video, GitHub repo |

## 3. Tools

| Stage | Tools |
|---|---|
| Collection | Python (`requests`, `BeautifulSoup`), `google-play-scraper`, `app-store-scraper`, Google Forms |
| Cleaning / Analysis | `pandas`, `NumPy`, `scipy` / `statsmodels` |
| NLP / Sentiment | `VADER`, `TextBlob`, or a small HuggingFace sentiment model |
| Visualization | Power BI or Tableau Public, `matplotlib` / `seaborn` / `plotly` |
| Delivery | Jupyter Notebook, GitHub, optional Streamlit app |

## 4. Datasets & sources

| Pillar | Source | Extract |
|---|---|---|
| Cost efficiency | MCA/RoC filings (Tofler, Zauba Corp), bank annual reports / investor decks | Revenue, net profit/loss, opex → cost-to-income ratio, burn multiple |
| CAC | Funding & press coverage (Inc42, Entrackr, Tracxn), marketing spend disclosures | Acquisition spend ÷ new customers |
| NPS (proxy) | Google Play / App Store reviews, own primary survey (Google Forms, n=50–100) | Star ratings + sentiment → promoter/detractor split |
| Product offerings | Bank/neobank websites and apps, RBI licensed-bank list | Feature matrix: savings, FD, cards, UPI, lending, investing, insurance, forex |
| Industry benchmarks | RBI annual report / Trend & Progress of Banking in India, Statista, sector reports (Inc42, Inventiva, UV Netware neobank coverage) | Market size, funding trends, sector profitability context |

## 5. Metrics & formulas

- **Cost-to-Income Ratio** = Operating Cost ÷ Operating Income × 100
- **Burn Multiple** = Net Cash Burned ÷ Net New Revenue
- **CAC** = Total Acquisition Spend ÷ New Customers Added
- **Proxy NPS** = % Promoters (4–5★ / positive sentiment) − % Detractors (1–2★ / negative sentiment)
- **Product Depth Score** = Σ(feature present × weight) ÷ max possible score
- **Composite Comparison Index** = weighted average of the four normalized pillar scores (0–100), feeds the radar chart

## 6. Deliverables

1. Cleaned dataset (CSV/Excel) — financials, sentiment scores, feature matrix
2. Analysis notebook (Jupyter) — every formula computed and commented
3. Interactive dashboard (Power BI / Tableau) — radar chart + financial trend lines
4. Findings report (2–4 pages) — thesis, method, results, limitations, recommendation
5. This README + public GitHub repo
6. 2–3 minute recorded walkthrough (for LinkedIn / interviews)

## 7. Suggested repo structure

```
neobank-vs-traditional-bank/
├── README.md
├── guide.html
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── analysis.ipynb
├── dashboard/
│   └── comparison.pbix (or .twbx)
├── survey/
│   └── nps_survey_responses.csv
└── report/
    └── findings.pdf
```

## 8. Known limitations to state upfront

- Neobank financials are often self-reported, modelled, or sourced from press coverage rather than audited statements.
- Official NPS is rarely published by either neobanks or traditional banks in India — treat all NPS figures in this project as **proxy scores**, and validate with your own survey where possible.
- App-store reviews skew toward extreme experiences (very happy or very frustrated users), so sentiment-based NPS should be read as directional, not definitive.
