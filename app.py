from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


@app.context_processor
def inject_date():
    return {'current_date': datetime.datetime.today()}

@app.route("/")
def home():
    return "<h1>Čia mano naujas puslapis</h1>"


@app.route("/user")
def user():
    return render_template("index.html")


@app.route("/skaiciavimas")
def skaiciavimas():
    return render_template("skaiciavimas.html")


@app.route("/vardai")
def vardai():
    zmones = ["Jonas", "Antanas", "Petras", "Donatas", "Laura"]
    return render_template("vardai.html", sarasas=zmones, kintamasis=5)

@app.route("/pasisveikinimas/<name>")
def pasisveikinimas(name):
    return render_template("pasisveikinimas.html", vardas=name)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        vardas = request.form['vardas']
        return render_template("greetings.html", vardas=vardas)



if __name__ == "__main__":
    app.run(debug=True)
