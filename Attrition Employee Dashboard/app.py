import streamlit as st
import pickle
import pandas as pd

# Load model dan scaler
model = pickle.load(open("logreg_model.pkl", "rb"))
robust_scaler = pickle.load(open("robust_scaler.pkl", "rb"))
minmax_scaler = pickle.load(open("minmax_scaler.pkl", "rb"))

st.title("Employee Attrition Prediction")

# Input user untuk 4 fitur
age = st.number_input("Age", 18, 65)
job_satisfaction = st.slider("Job Satisfaction", 1, 4)
monthly_income = st.number_input("Monthly Income", 1000, 20000)
overtime = st.selectbox("OverTime", ["Yes", "No"])
overtime_bin = 1 if overtime == "Yes" else 0

# Daftar lengkap 34 fitur, urut dan case sensitive sesuai training
feature_names = [
    'EmployeeId', 'Age', 'BusinessTravel', 'DailyRate', 'Department', 'DistanceFromHome',
    'Education', 'EducationField', 'EmployeeCount', 'EnvironmentSatisfaction', 'Gender',
    'HourlyRate', 'JobInvolvement', 'JobLevel', 'JobRole', 'JobSatisfaction', 'MaritalStatus',
    'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked', 'Over18', 'OverTime',
    'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction', 'StandardHours',
    'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance',
    'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager'
]

# Buat dataframe 1 baris dengan default 0 semua fitur
data = {feat: [0] for feat in feature_names}
df_input = pd.DataFrame(data)

# Isi kolom input user (pastikan sesuai nama fitur)
df_input.loc[0, 'Age'] = age
df_input.loc[0, 'JobSatisfaction'] = job_satisfaction
df_input.loc[0, 'MonthlyIncome'] = monthly_income
df_input.loc[0, 'OverTime'] = overtime_bin

# Predict jika tombol ditekan
if st.button("Predict"):
    # Transform fitur
    features_scaled = robust_scaler.transform(df_input)
    features_scaled = minmax_scaler.transform(features_scaled)

    # Predict
    pred = model.predict(features_scaled)[0]
    st.success("Attrition" if pred == 1 else "Not Attrition")