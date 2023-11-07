import os
import csv
import requests
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TimeField
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
    openTime = TimeField("Open Time:", validators=[DataRequired()])
    closeTime = TimeField("Close Time:", validators=[DataRequired()])
    coffeeRating = SelectField(
        "Coffee Rating:",
        choices=[
            ("✘", "☆☆☆☆☆"),
            ("☕️", "★☆☆☆☆"),
            ("☕️☕️", "★★☆☆☆"),
            ("☕️☕️☕️", "★★★☆☆"),
            ("☕️☕️☕️☕️", "★★★★☆"),
            ("☕️☕️☕️☕️☕️", "★★★★★"),
        ],
        validators=[DataRequired()],
    )
    wifiRating = SelectField(
        "Wi-Fi Rating:",
        choices=[
            ("✘", "☆☆☆☆☆"),
            ("📡", "★☆☆☆☆"),
            ("📡", "★★☆☆☆"),
            ("📡", "★★★☆☆"),
            ("📡", "★★★★☆"),
            ("📡", "★★★★★"),
        ],
        validators=[DataRequired()],
    )
    powerRating = SelectField(
        "Power Rating:",
        choices=[
            ("✘", "☆☆☆☆☆"),
            ("🔌", "★☆☆☆☆"),
            ("🔌🔌", "★★☆☆☆"),
            ("🔌🔌🔌", "★★★☆☆"),
            ("🔌🔌🔌🔌", "★★★★☆"),
            ("🔌🔌🔌🔌🔌", "★★★★★"),
        ],
        validators=[DataRequired()],
    )
    submit = SubmitField("Submit")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = cafeForm()
    if form.validate_on_submit():
        # print(form.data)

        with open("cafe-data.csv", mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow(
                [
                    form.cafeName.data,
                    form.mapLink.data,
                    form.openTime.data.strftime("%I:%M%p"),
                    form.closeTime.data.strftime("%I:%M%p"),
                    form.coffeeRating.data,
                    form.wifiRating.data,
                    form.powerRating.data,
                ]
            )

        return redirect(url_for("cafes"))

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
