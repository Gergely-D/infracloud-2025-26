import json
import requests
from config import ACCESS_TOKEN

url = "https://webexapis.com/v1/rooms"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
}

res = requests.get(url, headers=headers, params={"max": "100"}, timeout=15)
print("Status:", res.status_code)
print(json.dumps(res.json(), indent=2))
