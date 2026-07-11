# Roadmap

Neobanks vs Traditional Banks — 5–6 week project plan. See `README.md` for the project thesis and `guide.html` for the illustrated walkthrough.

## Week 1 — Scope & framework
- [ ] Finalize entity selection (neobank: Jupiter or Fi Money; traditional bank: HDFC or ICICI)
- [ ] Define KPI rubric for the four pillars: cost efficiency, CAC, NPS, product offerings
- [ ] Set up repo structure (`data/`, `notebooks/`, `dashboard/`, `survey/`, `report/`)
- **Output:** KPI rubric, entity selection

## Week 2 — Data collection
- [ ] Pull financials from MCA/RoC filings, annual reports, investor decks
- [ ] Scrape app-store / Play Store reviews (`google-play-scraper`, `app-store-scraper`)
- [ ] Draft and launch primary NPS survey (Google Forms, n=50–100)
- [ ] Collect CAC signals from funding & press coverage (Inc42, Entrackr, Tracxn)
- **Output:** Raw financials, reviews, survey responses

## Week 3 — Cleaning & NLP
- [x] Clean and normalize financial and survey datasets (`pandas`, `NumPy`)
- [x] Run sentiment scoring on reviews (`VADER` / `TextBlob` / HuggingFace model)
- [x] Build the feature matrix for product offerings
- **Output:** Clean dataset, sentiment-scored reviews — see `data/processed/` (`reviews_sentiment.csv`, `sentiment_summary.csv`, `cost_efficiency_clean.csv`, `feature_matrix_scored.csv`); pipeline scripts in `notebooks/01_scrape_reviews.py`–`04_feature_matrix.py`

## Week 4 — Analysis
- [x] Compute cost-to-income ratio and burn multiple
- [x] Compute CAC
- [x] Compute proxy-NPS from sentiment/star-rating split
- [x] Compute product-depth score
- [x] Compute composite comparison index
- **Output:** Cost-to-income, CAC, proxy-NPS, product-depth scores — see `data/processed/` (`cost_efficiency_scores.csv`, `cac_signals_clean.csv`, `proxy_nps.csv`, `product_depth_scores.csv`, `composite_index.csv`); pipeline notebooks in `analysis/01_cost_efficiency.ipynb`–`05_composite_index.ipynb`

## Week 5 — Visualization & story
- [ ] Build interactive dashboard (Power BI or Tableau Public) with radar chart + trend lines
- [ ] Draft findings narrative
- **Output:** Dashboard, findings narrative

## Week 6 — Polish
- [ ] Finalize README and guide.html
- [ ] Record 2–3 minute walkthrough video
- [ ] Publish GitHub repo
- **Output:** README, demo video, GitHub repo

## Known risks
- Neobank financials are often self-reported or modelled, not audited.
- Official NPS is rarely published in India — treat as proxy, validate with survey.
- App-store review sentiment skews toward extremes; read as directional, not definitive.
