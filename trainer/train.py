import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os
import time

DATASET_PATH = "dataset/motion_data.csv"
MODEL_PATH = "model/traffic_model.pkl"

print("ML trainer started")

while True:

    if not os.path.exists(DATASET_PATH):
        print("Dataset not found")
        time.sleep(10)
        continue

    df = pd.read_csv(DATASET_PATH)

    if len(df) < 10:
        print(f"Not enough data: {len(df)} rows")
        time.sleep(10)
        continue

    df["hour"] = pd.to_datetime(df["timestamp"]).dt.hour

    X = df[["hour"]]

    y = df["motion"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestClassifier()

    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    joblib.dump(model, MODEL_PATH)

    print(f"Model trained. Accuracy: {accuracy}")

    time.sleep(30)