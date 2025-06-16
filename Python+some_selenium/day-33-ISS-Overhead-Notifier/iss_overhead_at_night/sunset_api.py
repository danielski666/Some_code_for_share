import smtplib
import time

import requests
from datetime import datetime

# Bochnia LAT_LON
MAIL = "my_mail@mail.com"
PASS = "my_pass_to_login_to_mail"
parameters = {
    "lat": 49.96905,
    "lng": 20.43028,
    "formatted": 0
}


def is_iss_visible():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    json_response = response.json()

    longitude = float(json_response["iss_position"]["longitude"])
    latitude = float(json_response["iss_position"]["latitude"])

    iss_position = (longitude, latitude)
    print(iss_position)

    if parameters["lng"] - 5 <= longitude <= parameters["lng"] + 5 and \
            parameters["lat"] - 5 <= latitude <= parameters["lat"] + 5:
        return True
    else:
        return False


def is_night():
    res = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    res.raise_for_status()
    json_res = res.json()

    sunrise = json_res["results"]["sunrise"]
    sunset = json_res["results"]["sunset"]
    print(sunrise)
    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])
    print(sunrise_hour)
    time_now = datetime.now().hour

    if time_now >= sunset_hour or time_now <= sunrise_hour:
        return True


while True:
    if is_iss_visible() and is_night():
        # connection = smtplib.SMTP("smtp.gmail.com")
        # connection.starttls()
        # connection.login(MAIL, PASS)
        # connection.sendmail(
        #     from_addr="MAIL",
        #     to_addrs="MAIL",
        #     msg="Subject:Look UP!\n\nThe ISS is above you in the sky."
        #)
        pass

    time.sleep(60)
