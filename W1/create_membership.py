import json
import requests
from config import ACCESS_TOKEN, MEMBER_EMAIL_TO_ADD

room_id = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vZGE3ZGI2YTAtZjdmNy0xMWYwLTg5ZjItZTkyMjY3N2UwYzg1"

url = "https://webexapis.com/v1/memberships"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
}

payload = {"roomId": room_id, "personEmail": MEMBER_EMAIL_TO_ADD}
res = requests.post(url, headers=headers, json=payload, timeout=15)
print("Status:", res.status_code)
print(json.dumps(res.json(), indent=2))
