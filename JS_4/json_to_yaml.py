import json
import yaml

#''' --> multiline string

json_string = '''
{
  "interface": "GigabitEthernet0/0",
  "ip": "192.168.1.1",
  "status": "up"
}
'''

# JSON string → dict
# json.loads(...) betekent: load string.
# dict is een key value structuur

json_dict = json.loads(json_string)

# dict → YAML string
# yaml.dump(...) neemt een Python object (hier: dict) en maakt daar een YAML tekstrepresentatie van.
yaml_string = yaml.dump(json_dict)

print(type(json_string))   # str
print(type(json_dict))     # dict
print(type(yaml_string))   # str

print("\nYAML output:\n")
print(yaml_string)

#JSON (tekst)
#   ↓ json.loads()
#Python dict  ←—— dit is json_dict
#   ↓ yaml.dump()
#YAML (tekst)
