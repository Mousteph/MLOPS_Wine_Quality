from . import crud, models
from .database import SessionLocal, engine
import pandas as pd

models.Base.metadata.create_all(bind=engine)

class ManagerPostgres:    
    def __init__(self):
        self.db = SessionLocal()
        self.columns = ["fixed acidity", "volatile acidity",
                        "citric acid", "total sulfur dioxide",
                        "pH", "alcohol"]
        
    def get_prediction(self, time: int) -> pd.DataFrame:
        """Return predictions from database

        Args:
            time (int): Time to filter predictions

        Returns:
            pd.DataFrame: Return a dataframe with predictions
        """
        
        predictions = crud.get_predictions(self.db, time)
        return pd.DataFrame(predictions, columns=self.columns)
        
    def close(self):
        """Close database connection
        """
        
        self.db.close()