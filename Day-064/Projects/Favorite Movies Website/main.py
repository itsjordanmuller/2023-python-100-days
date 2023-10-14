import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-collection.db"
db.init_app(app)

Bootstrap5(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.Text, nullable=True)
    img_url = db.Column(db.String(500), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        movie_details = {
            "title": request.form.get("title"),
            "year": request.form.get("year"),
            "description": request.form.get("description"),
            "rating": request.form.get("rating"),
            "ranking": request.form.get("ranking"),
            "review": request.form.get("review"),
            "imageURL": request.form.get("imageURL"),
        }
        with app.app_context():
            new_movie = Movie(
                title=movie_details["title"],
                year=movie_details["year"],
                description=movie_details["description"],
                rating=movie_details["rating"],
                ranking=movie_details["ranking"],
                review=movie_details["review"],
                img_url=movie_details["imageURL"],
            )
            db.session.add(new_movie)
            print("Movie Added!")
            db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
