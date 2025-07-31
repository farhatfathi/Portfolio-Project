import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load model dan scaler
model = pickle.load(open("rf_model.pkl", "rb"))
scaler = pickle.load(open("standard_scaler.pkl", "rb"))

# Judul aplikasi
st.title("🎓 Prediksi Status Siswa Jaya Jaya Institut")
st.write("Masukkan data siswa untuk memprediksi apakah siswa akan **Dropout**, **Enrolled**, atau **Graduate**.")

st.title("Student Status Prediction")

# Input user untuk 15 fitur penting
course = st.number_input("Course (numeric code)", 1)
admission_grade = st.number_input("Admission Grade", 0.0, 200.0)
previous_qualification_grade = st.number_input("Previous Qualification Grade", 0.0, 200.0)
age_at_enrollment = st.number_input("Age at Enrollment", 15, 100)
tuition_fees_up_to_date = st.selectbox("Tuition Fees Up to Date", ["Yes", "No"])
tuition_fees_bin = 1 if tuition_fees_up_to_date == "Yes" else 0
approval_rate_sem1 = st.slider("Approval Rate Semester 1", 0.0, 1.0)
approval_rate_sem2 = st.slider("Approval Rate Semester 2", 0.0, 1.0)
curricular_units_1st_sem_grade = st.number_input("1st Sem Grade", 0.0, 20.0)
curricular_units_2nd_sem_grade = st.number_input("2nd Sem Grade", 0.0, 20.0)
curricular_units_1st_sem_approved = st.number_input("1st Sem Approved", 0, 10)
curricular_units_2nd_sem_approved = st.number_input("2nd Sem Approved", 0, 10)
curricular_units_1st_sem_evaluations = st.number_input("1st Sem Evaluations", 0, 20)
curricular_units_2nd_sem_evaluations = st.number_input("2nd Sem Evaluations", 0, 20)
fathers_occupation = st.number_input("Father's Occupation (code)", 0)

# Daftar lengkap 37 fitur (tanpa 'Status')
feature_names = [
    'Marital_status', 'Application_mode', 'Application_order', 'Course',
    'Daytime_evening_attendance', 'Previous_qualification',
    'Previous_qualification_grade', 'Nacionality', 'Mothers_qualification',
    'Fathers_qualification', 'Mothers_occupation', 'Fathers_occupation',
    'Admission_grade', 'Displaced', 'Educational_special_needs', 'Debtor',
    'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder',
    'Age_at_enrollment', 'International',
    'Curricular_units_1st_sem_credited',
    'Curricular_units_1st_sem_enrolled',
    'Curricular_units_1st_sem_evaluations',
    'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
    'Curricular_units_1st_sem_without_evaluations',
    'Curricular_units_2nd_sem_credited',
    'Curricular_units_2nd_sem_enrolled',
    'Curricular_units_2nd_sem_evaluations',
    'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade',
    'Curricular_units_2nd_sem_without_evaluations', 'Unemployment_rate',
    'Inflation_rate', 'GDP', 'approval_rate_sem1', 'approval_rate_sem2'
]

# Buat dataframe 1 baris dengan default 0
data = {feat: [0] for feat in feature_names}
df_input = pd.DataFrame(data)

# Isi kolom input user
df_input.loc[0, 'Course'] = course
df_input.loc[0, 'Admission_grade'] = admission_grade
df_input.loc[0, 'Previous_qualification_grade'] = previous_qualification_grade
df_input.loc[0, 'Age_at_enrollment'] = age_at_enrollment
df_input.loc[0, 'Tuition_fees_up_to_date'] = tuition_fees_bin
df_input.loc[0, 'approval_rate_sem1'] = approval_rate_sem1
df_input.loc[0, 'approval_rate_sem2'] = approval_rate_sem2
df_input.loc[0, 'Curricular_units_1st_sem_grade'] = curricular_units_1st_sem_grade
df_input.loc[0, 'Curricular_units_2nd_sem_grade'] = curricular_units_2nd_sem_grade
df_input.loc[0, 'Curricular_units_1st_sem_approved'] = curricular_units_1st_sem_approved
df_input.loc[0, 'Curricular_units_2nd_sem_approved'] = curricular_units_2nd_sem_approved
df_input.loc[0, 'Curricular_units_1st_sem_evaluations'] = curricular_units_1st_sem_evaluations
df_input.loc[0, 'Curricular_units_2nd_sem_evaluations'] = curricular_units_2nd_sem_evaluations
df_input.loc[0, 'Fathers_occupation'] = fathers_occupation

# Predict jika tombol ditekan
if st.button("Predict Status"):
    # Scaling fitur
    features_scaled = scaler.transform(df_input)

    # Predict status (0: Enrolled, 1: Graduate, 2: Dropout)
    pred = model.predict(features_scaled)[0]
    status_map = {0: "Dropout", 1: "Enrolled", 2: "Graduate"}
    st.success(f"Predicted Student Status: {status_map[pred]}")