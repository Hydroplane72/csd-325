import requests
import json

response = requests.get("https://swapi.dev/api/planets/1/")
print("Status Code: "+ str(response.status_code))
print("Unformattted JSON")
print(response.json())
print("Formatted JSON")
print(json.dumps(response.json(), sort_keys=True, indent=4))