# 📈 Bitcoin Market Sentiment vs. Trader Performance Analysis

## 📌 Project Overview

This project investigates the relationship between **Bitcoin Market Sentiment** (Fear & Greed Index) and **trader performance on Hyperliquid**.

Using over **211,000 real trading records** collected from **32 trading accounts** between **May 2023 and May 2025**, the project examines whether different market sentiment regimes influence:

- Trading profitability
- Win rate
- Position sizing
- Long/Short bias
- Risk appetite

The analysis combines historical trading data with the **Bitcoin Fear & Greed Index** to identify behavioral patterns that can help traders, quantitative researchers, and portfolio managers build more informed trading strategies.

---

# 🎯 Objectives

The primary objectives of this project are:

- Analyze how trader profitability changes across different sentiment regimes.
- Measure win rates under varying market emotions.
- Study trader behavior (Long vs Short positioning).
- Evaluate changes in position sizing during fear and greed.
- Discover whether traders behave contrarian or trend-following.
- Generate actionable insights for quantitative trading strategies.

---

# 📊 Dataset Information

## 1. Hyperliquid Historical Trades

**Period**

May 2023 – May 2025

### Records

- **211,224 trades**

### Trading Accounts

- **32 accounts**

### Important Columns

| Column | Description |
|---------|-------------|
| Timestamp | Trade execution time |
| Account | Trader ID |
| Coin | Asset traded |
| Side | Buy / Sell |
| Size USD | Position size in USD |
| Closed PnL | Profit or loss after closing trade |
| Direction | Long / Short |
| Fee | Trading fee |
| Price | Execution price |

---

## 2. Bitcoin Fear & Greed Index

Historical daily sentiment dataset covering:

**2018 – 2025**

Daily market sentiment is classified into five categories:

| Sentiment | Meaning |
|------------|----------|
| Extreme Fear | Heavy panic selling |
| Fear | Cautious market |
| Neutral | Balanced sentiment |
| Greed | Optimistic market |
| Extreme Greed | Euphoric market |

---

# 🔗 Data Integration

Trade timestamps were converted into calendar dates.

Each trade was matched with the corresponding day's Bitcoin Fear & Greed sentiment.

### Merge Success

- **99.997% match rate**

Almost every trade successfully received a market sentiment label.

---

# 📈 Methodology

## Step 1

Load both datasets

- Hyperliquid trade history
- Fear & Greed Index

---

## Step 2

Clean the datasets

- Remove invalid timestamps
- Standardize date formats
- Handle missing values
- Remove duplicate entries

---

## Step 3

Feature Engineering

Created several additional variables including:

- Trade Date
- Sentiment Label
- Trade Outcome
- Position Size Category
- Direction Flag

---

## Step 4

Merge Datasets

Trade Date

↓

Daily Fear & Greed Date

↓

Merged Dataset

---

## Step 5

Filter Closed Trades

Only trades with:

```
Closed PnL ≠ 0
```

were considered realized outcomes.

This avoids including open positions that have unrealized profit/loss.

---

## Step 6

Performance Metrics

For every sentiment regime, the following metrics were calculated:

- Total Trades
- Winning Trades
- Losing Trades
- Win Rate
- Average PnL
- Total PnL
- Median PnL
- Average Position Size
- Long Ratio
- Short Ratio

---

# 📉 Exploratory Data Analysis

The project contains multiple visualizations including:

### 1. Trade Distribution by Sentiment

Shows how trading activity changes across market emotions.

---

### 2. Win Rate by Sentiment

Compares trader success across all five sentiment categories.

---

### 3. Average Profit per Trade

Measures profitability during each sentiment regime.

---

### 4. Long vs Short Bias

Shows directional preference under different emotions.

---

### 5. Position Size Distribution

Analyzes trader confidence and risk exposure.

---

# 🔍 Key Findings

## 1. Emotional Extremes Produce Better Results

The highest trading performance occurred during:

- Extreme Greed
- Fear

### Win Rates

| Sentiment | Win Rate |
|------------|----------|
| Extreme Greed | **89.2%** |
| Fear | **87.3%** |

These periods generated the strongest average profitability.

---

## 2. Transitional Markets Perform Worse

Lower performance was observed during:

- Extreme Fear
- Greed

These market phases appear more uncertain and produce less consistent trading outcomes.

---

## 3. Traders Behave Contrarian

Directional analysis shows a clear behavioral pattern.

### During Fear

Approximately

**69% Long Positions**

Traders tend to buy after panic selling.

---

### During Greed

Approximately

**55–58% Short Positions**

Traders increasingly bet against market optimism.

This indicates traders often fade emotional extremes rather than follow momentum.

---

## 4. Larger Positions Occur During Fear

The largest trades are concentrated during fearful markets.

Among the top 1% largest trades:

- **46% occurred during Fear**

compared to only

- **29% expected from baseline distribution**

This suggests traders intentionally increase exposure during discounted market conditions.

---

## 5. Risk Reduces During Extreme Greed

Average position size decreases significantly during Extreme Greed.

Rather than chasing rallies with oversized positions, traders appear to reduce exposure.

This suggests disciplined capital allocation rather than FOMO-driven behavior.

---

## 6. Asset-Specific Behavior

Not every cryptocurrency reacts identically to sentiment.

Examples include:

- BTC may reward momentum following.
- ETH often benefits from contrarian positioning.
- Smaller altcoins display unique sentiment sensitivity.

This indicates that any sentiment-based strategy should be **asset-aware** rather than universally applied.

---

# 📊 Statistical Metrics Used

The project evaluates:

- Trade Count
- Total Profit
- Mean Profit
- Median Profit
- Win Rate
- Average Trade Size
- Long Ratio
- Short Ratio
- Sentiment Distribution

---

# 📁 Project Structure

```Bitcoin-Sentiment-Analysis/
│
├── data/
│   ├── historical_data.csv
│   ├── fear_greed_index.csv
│   ├── merged_dataset.csv
│   └── cleaned_dataset.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── src/
│   ├── data_preprocessing.py
│   ├── merge_data.py
│   ├── eda.py
│   ├── visualization.py
│   └── utils.py
│
├── charts/
│   ├── sentiment_distribution.png
│   ├── win_rate.png
│   ├── pnl_by_sentiment.png
│   ├── long_short_ratio.png
│   ├── trade_size_distribution.png
│   ├── correlation_heatmap.png
│   ├── monthly_performance.png
│   ├── top_assets.png
│   └── boxplot_pnl.png
│
├── report/
│   ├── Bitcoin_Market_Sentiment_Report.docx
│   ├── summary_tables.xlsx
│   └── findings.pdf
│
├── README.md
├── requirements.txt
└── main.py
```

---

# ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/bitcoin-sentiment-analysis.git
```

Move into the project directory

```bash
cd bitcoin-sentiment-analysis
```

Install dependencies

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook

```bash
jupyter notebook
```

---

# ▶️ Running the Analysis

Open

```
analysis.ipynb
```

Execute all notebook cells sequentially.

Outputs generated include:

- Clean dataset
- Merged dataset
- Statistical summary
- Visualizations
- Final report tables

---

# 📂 Deliverables

The completed project includes:

✅ Cleaned Hyperliquid trading dataset

✅ Historical Fear & Greed Index dataset

✅ Fully merged trade-level dataset

✅ Exploratory Data Analysis

✅ Five supporting charts

✅ Summary tables

✅ Strategic recommendations

✅ Executive report in Microsoft Word format

---

# ⚠️ Assumptions & Limitations

### Missing Leverage Information

The original project brief referenced a **Leverage** field.

However, the provided trading dataset did **not** contain leverage information.

To estimate trader risk appetite, **trade size (USD)** was used as the closest available proxy.

This substitution is documented transparently throughout the report.

---

### Market Sentiment Granularity

The Fear & Greed Index provides one sentiment label per day.

Intraday changes in sentiment are not captured.

---

### Sample Scope

The analysis covers:

- 32 trading accounts
- Hyperliquid exchange
- Two-year trading period

Results may not generalize to every exchange or trader population.

---

# 💡 Strategic Recommendations

Based on the findings:

- Consider increasing attention during Fear and Extreme Greed regimes, where realized trader performance is strongest.
- Incorporate sentiment as an additional feature rather than a standalone trading signal.
- Build asset-specific sentiment models instead of universal rules.
- Use dynamic position sizing aligned with market sentiment.
- Combine sentiment with technical indicators, volatility measures, and on-chain metrics for stronger predictive performance.

---

# 🚀 Future Improvements

Potential enhancements include:

- Incorporating leverage data if available.
- Adding funding rate analysis.
- Integrating on-chain metrics.
- Including liquidation events.
- Applying machine learning models for profitability prediction.
- Building an interactive dashboard using Streamlit or Dash.
- Performing account-level behavioral clustering.
- Conducting statistical significance testing for sentiment-performance relationships.

---

# 📜 Conclusion

This project demonstrates that **market psychology has a measurable relationship with trading performance**. By merging over **211,000 Hyperliquid trades** with the **Bitcoin Fear & Greed Index**, the analysis reveals distinct behavioral and profitability patterns across different sentiment regimes.

The findings suggest that traders generally adopt **contrarian positioning**, increase exposure during fearful markets, and reduce risk during euphoric conditions. While sentiment alone should not dictate trading decisions, it provides valuable context when combined with technical, quantitative, and asset-specific signals.

Overall, this project serves as a practical example of how behavioral finance and market sentiment can be integrated into data-driven trading research and strategy development.

---

## 👨‍💻 Author

**Roshan Yadav**

B.Tech in Robotics & Artificial Intelligence

Passionate about AI, Machine Learning, Data Analytics, Quantitative Research, and Financial Technology.

Feel free to connect or contribute to improve this project.
