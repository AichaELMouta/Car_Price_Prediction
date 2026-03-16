# 🚗 Car Price Prediction using Machine Learning

## 📌 Project Overview

Pricing used cars accurately is a challenge for both buyers and sellers. Many factors such as car age, fuel type, transmission, and kilometers driven influence the final selling price.

The goal of this project is to build a **machine learning model capable of predicting the selling price of a used car** based on its characteristics.

This project demonstrates a **complete data science workflow**, including:

* Exploratory Data Analysis (EDA)
* Statistical analysis
* Feature engineering
* Machine learning model comparison
* Model explainability using SHAP

---

# 🎯 Business Problem

Determining the fair value of a used car can be difficult due to the many variables that influence its price.

This project aims to develop a predictive model that can estimate the selling price of a car based on features such as:

* Manufacturing year
* Kilometers driven
* Fuel type
* Transmission
* Ownership history
* Present price

Such a model could be useful for:

* 🚗 Car dealerships to estimate resale prices
* 💰 Buyers to determine fair market value
* 📊 Online marketplaces to automate price suggestions

---

# 📊 Dataset

The dataset contains information about used cars and their characteristics.

### Main Variables

| Feature       | Description                                |
| ------------- | ------------------------------------------ |
| Car_Name      | Name of the car                            |
| Year          | Manufacturing year                         |
| Selling_Price | Selling price of the car (Target variable) |
| Present_Price | Current showroom price                     |
| Kms_Driven    | Total kilometers driven                    |
| Fuel_Type     | Type of fuel (Petrol, Diesel, CNG)         |
| Seller_Type   | Dealer or Individual                       |
| Transmission  | Manual or Automatic                        |
| Owner         | Number of previous owners                  |

Each row represents a **car listing with its corresponding price**.

---

# 🔎 Exploratory Data Analysis (EDA)

EDA was performed to understand the structure of the dataset and identify relationships between variables.

### Key analyses performed

* Distribution of the target variable (Selling Price)
* Relationship between **car age and price**
* Analysis of **fuel type impact on price**
* Correlation analysis between numerical variables
* Outlier detection

### Key insights

* Older cars tend to have **lower selling prices**.
* Diesel vehicles generally have **higher resale value** compared to petrol cars.
* Cars with **higher mileage (kms driven)** tend to have lower prices.

---

# 📈 Statistical Analysis

Statistical tests were conducted to better understand the relationships between variables.

### Methods used

* **Spearman correlation** to measure monotonic relationships
* **ANOVA tests** to compare mean prices across categories
* **Tukey HSD tests** for post-hoc comparisons

These tests help confirm whether observed relationships are **statistically significant rather than random patterns**.

---

# 🛠 Feature Engineering

Several transformations were applied to improve model performance.

### Examples

* Creation of **Car Age** from the manufacturing year
* Encoding categorical variables using **one-hot encoding**
* Analysis of skewness and variable distributions

Feature engineering helps models capture **more meaningful relationships in the data**.

---

# 🤖 Machine Learning Models

Several machine learning models were trained and compared.

### Models implemented

* Linear Regression
* Lasso Regression
* Ridge Regression
* ElasticNet
* Random Forest Regressor
* Gradient Boosting Regressor

Testing multiple models allows identification of the **best performing approach** for price prediction.

---

# 📊 Model Evaluation

Models were evaluated using the following metrics:

* **RMSE (Root Mean Squared Error)**
* **R² Score**

Example comparison:

| Model             | RMSE | R²   |
| ----------------- | ---- | ---- |
| Linear Regression | 2.96 | 0.88 |
| Lasso Regression  | 5.53 | 0.79 |
| Ridge Regression  | 2.96 | 0.89 |
| ElasticNet        | 5.10 | 0.80 |
| Random Forest     | 0.38 | 0.98 |
| Gradient Boosting | 0.11 | 0.99 |

Tree-based ensemble models achieved the **best predictive performance**.

---

# 🔍 Model Explainability

To understand how the model makes predictions, **SHAP (SHapley Additive Explanations)** was used.

SHAP helps identify how each feature contributes to predictions.

### Key findings

* **Car age** strongly influences selling price.
* **Kilometers driven** negatively affects the predicted value.
* **Fuel type** plays an important role in determining price.

This analysis improves **model transparency and interpretability**.

---

# 🚀 Deployment

The trained model can be deployed using **Streamlit** to create an interactive web application where users can input car characteristics and obtain predicted prices.

### inputs

* Year
* Kilometers Driven
* Fuel Type
* Transmission
* Number of Owners
* Present Price

### Output

Predicted **car selling price**.

---

# 🧰 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* SHAP

---

# 📂 Project Structure

```
Car_Price_Prediction
│
├── data
│
├── notebooks
│   └── car_price_prediction.ipynb
│
├── models
│
├── README.md
```

---

# ▶️ How to Run the Project

Clone the repository:

```
git clone https://github.com/AichaELMouta/Car_Price_Prediction.git
```

Install required libraries:

```
pip install -r requirements.txt
```

Open the notebook:

```
car_price_prediction.ipynb
```

---

# 📌 Conclusion

This project demonstrates a **complete machine learning workflow**, from data exploration and statistical analysis to model training and interpretation.

The results show that **ensemble models such as Gradient Boosting and Random Forest provide the most accurate predictions for car prices**.

---

⭐ If you found this project interesting, feel free to **star the repository**.
