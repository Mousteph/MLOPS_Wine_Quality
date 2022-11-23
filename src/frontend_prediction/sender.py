import json
import requests
import os

# BASE_URL = "http://backendprediction:80"
BASE_URL = f"http://{os.environ.get('HOST_B')}:{os.environ.get('PORT_B')}"


def _request_deco(method):
    def wrapper(*args, **kwargs):
        try:
            response = method(*args, **kwargs)
            if response.status_code != 200:
                return {
                    "status": 0,
                    "message": f"Error, status code: {response.status_code}",
                    "data": None
                }
            return response.json()
        
        except Exception as e:
            print(f"ERROR: {__file__} | {e}", flush=True)
            return {
                    "status": 0,
                    "message": "Streamlit Internal Error",
                    "data": None
                }
    return wrapper

@_request_deco
def _post_request(url, data):
    return requests.post(BASE_URL + url, json=data)

@_request_deco
def _get_request(url):
    return requests.get(BASE_URL + url)

def get_prediction(json: dict):
    return _post_request("/predict", json)
