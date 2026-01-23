#!/usr/bin/env python3
"""
Js3 - Filteren van JSON met Python (netwerkapplicatie)
Gebaseerd op DNAC / Catalyst Center inventory JSON (slides).
"""

import json

# Open lokaal JSON-bestand (opgeslagen API-output)
with open("dnac_inventory.json", "r") as f:
    data = json.load(f)

# DNAC inventory staat onder de key "response"
devices = data["response"]

print("Hostname | IP Address | MAC | Software")

for dev in devices:
    hostname = dev.get("hostname")
    ip = dev.get("managementIpAddress")
    mac = dev.get("macAddress")
    sw_type = dev.get("softwareType")
    sw_ver = dev.get("softwareVersion")

    print(f"{hostname} | {ip} | {mac} | {sw_type} {sw_ver}")
