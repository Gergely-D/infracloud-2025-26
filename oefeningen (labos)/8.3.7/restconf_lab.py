import json
import requests

requests.packages.urllib3.disable_warnings()

HOST = "192.168.56.102"
BASE = f"https://{HOST}/restconf"
AUTH = ("cisco", "cisco123!")
HEADERS = {
    "Accept": "application/yang-data+json",
    "Content-type": "application/yang-data+json",
}

def show_response(resp, label):
    print(f"\n{label} -> {resp.status_code}")
    ctype = resp.headers.get("Content-Type", "")
    print(f"Content-Type: {ctype}")

    try:
        data = resp.json()
        print(json.dumps(data, indent=4))
    except ValueError:
        print("ERROR: Response body is not valid JSON:")
        print(resp.text)

# 1) RESTCONF root (optioneel, maar jij deed dit al)
resp = requests.get(f"{BASE}/", auth=AUTH, headers=HEADERS, verify=False)
show_response(resp, f"GET {BASE}/restconf/")

# 2) GET alle interfaces
api_url = f"{BASE}/data/ietf-interfaces:interfaces"
resp = requests.get(api_url, auth=AUTH, headers=HEADERS, verify=False)
show_response(resp, f"GET {api_url}")

# 3) PUT Loopback2 (zoals in de lab)
put_url = f"{BASE}/data/ietf-interfaces:interfaces/interface=Loopback2"
yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback2",
        "description": "My second RESTCONF loopback",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {"ip": "10.2.1.1", "netmask": "255.255.255.0"}
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

resp = requests.put(
    put_url,
    data=json.dumps(yangConfig),
    auth=AUTH,
    headers=HEADERS,
    verify=False
)
show_response(resp, f"PUT {put_url}")
