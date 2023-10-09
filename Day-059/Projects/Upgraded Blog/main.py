from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/5e6104dab7d489a76a57"
response = requests.get(blog_url)
all_posts = response.json()

# print(all_posts[0]["id"])
# print(all_posts[0]["body"])
# print(all_posts[0]["date"])
# print(all_posts[0]["title"])
# print(all_posts[0]["author"])
# print(all_posts[0]["subtitle"])
# print(all_posts[0]["image_alt"])
# print(all_posts[0]["image_url"])


@app.route("/")
def home_page():
    return render_template("index.html", posts=all_posts)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


@app.route("/post/<num>")
def post_page(num):
    return render_template("post.html")


if __name__ == "__main__":
    app.run(debug=True)
