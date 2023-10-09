from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")


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
