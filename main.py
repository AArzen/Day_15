from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello")
def hello():
    return render_template("/portfolio/hello.html")


@app.route("/Boogle")
def boogle():
    return render_template("/portfolio/Boogle/index.html")


@app.route("/Glamatic")
def glamatic():
    return render_template("/portfolio/Glamatic/index.html")


@app.route("/HairSalon")
def hair_salon():
    return render_template("/portfolio/HairSalon/index.html")


if __name__ == "__main__":
    app.run()
