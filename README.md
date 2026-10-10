# Swiggy Delivery Time Prediction

## Project Overview

This project predicts estimated food delivery time using machine learning. It features an interactive web application built with Streamlit.

## Features

- Predicts estimated food delivery time in minutes.
- Accepts inputs such as distance, traffic, weather, ratings, and vehicle condition.
- Uses a trained XGBoost regression model.
- Provides a customized user interface with a delivery time prediction card.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- XGBoost
- Streamlit

## Project Files

- `app.py` — Main Streamlit application.
- `swiggydeliverytime.pkl` — Trained machine learning model.
- `swiggy_demographic.csv` — Dataset, if required by the application.
- `requirements.txt` — Required Python libraries.
- `Rainy Night Delivery Rider in City Lights.png` — Background image.

## How to Run the Application Locally

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install the required libraries:

   pip install -r requirements.txt

4. Run the application:

   streamlit run app.py


## Machine Learning Model

The application uses an XGBoost regression model to estimate delivery time based on delivery-related features.

## Model Evaluation

## Model Performance and Evaluation

The XGBoost regression model was optimized using Optuna hyperparameter tuning and evaluated on a held-out test dataset.

| Evaluation Metric | Result |
|---|---:|
| Mean Absolute Error (MAE) | 3.15 minutes |
| Root Mean Squared Error (RMSE) | 3.99 minutes |
| R² Score | 0.82 |
| Cross-Validation MAE | 3.14 minutes |

### Interpretation

- MAE — 3.15 minutes: The model's predictions differ from the actual delivery times by approximately 3.15 minutes on average.
- RMSE — 3.99 minutes: The RMSE is higher than the MAE, reflecting the greater penalty assigned to larger prediction errors.
- R² Score — 0.82: The model explains approximately 82% of the variation in delivery time on the test dataset, relative to a mean-prediction baseline.
- Cross-Validation MAE — 3.14 minutes: The cross-validation result is close to the test MAE, suggesting consistent predictive performance across the evaluated data splits.

Overall, the model demonstrates promising performance for predicting food delivery times using delivery-related and contextual features.

## Author

Charitha.L
