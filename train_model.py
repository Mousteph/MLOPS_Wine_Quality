import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
import joblib
    
def build_model(path: str):
    """Train model and save it as a joblib file in model folder as wine_class.joblib

    Args:
        path (str): Path to dataset
    """
    
    df = pd.read_pickle(path)
    y = df.quality
    X = df.drop(columns=["quality"])
    model = RandomForestClassifier(n_estimators=60)
    model.fit(X.values, y.values)
    joblib.dump(model, "model/wine_class.joblib")
    
if __name__ == '__main__':
    build_model("data/training/wine.pkl")
