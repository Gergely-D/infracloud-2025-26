import json
import requests
from config import ACCESS_TOKEN

room_id = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vZGE3ZGI2YTAtZjdmNy0xMWYwLTg5ZjItZTkyMjY3N2UwYzg1"
message = "Hello **DevNet Associates**!!"

url = "https://webexapis.com/v1/messages"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
}

payload = {"roomId": room_id, "markdown": message}
res = requests.post(url, headers=headers, json=payload, timeout=15)
print("Status:", res.status_code)
print(json.dumps(res.json(), indent=2))
