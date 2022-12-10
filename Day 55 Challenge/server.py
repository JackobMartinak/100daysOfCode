from flask import Flask
import random as rd

app = Flask(__name__)
rnum = rd.randint(0, 9)


@app.route("/")
def home():
    return f'<h1> Guess the number between 0 and 9</h1><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:guess>")
def corret_guess(guess):
    if guess > rnum:
        return f'<h1 style="color: purple">Too high, try again! </h1>'
    elif guess < rnum:
        return f'<h1 style="color: red">Too low, try again!</h1>'
    else:
        return f"<h1>You found me!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
