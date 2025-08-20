# How to Create the GitHub Pull Request (PR)

> This guide shows both the **GitHub Website** method and the **Git CLI** method.
> Replace placeholders like `[YOUR_USERNAME]` with your actual values.

---

## Option A — GitHub Website (easiest)

1. **Create a new repository** (suggested name): `ecommerce-retention-analysis`.
2. Click **Add file → Upload files** and upload everything from this folder:
   - `analyze_retention.py`
   - `data/retention_2024.csv`
   - `figures/retention_trend.png`
   - `figures/target_gap.png`
   - `metrics.json`
   - `README.md` (contains your email and the correct average: **74.15**)
   - `requirements.txt`
3. On the repo page, click the **branch dropdown** (usually says `main`) → type a new branch name like `feature/retention-analysis` and **create branch**.
4. Make any small edit (e.g., tweak README) on this new branch and **Commit changes**.
5. Now click **Compare & pull request**.
6. Fill the PR title and description. Ensure the PR shows:
   - Your **email** somewhere in the content: `23f1002420@ds.study.iitm.ac.in`
   - The average value **74.15** in `README.md`
   - The phrase **"implement targeted retention campaigns"**
7. Click **Create pull request**.
8. **Copy the PR URL** from your browser. It will look like:
   `https://github.com/[YOUR_USERNAME]/ecommerce-retention-analysis/pull/1`

---

## Option B — Git (VS Code / Terminal)

```bash
# 1) Create and enter folder
git init ecommerce-retention-analysis
cd ecommerce-retention-analysis

# 2) Copy the files from this package into the folder (or unzip here)

# 3) Create repo on GitHub (website) and add remote
git remote add origin https://github.com/[YOUR_USERNAME]/ecommerce-retention-analysis.git

# 4) Commit to main
git add .
git commit -m "Add retention analysis, charts, and README (74.15 avg)"

# 5) Push main
git branch -M main
git push -u origin main

# 6) Create a feature branch for the PR
git checkout -b feature/retention-analysis
echo "" >> README.md  # (Optional tiny change so the branch differs)
git add README.md
git commit -m "Minor update to README for PR demo"
git push -u origin feature/retention-analysis
```

7. On GitHub, open a **Pull Request** from `feature/retention-analysis` → `main`.
8. Copy the **PR URL** (e.g. `https://github.com/[YOUR_USERNAME]/ecommerce-retention-analysis/pull/1`).

---

## Raw file URLs (if needed)

- Raw README:
  `https://raw.githubusercontent.com/[YOUR_USERNAME]/ecommerce-retention-analysis/main/README.md`
- Raw dataset:
  `https://raw.githubusercontent.com/[YOUR_USERNAME]/ecommerce-retention-analysis/main/data/retention_2024.csv`
- Raw code:
  `https://raw.githubusercontent.com/[YOUR_USERNAME]/ecommerce-retention-analysis/main/analyze_retention.py`

