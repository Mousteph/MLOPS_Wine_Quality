from pydantic import BaseModel
from fastapi import FastAPI
from typing import List
import uvicorn
import numpy as np
import os

import model_prediction
import producer_kafka

app = FastAPI()

model_path = "/model/wine_class.joblib"
servers_kafka = os.environ.get("SERVERS_K")
topic_wine = os.environ.get("TOPIC_WINE")

model = model_prediction.ModelPrediction(model_path)
producer = producer_kafka.PredictionProducer([servers_kafka], topic_wine)

class Item(BaseModel):
    data: List #size, nb_rooms, garden

@app.post("/predict")
async def response(value: Item):
    x = np.array(value.data).reshape((1, -1))
    success, val = model.prediction(x)
    
    # producer.produce_wine(value.data, val)

    if not success:
        return {
            "status": 0,
            "message": "Prediction Internal Error",
            "data": None
        }

    return {
        "status": 1,
        "message": "",
        "data": float(val)
    }

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=80) 
