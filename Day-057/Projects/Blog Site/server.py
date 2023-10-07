from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

blog_url = "https://api.npoint.io/2f41322a9185c7a94a7a"
response = requests.get(blog_url)
all_posts = response.json()


@app.route("/")
def hello_world():
    return render_template("index.html", posts=all_posts)


@app.route("/posts/<id>")
def blog_post(id):
    postID = int(id) - 1
    return render_template("post.html", posts=all_posts, postID=postID)


if __name__ == "__main__":
    app.run(debug=True)
