from flask import Flask, render_template
import random
import datetime
import requests
import json
import os

app = Flask(__name__)


@app.route("/")
def hello_world():
    random_number = random.randint(1, 10)
    today = datetime.date.today()
    year = today.year
    return render_template("index.html", num=random_number, year=year)


def get_data_from_api(name):
    data = {}

    ageResponse = requests.get(f"https://api.agify.io?name={name}")
    if ageResponse.status_code == 200:
        ageAPIData = ageResponse.json()
        data["age"] = ageAPIData["age"]

    genderResponse = requests.get(f"https://api.genderize.io?name={name}")
    if genderResponse.status_code == 200:
        genderAPIData = genderResponse.json()
        data["gender"] = genderAPIData["gender"]

    return data


@app.route("/guess/<name>")
def guess(name):
    filename = "data.json"

    if os.path.exists(filename):
        with open(filename, "r") as file:
            data = json.load(file)
    else:
        data = {}

    if name in data:
        print(f"Data for {name} found in JSON file")
        ageData = data[name]["age"]
        genderData = data[name]["gender"]
    else:
        print(f"Data for {name} not found in JSON file, making API call")
        api_data = get_data_from_api(name)
        ageData = api_data["age"]
        genderData = api_data["gender"]

        data[name] = api_data

        with open(filename, "w") as file:
            json.dump(data, file, indent=2, sort_keys=True)

    return render_template(
        "demographics.html", name=name, gender=genderData, age=ageData
    )


@app.route("/blog/<num>")
def get_blog(num):
    number = int(num)
    blog_url = "https://api.npoint.io/2f41322a9185c7a94a7a"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts, number=number)


if __name__ == "__main__":
    app.run(debug=True)
