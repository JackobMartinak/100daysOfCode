from flask import Flask

app = Flask(__name__)


def make_bold(fun):
    def wrapper():
        return f"<b>{fun()}</b>"

    return wrapper


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/bye")
@make_bold
def bye():
    return "Bye!"


@app.route("/<name>")
def greet(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True)
