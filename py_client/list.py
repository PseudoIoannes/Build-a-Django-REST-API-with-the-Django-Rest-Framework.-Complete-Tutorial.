import requests
from getpass import getpass


auth_endpoint = "http://127.0.0.1:8000/api/auth/"
password = getpass()

auth_response = requests.get(auth_endpoint, json={"username":"cfe", "password": password})
print(auth_response.json())


if auth_response.status_code == 200:
    token = auth_response.json()["token"]
    headers = {
        "Authorization":f"Token {token}"
    }
    endpoint = "http://127.0.0.1:8000/api/products/"

    data = {"title": "Sample title"}
    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())