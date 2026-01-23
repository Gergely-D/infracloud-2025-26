from flask import Flask, request, jsonify, render_template
import subprocess
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "OK - AP6 running. Open /form/loopback"

@app.route("/form/loopback", methods=["GET"])
def form_loopback():
    return render_template("loopback_form.html")

@app.route("/form/loopback", methods=["POST"])
def create_loopback_from_form():
    name = request.form.get("name")
    ip = request.form.get("ip")
    netmask = request.form.get("netmask")

    if not name or not ip or not netmask:
        return jsonify(error="Missing form fields"), 400

    payload = {
        "ietf-interfaces:interface": {
            "name": name,
            "description": "Created via Form + Curl (AP6)",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [{"ip": ip, "netmask": netmask}]
            }
        }
    }

    curl_cmd = [
        "curl", "-k", "-i", "-X", "POST",
        "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces",
        "-H", "Content-Type: application/yang-data+json",
        "-H", "Accept: application/yang-data+json",
        "-u", "cisco:cisco123!",
        "-d", json.dumps(payload)
    ]

    result = subprocess.run(curl_cmd, capture_output=True, text=True)

    return jsonify(
        ok=True,
        message="Loopback created via FORM + curl (AP6)",
        interface=name,
        ip_address=ip,
        curl_output=result.stdout
    ), 201

if __name__ == "__main__":
    print(app.url_map)
    app.run(host="0.0.0.0", port=5000)
    