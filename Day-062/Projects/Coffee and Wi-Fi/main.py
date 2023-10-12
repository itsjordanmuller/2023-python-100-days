import os
import csv
from dotenv import load_dotenv
from flask import Flask, render_template
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


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = cafeForm()
    if form.validate_on_submit():
        print(form.data)
        print("Cafe Name:", form.cafeName.data)
        print("Map Link:", form.mapLink.data)
        print("Open Time:", form.openTime.data.strftime("%I:%M%p").lstrip("0"))
        print("Close Time:", form.closeTime.data.strftime("%I:%M%p").lstrip("0"))
        print("Coffee Rating:", form.coffeeRating.data)
        print("Wi-Fi Rating:", form.wifiRating.data)
        print("Power Rating:", form.powerRating.data)
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
