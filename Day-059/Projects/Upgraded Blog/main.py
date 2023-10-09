from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)

blog_url = "https://api.npoint.io/5e6104dab7d489a76a57"
response = requests.get(blog_url)
all_posts = response.json()


@app.context_processor
def inject_current_year():
    current_year = datetime.datetime.now().year
    return {"current_year": current_year}


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
    id = int(num) - 1
    return render_template("post.html", posts=all_posts, postID=id)


if __name__ == "__main__":
    app.run(debug=True)
