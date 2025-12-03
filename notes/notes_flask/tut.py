from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])

def home():
    if request.method == "POST":
        return redirect(url_for("user", name=request.form["name"]))
    return render_template("index.html") 

@app.route("/about")
def about():
    return "<h1>Hello!</h1>"

@app.route("/contact")
def contact():
    return "<p>please dont contact me</p>"

@app.route("/<name>")
def user(name):
    return render_template("user.html")


if __name__ == "__main__":
    app.run(debug=True)