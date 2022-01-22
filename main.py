from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    current_year = datetime.datetime.now().year
    return render_template("index.html", year=current_year)

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/login", methods=["POST"])
def receive_data():
    name = request.form["username"]
    password = request.form["password"]
    return f"<h1>Name: {name}, Password: {password}</h1>"

if __name__ == "__main__":
    app.run(debug=True)


