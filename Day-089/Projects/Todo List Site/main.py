import os
import csv
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerRangeField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
bootstrap = Bootstrap5(app)

csv_file_path = "tasks.csv"


class taskForm(FlaskForm):
    taskName = StringField("Task Name:", validators=[DataRequired()])
    taskDescription = StringField("Describe Task:", validators=[DataRequired()])
    taskDifficulty = StringField(
        "Difficulty (1-10):",
        validators=[DataRequired()],
    )
    submit = SubmitField("Submit")


def check_and_create_csv():
    if not os.path.exists(csv_file_path):
        with open(csv_file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Task Name", "Task Description", "Task Difficulty"])


def append_to_csv(task_name, task_description, task_difficulty):
    with open(csv_file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([task_name, task_description, task_difficulty])


@app.route("/")
def home():
    return render_template("index.html")


check_and_create_csv()


@app.route("/add", methods=["GET", "POST"])
def add():
    form = taskForm()
    if form.validate_on_submit():
        append_to_csv(
            form.taskName.data, form.taskDescription.data, form.taskDifficulty.data
        )
        flash("Task added successfully!", "success")
        return redirect(url_for("add"))
    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True, port=3000)
