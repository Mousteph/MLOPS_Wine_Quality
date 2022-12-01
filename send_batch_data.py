import sys

import requests
import pandas as pd
import numpy as np

def get_bad_data(path):
    data = pd.read_pickle(path).drop(columns=['quality'])
    data["volatile acidity"] = 3 + data["volatile acidity"]
    data["citric acid"] = 5 + data["citric acid"]
    data["alcohol"] = 20

    return data.values

def get_good_data(path):
    data = pd.read_pickle(path).drop(columns=['quality'])
    return data.values

def get_noisy_data(path):
    data = pd.read_pickle(path).drop(columns=['quality'])
    data[:data.shape[0] // 2] = data[:data.shape[0] // 2] + np.random.normal(0.1, 0.01, (data.shape[0] // 2,  data.shape[1]))
    return data.values

def send_data(data):
    json = {"data": data.tolist()}
    requests.post("http://localhost:80/batch", json=json)

if __name__ == '__main__':
    arg = sys.argv
    
    if len(arg) != 2:
        exit(0)
    
    path = "./data/training/wine.pkl"
    if arg[1] == "corrupted":
        data = get_bad_data(path)
    
    elif arg[1] == "normal":
        data = get_good_data(path)
        
    elif arg[1] == "noisy":
        data = get_noisy_data(path)
    
    send_data(data)
