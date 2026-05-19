from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import os

app = FastAPI()

DATASET_PATH = "dataset/motion_data.csv"


class MotionData(BaseModel):
    motion: int
    timestamp: str


@app.get("/")
def home():
    return {
        "status": "API is running"
    }


@app.post("/sensor")
def receive_data(data: MotionData):

    new_row = {
        "motion": data.motion,
        "timestamp": data.timestamp
    }

    df = pd.DataFrame([new_row])

    write_header = (
        not os.path.exists(DATASET_PATH)
        or os.path.getsize(DATASET_PATH) == 0
    )

    df.to_csv(
        DATASET_PATH,
        mode='a',
        header=write_header,
        index=False
    )

    return {
        "status": "success",
        "saved_data": new_row
    }