from pydantic import BaseModel

class PredictionBase(BaseModel):
    features: list[int]
    prediction: float
    heure: int

class PredictionCreate(PredictionBase):
    pass


class Prediction(PredictionBase):
    id: int

    class Config:
        orm_mode = True