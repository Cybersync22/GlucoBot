# 🩺 GlucoBot

## 📝 Problem Statement
Diabetes is a chronic disease affecting millions globally. Early prediction and intervention can significantly reduce complications and healthcare costs. However, many at-risk individuals go undiagnosed due to lack of awareness or access to diagnostic tools.

#### Goal: The main aim is to build a machine learning-based system that predicts whether an individual is likely to be diabetic based on clinical and lifestyle parameters — quickly, accurately, and interactively.

## 💡 Solution Approach
GlucoBot is a smart AI-powered web application that predicts diabetes based on various user inputs such as age, gender, weight, height, blood sugar levels, HbA1c and lifestyle factors. The solution consists of:

- Data Collection: Clean, structured dataset of anonymized health records.

- Preprocessing: Handling missing data, encoding categorical variables, scaling numeric features.

- Model Training: Selecting the best classifier model through evaluation.

- Deployment: User-friendly interface via Streamlit for real-time prediction.

## 📈 Input Features Used (from dataset_diabetes.csv)

## 🖥️ Tech Stack 

- **Python:** The primary programming language used for development.
- **scikit-learn:** A comprehensive machine learning library for various tasks like model selection (`train_test_split`), preprocessing (`StandardScaler`, `LabelEncoder`), and evaluation          metrics (`accuracy_score`, `confusion_matrix`, `classification_report`, `roc_curve`, `auc`).
- **XGBoost:** An optimized distributed gradient boosting library designed for speed and performance.
- **Joblib:** Used for saving and loading Python objects, particularly trained machine learning models.
- **Seaborn:** A data visualization library based on matplotlib, used for creating informative and attractive statistical graphics (e.g., `confusion_matrix` visualizations).
- **Matplotlib:** A fundamental plotting library for creating static, interactive, and animated visualizations in Python.
