import os
import csv
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TimeField
from wtforms.validators import DataRequired


load_dotenv()


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
bootstrap = Bootstrap5(app)


class cafeForm(FlaskForm):
    cafeName = StringField("Cafe Name:", validators=[DataRequired()])
    mapLink = StringField("Google Maps Link URL:", validators=[DataRequired()])
    openTime = TimeField("Open Time:", format="%I:%M%p", validators=[DataRequired()])
    closeTime = TimeField("Close Time:", format="%I:%M%p", validators=[DataRequired()])
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
            ("🛜", "★☆☆☆☆"),
            ("🛜🛜", "★★☆☆☆"),
            ("🛜🛜🛜", "★★★☆☆"),
            ("🛜🛜🛜🛜", "★★★★☆"),
            ("🛜🛜🛜🛜🛜", "★★★★★"),
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


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add")
def add_cafe():
    form = cafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", newline="", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        headers = next(csv_data, None)
        rows = [row for row in csv_data]
    return render_template("cafes.html", headers=headers, rows=rows)


if __name__ == "__main__":
    app.run(debug=True)
