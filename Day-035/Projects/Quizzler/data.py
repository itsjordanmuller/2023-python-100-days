import requests


def get_question_data(difficulty="medium"):
    parameters = {"amount": 10, "type": "boolean", "difficulty": difficulty}

    response = requests.get("https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()

    print(f"API Request URL: {response.url}")

    data = response.json()

    return data["results"]
