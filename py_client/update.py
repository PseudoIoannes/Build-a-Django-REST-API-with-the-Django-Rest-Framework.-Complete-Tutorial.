import requests

endpoint = "http://127.0.0.1:8000/api/products/1/update/"

data = {"title":"Hello darkness my old friend"}

get_response = requests.put(endpoint, json=data)
print(get_response.json())
# print(get_response.status_code)