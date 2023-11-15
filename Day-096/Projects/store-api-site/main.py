import os
import requests
from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


@app.route("/", methods=["GET"])
def home():
    response = requests.get("https://fakestoreapi.com/products")
    if response.status_code == 200:
        products = response.json()
        return render_template("index.html", products=products)
    else:
        return "Failed to fetch data", response.status_code


if __name__ == "__main__":
    app.run(debug=True, port=3000)
