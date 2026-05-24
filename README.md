# ⚽ MLS Betting Market Efficiency Analysis (2012–2026)

## 📌 Project Overview

This project explores betting market efficiency and match unpredictability in Major League Soccer (MLS) using historical match results and bookmaker odds from 2012 to 2026.

The analysis combines football analytics, probability, and business intelligence to investigate how accurately betting markets predict MLS matches and how league competitiveness has evolved over time.

Using pre-match odds from Pinnacle Sports, the project evaluates:

* Market prediction accuracy
* Home advantage trends
* Team-level market outperformance
* League unpredictability
* Upset frequency across betting odds ranges

The project demonstrates how football data can be translated into meaningful business insights for sportsbooks, analysts, clubs, and media organizations.

---

# 🎯 Business Objective

The primary objective of this project is to evaluate:

> How efficiently the betting market predicts MLS match outcomes.

The analysis also investigates whether MLS has become more competitive and unpredictable over time.

---

# 📊 Dataset Description

The dataset contains historical MLS match results and betting odds data covering the 2012–2026 seasons.

Each row represents one MLS match.

## Dataset Information

* Total matches after cleaning: 5,800
* Seasons covered: 2012–2026
* Main bookmaker used: Pinnacle Sports

## Variables Used

| Column | Description            |
| ------ | ---------------------- |
| Season | MLS season year        |
| Date   | Match date             |
| Home   | Home team              |
| Away   | Away team              |
| HG     | Home goals scored      |
| AG     | Away goals scored      |
| Res    | Match result (H/D/A)   |
| PSCH   | Pinnacle home win odds |
| PSCD   | Pinnacle draw odds     |
| PSCA   | Pinnacle away win odds |

---

# 🧹 Data Cleaning & Preparation

The original dataset contained multiple bookmaker columns with substantial missing values.

To improve analytical consistency:

* Only relevant columns were retained
* Rows with missing Pinnacle odds were removed
* Non-essential bookmaker columns were excluded

This resulted in a fully cleaned dataset with:

* 5,800 observations
* No missing values in selected features

---

# 🧠 Analytical Framework

The analysis treats Pinnacle betting odds as a representation of:

> The market’s expectation before kickoff.

The betting market prediction was determined using the lowest odds value:

* Lowest PSCH → Home Win prediction
* Lowest PSCD → Draw prediction
* Lowest PSCA → Away Win prediction

This allows direct comparison between:

* Market expectation
* Actual match outcomes

---

# ❓ Business Question 1

# How Accurate Is the MLS Betting Market at Predicting Match Outcomes?

## Objective

Evaluate how often the betting market correctly predicts MLS match outcomes.

## Methodology

* Created a market prediction column using the lowest Pinnacle odds
* Compared market prediction against actual match results
* Calculated overall prediction accuracy

## Key Result

### Market Accuracy: 50.66%

## Interpretation

The betting market correctly predicted approximately half of MLS matches.

This suggests:

* MLS is moderately unpredictable
* Favorites do not consistently dominate
* Betting markets face difficulty pricing league volatility

## Business Insight

MLS demonstrates a relatively high level of competitive balance compared to more predictable football leagues.

---

# ❓ Business Question 2

# Has Home Advantage in MLS Changed Over Time?

## Objective

Determine whether the strength of home advantage has changed across seasons.

## Methodology

* Calculated home win percentage by season
* Tracked long-term trends from 2012–2025

## Key Findings

### Pre-2020

* Home win rates remained mostly between 50–55%

### Post-2020

* Home win rates declined significantly
* 2024: 45.02%
* 2025: 44.19%

## Interpretation

Home advantage in MLS has weakened over time.

Possible contributing factors:

* Improved travel logistics
* Greater tactical parity
* Reduced crowd influence
* Increased league competitiveness

## Business Insight

Traditional assumptions about strong home-field advantage may no longer hold consistently in MLS.

---

# ❓ Business Question 3

# Which MLS Teams Consistently Outperform Betting Market Expectations?

## Objective

Identify teams that frequently win matches the market does not expect them to win.

## Methodology

* Identified matches where the betting market prediction failed
* Measured how often teams still achieved victories
* Calculated Beat Market Rate for each club

## Top Teams by Beat Market Rate

| Team                | Beat Market Rate |
| ------------------- | ---------------: |
| San Diego FC        |           19.44% |
| Vancouver Whitecaps |           17.39% |
| Minnesota United    |           17.26% |
| Charlotte FC        |           17.02% |
| Inter Miami         |           16.34% |

## Interpretation

Several MLS teams consistently exceed bookmaker expectations.

The strongest long-term evidence comes from:

* Vancouver Whitecaps
* Minnesota United

These teams repeatedly produced results the betting market failed to anticipate.

## Business Insight

Some MLS clubs may possess tactical or performance characteristics not fully captured in bookmaker pricing models.

---

# ❓ Business Question 4

# Are MLS Matches Becoming More Unpredictable Over Time?

## Objective

Evaluate whether MLS match outcomes are becoming harder for betting markets to forecast.

## Methodology

* Calculated seasonal betting market prediction accuracy
* Compared trends over time

## Key Findings

### 2012–2019

* Market accuracy remained around 52–55%

### 2020–2025

* Accuracy declined toward 46–50%

## Interpretation

MLS matches have become increasingly unpredictable over time.

This trend aligns with:

* Declining home advantage
* Greater competitive balance
* Rising upset frequency

## Business Insight

Betting markets are finding MLS outcomes increasingly difficult to price accurately.

---

# ❓ Business Question 5

# Which Betting Odds Ranges Produce the Highest Upset Frequency?

## Objective

Identify which betting odds ranges are most associated with unexpected match outcomes.

## Methodology

* Identified upset matches where market predictions failed
* Grouped matches by favorite odds ranges
* Calculated upset frequency within each range

## Results

| Favorite Odds Range | Upset Rate |
| ------------------- | ---------: |
| 1.0–1.5             |     29.46% |
| 1.5–2.0             |     43.62% |
| 2.0–2.5             |     56.40% |
| 2.5–3.0             |     63.03% |

## Interpretation

Upset frequency increases significantly as favorite odds rise.

Once favorite odds exceed 2.0:

> The market becomes wrong more often than correct.

## Business Insight

Balanced MLS matches are highly volatile and difficult for betting markets to predict accurately.

---

# 📈 Key Project Insights

The analysis produced several major findings:

1. MLS betting market accuracy is relatively moderate
2. Home advantage has declined significantly after 2020
3. Certain clubs consistently outperform market expectations
4. MLS matches are becoming increasingly unpredictable
5. Upsets are concentrated in balanced fixtures

Together, these findings suggest that:

> MLS has evolved into a more competitive and volatile football league.

---

# 💼 Business Recommendations

## For Sportsbooks

* Recalibrate home advantage assumptions
* Improve pricing models for balanced fixtures
* Increase focus on volatility management

## For Football Analysts

* Incorporate contextual variables beyond odds
* Use season-adjusted prediction models
* Study tactical causes of market inefficiency

## For MLS & Media

* Emphasize league unpredictability in storytelling
* Promote competitive balance as an entertainment asset

---

# 🖥 Recommended Dashboard Features

A Streamlit dashboard for this project could include:

* KPI cards
* Seasonal trend analysis
* Team comparison filters
* Interactive upset analysis
* Home advantage visualization
* Betting odds exploration

---

# 🛠 Tools & Technologies

* Python
* Pandas
* Matplotlib
* Streamlit
* Football Analytics
* Sports Betting Analysis

---

# 📌 Conclusion

This project demonstrates how football match data and betting market information can be transformed into actionable business intelligence.

The findings reveal that MLS has become increasingly unpredictable over time, with weakening home advantage and growing volatility in balanced fixtures.

The project highlights the intersection between:

* Football analytics
* Probability modeling
* Betting market behavior
* Business intelligence

and showcases how data-driven storytelling can uncover deeper insights beyond match results.

---

# 🚀 Future Improvements

Potential future extensions include:

* Machine learning match prediction models
* Probability calibration analysis
* Team-specific tactical profiling
* Expected goals (xG) integration
* Betting ROI simulation
* Advanced bookmaker efficiency comparisons
