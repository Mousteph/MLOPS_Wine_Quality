import argparse

import requests
import pandas as pd
import numpy as np

def get_bad_data(path: str) -> np.ndarray:
    """Generate bad data

    Args:
        path (str): Path to dataset

    Returns:
        np.ndarray: Array of bad data
    """
    
    data = pd.read_pickle(path).drop(columns=['quality'])
    data["volatile acidity"] = 3 + data["volatile acidity"]
    data["citric acid"] = 5 + data["citric acid"]
    data["alcohol"] = 20

    return data.values

def get_good_data(path: str) -> np.ndarray:
    """Generate normal data

    Args:
        path (str): Path to dataset

    Returns:
        np.ndarray: Array of normal data
    """
    
    data = pd.read_pickle(path).drop(columns=['quality'])
    return data.values

def get_noisy_data(path: str) -> np.ndarray:
    """Generate noisy data

    Args:
        path (str): Path to dataset

    Returns:
        np.ndarray: Array of noisy data
    """
    
    data = pd.read_pickle(path).drop(columns=['quality'])
    data[:data.shape[0] // 2] = data[:data.shape[0] // 2] + np.random.normal(0.1, 0.01, (data.shape[0] // 2,  data.shape[1]))
    return data.values

def send_data(data: np.ndarray):
    """Send data to backend

    Args:
        data (np.ndarray): Array of data
    """
    
    json = {"data": data.tolist()}
    requests.post("http://localhost:80/batch", json=json)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Send a batch of data to the backend.")
    parser.add_argument("data_type", choices=["corrupted", "normal", "noisy"], 
                        help="""Type of data to process:
                                - corrupted: data that do not respect the initial distribution
                                - normal: data that respect the initial distribution
                                - noisy: data that respect the initial distribution but with noise
                                """)

    args = parser.parse_args()

    path = "./data/training/wine.pkl"

    if args.data_type == "corrupted":
        data = get_bad_data(path)
    elif args.data_type == "normal":
        data = get_good_data(path)
    elif args.data_type == "noisy":
        data = get_noisy_data(path)

    send_data(data)
