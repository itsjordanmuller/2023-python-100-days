import os

import bcrypt
from dotenv import load_dotenv
from flask import (
    Flask,
    abort,
    flash,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# CONNECT TO DB
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQL_DB_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
db.init_app(app)


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password").encode("utf-8")

        user = User.query.filter_by(email=email).first()

        if user:
            flash("Email already exists. Login or choose another one.")
            return redirect(url_for("register"))

        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt()).decode("utf-8")

        new_user = User(email=email, name=name, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        return redirect(url_for("secrets"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password").encode("utf-8")

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.checkpw(password, user.password.encode("utf-8")):
            login_user(user)
            return redirect(url_for("secrets"))
        else:
            flash("Invalid email or password. Please try again.")

    return render_template("login.html")


@app.route("/secrets")
@login_required
def secrets():
    return render_template("secrets.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("home"))


@app.route("/download")
@login_required
def download():
    try:
        return send_from_directory(
            os.path.join(app.root_path, "static", "files"),
            "cheat_sheet.pdf",
            as_attachment=True,
        )
    except FileNotFoundError:
        abort(404)


if __name__ == "__main__":
    app.run(debug=True)
