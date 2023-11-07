import os
import csv
import requests
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, ValidationError


load_dotenv()


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
bootstrap = Bootstrap5(app)


class checkLink:
    def __init__(self, message="The URL must start with http"):
        self.message = message

    def __call__(self, form, field):
        if not field.data.startswith("http"):
            raise ValidationError(self.message)


class cafeForm(FlaskForm):
    cafeName = StringField("Cafe Name:", validators=[DataRequired()])
    mapLink = StringField(
        "Google Maps Link URL:", validators=[DataRequired(), checkLink()]
    )
    imgLink = StringField("Image URL:", validators=[DataRequired(), checkLink()])
    location = StringField("Location:", validators=[DataRequired()])
    seats = StringField("Number of Seats:", validators=[DataRequired()])
    has_toilet = BooleanField("Toilet Available:")
    has_wifi = BooleanField("WiFi Available:")
    has_sockets = BooleanField("Sockets Available:")
    can_take_calls = BooleanField("Can Take Calls:")
    coffee_price = StringField("Coffee Price:", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = cafeForm()
    if form.validate_on_submit():
        data = {
            "name": form.cafeName.data,
            "map_url": form.mapLink.data,
            "img_url": form.imgLink.data,
            "loc": form.location.data,
            "seats": form.seats.data,
            "toilet": form.has_toilet.data,
            "wifi": form.has_wifi.data,
            "sockets": form.has_sockets.data,
            "calls": form.can_take_calls.data,
            "coffee_price": form.coffee_price.data,
        }

        response = requests.post("http://localhost:5000/add", data=data)

        if response.status_code == 200:
            return redirect(url_for("cafes"))
        else:
            error_message = "Failed to send data to the backend."
            return render_template("error.html", error=error_message)

    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    response = requests.get("http://localhost:5000/all")
    if response.ok:
        cafes_list = response.json().get("cafes", [])
        return render_template("cafes.html", cafes=cafes_list)
    else:
        error_message = "Failed to fetch data from the backend."
        return render_template("error.html", error=error_message)


if __name__ == "__main__":
    app.run(debug=True, port=3000)
