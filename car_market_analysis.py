# =============================================================================
#  Car Market Analysis — Car Dekho Dataset
#  Author  : [Your Name]
#  Tool    : Python | Pandas | NumPy | Matplotlib | Seaborn
# =============================================================================
#
#  Sections
#  --------
#  0.  Imports & Setup
#  1.  Load & Inspect Data
#  2.  Data Cleaning & Feature Engineering
#  3.  Exploratory Data Analysis (EDA)
#      3.1  Fuel Type Distribution
#      3.2  Avg Selling Price by Fuel Type
#      3.3  Selling Price by Transmission Type
#      3.4  Selling Price vs Kms Driven
#      3.5  Year-wise Avg Selling Price Trend
#      3.6  Feature Correlation Heatmap
#      3.7  Avg Selling Price by Seller Type
#      3.8  Car Age vs Selling Price
#      3.9  Top 10 Most Listed Car Models
#  4.  Key Insights Summary
# =============================================================================


# ─────────────────────────────────────────────────────────────────────────────
#  0. IMPORTS & SETUP
# ─────────────────────────────────────────────────────────────────────────────
import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns

warnings.filterwarnings("ignore")

# Output directory for saved plots
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Colour palette
COLORS = {
    "primary":  "#1565C0",
    "accent1":  "#00ACC1",
    "accent2":  "#43A047",
    "accent3":  "#FB8C00",
    "accent4":  "#E53935",
    "light":    "#E3F2FD",
}
PALETTE = [COLORS["primary"], COLORS["accent1"], COLORS["accent2"],
           COLORS["accent3"], COLORS["accent4"]]

# ── Global matplotlib defaults
plt.rcParams.update({
    "font.family":        "DejaVu Sans",
    "axes.spines.top":    False,
    "axes.spines.right":  False,
    "axes.grid":          True,
    "grid.alpha":         0.3,
    "grid.color":         "#BDBDBD",
    "figure.dpi":         150,
})


# ─────────────────────────────────────────────────────────────────────────────
#  1. LOAD & INSPECT DATA
# ─────────────────────────────────────────────────────────────────────────────
print("=" * 65)
print("  CAR MARKET ANALYSIS — Car Dekho Dataset")
print("=" * 65)

df = pd.read_csv("data/car_data.csv")

print(f"\n[1] Dataset loaded  →  {df.shape[0]} rows × {df.shape[1]} columns")
print("\nColumn names:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())
print("\nData types:")
print(df.dtypes)
print("\nBasic statistics:")
print(df.describe())
print("\nMissing values per column:")
print(df.isnull().sum())


# ─────────────────────────────────────────────────────────────────────────────
#  2. DATA CLEANING & FEATURE ENGINEERING
# ─────────────────────────────────────────────────────────────────────────────
print("\n[2] Feature engineering …")

# Car age (relative to 2024)
df["Car_Age"] = 2024 - df["Year"]

# Price depreciation (absolute & percentage)
df["Price_Drop"]         = df["Present_Price"] - df["Selling_Price"]
df["Depreciation_Pct"]   = (df["Price_Drop"] / df["Present_Price"]) * 100

print(f"    Car_Age range   : {df['Car_Age'].min()} – {df['Car_Age'].max()} years")
print(f"    Avg depreciation: {df['Depreciation_Pct'].mean():.1f}%")
print(f"    Avg selling price: ₹{df['Selling_Price'].mean():.2f} Lakhs")


# ─────────────────────────────────────────────────────────────────────────────
#  3. EXPLORATORY DATA ANALYSIS
# ─────────────────────────────────────────────────────────────────────────────


# ── 3.1  FUEL TYPE DISTRIBUTION  ─────────────────────────────────────────────
print("\n[3.1] Fuel Type Distribution …")

fuel_counts = df["Fuel_Type"].value_counts()
print(fuel_counts)

fig, ax = plt.subplots(figsize=(7, 5), facecolor="white")
wedge_colors = [COLORS["primary"], COLORS["accent1"], COLORS["accent2"]]
wedges, texts, autotexts = ax.pie(
    fuel_counts.values,
    labels=fuel_counts.index,
    autopct="%1.1f%%",
    colors=wedge_colors,
    startangle=90,
    wedgeprops=dict(edgecolor="white", linewidth=2),
)
for t in texts:
    t.set_fontsize(12)
for t in autotexts:
    t.set_fontsize(11)
    t.set_fontweight("bold")
    t.set_color("white")
ax.set_title("Fuel Type Distribution", fontsize=14, fontweight="bold",
             pad=15, color="#212121")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/plot1_fuel_distribution.png",
            dpi=150, bbox_inches="tight", facecolor="white")
plt.show()
print(f"    → saved: {OUTPUT_DIR}/plot1_fuel_distribution.png")


# ── 3.2  AVG SELLING PRICE BY FUEL TYPE  ─────────────────────────────────────
print("\n[3.2] Avg Selling Price by Fuel Type …")

avg_price = df.groupby("Fuel_Type")["Selling_Price"].mean().sort_values(ascending=False)
print(avg_price)

fig, ax = plt.subplots(figsize=(7, 5), facecolor="white")
bars = ax.bar(avg_price.index, avg_price.values,
              color=wedge_colors[: len(avg_price)],
              edgecolor="white", linewidth=1.5, width=0.5)
for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.3,
            f"₹{bar.get_height():.1f}L",
            ha="center", va="bottom", fontsize=11, fontweight="bold")
ax.set_title("Avg Selling Price by Fuel Type", fontsize=14,
             fontweight="bold", color="#212121")
ax.set_ylabel("Avg Selling Price (Lakhs ₹)", fontsize=11)
ax.set_xlabel("Fuel Type", fontsize=11)
ax.set_ylim(0, avg_price.max() * 1.2)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/plot2_avg_price_fuel.png",
            dpi=150, bbox_inches="tight", facecolor="white")
plt.show()
print(f"    → saved: {OUTPUT_DIR}/plot2_avg_price_fuel.png")


# ── 3.3  SELLING PRICE BY TRANSMISSION TYPE  ─────────────────────────────────
print("\n[3.3] Selling Price by Transmission …")

manual_avg = df[df["Transmission"] == "Manual"]["Selling_Price"].mean()
auto_avg   = df[df["Transmission"] == "Automatic"]["Selling_Price"].mean()
print(f"    Manual avg   : ₹{manual_avg:.2f}L")
print(f"    Automatic avg: ₹{auto_avg:.2f}L")

trans_groups = [
    df[df["Transmission"] == t]["Selling_Price"].values
    for t in ["Manual", "Automatic"]
]

fig, ax = plt.subplots(figsize=(7, 5), facecolor="white")
bp = ax.boxplot(
    trans_groups, labels=["Manual", "Automatic"],
    patch_artist=True,
    medianprops=dict(color=COLORS["primary"], linewidth=2.5),
    whiskerprops=dict(color="#666"),
    capprops=dict(color="#666"),
)
bp["boxes"][0].set_facecolor("#E3F2FD")
bp["boxes"][1].set_facecolor("#E0F7FA")
ax.set_title("Selling Price by Transmission Type", fontsize=14,
             fontweight="bold", color="#212121")
ax.set_ylabel("Selling Price (Lakhs ₹)", fontsize=11)
ax.set_xlabel("Transmission Type", fontsize=11)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/plot3_price_transmission.png",
            dpi=150, bbox_inches="tight", facecolor="white")
plt.show()
print(f"    → saved: {OUTPUT_DIR}/plot3_price_transmission.png")


# ── 3.4  SELLING PRICE VS KMS DRIVEN  ────────────────────────────────────────
print("\n[3.4] Selling Price vs Kms Driven …")

fuel_palette = {
    "Petrol": COLORS["primary"],
    "Diesel": COLORS["accent1"],
    "CNG":    COLORS["accent2"],
}

fig, ax = plt.subplots(figsize=(8, 5), facecolor="white")
for fuel, grp in df.groupby("Fuel_Type"):
    ax.scatter(
        grp["Kms_Driven"] / 1000,
        grp["Selling_Price"],
        label=fuel,
        color=fuel_palette.get(fuel, "gray"),
        alpha=0.65, s=60,
        edgecolors="white", linewidth=0.5,
    )
ax.set_title("Selling Price vs Kms Driven", fontsize=14,
             fontweight="bold", color="#212121")
ax.set_xlabel("Kms Driven (Thousands)", fontsize=11)
ax.set_ylabel("Selling Price (Lakhs ₹)", fontsize=11)
ax.legend(fontsize=10, framealpha=0.8)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/plot4_price_vs_kms.png",
            dpi=150, bbox_inches="tight", facecolor="white")
plt.show()
print(f"    → saved: {OUTPUT_DIR}/plot4_price_vs_kms.png")


# ── 3.5  YEAR-WISE AVG SELLING PRICE TREND  ──────────────────────────────────
print("\n[3.5] Year-wise Avg Selling Price Trend …")

year_price = df.groupby("Year")["Selling_Price"].mean().reset_index()
print(year_price.to_string(index=False))

fig, ax = plt.subplots(figsize=(8, 5), facecolor="white")
ax.plot(
    year_price["Year"], year_price["Selling_Price"],
    color=COLORS["primary"], marker="o", linewidth=2.5,
    markersize=8,
    markerfacecolor=COLORS["accent1"],
    markeredgecolor="white", markeredgewidth=1.5,
)
ax.fill_between(year_price["Year"], year_price["Selling_Price"],
                alpha=0.15, color=COLORS["primary"])
for _, row in year_price.iterrows():
    ax.text(row["Year"], row["Selling_Price"] + 0.3,
            f"₹{row['Selling_Price']:.1f}L",
            ha="center", fontsize=8, color="#444")
ax.set_title("Year-wise Avg Selling Price Trend", fontsize=14,
             fontweight="bold", color="#212121")
ax.set_xlabel("Manufacturing Year", fontsize=11)
ax.set_ylabel("Avg Selling Price (Lakhs ₹)", fontsize=11)
ax.set_xticks(year_price["Year"])
ax.tick_params(axis="x", rotation=30)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/plot5_year_trend.png",
            dpi=150, bbox_inches="tight", facecolor="white")
plt.show()
print(f"    → saved: {OUTPUT_DIR}/plot5_year_trend.png")


# ── 3.6  FEATURE CORRELATION HEATMAP  ────────────────────────────────────────
print("\n[3.6] Feature Correlation Heatmap …")

corr_cols = ["Selling_Price", "Present_Price", "Kms_Driven", "Car_Age", "Owner"]
corr      = df[corr_cols].corr()
labels    = ["Selling\nPrice", "Present\nPrice", "Kms\nDriven", "Car\nAge", "Owner"]
print(corr.round(2))

fig, ax = plt.subplots(figsize=(7, 5.5), facecolor="white")
sns.heatmap(
    corr, annot=True, fmt=".2f", cmap="Blues", ax=ax,
    linewidths=0.5, linecolor="white",
    cbar_kws={"shrink": 0.8},
    xticklabels=labels, yticklabels=labels,
    annot_kws={"size": 11},
)
ax.set_title("Feature Correlation Heatmap", fontsize=14,
             fontweight="bold", color="#212121")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/plot6_correlation_heatmap.png",
            dpi=150, bbox_inches="tight", facecolor="white")
plt.show()
print(f"    → saved: {OUTPUT_DIR}/plot6_correlation_heatmap.png")


# ── 3.7  AVG SELLING PRICE BY SELLER TYPE  ───────────────────────────────────
print("\n[3.7] Avg Selling Price by Seller Type …")

seller_avg = df.groupby("Seller_Type")["Selling_Price"].mean()
seller_cnt = df.groupby("Seller_Type")["Selling_Price"].count()
print("Avg price:", seller_avg.round(2).to_dict())
print("Count    :", seller_cnt.to_dict())

fig, ax = plt.subplots(figsize=(7, 5), facecolor="white")
x    = np.arange(len(seller_avg))
bars = ax.bar(x, seller_avg.values,
              color=[COLORS["primary"], COLORS["accent1"]],
              edgecolor="white", linewidth=1.5, width=0.5)
ax.set_xticks(x)
ax.set_xticklabels(seller_avg.index, fontsize=12)
ax.set_ylabel("Avg Selling Price (Lakhs ₹)", fontsize=11)
ax.set_title("Avg Selling Price by Seller Type", fontsize=14,
             fontweight="bold", color="#212121")
for bar, cnt in zip(bars, seller_cnt.values):
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.2,
            f"₹{bar.get_height():.1f}L\n(n={cnt})",
            ha="center", fontsize=11, fontweight="bold")
ax.set_ylim(0, seller_avg.max() * 1.35)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/plot7_seller_type.png",
            dpi=150, bbox_inches="tight", facecolor="white")
plt.show()
print(f"    → saved: {OUTPUT_DIR}/plot7_seller_type.png")


# ── 3.8  CAR AGE VS SELLING PRICE  ───────────────────────────────────────────
print("\n[3.8] Car Age vs Selling Price …")

corr_age_price = df["Car_Age"].corr(df["Selling_Price"])
print(f"    Pearson correlation (Age vs Price): {corr_age_price:.3f}")

z      = np.polyfit(df["Car_Age"], df["Selling_Price"], 1)
p      = np.poly1d(z)
x_line = np.linspace(df["Car_Age"].min(), df["Car_Age"].max(), 100)

fig, ax = plt.subplots(figsize=(8, 5), facecolor="white")
ax.scatter(df["Car_Age"], df["Selling_Price"],
           color=COLORS["primary"], alpha=0.55, s=55,
           edgecolors="white", linewidth=0.5)
ax.plot(x_line, p(x_line),
        color=COLORS["accent3"], linewidth=2.5,
        linestyle="--", label="Trend Line")
ax.set_title("Car Age vs Selling Price", fontsize=14,
             fontweight="bold", color="#212121")
ax.set_xlabel("Car Age (Years)", fontsize=11)
ax.set_ylabel("Selling Price (Lakhs ₹)", fontsize=11)
ax.legend(fontsize=10)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/plot8_age_vs_price.png",
            dpi=150, bbox_inches="tight", facecolor="white")
plt.show()
print(f"    → saved: {OUTPUT_DIR}/plot8_age_vs_price.png")


# ── 3.9  TOP 10 MOST LISTED CAR MODELS  ──────────────────────────────────────
print("\n[3.9] Top 10 Most Listed Car Models …")

top_cars = df["Car_Name"].value_counts().head(10)
print(top_cars)

fig, ax = plt.subplots(figsize=(8, 5), facecolor="white")
bars = ax.barh(
    top_cars.index[::-1],
    top_cars.values[::-1],
    color=[PALETTE[i % len(PALETTE)] for i in range(len(top_cars))],
    edgecolor="white", linewidth=1,
)
for bar in bars:
    ax.text(bar.get_width() + 0.2,
            bar.get_y() + bar.get_height() / 2,
            str(int(bar.get_width())),
            va="center", fontsize=10, fontweight="bold")
ax.set_title("Top 10 Most Listed Car Models", fontsize=14,
             fontweight="bold", color="#212121")
ax.set_xlabel("Number of Listings", fontsize=11)
ax.set_xlim(0, top_cars.max() * 1.18)
ax.set_yticklabels([n.upper() for n in top_cars.index[::-1]], fontsize=10)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/plot9_top_10_cars.png",
            dpi=150, bbox_inches="tight", facecolor="white")
plt.show()
print(f"    → saved: {OUTPUT_DIR}/plot9_top_10_cars.png")


# ─────────────────────────────────────────────────────────────────────────────
#  4. KEY INSIGHTS SUMMARY
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 65)
print("  KEY INSIGHTS SUMMARY")
print("=" * 65)

print(f"""
  Dataset       : {len(df)} records | {df['Year'].min()}–{df['Year'].max()}
  Avg sell price: ₹{df['Selling_Price'].mean():.2f}L
  Price range   : ₹{df['Selling_Price'].min():.2f}L – ₹{df['Selling_Price'].max():.2f}L
  Avg kms driven: {df['Kms_Driven'].mean():.0f} km
  Avg deprec.   : {df['Depreciation_Pct'].mean():.1f}%

  Fuel split    : Petrol {fuel_counts.get('Petrol', 0)/len(df)*100:.1f}%
                  Diesel {fuel_counts.get('Diesel', 0)/len(df)*100:.1f}%
                  CNG    {fuel_counts.get('CNG', 0)/len(df)*100:.1f}%

  Transmission  : Manual   avg ₹{manual_avg:.2f}L
                  Automatic avg ₹{auto_avg:.2f}L  (+{auto_avg/manual_avg:.1f}x)

  Seller type   : Dealer     avg ₹{seller_avg.get('Dealer', 0):.2f}L (n={seller_cnt.get('Dealer', 0)})
                  Individual avg ₹{seller_avg.get('Individual', 0):.2f}L (n={seller_cnt.get('Individual', 0)})

  Top car model : {top_cars.index[0].upper()} ({top_cars.iloc[0]} listings)
  Corr (Age↔Price): {corr_age_price:.3f}  (negative → older cars cost less)
""")

print(f"All {len(os.listdir(OUTPUT_DIR))} plots saved to '{OUTPUT_DIR}/' folder.")
print("=" * 65)
