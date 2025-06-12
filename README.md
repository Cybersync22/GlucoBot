# <p align="center"> 🩺 GlucoBot : AI-powered Diabetes Risk Predictor</p>

<p align="center"> 

![image](https://github.com/user-attachments/assets/6f8dddec-090f-463c-8c52-7f2aa8ac6a37) 

![image](https://github.com/user-attachments/assets/3b4a9643-58fa-4712-b7f8-f182d4aebb49)

</p>

## 📝 Problem Statement
Diabetes is a chronic disease affecting millions globally. Early prediction and intervention can significantly reduce complications and healthcare costs. However, many at-risk individuals go undiagnosed due to lack of awareness or access to diagnostic tools.

#### Goal: The main aim is to build a machine learning-based system that predicts whether an individual is likely to be diabetic based on clinical and lifestyle parameters — quickly, accurately, and interactively.

## 💡 Solution Approach
GlucoBot is a smart AI-powered web application that predicts diabetes risk based on various user inputs such as age, gender, weight, height, blood sugar levels, HbA1c and lifestyle factors. The solution consists of:

- Data Collection: Clean, structured dataset of anonymized health records.
- Preprocessing: Handling missing data, encoding categorical variables, scaling numeric features.
- Model Training: Selecting the best classifier model through evaluation.
- Deployment: User-friendly interface via Streamlit for real-time prediction.

## 📈 Input Features Used (from dataset_diabetes.csv)
- Gender (Male/Female)
- Age	in years
- Height in cm
- Weight	in kg
- Hypertension (0 = No, 1 = Yes)	
- Heart Disease	(0 = No, 1 = Yes)
- Smoking History	
- HbA1c Level	
- Blood Sugar Level (Fasting Blood Glucose) in mg/dL

## ✅ Target Feature
- Risk of Diabetes

## 🖥️ Tech Stack 
- **Python:** The primary programming language used for development.
- **scikit-learn:** A comprehensive machine learning library for various tasks like model selection (`train_test_split`), preprocessing (`StandardScaler`, `LabelEncoder`), and evaluation          metrics (`accuracy_score`, `confusion_matrix`, `classification_report`, `roc_curve`, `auc`).
- **XGBoost:** An optimized distributed gradient boosting library designed for speed and performance.
- **Joblib:** Used for saving and loading Python objects, particularly trained machine learning models.
- **Seaborn:** A data visualization library based on matplotlib, used for creating informative and attractive statistical graphics (e.g., `confusion_matrix` visualizations).
- **Matplotlib:** A fundamental plotting library for creating static, interactive, and animated visualizations in Python.

## 🛠️ Installation Guide 
### Requirements
- Python 3.7+
- Streamlit
- scikit-learn
- Pandas
- NumPy
- Matplotlib
- Seaborn
  <p> (Install using pip install -r requirements.txt) </p>

- Clone the repository
- Run the Streamlit app
  <p> (streamlit run app.py) </p>


##### <p align="right"> ~ Developed by Haimanti Chakraborty </p>
