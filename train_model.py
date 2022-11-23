import pandas as pd 
from sklearn.linear_model import LinearRegression
import joblib

def build_model():
    df = pd.read_csv('data/training/houses.csv')
    X = df[['size', 'nb_rooms', 'garden']]
    y = df['price']
    model = LinearRegression()
    model.fit(X.values, y.values)
    joblib.dump(model, "model/regression.joblib")
    
if __name__ == '__main__':
    build_model()
