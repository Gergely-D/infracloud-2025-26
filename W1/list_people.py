import json
import requests
from config import ACCESS_TOKEN, PERSON_EMAIL_TO_LOOKUP

base = "https://webexapis.com/v1"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
}

# Step 2: List People by email
res = requests.get(
    f"{base}/people",
    headers=headers,
    params={"email": PERSON_EMAIL_TO_LOOKUP},
    timeout=15,
)
print("LIST PEOPLE status:", res.status_code)
data = res.json()
print(json.dumps(data, indent=4))

# Step 3: Get Person details by ID (if found)
items = data.get("items") or []
if not items:
    print("\nNo people found for that email. Update PERSON_EMAIL_TO_LOOKUP in config.py.")
    raise SystemExit(1)

person_id = items[0].get("id")
print("\nUsing person_id:", person_id)

res2 = requests.get(f"{base}/people/{person_id}", headers=headers, timeout=15)
print("GET PERSON status:", res2.status_code)
print(json.dumps(res2.json(), indent=4))
