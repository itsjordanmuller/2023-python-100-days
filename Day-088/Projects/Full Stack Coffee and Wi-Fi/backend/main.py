import os
from dotenv import load_dotenv
import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

API_KEY = os.getenv("API_KEY")

app = Flask(__name__)

##Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record


# @app.route("/random", methods=["GET"])
# GET is allowed by Default on All Routes
@app.route("/random")
def random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(
        cafe={
            "id": random_cafe.id,
            "name": random_cafe.name,
            "map_url": random_cafe.map_url,
            "img_url": random_cafe.img_url,
            "location": random_cafe.location,
            "amenities": {
                "seats": random_cafe.seats,
                "has_toilet": random_cafe.has_toilet,
                "has_wifi": random_cafe.has_wifi,
                "has_sockets": random_cafe.has_sockets,
                "can_take_calls": random_cafe.can_take_calls,
                "coffee_price": random_cafe.coffee_price,
            },
        }
    )


@app.route("/all")
def all_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    cafes_list = []
    for cafe in all_cafes:
        cafe_data = {
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "amenities": {
                "seats": cafe.seats,
                "has_toilet": cafe.has_toilet,
                "has_wifi": cafe.has_wifi,
                "has_sockets": cafe.has_sockets,
                "can_take_calls": cafe.can_take_calls,
                "coffee_price": cafe.coffee_price,
            },
        }
        cafes_list.append(cafe_data)

    return jsonify(cafes=cafes_list)


@app.route("/search")
def search_cafes():
    loc = request.args.get("loc")
    if loc:
        cafes = Cafe.query.filter(Cafe.location.ilike(f"%{loc}%")).all()
        if cafes:
            cafes_list = []
            for cafe in cafes:
                cafe_data = {
                    "id": cafe.id,
                    "name": cafe.name,
                    "map_url": cafe.map_url,
                    "img_url": cafe.img_url,
                    "location": cafe.location,
                    "amenities": {
                        "seats": cafe.seats,
                        "has_toilet": cafe.has_toilet,
                        "has_wifi": cafe.has_wifi,
                        "has_sockets": cafe.has_sockets,
                        "can_take_calls": cafe.can_take_calls,
                        "coffee_price": cafe.coffee_price,
                    },
                }
                cafes_list.append(cafe_data)

            return jsonify(cafes=cafes_list)
        else:
            return (
                jsonify(
                    error={
                        "error": "Sorry, we couldn't find any cafes at that location."
                    }
                ),
                404,
            )
    else:
        return (
            jsonify(
                error={
                    "error": "Please provide the location parameter /search?loc=<location>"
                }
            ),
            400,
        )


## HTTP POST - Create Record


@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(
        response={"status": "success", "message": "Successfully added a new cafe."}
    )


## HTTP PUT/PATCH - Update Record


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    if new_price:
        cafe = Cafe.query.get(cafe_id)
        if cafe:
            cafe.coffee_price = new_price
            db.session.commit()
            return (
                jsonify(
                    response={
                        "status": "success",
                        "message": f"Successfully updated the price to {new_price}.",
                    }
                ),
                200,
            )
        else:
            return (
                jsonify(error={"error": "Cafe not found."}),
                404,
            )
    else:
        return (
            jsonify(error={"error": "Please provide the new price."}),
            400,
        )


## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    api_key = request.args.get("api_key")
    if api_key == API_KEY:
        cafe = Cafe.query.get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return (
                jsonify(
                    response={
                        "status": "success",
                        "message": f"Cafe {cafe.name} successfully deleted.",
                    }
                ),
                200,
            )
        else:
            return (
                jsonify(error={"error": "Cafe not found."}),
                404,
            )
    else:
        return (
            jsonify(
                error={"error": "Unauthorized request. Please provide a valid API key."}
            ),
            401,
        )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
