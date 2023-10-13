from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

all_books = []


@app.route("/")
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book_details = {
            "name": request.form.get("name"),
            "author": request.form.get("author"),
            "rating": request.form.get("rating"),
        }
        all_books.append(book_details)
        print(all_books)
        return redirect(url_for("home"))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
