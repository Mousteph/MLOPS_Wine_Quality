import pandas as pd 
from sklearn.linear_model import LinearRegression
import joblib

def build_model():
    df = pd.read_csv('houses.csv')
    X = df[['size', 'nb_rooms', 'garden']]
    y = df['price']
    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, "regression.joblib")
    
if __name__ == '__main__':
    build_model()
