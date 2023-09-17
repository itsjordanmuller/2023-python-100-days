import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("MY_TEST_KEY")

print(api_key)
