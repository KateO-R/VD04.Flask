from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def base():
    return render_template("contacts.html")


@app.route("/products/")
def products():
    return render_template("index.html")

@app.route("/blog/")
def blog():
    return render_template("blog.html")


if __name__ == "__main__":
    app.run()
