import os
import requests
from dotenv import load_dotenv

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "itsjordanmuller"
TOKEN_KEY = os.getenv("PIXELA_TOKEN_KEY")

user_params = {
    "token": TOKEN_KEY,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# API Key Storage Test
# api_key = os.getenv("MY_TEST_KEY")
# print(api_key)
