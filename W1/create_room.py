import json
import requests
from config import ACCESS_TOKEN, ROOM_TITLE

url = "https://webexapis.com/v1/rooms"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
}

payload = {"title": ROOM_TITLE}
res = requests.post(url, headers=headers, json=payload, timeout=15)
print("Status:", res.status_code)
data = res.json()
print(json.dumps(data, indent=2))

room_id = data.get("id")
if room_id:
    print("\nROOM_ID (save this for next steps):", room_id)
else:
    print("\nNo room id returned. Check token/permissions.")
