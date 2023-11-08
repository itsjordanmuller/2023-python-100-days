import os
import csv
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerRangeField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
bootstrap = Bootstrap5(app)


class taskForm(FlaskForm):
    taskName = StringField("Task Name:", validators=[DataRequired()])
    taskDescription = StringField("Describe Task:", validators=[DataRequired()])
    taskDifficulty = IntegerRangeField(
        "Difficulty:",
        validators=[DataRequired()],
    )
    submit = SubmitField("Submit")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add")
def add():
    form = taskForm()
    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True, port=3000)
