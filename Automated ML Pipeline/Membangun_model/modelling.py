# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn

# Aktifkan autolog MLflow
mlflow.sklearn.autolog()

# Load preprocessed dataset
link = 'https://raw.githubusercontent.com/farhatfathi/Eksperimen_SML_Muhammad-Fathi-Farhat/refs/heads/main/preprocessing/df_preprocessed.csv'
df = pd.read_csv(link, delimiter=',')
df = df.drop('CustomerID', axis=1)

# Pisahkan fitur dan target
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Mulai eksperimen MLflow
mlflow.set_experiment("MSML-churn-prediction")

with mlflow.start_run():
    # Training model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Prediksi dan evaluasi
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    # Output ke konsol (opsional)
    print(f"Akurasi model: {acc}")