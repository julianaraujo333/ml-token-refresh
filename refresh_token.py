import requests
import json
import os
from datetime import datetime

print("ENV OK:", os.environ.get("ML_CLIENT_ID") is not None)

url = "https://api.mercadolibre.com/oauth/token"

data = {
    "grant_type": "refresh_token",
    "client_id": os.environ["ML_CLIENT_ID"],
    "client_secret": os.environ["ML_CLIENT_SECRET"],
    "refresh_token": os.environ["ML_REFRESH_TOKEN"]
}

response = requests.post(url, data=data)
print("STATUS:", response.status_code)
print("BODY:", response.text)

response.raise_for_status()
res = response.json()

with open("token.json", "w") as f:
    json.dump(res, f)
