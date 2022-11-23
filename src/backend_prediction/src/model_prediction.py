import joblib
import sklearn

class ModelPrediction:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def prediction(self, x):
        try:
            return self.model.predict(x)

        except Exception as e:
            print(f"{__file__} ERROR: {e}")
            return None
