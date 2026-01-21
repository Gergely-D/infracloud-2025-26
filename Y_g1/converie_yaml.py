import yaml
import json

# -------- Bestanden ----------
YAML_INPUT_FILE = "input.yaml"
JSON_OUTPUT_FILE = "output.json"

# -------- YAML lezen ----------
with open(YAML_INPUT_FILE, "r") as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

# -------- JSON naar terminal ----------
print(json.dumps(yaml_data, indent=2))

print(f"Conversie voltooid: {YAML_INPUT_FILE} → json in terminal weergeven")

