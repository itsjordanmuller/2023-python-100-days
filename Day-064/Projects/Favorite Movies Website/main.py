import os
import json
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
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


class movieForm(FlaskForm):
    rating = FloatField(
        "Your Rating Out of 10 (e.g. 7.5):", validators=[DataRequired()]
    )
    ranking = IntegerField("Your Ranking (1-10):", validators=[DataRequired()])
    review = StringField("Your Short Text Review: ", validators=[DataRequired()])
    submit = SubmitField("Submit")


class SearchForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Search")


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    movies = Movie.query.all()
    return render_template("index.html", movies=movies)


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


@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    movie = Movie.query.get(movie_id)
    if movie is None:
        return redirect(url_for("home"))

    form = movieForm()

    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        movie.ranking = form.ranking.data
        db.session.commit()
        print("Movie Updated!")
        return redirect(url_for("home"))

    form.rating.data = movie.rating
    form.review.data = movie.review
    form.ranking.data = movie.ranking

    return render_template("edit.html", form=form, movie=movie)


@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    movie = Movie.query.get(movie_id)
    if movie:
        db.session.delete(movie)
        db.session.commit()
        print(f"Movie ID {movie_id} Deleted!")
    return redirect(url_for("home"))


@app.route("/search", methods=["GET", "POST"])
def search():
    form = SearchForm()
    movies = []
    if form.validate_on_submit():
        url = f"https://api.themoviedb.org/3/search/movie?api_key={os.getenv('TMDB_KEY')}&query={form.title.data}"
        response = requests.get(url)
        data = response.json()
        movies = data["results"]

    return render_template("search.html", form=form, movies=movies)


@app.route("/select/<int:movie_id>")
def select(movie_id):
    url = (
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={os.getenv('TMDB_KEY')}"
    )
    response = requests.get(url)
    data = response.json()

    new_movie = Movie(
        title=data["title"],
        year=data["release_date"][:4],
        description=data["overview"],
        img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
    )

    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for("edit", movie_id=new_movie.id))


if __name__ == "__main__":
    app.run(debug=True)
