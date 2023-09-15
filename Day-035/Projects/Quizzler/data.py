import requests


def get_categories():
    response = requests.get("https://opentdb.com/api_category.php")
    response.raise_for_status()

    data = response.json()
    categories = {item["name"]: item["id"] for item in data["trivia_categories"]}
    return categories


def get_question_data(difficulty="medium", category_id=None):
    parameters = {"amount": 10, "type": "boolean", "difficulty": difficulty}
    if category_id:
        parameters["category"] = category_id

    response = requests.get("https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()

    print(f"API Request URL: {response.url}")

    data = response.json()

    return data["results"]
