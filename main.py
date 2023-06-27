from flask import Flask, render_template, request, make_response
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    username = request.cookies.get("user_name")
    # if username is None:
    #    username = ''
    return render_template("index.html", cookie_name=username)


@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == 'POST':
        comment_name = request.form.get("name")
        comment_email = request.form.get("email")
        comment_message = request.form.get("message")
        print(comment_name, comment_email, comment_message)

        response = make_response(render_template("/portfolio/saveData.html", user_name=comment_name))
        response.set_cookie("user_name", comment_name)
        return response
    else:
        d = datetime.datetime.now()
        name = 'Anže'
        return render_template("/portfolio/hello.html", todays_day=d, user_name=name)


@app.route("/save-data", methods=["POST"])
def save_data():
    comment_name = request.form.get("name")
    comment_email = request.form.get("email")
    comment_message = request.form.get("message")
    print(comment_name, comment_email, comment_message)

    return render_template("/portfolio/saveData.html", user_name=comment_name)


@app.route("/Boogle")
def boogle():
    return render_template("/portfolio/Boogle/index.html")


@app.route("/Glamatic")
def glamatic():
    return render_template("/portfolio/Glamatic/index.html")


@app.route("/HairSalon")
def hair_salon():
    return render_template("/portfolio/HairSalon/index.html")


@app.route("/delete-me", methods=["POST"])
def delete():
    pass


if __name__ == "__main__":
    app.run()
