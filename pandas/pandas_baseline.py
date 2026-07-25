import time
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Start timing execution
start_time = time.time()

# 1. Define required columns (Column Pruning for Memory Efficiency)
required_cols = ["genre", "platform", "current_price_usd", "revenue_cumulative"]

print("Loading dataset into Pandas...\n")
df = pd.read_csv("data/video_game_market.csv", usecols=required_cols)

# 2. Check and drop missing values
print(f"Missing values before drop:\n{df.isnull().sum()}\n")
df = df.dropna()

# --- Analysis 1: Revenue by Genre ---
genre_revenue = (
    df.groupby("genre")["revenue_cumulative"]
    .sum()
    .sort_values(ascending=False)
)
print("--- Revenue by Genre ---")
print(genre_revenue)
print("\n" + "=" * 40 + "\n")

# --- Analysis 2: Revenue by Platform ---
platform_revenue = (
    df.groupby("platform")["revenue_cumulative"]
    .sum()
    .sort_values(ascending=False)
)
print("--- Revenue by Platform ---")
print(platform_revenue)
print("\n" + "=" * 40 + "\n")

# --- Analysis 3: Average Price by Genre ---
genre_price = (
    df.groupby("genre")["current_price_usd"]
    .mean()
    .sort_values(ascending=False)
)
print("--- Average Price by Genre ---")
print(genre_price)
print("\n" + "=" * 40 + "\n")

# --- Analysis 4: Summary Table ---
summary = (
    df.groupby(["genre", "platform"])
    .agg(
        Total_Revenue=("revenue_cumulative", "sum"),
        Average_Price=("current_price_usd", "mean"),
        Number_of_Games=("genre", "count"),
    )
    .reset_index()
)

print("--- Summary Table (Head) ---")
print(summary.head())
print("\n" + "=" * 40 + "\n")

# 3. Save Summary Table to CSV File
summary.to_csv("outputs/pandas_market_analysis.csv", index=False)
print("Saved summary table to 'pandas_market_analysis.csv'")

# 4. Additional: Generate and Save Visual Charts
print("Generating charts...")
sns.set_theme(style="whitegrid")

# Graph 1: Revenue by Genre
plt.figure(figsize=(12, 6))
sns.barplot(
    data=genre_revenue.reset_index(),
    x="revenue_cumulative",
    y="genre",
    hue="genre",
    palette="Blues_r",
    legend=False,
)
plt.title("Total Cumulative Revenue by Game Genre", fontsize=14, fontweight="bold")
plt.xlabel("Total Revenue (USD)", fontsize=12)
plt.ylabel("Genre", fontsize=12)
plt.tight_layout()
plt.savefig("outputs/genre_revenue_chart.png", dpi=300)
plt.close()

# Graph 2: Revenue by Platform
plt.figure(figsize=(10, 5))
sns.barplot(
    data=platform_revenue.reset_index(),
    x="revenue_cumulative",
    y="platform",
    hue="platform",
    palette="viridis",
    legend=False,
)
plt.title("Total Cumulative Revenue by Platform", fontsize=14, fontweight="bold")
plt.xlabel("Total Revenue (USD)", fontsize=12)
plt.ylabel("Platform", fontsize=12)
plt.tight_layout()
plt.savefig("outputs/platform_revenue_chart.png", dpi=300)
plt.close()

print("Charts successfully saved as 'outputs/genre_revenue_chart.png' and 'outputs/platform_revenue_chart.png'")

# Measure Total Execution Time
end_time = time.time()
print(f"\nTotal Pandas Execution Time: {end_time - start_time:.2f} seconds")