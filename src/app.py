import datetime

from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "iweuwrwoerwioureowruw324234"

notes = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return render_template("hello.html", name=name)


@app.route("/isitnewyear")
def new_year():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template("new-year.html", new_year=new_year)


@app.route("/loop")
def exmaple_loop():
    names = {"Abdul", "Wahhab", "Khan"}
    return render_template("loops.html", names=names)


@app.route('/notes', methods=["POST", "GET"])
def notes_view():
    if session.get("notes") is None:
        session['notes'] = []

    if request.method == "POST":
        session['notes'].append(request.form.get('note'))

    return render_template("notes.html", notes=session['notes'])

