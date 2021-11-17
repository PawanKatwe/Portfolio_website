from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "this home v4"

@app.route("/<name>")
def user(name):
    return f"hello.{name}!"

if __name__ == "__main__":
    app.run()
