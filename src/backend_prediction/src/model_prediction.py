import joblib
from typing import Tuple, List

class ModelPrediction:
    def __init__(self, model_path: str):
        """Init ModelPrediction class

        Args:
            model_path (str): Model path
        """
        
        self.model = joblib.load(model_path)

    def prediction(self, x: List) -> Tuple:
        """Return prediction from model

        Args:
            x (List): Input data

        Returns:
            Tuple: Tuple of (bool, prediction), True if success, False if error
        """
        
        try:
            return True, self.model.predict(x)

        except Exception as e:
            print(f"{__file__} ERROR: {e}")
            return False, e
