from flask import Flask

app = Flask(__name__)

# Decorator Example
# def make_bold(function):
#     def bold():
#         return f"<b>{function()}</b>"

#     return bold

# Routes and Variables Examples
# @app.route("/bye")
# def bye():
#     return "<p>Bye!</p>"

# @app.route("/username/<name>/<int:age>")
# def greet(name, age):
#     return f"<p>Hello there {name}! You are {age} years old!</p>"


@app.route("/")
def hello_world():
    return (
        "<h1>Guess a number between 0 and 9</h1>"
        "<img src='https://media4.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif?cid=ecf05e47ft1azodpvyl0fzwiefazc762oozdkjb6yt3dpg7l&ep=v1_gifs_search&rid=giphy.gif&ct=g' width=400>"
    )


if __name__ == "__main__":
    app.run(debug=True)
