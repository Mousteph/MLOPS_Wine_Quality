from sqlalchemy.orm import Session
from . import models, schemas

def add_prediction(db: Session, pred: schemas.PredictionCreate):
    db_pred = models.Prediction(
        fixed_acidity=pred.features[0],
        volatile_acidity=pred.features[1],
        citric_acid=pred.features[2],
        sulfur_dioxide=pred.features[3],
        pH=pred.features[4],
        alcohol=pred.features[5],
        quality=pred.quality,
        heure=pred.heure,
    )
    
    db.add(db_pred)
    db.commit()
    db.refresh(db_pred)