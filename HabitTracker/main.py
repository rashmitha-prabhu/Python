import requests
import datetime as dt
import os

USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
GRAPH = "study"
headers = {
    "X-USER-TOKEN": TOKEN
}

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# ----- Create User -----
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# ----- Create Graph -----
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config = {
#     "id": GRAPH,
#     "name": "Study Tracker",
#     "unit": "hours",
#     "type": "float",
#     "color": "sora",
# }
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# ----- Delete Graph -----
# response = requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/study", headers=headers)
# print(response.text)


# ----- Add Pixels -----
today = dt.datetime.now()

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "7",
}

response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

# ----- Update Pixels -----

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"
date = dt.datetime.now().strftime("%Y%m%d")
update_config = {
    "quantity": "14"
}
update = requests.put(url=f"{update_pixel_endpoint}/{date}", json=update_config, headers=headers)
print(update.text)


# ----- Delete Pixels -----
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"
date = dt.datetime.now().strftime("%Y%m%d")
delete = requests.delete(url=f"{delete_pixel_endpoint}/{date}", headers=headers)
print(delete.text)
