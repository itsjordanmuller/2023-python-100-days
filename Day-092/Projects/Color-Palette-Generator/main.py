import os
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


def extract_colors(image, num_colors):
    image = image.resize((150, 150))

    data = np.array(image).reshape((-1, 3))

    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(data)

    colors = kmeans.cluster_centers_

    hex_colors = [
        "#%02x%02x%02x" % (int(color[0]), int(color[1]), int(color[2]))
        for color in colors
    ]

    return hex_colors


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    if "image" not in request.files or "num_colors" not in request.form:
        return redirect(request.url)

    file = request.files["image"]
    num_colors = int(request.form.get("num_colors", 9))
    if file:
        image = Image.open(file.stream)
        colors = extract_colors(image, num_colors)

        grid_size = int(np.ceil(np.sqrt(num_colors)))
        return render_template("palette.html", colors=colors, grid_size=grid_size)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True, port=3000)
