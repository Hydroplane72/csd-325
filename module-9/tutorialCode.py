import requests
import json

response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)
print(json.dumps(response.json(), sort_keys=True, indent=4))