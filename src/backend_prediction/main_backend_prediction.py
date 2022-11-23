from pydantic import BaseModel
from fastapi import FastAPI
from typing import List
import uvicorn
import numpy as np

import model_prediction

app = FastAPI()

model_path = "/model/regression.joblib"
model = model_prediction.ModelPrediction(model_path)

class Item(BaseModel):
    data: List #size, nb_rooms, garden

@app.post("/predict")
async def response(value: Item):
    x = np.array(value.data).reshape((1, -1))
    val = model.prediction(x)[0]

    if val is None:
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
