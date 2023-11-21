import os
import requests
from datetime import datetime
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Pixela API base endpoint
pixela_endpoint = "https://pixe.la/v1/users"

# User credentials and graph ID
USERNAME = "itsjordanmuller"
TOKEN_KEY = os.getenv("PIXELA_TOKEN_KEY")
TEST_GRAPH_ID = "testhabittracker"

# User registration parameters
user_params = {
    "token": TOKEN_KEY,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Graph endpoint URL
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Graph configuration settings
graph_config = {
    "id": TEST_GRAPH_ID,
    "name": "Test Habit Tracker",
    "unit": "successes",
    "type": "int",
    "color": "ajisai",
}

# Headers for authentication
headers = {"X-USER-TOKEN": TOKEN_KEY}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# Specific endpoint for the test graph
test_graph_endpoint = f"{graph_endpoint}/{TEST_GRAPH_ID}"

# Get current date in Pixela format
today = datetime.now().strftime("%Y%m%d")
# print(today)

# Configuration for adding a pixel
pixel_config = {
    "date": today,
    "quantity": "1",
}

# response = requests.post(url=test_graph_endpoint, json=pixel_config, headers=headers)

# URL for today's pixel data in the test graph
today_test_graph_pixels = f"{test_graph_endpoint}/{today}"

# response = requests.delete(url=today_test_graph_pixels, headers=headers)

# Configuration for updating a pixel
update_config = {"date": today, "quantity": "2"}

# response = requests.put(
#     url=today_test_graph_pixels, json=update_config, headers=headers
# )
