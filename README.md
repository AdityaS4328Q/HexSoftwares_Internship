# HexSoftwares_Internship
My work as a Data Science intern in Hex Softwares.
# Week 1 Project 2
# Simple Linear Regression on Housing Prices

## Project Overview

This project builds a **Linear Regression model** to 
predict California housing prices using features like 
median income, average rooms, occupancy rate and 
geographic location.

The project follows a complete data science workflow —
from raw data loading to model evaluation and 
interpretation.

---

## Objective

- Load and explore the California Housing dataset
- Perform data cleaning and outlier removal
- Conduct Exploratory Data Analysis (EDA)
- Select relevant features using correlation analysis
- Normalize features and build a Linear Regression model
- Evaluate and interpret model performance

---

## Project Structure
```
housing-price-prediction/
│
├── housing_price_regression.ipynb   ← main notebook
├── README.md                        ← this file
└── requirements.txt                 ← dependencies
```

---


---

## Dataset

- Source: California Housing Dataset (scikit-learn)  
- Size: 20,640 rows × 9 columns  
- Target: PRICE (median house value in $100,000s)

| Feature     | Description                              |
|-------------|------------------------------------------|
| MedInc      | Median income in block group             |
| HouseAge    | Median house age                         |
| AveRooms    | Avg rooms per household                  |
| AveBedrms   | Avg bedrooms per household               |
| Population  | Block population                         |
| AveOccup    | Avg household size                       |
| Latitude    | Latitude                                 |
| Longitude   | Longitude                                |

---

## Tech Stack

- Python  
- pandas  
- numpy  
- matplotlib  
- seaborn  
- scikit-learn  
- Jupyter Notebook  

---

## Workflow

### 1. Data Loading and Inspection
- Loaded dataset using sklearn  
- Checked shape, data types, and null values  
- Used describe() for statistical overview  

### 2. Exploratory Data Analysis
- Plotted feature distributions  
- Built correlation heatmap  
- Scatter plot: MedInc vs PRICE  
- Pairplots for key features  

Key observation:  
MedInc showed the strongest positive correlation with price.

---

### 3. Data Cleaning
- Detected extreme outliers:
  - AveOccup (max = 1243 vs mean ~3)  
  - AveRooms (max = 141 vs mean ~5)  
- Applied IQR method for removal  
- Removed ~5.9% of data  
- Reset index after cleaning  

---

### 4. Feature Selection
- Used absolute correlation with target  
- Threshold: |correlation| > 0.15  

Reason:  
Avoided dropping negatively correlated but important features.

Selected features:
- MedInc  
- AveRooms  
- AveOccup  
- Latitude  

---

### 5. Preprocessing
- Train-test split (80/20, random_state=42)  
- Applied StandardScaler  
- Fit on training data only to avoid data leakage  

---

### 6. Model Building
- Used LinearRegression from scikit-learn  
- Trained on scaled features  

---

### 7. Model Evaluation

Final Model Performance:

| Metric | Value |
|--------|------|
| R²     | 0.69 |
| RMSE   | 0.6412 |
| MAE    | 0.4713 |

- Explains ~69% of variance  
- No overfitting (train ≈ test performance)

Model Comparison:

| Metric | 8 Features | 4 Features |
|--------|-----------|-----------|
| R²     | 0.6900 | 0.6329 |
| RMSE   | 0.6412 | 0.6977 |
| MAE    | 0.4713 | 0.5116 |

Conclusion:  
Even weaker features improved performance collectively.

---

## Key Insights

- Median income is the strongest predictor  
- Location (latitude) plays a significant role  
- Higher occupancy tends to reduce house prices  
- Dataset has capped prices, affecting predictions  
- Removing features reduced model performance  

---

## Limitations

- Price capped at $500,000 limits accuracy  
- Linear model cannot capture complex relationships  
- Missing real-world factors (crime, schools, amenities)  
- Can produce unrealistic predictions in edge cases  

---
# Week 2 Project
# Analyzing and Visualizing IMDB Movie Ratings 🎬📊

**Company:** Hex Softwares  
**Role:** Data Science Intern  
**Project:** Exploratory Data Analysis (EDA) & Dashboard Creation  

## 📝 Project Overview
This project focuses on extracting actionable business intelligence from historical IMDB movie data. The goal of this task was to clean raw data, calculate statistical summaries, and build a consolidated visual dashboard to identify the characteristics of critically successful movies. 

## 🛠️ Tools & Technologies Used
* **Language:** Python
* **Data Manipulation:** Pandas, NumPy
* **Data Visualization:** Matplotlib, Seaborn
* **Environment:** Jupyter Notebook

## 🔍 Step-by-Step Implementation

### 1. Data Cleaning & Preprocessing
* Loaded the raw IMDB dataset containing 1,000 movies.
* Identified missing values in the `Revenue (Millions)` and `Metascore` columns.
* Imputed missing values using the **median** of their respective columns to maintain dataset integrity without skewing the data with extreme financial outliers.

### 2. Statistical Analysis
* Calculated core summary statistics for the `Rating` target variable:
  * **Mean:** 6.72 
  * **Median:** 6.80 
  * **Mode:** 7.10
* Identified a clear **left-skewed distribution**, indicating that most movies in this dataset are rated favorably, with a small number of severe underperformers pulling the mean down.

### 3. Visualizing Distributions & Outliers
* **Histogram:** Built to visualize the frequency of ratings, confirming the concentration of movies in the 6.0 - 8.0 range.
* **Box Plot:** Generated a vertical box plot to visually isolate statistical outliers (movies rated < 4.0).

### 4. Identifying Top Performers
* Utilized Pandas grouping and sorting to extract the highest-performing segments:
  * **Top Movie:** *The Dark Knight*
  * **Top Genre Combination:** Action, Crime, Drama

### 5. Executive Dashboard
* Consolidated all individual visual findings into a single, high-level 2x2 dashboard using `matplotlib.subplots`.
* This dashboard provides stakeholders with an immediate, at-a-glance understanding of the rating distribution, outliers, and top-performing categories without needing to read the underlying code.

## 💡 Business Conclusion & Insights
The data suggests that to maximize critical reception, studios should prioritize the `Action, Crime, Drama` genre combination. Furthermore, while the average movie is generally well-received (rated ~7/10), studios must be wary of the severe negative outliers that exist at the bottom of the distribution curve, as they heavily drag down overall studio averages.

---
*Feel free to explore the Jupyter Notebook in this repository to see the complete code, data cleaning steps, and final visualizations!*

# Week 3 Task
# Building a YouTube Data Dashboard with Streamlit 📺📊

**Company:** Hex Softwares  
**Role:** Data Science Intern  
**Project:** YouTube Data API Integration & Interactive Web Dashboard

## 📝 Project Overview
This project is an interactive web-based data dashboard built using Python and Streamlit. It integrates with the official Google YouTube Data API (v3) to fetch real-time analytics for any public YouTube channel. By inputting a Channel ID, users can instantly visualize channel-level metrics and deep-dive into the performance of recent uploads.

## 🛠️ Tools & Technologies
* **Framework:** Streamlit (for building the web application interface)
* **API Integration:** `google-api-python-client` (YouTube Data API v3)
* **Data Manipulation:** Pandas
* **Data Visualization:** Plotly Express (for interactive charts)
* **Language:** Python

## ✨ Key Features
* **Live API Connection:** Fetches real-time channel statistics including total subscribers, total views, and total video count.
* **Dynamic Video Fetching:** Retrieves the most recent uploads from a specific channel (adjustable from 5 to 50 videos via UI slider).
* **Interactive Visualizations:** Utilizes Plotly to generate dynamic bar charts analyzing video performance.
* **State Management:** Implements `st.session_state` to ensure seamless data filtering and UI interaction without triggering unwanted API re-fetches.
* **Custom Sorting:** Users can interactively sort the dashboard by 'Total Views' or 'Total Likes'.

## 🚀 How to Run the App Locally

### 1. Install Prerequisites
Ensure you have Python installed, then install the required libraries via your terminal:
```bash
pip install streamlit google-api-python-client pandas plotly
