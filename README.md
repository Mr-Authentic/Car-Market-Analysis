# 🚗 Car Market Analysis — Car Dekho Dataset

> **AICTE Internship DIY Project** | Data Analysis & Visualization using Python

---

## 📌 Problem Statement

The used-car market contains vehicles with different prices, fuel types, transmission types, and usage levels. It is difficult to understand which factors have the greatest impact on a car's selling price. Buyers and sellers need data-driven insights to evaluate a vehicle's fair market value.

This project analyzes historical **Car Dekho** data to identify important market trends and pricing patterns, providing meaningful insights that support better buying, selling, and pricing decisions.

---

## 📂 Repository Structure

```
car-market-analysis/
│
├── data/
│   └── car_data.csv                  # Car Dekho dataset (301 records)
│
├── outputs/                          # Generated plots (auto-created on run)
│   ├── plot1_fuel_distribution.png
│   ├── plot2_avg_price_fuel.png
│   ├── plot3_price_transmission.png
│   ├── plot4_price_vs_kms.png
│   ├── plot5_year_trend.png
│   ├── plot6_correlation_heatmap.png
│   ├── plot7_seller_type.png
│   ├── plot8_age_vs_price.png
│   └── plot9_top_10_cars.png
│
├── car_market_analysis.py            # Main Python script
├── car_market_analysis.ipynb         # Jupyter / Google Colab notebook
├── requirements.txt                  # Python dependencies
├── .gitignore
└── README.md
```

---

## 📊 Dataset Overview

| Feature        | Description                                     |
|----------------|-------------------------------------------------|
| `Car_Name`     | Name / model of the car                         |
| `Year`         | Year of manufacture                             |
| `Selling_Price`| Price at which the car is being sold (Lakhs ₹) |
| `Present_Price`| Current ex-showroom price of the car (Lakhs ₹) |
| `Kms_Driven`   | Total kilometres driven                         |
| `Fuel_Type`    | Petrol / Diesel / CNG                           |
| `Seller_Type`  | Dealer / Individual                             |
| `Transmission` | Manual / Automatic                              |
| `Owner`        | Number of previous owners                       |

**Records:** 301 &nbsp;|&nbsp; **Year range:** 2003–2018 &nbsp;|&nbsp; **Missing values:** None

---

## 🔍 Analyses & Visualisations

| # | Analysis | Plot |
|---|----------|------|
| 1 | Fuel Type Distribution | Pie chart |
| 2 | Avg Selling Price by Fuel Type | Bar chart |
| 3 | Selling Price by Transmission Type | Box plot |
| 4 | Selling Price vs Kms Driven | Scatter plot |
| 5 | Year-wise Avg Selling Price Trend (2003–2018) | Line chart |
| 6 | Feature Correlation Heatmap | Heatmap |
| 7 | Avg Selling Price by Seller Type | Bar chart |
| 8 | Car Age vs Selling Price | Scatter + regression line |
| 9 | Top 10 Most Listed Car Models | Horizontal bar chart |

---

## 💡 Key Insights

| Insight | Finding |
|---------|---------|
| **Fuel dominance** | Petrol cars make up 79.4% of listings; Diesel 19.9%; CNG 0.7% |
| **Diesel premium** | Diesel avg ₹10.3L vs Petrol avg ₹3.3L |
| **Transmission gap** | Automatic avg ₹9.4L — 2.4× more than Manual (₹3.9L) |
| **Dealer vs Individual** | Dealers list cars at avg ₹6.7L; Individuals at avg ₹0.9L |
| **Depreciation** | Average vehicle loses ~36.6% of its present value |
| **Price trend** | Newer cars command significantly higher resale prices |
| **Age-Price correlation** | −0.24 — older cars tend to sell for less |
| **Most listed model** | City (26 listings), Corolla Altis (16), Verna (14) |

---

## 🛠 Technology Stack

| Tool | Purpose |
|------|---------|
| **Python 3.x** | Core programming language |
| **Pandas** | Data loading, cleaning, groupby, aggregation |
| **NumPy** | Numerical operations, polynomial regression |
| **Matplotlib** | Charts — bar, pie, line, scatter, box |
| **Seaborn** | Heatmap and styled statistical plots |
| **Jupyter Notebook / Google Colab** | Interactive development environment |

---

## 🚀 How to Run

### Option 1 — Google Colab (recommended, no setup needed)

1. Open [Google Colab](https://colab.research.google.com/)
2. Upload `car_market_analysis.ipynb`
3. Upload `car_data.csv` to the `data/` folder in the Colab file browser
4. Click **Runtime → Run all**

### Option 2 — Local (Jupyter Notebook)

```bash
# 1. Clone the repository
git clone https://github.com/Mr-Authentic/car-market-analysis.git
cd car-market-analysis

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch Jupyter
jupyter notebook car_market_analysis.ipynb
```

### Option 3 — Local (Python script)

```bash
# 1. Clone & install (same as above)

# 2. Run the script
python car_market_analysis.py
```

All 9 plots are saved automatically to the `outputs/` folder.

---

## 📸 Sample Output

The analysis generates 9 professional visualisations. Example charts include:

- **Fuel Type Distribution** — Petrol dominates with 79.4%
- **Year-wise Price Trend** — Clear upward trend for newer vehicles
- **Correlation Heatmap** — Selling Price & Present Price show 0.88 correlation

---

## 👥 End Users

- **Car Buyers** — Compare vehicles and find fair prices
- **Car Sellers** — Estimate competitive resale value
- **Car Dealers** — Understand demand and pricing by segment
- **Used-Car Businesses** — Data-driven inventory and pricing decisions
- **Data Analysts** — Automobile market insights and reporting

---

## 📝 Project Submission

- **Course:** AICTE VOIS for Tech Internship
- **Submitted on:** VOIS LMS — [https://voisfortech.com/attemptassignment-sm/63](https://voisfortech.com/attemptassignment-sm/63)
- **Submission format:** `.pptx` (PowerPoint)

---

## 📄 License

This project is submitted as part of an academic internship programme. The dataset is sourced from Car Dekho and used for educational purposes only.
