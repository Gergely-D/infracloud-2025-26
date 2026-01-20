#!/usr/bin/env python3
import json
import sys
import requests

# Disable SSL warnings (lab uses self-signed/no cert validation)
requests.packages.urllib3.disable_warnings()

HOST = "192.168.56.102"
USER = "cisco"
PASS = "cisco123!"

HEADERS = {
    "Accept": "application/yang-data+json",
    "Content-type": "application/yang-data+json",
}

BASE = f"https://{HOST}/restconf"


def pretty(obj) -> str:
    return json.dumps(obj, indent=4)


def http_ok(resp: requests.Response) -> bool:
    return 200 <= resp.status_code <= 299


def die(msg: str, code: int = 1):
    print(msg)
    sys.exit(code)


def get_json(url: str):
    resp = requests.get(url, auth=(USER, PASS), headers=HEADERS, verify=False)
    print(f"GET {url} -> {resp.status_code}")

    if not http_ok(resp):
        # Try to print server JSON error (if any)
        try:
            return die(f"ERROR: {resp.status_code}\n{pretty(resp.json())}")
        except Exception:
            return die(f"ERROR: {resp.status_code}\n{resp.text}")

    try:
        return resp.json()
    except Exception:
        die(f"ERROR: Response is not JSON\n{resp.text}")


def put_json(url: str, payload: dict):
    resp = requests.put(
        url,
        data=json.dumps(payload),
        auth=(USER, PASS),
        headers=HEADERS,
        verify=False,
    )
    print(f"PUT {url} -> {resp.status_code}")

    if http_ok(resp):
        print("STATUS OK")
        # Many RESTCONF PUTs return empty body; print if present
        if resp.text.strip():
            try:
                print(pretty(resp.json()))
            except Exception:
                print(resp.text)
        return

    # Error path
    try:
        die(f"ERROR: {resp.status_code}\n{pretty(resp.json())}")
    except Exception:
        die(f"ERROR: {resp.status_code}\n{resp.text}")


def main():
    # (Optional) Basic RESTCONF reachability test
    root_url = f"{BASE}/"
    root = get_json(root_url)
    print("\nRESTCONF ROOT:")
    print(pretty(root))

    # GET all interfaces
    interfaces_url = f"{BASE}/data/ietf-interfaces:interfaces"
    interfaces = get_json(interfaces_url)
    print("\nALL INTERFACES:")
    print(pretty(interfaces))

    # GET specific interface (GigabitEthernet1)
    gi1_url = f"{BASE}/data/ietf-interfaces:interfaces/interface=GigabitEthernet1"
    gi1 = get_json(gi1_url)
    print("\nGigabitEthernet1:")
    print(pretty(gi1))

    # PUT create Loopback2 (as per lab)
    loop2_url = f"{BASE}/data/ietf-interfaces:interfaces/interface=Loopback2"
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

    print("\nCREATING Loopback2...")
    put_json(loop2_url, yangConfig)

    # Verify again
    interfaces_after = get_json(interfaces_url)
    print("\nALL INTERFACES (AFTER PUT):")
    print(pretty(interfaces_after))


if __name__ == "__main__":
    main()
