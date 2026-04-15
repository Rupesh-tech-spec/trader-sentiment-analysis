import streamlit as st
import pandas as pd

st.title("📊 Trader Behavior vs Market Sentiment")

# Load data
data = pd.read_csv("merged_data.csv")

# Sidebar filter
st.sidebar.header("Filters")
sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment",
    options=data['classification'].unique(),
    default=data['classification'].unique()
)

filtered_data = data[data['classification'].isin(sentiment_filter)]

# Show data
st.subheader("📄 Sample Data")
st.write(filtered_data.head())

# 🔷 1. PnL by Sentiment
st.subheader("💰 Average PnL by Sentiment")
pnl_chart = filtered_data.groupby('classification')['Closed PnL'].mean()
st.bar_chart(pnl_chart)

# 🔷 2. Win Rate
st.subheader("✅ Win Rate by Sentiment")
filtered_data['win'] = filtered_data['Closed PnL'] > 0
win_chart = filtered_data.groupby('classification')['win'].mean()
st.bar_chart(win_chart)

# 🔷 3. Trade Size Distribution
st.subheader("📊 Trade Size Distribution")
st.bar_chart(filtered_data['Size USD'].value_counts().head(20))

# 🔷 4. Trades per Day
st.subheader("📅 Trades Per Day")
trades_per_day = filtered_data.groupby('date').size()
st.line_chart(trades_per_day)

# 🔷 5. Long vs Short
st.subheader("📈 Long vs Short Trades")
long_short = filtered_data['Side'].value_counts()
st.bar_chart(long_short)

# 🔷 6. Summary Metrics
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Trades", len(filtered_data))
col2.metric("Avg PnL", round(filtered_data['Closed PnL'].mean(), 2))
col3.metric("Win Rate", round(filtered_data['win'].mean(), 2))
