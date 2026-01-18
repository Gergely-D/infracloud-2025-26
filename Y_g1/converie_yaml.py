import yaml
import json

# -------- Bestanden ----------
YAML_INPUT_FILE = "input.yaml"
JSON_OUTPUT_FILE = "output.json"

# -------- YAML lezen ----------
with open(YAML_INPUT_FILE, "r") as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

# -------- JSON schrijven ----------
with open(JSON_OUTPUT_FILE, "w") as json_file:
    json.dump(yaml_data, json_file, indent=2)

print(f"Conversie voltooid: {YAML_INPUT_FILE} → {JSON_OUTPUT_FILE}")