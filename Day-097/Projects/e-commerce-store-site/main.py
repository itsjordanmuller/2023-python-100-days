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


def get_all_categories():
    response = requests.get("https://fakestoreapi.com/products/categories")
    return response.json() if response.status_code == 200 else []


def get_all_carts():
    response = requests.get("https://fakestoreapi.com/carts")
    return response.json() if response.status_code == 200 else []


def get_all_users():
    response = requests.get("https://fakestoreapi.com/users")
    return response.json() if response.status_code == 200 else []


@app.route("/", methods=["GET"])
def home():
    products = get_all_products()
    categories = get_all_categories()

    return render_template("index.html", products=products, categories=categories)


@app.route("/product/<int:product_id>", methods=["GET"])
def product_details(product_id):
    response = requests.get(f"https://fakestoreapi.com/products/{product_id}")
    product = response.json() if response.status_code == 200 else None
    return render_template("details.html", product=product)


@app.route("/category/<string:category_name>", methods=["GET"])
def category(category_name):
    response = requests.get(
        f"https://fakestoreapi.com/products/category/{category_name}"
    )
    products = response.json() if response.status_code == 200 else []
    return render_template(
        "index.html", products=products, categories=get_all_categories()
    )


if __name__ == "__main__":
    app.run(debug=True, port=3000)
