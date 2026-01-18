import requests
import json

# -------- Configuratie ----------
WEBEX_ACCESS_TOKEN = "<Vul hier je access token in>"
WEBEX_ROOMS_URL = "https://api.ciscospark.com/v1/rooms"

REQUEST_HEADERS = {
    "Authorization": f"Bearer {WEBEX_ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# -------- API-call: Webex rooms ophalen --------
rooms_response = requests.get(WEBEX_ROOMS_URL, headers=REQUEST_HEADERS)
rooms_json = rooms_response.json()  # JSON response

# -------- Filter: enkel rooms met 'KVR' in de titel --------
kvr_rooms = [
    room for room in rooms_json.get("items", [])
    if "KVR" in room.get("title", "")
]

# -------- Resultaten afdrukken --------
print("Gefilterde Webex Rooms (KVR):")
for room in kvr_rooms:
    print(f"- {room['title']} (Room ID: {room['id']})")