# E-commerce Performance Analysis — Customer Retention (2024)

**Email (for verification): 23f1002420@ds.study.iitm.ac.in**

This repository analyzes quarterly customer retention for 2024 and compares it with the industry benchmark of **85**.
It includes code, visualizations, and a data story that outlines findings, implications, and concrete recommendations.

---

## Dataset
| Quarter | RetentionRate |
| :-----: | -------------: |
| Q1 | 68.44 |
| Q2 | 74.71 |
| Q3 | 76.71 |
| Q4 | 76.73 |

**Average (2024): 74.15**  ← must appear in the README.

---

## Visualizations
Trend vs. benchmark:

![Retention Trend](figures/retention_trend.png)

Gap to benchmark by quarter:

![Gap to Benchmark](figures/target_gap.png)

---

## Key Findings
- Retention improved from **68.44** (Q1) to **76.73** (Q4), a **+8.29** pp rise.
- The 2024 average retention is **74.15**, which is **10.85** points **below** the industry benchmark of **85**.
- Momentum exists (QoQ growth), but progress is **not sufficient** to reach the target without intervention.

## Business Implications
- Being below benchmark indicates **higher churn risk**, leading to **lost LTV** and **increased acquisition costs** to replace churned customers.
- Under-benchmark retention reduces cross-sell / upsell opportunities and **compresses margins**.

## Recommendations to reach 85
1. **Implement targeted retention campaigns** (required solution): personalize offers by customer cohort (tenure, spend, category).
2. Launch a **win-back workflow** for customers with declining activity (email, SMS, WhatsApp with progressive incentives).
3. Introduce **loyalty tiers** and **cashback** for high-value segments; tie rewards to repeat purchase frequency.
4. **On-site UX nudges**: low-stock reminders, smart re-order, and cart-recovery within 24h.
5. **Support SLAs**: <2 min chat response for premium customers; prioritize post-purchase issues to prevent churn.
6. Continuous **A/B testing** of incentives to maximize uplift while protecting margin.

## How to run locally
```bash
pip install -r requirements.txt
python analyze_retention.py
```

This will regenerate the charts in `figures/` and update `metrics.json`.

## LLM Assistance
Analysis materials were prepared with assistance from an LLM (Jules / ChatGPT Codex guidance).

---

## Repo Structure
```
.
├── analyze_retention.py
├── data/
│   └── retention_2024.csv
├── figures/
│   ├── retention_trend.png
│   └── target_gap.png
├── metrics.json
├── README.md
└── requirements.txt
```
