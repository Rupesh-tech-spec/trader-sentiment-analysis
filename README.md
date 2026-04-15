# Trader Behavior vs Market Sentiment

##  Objective

Analyze how Bitcoin market sentiment (Fear/Greed) affects trader performance and behavior.

---

##  Dataset

* Bitcoin Fear & Greed Index (daily sentiment)
* Hyperliquid trading data (PnL, size, trades)

---

## ⚙️ Methodology

* Converted timestamps to daily format
* Aligned trading data with sentiment
* Created key metrics:

  * PnL
  * Win rate
  * Trade frequency
  * Trade size

---

## 📊 Key Insights

* Traders perform best during **Extreme Greed**
* Trading activity is highest during **Fear** (overtrading behavior)
* Larger trades occur during Fear → higher risk-taking
* Win rate is lowest during Extreme Fear

---

## 📈 Strategy Recommendations

1. Reduce risk during Fear markets
2. Increase exposure during Extreme Greed
3. Avoid aggressive trading during Extreme Fear

---

## 📊 Outputs

* Average PnL by sentiment
* Win rate by sentiment
* Trade frequency analysis

---

## 🖥️ How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run notebook:

[```](http://localhost:8501/)
notebooks/analysis.ipynb


## 👤 Author

Rupesh Kumar Shaw
MSc Statistics, IIT Kanpur
