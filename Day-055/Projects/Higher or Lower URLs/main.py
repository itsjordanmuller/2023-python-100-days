from flask import Flask
import random

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

random_num = random.randint(0, 9)
print(random_num)


@app.route("/")
def hello_world():
    return (
        "<h1>Guess a number between 0 and 9</h1>"
        "<img src='https://media4.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif?cid=ecf05e47ft1azodpvyl0fzwiefazc762oozdkjb6yt3dpg7l&ep=v1_gifs_search&rid=giphy.gif&ct=g' width=400>"
    )


@app.route("/<int:guess>")
def check_num(guess):
    if guess == random_num:
        return (
            "<h1>Correct!</h1>"
            "<img src='https://media3.giphy.com/media/l2JHPB58MjfV8W3K0/giphy.gif?cid=ecf05e47q8vi3qlnb8nhmjdkr211moc6am6g6y1ugoa5avdw&ep=v1_gifs_search&rid=giphy.gif&ct=g' width=400>"
        )
    elif guess < random_num:
        return (
            "<h1>Too low! Try again</h1>"
            "<img src='https://media3.giphy.com/media/YqEtNGbBc6nHOv4YG4/giphy.gif?cid=ecf05e47anqszeliae7kvuadjn9xinzuzfeo7vuo00fus73x&ep=v1_gifs_search&rid=giphy.gif&ct=g' width=400>"
        )
    else:
        return (
            "<h1>Too high! Try again</h1>"
            "<img src='https://media2.giphy.com/media/HoUgegTjteXCw/giphy.gif?cid=ecf05e478njrwy8cy85w63i3ct1isp379ct7zfbjtrd41vb4&ep=v1_gifs_search&rid=giphy.gif&ct=g' width=400>"
        )


if __name__ == "__main__":
    app.run(debug=True)
