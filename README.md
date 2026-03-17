# HexSoftwares_Internship
My work as a Data Science intern in Hex Softwares.
# Week 1 Project 2
# 🏠 Simple Linear Regression on Housing Prices

## 📌 Project Overview

This project builds a **Linear Regression model** to 
predict California housing prices using features like 
median income, average rooms, occupancy rate and 
geographic location.

The project follows a complete data science workflow —
from raw data loading to model evaluation and 
interpretation.

---

## 🎯 Objective

- Load and explore the California Housing dataset
- Perform data cleaning and outlier removal
- Conduct Exploratory Data Analysis (EDA)
- Select relevant features using correlation analysis
- Normalize features and build a Linear Regression model
- Evaluate and interpret model performance

---

## 📂 Project Structure
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
