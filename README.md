# ESP32 Motion Traffic Prediction System

## Overview

This project is a mini IoT + Machine Learning system based on ESP32, FastAPI, Docker and Python.

The system simulates or receives motion sensor data from an ESP32 microcontroller, stores the collected data, and trains a machine learning model to analyze room traffic activity.

The project demonstrates:
- IoT device communication
- REST API interaction
- Docker containerization
- Dataset generation
- Machine Learning pipeline
- Real-time sensor simulation

---

# Architecture

```text
ESP32 / Simulator
        ↓
FastAPI Backend
        ↓
CSV Dataset
        ↓
ML Trainer
        ↓
Trained Model (.pkl)
```

---

# Technologies Used

## Backend
- Python
- FastAPI
- Pandas

## Machine Learning
- Scikit-learn
- RandomForestClassifier
- Joblib

## IoT
- ESP32
- Arduino Framework
- PIR Motion Sensor

## DevOps
- Docker
- Docker Compose

---

# Project Structure

```text
ESP32-ML-Container/
│
├── api/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── simulator/
│   ├── simulator.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── trainer/
│   ├── train.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── esp32/
│   ├── esp32_motion_sensor.ino
│   └── esp32_config.h
│
├── dataset/
│   └── motion_data.csv
│
├── model/
│   └── traffic_model.pkl
│
├── docker-compose.yml
├── config.json
└── README.md
```

---

# System Components

## 1. FastAPI Backend

The backend service:
- receives sensor data,
- validates JSON payloads,
- stores events into CSV dataset.

### Endpoint

```http
POST /sensor
```

### Example Payload

```json
{
  "motion": 1,
  "timestamp": "2026-05-19T12:00:00"
}
```

---

## 2. ESP32 Simulator

The simulator emulates:
- ESP32 board
- PIR motion sensor

The simulator automatically sends HTTP POST requests to the backend.

---

## 3. Machine Learning Trainer

The trainer service:
- reads the generated dataset,
- preprocesses timestamps,
- trains a RandomForest model,
- saves the model to `.pkl`.

---

## 4. ESP32 Firmware

The repository also contains real ESP32 firmware code.

Features:
- WiFi connection
- PIR motion detection
- HTTP POST requests
- JSON serialization

Main libraries:
- WiFi.h
- HTTPClient.h
- ArduinoJson.h

---

# Configuration

## Python Services

All backend and ML configuration is stored in:

```text
config.json
```

Contains:
- API settings
- dataset path
- model settings
- simulator settings

---

## ESP32

ESP32 configuration is stored in:

```text
esp32/esp32_config.h
```

Contains:
- WiFi credentials
- backend server URL
- PIR GPIO pin
- request interval

---

# Docker Launch

## Build and start containers

```bash
docker compose up --build
```

---

# Running Containers

The following containers will start:

| Container | Purpose |
|---|---|
| motion_api | FastAPI backend |
| motion_simulator | ESP32 simulator |
| ml_trainer | ML training service |

---

# Generated Files

## Dataset

```text
dataset/motion_data.csv
```

Contains collected sensor events.

---

## Trained Model

```text
model/traffic_model.pkl
```

Contains trained RandomForest model.

---

# Example Workflow

1. Simulator generates motion events
2. FastAPI receives JSON requests
3. Data is appended to CSV dataset
4. Trainer reads dataset
5. ML model is trained automatically
6. Model is saved to `.pkl`

---

# Real ESP32 Usage

The system supports real ESP32 hardware.

Required components:
- ESP32 DevKit
- PIR motion sensor HC-SR501
- WiFi connection

ESP32 sends sensor data directly to the FastAPI backend.

---

# Educational Purpose

This project was created for educational purposes to demonstrate:
- IoT architecture
- REST APIs
- Docker containerization
- ML pipelines
- Sensor data processing
- Embedded integration with Python backend

---

# Future Improvements

Possible future improvements:
- SQLite/PostgreSQL integration
- Real-time dashboard
- Traffic level classification
- MQTT support
- Grafana visualization
- TinyML deployment on ESP32