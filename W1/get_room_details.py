import json
import requests
from config import ACCESS_TOKEN

room_id = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vZGE3ZGI2YTAtZjdmNy0xMWYwLTg5ZjItZTkyMjY3N2UwYzg1"

url = f"https://webexapis.com/v1/rooms/{room_id}/meetingInfo"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
}

res = requests.get(url, headers=headers, timeout=15)
print("Status:", res.status_code)
print(json.dumps(res.json(), indent=2))
