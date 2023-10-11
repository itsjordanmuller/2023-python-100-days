import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

load_dotenv()


class LoginForm(FlaskForm):
    email = StringField("Email:", validators=[DataRequired()])
    password = StringField("Password:", validators=[DataRequired()])


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
