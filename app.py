from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/posts")
def posts():
    return render_template("posts.html")


@app.route("/rate")
def rate():
    return render_template("rate.html")


@app.route("/shop")
def shop():
    return render_template("shop.html")


@app.route("/wallet")
def wallet():
    return render_template("wallet.html")


if __name__ == "__main__":
    app.run(debug=True)
