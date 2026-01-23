import json
import requests
from config import ACCESS_TOKEN

url = "https://webexapis.com/v1/people/me"
headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

res = requests.get(url, headers=headers, timeout=15)
print("Status:", res.status_code)
print(json.dumps(res.json(), indent=4))
