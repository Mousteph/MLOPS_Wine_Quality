from . import crud, models
from .database import SessionLocal, engine
import pandas as pd

models.Base.metadata.create_all(bind=engine)

class ManagerPostgres:    
    def __init__(self):
        self.db = SessionLocal()
        
    def get_prediction(self, time: int):
        predictions = crud.get_predictions(self.db, time)
        return pd.DataFrame(predictions, columns =['size', 'nb_rooms', 'garden'])
        
        
    def close(self):
        self.db.close()