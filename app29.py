# ---------------------------------------------------
# IMPORT LIBRARIES
# ---------------------------------------------------
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="MLS Betting Market Efficiency Analysis",
    layout="wide"
)

# ---------------------------------------------------
# TITLE SECTION
# ---------------------------------------------------
st.title("⚽ MLS Betting Market Efficiency Analysis (2012–2026)")

st.markdown(
    """
This dashboard analyzes betting market efficiency in Major League Soccer (MLS)
using historical match results and Pinnacle betting odds.

### Key Focus Areas
- Betting market prediction accuracy
- Home advantage trends
- Team market outperformance
- League unpredictability
- Upset frequency analysis
"""
)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------
@st.cache_data

def load_data():
    df = pd.read_excel("USA.xlsx")


    df["Date"] = pd.to_datetime(df["Date"])

    return df


df = load_data()

# ---------------------------------------------------
# DATA CLEANING
# ---------------------------------------------------
analysis_df = df[[
    "Season",
    "Date",
    "Home",
    "Away",
    "HG",
    "AG",
    "Res",
    "PSCH",
    "PSCD",
    "PSCA"
]].copy()

analysis_df = analysis_df.dropna(
    subset=["PSCH", "PSCD", "PSCA"]
)

# ---------------------------------------------------
# MARKET PREDICTION
# ---------------------------------------------------
def market_prediction(row):

    lowest_odds = min(
        row["PSCH"],
        row["PSCD"],
        row["PSCA"]
    )

    if lowest_odds == row["PSCH"]:
        return "H"

    elif lowest_odds == row["PSCD"]:
        return "D"

    else:
        return "A"


analysis_df["Market_Prediction"] = analysis_df.apply(
    market_prediction,
    axis=1
)

# ---------------------------------------------------
# CORRECT PREDICTION
# ---------------------------------------------------
analysis_df["Correct_Prediction"] = (
    analysis_df["Market_Prediction"]
    == analysis_df["Res"]
)

# ---------------------------------------------------
# HOME WIN INDICATOR
# ---------------------------------------------------
analysis_df["Home_Win"] = (
    analysis_df["Res"] == "H"
).astype(int)

# ---------------------------------------------------
# UPSET INDICATOR
# ---------------------------------------------------
analysis_df["Upset"] = (
    analysis_df["Correct_Prediction"] == False
).astype(int)

# ---------------------------------------------------
# FAVORITE ODDS
# ---------------------------------------------------
analysis_df["Favorite_Odds"] = analysis_df[
    ["PSCH", "PSCD", "PSCA"]
].min(axis=1)

# ---------------------------------------------------
# ODDS RANGE
# ---------------------------------------------------
bins = [1, 1.5, 2.0, 2.5, 3.0, 5.0]

labels = [
    "1.0–1.5",
    "1.5–2.0",
    "2.0–2.5",
    "2.5–3.0",
    "3.0+"
]

analysis_df["Odds_Range"] = pd.cut(
    analysis_df["Favorite_Odds"],
    bins=bins,
    labels=labels
)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.header("Dashboard Filters")

selected_seasons = st.sidebar.multiselect(
    "Select Seasons",
    sorted(analysis_df["Season"].unique()),
    default=sorted(analysis_df["Season"].unique())
)

filtered_df = analysis_df[
    analysis_df["Season"].isin(selected_seasons)
]

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------
market_accuracy = (
    filtered_df["Correct_Prediction"]
    .mean() * 100
)

home_win_rate = (
    filtered_df["Home_Win"]
    .mean() * 100
)

upset_rate = (
    filtered_df["Upset"]
    .mean() * 100
)

matches = len(filtered_df)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Market Accuracy",
    f"{market_accuracy:.2f}%"
)

col2.metric(
    "Home Win Rate",
    f"{home_win_rate:.2f}%"
)

col3.metric(
    "Upset Rate",
    f"{upset_rate:.2f}%"
)

col4.metric(
    "Matches",
    f"{matches:,}"
)

# ---------------------------------------------------
# BUSINESS QUESTION 1
# ---------------------------------------------------
st.header("1️⃣ Betting Market Accuracy")

season_accuracy = (
    filtered_df.groupby("Season")
    ["Correct_Prediction"]
    .mean() * 100
).reset_index()

fig1 = px.line(
    season_accuracy,
    x="Season",
    y="Correct_Prediction",
    markers=True,
    title="Betting Market Accuracy Over Time"
)

fig1.update_layout(
    yaxis_title="Accuracy (%)"
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------------------------------------------
# BUSINESS QUESTION 2
# ---------------------------------------------------
st.header("2️⃣ Home Advantage Trend")

home_trend = (
    filtered_df.groupby("Season")
    ["Home_Win"]
    .mean() * 100
).reset_index()

fig2 = px.line(
    home_trend,
    x="Season",
    y="Home_Win",
    markers=True,
    title="Home Win Percentage by Season"
)

fig2.update_layout(
    yaxis_title="Home Win %"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------------------------
# BUSINESS QUESTION 3
# ---------------------------------------------------
st.header("3️⃣ Teams That Beat Market Expectations")

analysis_df["Market_Correct"] = (
    analysis_df["Market_Prediction"]
    == analysis_df["Res"]
).astype(int)

analysis_df["Away_Win"] = (
    analysis_df["Res"] == "A"
).astype(int)

home_performance = pd.DataFrame({
    "Team": analysis_df["Home"],
    "Win": analysis_df["Home_Win"],
    "Market_Correct": analysis_df["Market_Correct"]
})

away_performance = pd.DataFrame({
    "Team": analysis_df["Away"],
    "Win": analysis_df["Away_Win"],
    "Market_Correct": analysis_df["Market_Correct"]
})

team_performance = pd.concat([
    home_performance,
    away_performance
])

team_performance["Beat_Market"] = (
    (team_performance["Win"] == 1)
    &
    (team_performance["Market_Correct"] == 0)
).astype(int)

team_market_outperformance = (
    team_performance.groupby("Team")
    .agg(
        Matches=("Win", "count"),
        Wins=("Win", "sum"),
        Beat_Market=("Beat_Market", "sum")
    )
)

team_market_outperformance[
    "Beat_Market_Rate"
] = (
    team_market_outperformance["Beat_Market"]
    /
    team_market_outperformance["Matches"]
) * 100

team_market_outperformance = (
    team_market_outperformance
    .sort_values(
        "Beat_Market_Rate",
        ascending=False
    )
    .head(10)
    .reset_index()
)

fig3 = px.bar(
    team_market_outperformance,
    x="Beat_Market_Rate",
    y="Team",
    orientation="h",
    title="Top Teams That Beat Market Expectations"
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------------------------------------------
# BUSINESS QUESTION 4
# ---------------------------------------------------
st.header("4️⃣ MLS Unpredictability Over Time")

season_unpredictability = (
    filtered_df.groupby("Season")
    ["Upset"]
    .mean() * 100
).reset_index()

fig4 = px.line(
    season_unpredictability,
    x="Season",
    y="Upset",
    markers=True,
    title="Upset Frequency Over Time"
)

fig4.update_layout(
    yaxis_title="Upset Rate (%)"
)

st.plotly_chart(fig4, use_container_width=True)

# ---------------------------------------------------
# BUSINESS QUESTION 5
# ---------------------------------------------------
st.header("5️⃣ Upset Frequency by Favorite Odds Range")

upset_analysis = (
    filtered_df.groupby("Odds_Range")
    .agg(
        Matches=("Upset", "count"),
        Upsets=("Upset", "sum")
    )
)

upset_analysis["Upset_Rate"] = (
    upset_analysis["Upsets"]
    /
    upset_analysis["Matches"]
) * 100

upset_analysis = upset_analysis.reset_index()

fig5 = px.bar(
    upset_analysis,
    x="Odds_Range",
    y="Upset_Rate",
    title="Upset Frequency by Favorite Odds Range"
)

st.plotly_chart(fig5, use_container_width=True)

# ---------------------------------------------------
# RAW DATA SECTION
# ---------------------------------------------------
st.header("📋 Dataset Preview")

st.dataframe(filtered_df.head(20))

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")

st.markdown(
    """
### ⚽ Key Insight
MLS has become increasingly unpredictable over time, with declining home advantage
and rising upset frequency in balanced fixtures.

Built using:
- Python
- Pandas
- Plotly
- Streamlit
"""
)
