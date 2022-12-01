from . import crud, models, schemas
from .database import SessionLocal, engine
from typing import List
import time

models.Base.metadata.create_all(bind=engine)

class ManagerPostgres:    
    def __init__(self):
        self.db = SessionLocal()
    
    def add_new_prediction(self, x: List[float], y: int):
        user = schemas.PredictionCreate(features=x, quality=y, heure=time.time())
        crud.add_prediction(self.db, user)
        
    def close(self):
        self.db.close()