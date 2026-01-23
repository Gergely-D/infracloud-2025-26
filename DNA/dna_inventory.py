#!/usr/bin/env python3
import requests

DNAC_HOST = "https://10.10.20.85"
USERNAME = "administrator"
PASSWORD = "Cisco1234!"

requests.packages.urllib3.disable_warnings()

# 1) Token ophalen
token_url = f"{DNAC_HOST}/dna/system/api/v1/auth/token"
r = requests.post(token_url, auth=(USERNAME, PASSWORD), verify=False)
r.raise_for_status()

token = r.json()["Token"]
print("Token obtained")

# 2) Inventory ophalen
headers = {"X-Auth-Token": token}
inv_url = f"{DNAC_HOST}/dna/intent/api/v1/network-device"

r2 = requests.get(inv_url, headers=headers, verify=False)
r2.raise_for_status()

devices = r2.json()["response"]

print("\nDNAC DEVICE INVENTORY:")
for d in devices:
    print(
        d.get("hostname"),
        d.get("managementIpAddress"),
        d.get("platformId"),
        d.get("softwareVersion")
    )
