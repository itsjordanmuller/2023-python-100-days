from flask import Flask, render_template
import random
import datetime
import requests
import json

app = Flask(__name__)


@app.route("/")
def hello_world():
    random_number = random.randint(1, 10)
    today = datetime.date.today()
    year = today.year
    return render_template("index.html", num=random_number, year=year)


@app.route("/guess/<name>")
def guess(name):
    nameData = name

    ageResponse = requests.get(f"https://api.agify.io?name={nameData}")
    if ageResponse.status_code == 200:
        ageAPIData = ageResponse.json()
        ageData = ageAPIData["age"]

    genderResponse = requests.get(f"https://api.genderize.io?name={nameData}")
    if genderResponse.status_code == 200:
        genderAPIData = genderResponse.json()
        genderData = genderAPIData["gender"]

    return render_template(
        "demographics.html", name=nameData, gender=genderData, age=ageData
    )


if __name__ == "__main__":
    app.run(debug=True)
