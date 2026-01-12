import requests
import json

local_info = requests.get("https://ipinfo.io/json") 
local_info = local_info.text
local_info_dict = json.loads(local_info)
local_coordinate_info = local_info_dict.get("loc")
print(local_coordinate_info)
lat, lon = map(float, local_coordinate_info.split(","))
print(lat)
print(lon)