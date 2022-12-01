import requests
import pandas as pd

def get_data(path):
    data = pd.read_pickle(path).drop(columns=['quality'])
    data["volatile acidity"] = 3 + data["volatile acidity"]
    data["citric acid"] = 5 + data["citric acid"]
    data["alcohol"] = 20

    return data.values

def send_data(data):
    json = {"data": data.tolist()}
    requests.post("http://localhost:80/batch", json=json)

if __name__ == '__main__':
    path = "./data/training/wine.pkl"
    data = get_data(path)
    send_data(data)
