from sqlalchemy.orm import Session
from . import models 

def get_predictions(db: Session, time: int):
    return db.query(models.Prediction)\
        .with_entities(models.Prediction.size,
                       models.Prediction.nbrooms,
                       models.Prediction.garden)\
        .filter(models.Prediction.heure >= time).all()