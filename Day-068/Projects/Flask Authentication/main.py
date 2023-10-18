import os
from dotenv import load_dotenv
from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    flash,
    send_from_directory,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# CONNECT TO DB
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQL_DB_URI")
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
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user:
            flash("Email already exists. Login or choose another one.")
            return redirect(url_for("register"))

        hashed_password = generate_password_hash(
            password, method="pbkdf2:sha256", salt_length=8
        )

        new_user = User(email=email, name=name, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        return redirect(url_for("secrets"))

    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/secrets")
@login_required
def secrets():
    return render_template("secrets.html")


@app.route("/logout")
def logout():
    pass


@app.route("/download")
def download():
    pass


if __name__ == "__main__":
    app.run(debug=True)
