import json
import yaml

json_string = '''
{
  "interface": "GigabitEthernet0/0",
  "ip": "192.168.1.1",
  "status": "up"
}
'''

# JSON string → dict
json_dict = json.loads(json_string)

# dict → YAML string
yaml_string = yaml.dump(json_dict)

print(type(json_string))   # str
print(type(json_dict))     # dict
print(type(yaml_string))   # str

print("\nYAML output:\n")
print(yaml_string)