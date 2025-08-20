# analyze_retention.py
# Email for verification: 23f1002420@ds.study.iitm.ac.in

import json
import pandas as pd
import matplotlib.pyplot as plt

BENCHMARK = 85.0

def main():
    df = pd.read_csv("data/retention_2024.csv")
    avg = df["RetentionRate"].mean()
    avg_rounded = round(avg, 2)
    print(f"Average Retention (2024): {avg_rounded}")  # Should be 74.15

    # Trend plot
    plt.figure(figsize=(7, 4))
    plt.plot(df["Quarter"], df["RetentionRate"], marker="o", label="Retention Rate")
    plt.axhline(BENCHMARK, linestyle="--", label=f"Benchmark ({BENCHMARK})")
    for i, v in enumerate(df["RetentionRate"]):
        plt.annotate(f"{v:.2f}", (df["Quarter"][i], v), textcoords="offset points", xytext=(0,6), ha="center")
    plt.title("Customer Retention Trend - 2024")
    plt.xlabel("Quarter")
    plt.ylabel("Retention Rate")
    plt.legend()
    plt.tight_layout()
    plt.savefig("figures/retention_trend.png", dpi=200)
    plt.close()

    # Gap plot
    gap = BENCHMARK - df["RetentionRate"]
    plt.figure(figsize=(7, 4))
    plt.bar(df["Quarter"], gap)
    for i, v in enumerate(gap):
        plt.annotate(f"{v:.2f}", (df["Quarter"][i], v), textcoords="offset points", xytext=(0,6), ha="center")
    plt.title("Gap to Benchmark (85) by Quarter")
    plt.xlabel("Quarter")
    plt.ylabel("Points below benchmark")
    plt.tight_layout()
    plt.savefig("figures/target_gap.png", dpi=200)
    plt.close()

    # Save metrics
    metrics = {
        "average_retention": avg_rounded,
        "benchmark": BENCHMARK,
        "avg_gap_to_benchmark": float(BENCHMARK - avg),
    }
    with open("metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

if __name__ == "__main__":
    main()
