import os
import requests
from dotenv import load_dotenv

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"

token_key = os.getenv("PIXELA_TOKEN_KEY")

user_params = {
    "token": token_key,
    "username": "itsjordanmuller",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# requests.post()

# API Key Storage Test
# api_key = os.getenv("MY_TEST_KEY")
# print(api_key)
