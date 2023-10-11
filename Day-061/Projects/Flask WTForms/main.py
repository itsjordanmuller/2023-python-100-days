import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError

load_dotenv()


class LoginForm(FlaskForm):
    email = StringField(label="Email:", validators=[DataRequired()])
    password = PasswordField(label="Password:", validators=[DataRequired()])
    submit = SubmitField(label="Log In")

    def validate_email(self, email):
        email_data = email.data
        if "@" not in email_data or "." not in email_data:
            raise ValidationError("Invalid Email Address")

    def validate_password(self, password):
        password_data = password.data
        if len(password_data) < 8:
            raise ValidationError("Password must be 8 characters long.")


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "test@example.com" and form.password.data == "password":
            return redirect(url_for("success"))
        else:
            return redirect(url_for("denied"))
    return render_template("login.html", form=form)


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/denied")
def denied():
    return render_template("denied.html")


if __name__ == "__main__":
    app.run(debug=True)
