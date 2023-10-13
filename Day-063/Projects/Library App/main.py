from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    all_books = Book.query.all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book_details = {
            "name": request.form.get("name"),
            "author": request.form.get("author"),
            "rating": request.form.get("rating"),
        }
        # all_books.append(book_details)
        # print(all_books)
        with app.app_context():
            new_book = Book(
                title=book_details["name"],
                author=book_details["author"],
                rating=book_details["rating"],
            )
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = Book.query.get_or_404(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))
    book_id = request.args.get("id")
    book_selected = Book.query.get_or_404(book_id)
    return render_template("edit.html", book=book_selected)


if __name__ == "__main__":
    app.run(debug=True)
