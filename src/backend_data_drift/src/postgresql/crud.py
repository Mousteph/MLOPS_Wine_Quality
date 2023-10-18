from sqlalchemy.orm import Session
from . import models 
from typing import List

def get_predictions(db: Session, time: int) -> List:
    """Return predictions from database

    Args:
        db (Session): SQLAlchemy session
        time (int): Filter predictions by time

    Returns:
        List: A list of predictions
    """
    
    return db.query(models.Prediction)\
        .with_entities(models.Prediction.fixed_acidity,
                       models.Prediction.volatile_acidity,
                       models.Prediction.citric_acid,
                       models.Prediction.sulfur_dioxide,
                       models.Prediction.pH,
                       models.Prediction.alcohol)\
        .filter(models.Prediction.heure >= time).all()