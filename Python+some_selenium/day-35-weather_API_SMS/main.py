import requests
from twilio.rest import Client
API_KEY = "278407dfe11a2ffcb8191812249abe13"
API_URL = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "This will be an ID for those API"
auth_token = "This will be the password for those API"

weather_params = {
    "lat": 49.96905,
    "lon": 20.43028,
    "cnt": 4,
    "units": "metric",
    "appid": API_KEY,

}

request = requests.get(url=API_URL, params=weather_params)
request.raise_for_status()

print(request)
weather_data = request.json()
data_list = weather_data["list"]
will_rain = False
for i in range(len(weather_data["list"])):
    if weather_data["list"][i]["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(username=account_sid, password=auth_token)
    message = client.messages.create(
                            body="It's Raining Today. Take the umbrella.",
                            from_="Gained number for API",
                            to="ANY PROVIDED and VERIFIED NUMBER"
                                    )
    print(message.status)




