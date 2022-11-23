from sqlalchemy.orm import Session
from . import models, schemas

def add_prediction(db: Session, pred: schemas.PredictionCreate):
    db_pred = models.Prediction(features=pred.features,
                                prediction=pred.prediction,
                                heure=pred.heure)
    db.add(db_pred)
    db.commit()
    db.refresh(db_pred)