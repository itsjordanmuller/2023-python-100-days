import os
import requests
from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


def get_all_products():
    response = requests.get("https://fakestoreapi.com/products")
    return response.json() if response.status_code == 200 else []


def get_categories():
    response = requests.get("https://fakestoreapi.com/products/categories")
    return response.json() if response.status_code == 200 else []


@app.route("/", methods=["GET"])
def home():
    products = get_all_products()
    categories = get_categories()

    return render_template("index.html", products=products, categories=categories)


if __name__ == "__main__":
    app.run(debug=True, port=3000)
