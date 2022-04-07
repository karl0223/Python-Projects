import requests
from datetime import datetime
TOKEN = "qwertyuiop"
USER = "karl0223"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_end_point, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}"

today = datetime.now()
formatted_date = today.strftime("%Y%m%d")

pixel_graph_config = {
    "date": formatted_date,
    "quantity": "20",
}

response = requests.post(url=pixel_endpoint, json=pixel_graph_config, headers=headers)
print(response.text)

update_delete_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}/{formatted_date}"

update_config = {
    "quantity": "13"
}

# response = requests.put(url=pixel_update_endpoint, json=update_config, headers=headers)
# print(response.text)

# response = requests.delete(url=update_delete_endpoint, headers=headers)
# print(response.text)