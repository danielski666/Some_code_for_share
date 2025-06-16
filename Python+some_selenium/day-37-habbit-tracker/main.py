import datetime

import requests
USERNAME = "myname123"
MY_TOKEN = "pixelaTokenForLearning1249682"
PIX_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIX_ENDPOINT}/{USERNAME}/graphs"
PIXEL_ENDPOINT = f"{PIX_ENDPOINT}/{USERNAME}/graphs/id{USERNAME}"
user_params = {
    "token": MY_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
graph_config = {
    "id": f"id{USERNAME}",
    "name": "APP Working on",
    "unit": "commit",
    "type": "int",
    "color": "shibafu"
}
today = datetime.datetime.now().strftime("%Y%m%d")
pixel_config = {
    "date": (str(datetime.date.today())).replace('-', ''), #today
    "quantity": "5",
    #"optionalData": "Optional comment"
}

headers = {
    "X-USER-TOKEN": MY_TOKEN,
}
# response = requests.post(url=PIX_ENDPOINT, json=user_params)
# print(response.text)

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

response = requests.post(url=PIXEL_ENDPOINT, json=pixel_config, headers=headers)
print(response.text)