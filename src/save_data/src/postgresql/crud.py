from sqlalchemy.orm import Session
from . import models, schemas

def add_prediction(db: Session, pred: schemas.PredictionCreate):
    db_pred = models.Prediction(
        size=pred.features[0],
        nbrooms=pred.features[1],
        garden=pred.features[2],
        prediction=pred.prediction,
        heure=pred.heure
    )
    
    db.add(db_pred)
    db.commit()
    db.refresh(db_pred)