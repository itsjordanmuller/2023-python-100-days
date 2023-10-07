from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route("/")
def hello_world():
    blog_url = "https://api.npoint.io/2f41322a9185c7a94a7a"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
