from flask import Flask, redirect, url_for, render_template
import project_dict

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/portfolio")
def projects():
    return render_template("projects.html",project = project_dict.project )

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/<name>")
def user(name):
    return f"Hey! page '{name}' not found on this site"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Welcome Admin!!!"))

if __name__ == "__main__":
    app.run(debug=True)
