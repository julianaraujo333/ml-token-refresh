import requests
import json
import os
from datetime import datetime


url = "https://api.mercadolibre.com/oauth/token"

data = {
    "grant_type": "refresh_token",
    "client_id":  os.environ["ML_CLIENT_ID"],
    "client_secret": os.environ["ML_CLIENT_SECRET"],
    "refresh_token": os.environ["ML_REFRESH_TOKEN"]
}

r = requests.post(url, data=data)
r.raise_for_status()
res = r.json()

with open("token.json", "w") as f:
    json.dump({
        "access_token": res["access_token"],
        "refresh_token": res["refresh_token"],
        "updated_at": datetime.utcnow().isoformat()
    }, f)
