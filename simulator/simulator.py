import requests
import random
import time
from datetime import datetime
import json

with open("config.json", "r") as f:
    config = json.load(f)

API_URL = config["simulator"]["api_url"]

SEND_INTERVAL = config["simulator"]["send_interval_seconds"]

print("ESP32 motion simulator started")

while True:

    current_hour = datetime.now().hour

    # Имитируем реалистичную активность
    # Днем людей больше

    if 8 <= current_hour <= 18:
        motion_probability = 0.8
    else:
        motion_probability = 0.2

    motion = 1 if random.random() < motion_probability else 0

    payload = {
        "motion": motion,
        "timestamp": datetime.now().isoformat()
    }

    try:

        response = requests.post(
            API_URL,
            json=payload
        )

        print(f"Sent: {payload}")
        print(f"Response: {response.status_code}")

    except Exception as e:

        print("Error:", e)

    time.sleep(SEND_INTERVAL)