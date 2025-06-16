import requests

res = requests.get(url="http://api.open-notify.org/iss-now.json")
json_res = res.json()

longitude = json_res["iss_position"]["longitude"]
latitude = json_res["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)