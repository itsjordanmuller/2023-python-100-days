import os
import requests
from dotenv import load_dotenv

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "itsjordanmuller"
TOKEN_KEY = os.getenv("PIXELA_TOKEN_KEY")
TEST_GRAPH_ID = "testhabittracker"

user_params = {
    "token": TOKEN_KEY,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": TEST_GRAPH_ID,
    "name": "Test Habit Tracker",
    "unit": "successes",
    "type": "int",
    "color": "ajisai",
}

headers = {"X-USER-TOKEN": TOKEN_KEY}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

test_graph_endpoint = f"{graph_endpoint}/{TEST_GRAPH_ID}"

pixel_config = {
    "date": "20230917",
    "quantity": "1",
}

response = requests.post(url=test_graph_endpoint, json=pixel_config, headers=headers)
print(response.text)

# API Key Storage Test
# api_key = os.getenv("MY_TEST_KEY")
# print(api_key)
