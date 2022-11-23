import requests


if __name__ == '__main__':
    myobj = {'data': [1, 2, 1]}

    response = requests.post("http://127.0.0.1:80/predict", json=myobj)
    print(response.json())

