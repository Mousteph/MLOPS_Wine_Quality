from data_drift import DataDriftManager
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI
import uvicorn
import pandas as pd

TRANING_DATA = "/data/training/wine.pkl"
DRIFTING = "/data/drift/drifting_wine.csv"

TRANING_DATA = "../../../data/training/wine.pkl"
DRIFTING = "../../../data/drift/drifting_wine.csv"

data_drift = DataDriftManager(DRIFTING, TRANING_DATA)
sched = BackgroundScheduler()

sched.add_job(data_drift.check, 'interval', seconds=6)
sched.start()

app = FastAPI()

@app.get("/drift")
async def response():
   return pd.read_csv(DRIFTING).to_json()

@app.get("/forcedirft")
async def response_force():
   data_drift.check()
   return pd.read_csv(DRIFTING).to_json()

if __name__ == '__main__':
   uvicorn.run(app, host="0.0.0.0", port=90) 