from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def base():
   return render_template("base.html")


@app.route("/home/")
def products():
    context = {
        "link": "Бронируй сейчас!"
    }
    return render_template("home.html", **context)

@app.route("/about/")
def blog():
    context = {
        "link": "Узнать больше"
    }
    return render_template("about.html", **context)


if __name__ == "__main__":
    app.run()