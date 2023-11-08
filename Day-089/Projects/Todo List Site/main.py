import os
import csv
from flask import Flask, render_template, redirect, url_for, flash, request
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


def read_tasks_from_csv():
    tasks = []
    with open(csv_file_path, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        tasks = [row for row in reader]
    return tasks


def write_tasks_to_csv(tasks):
    with open(csv_file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Task Name", "Task Description", "Task Difficulty"])
        writer.writerows(tasks)


@app.route("/")
def home():
    tasks = []
    with open(csv_file_path, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            tasks.append(row)
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = taskForm()
    if form.validate_on_submit():
        append_to_csv(
            form.taskName.data, form.taskDescription.data, form.taskDifficulty.data
        )
        flash("Task added successfully!", "success")
        return redirect(url_for("home"))
    return render_template("add.html", form=form)


@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit(task_id):
    tasks = read_tasks_from_csv()
    task = tasks[task_id]
    form = taskForm()

    if request.method == "GET":
        form.taskName.data = task[0]
        form.taskDescription.data = task[1]
        form.taskDifficulty.data = task[2]

    if form.validate_on_submit():
        tasks[task_id] = [
            form.taskName.data,
            form.taskDescription.data,
            form.taskDifficulty.data,
        ]
        write_tasks_to_csv(tasks)
        flash("Task updated successfully!", "success")
        return redirect(url_for("home"))

    return render_template("edit.html", form=form, task_id=task_id)


@app.route("/delete/<int:task_id>", methods=["GET", "POST"])
def delete(task_id):
    tasks = read_tasks_from_csv()
    try:
        tasks.pop(task_id)
        write_tasks_to_csv(tasks)
        flash("Task deleted successfully!", "success")
    except IndexError:
        flash("Task not found.", "error")

    return redirect(url_for("home"))


check_and_create_csv()

if __name__ == "__main__":
    app.run(debug=True, port=3000)
