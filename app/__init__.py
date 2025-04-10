# Will Nzeuton, Andy Shyklo, Kyle Lee, Margie Cao
# JOY ACROSS BORDERS 🔥🔥😵‍💫 by madeinguatemala
# SoftDev
# p04
# 2025-03-28
from flask import Flask, render_template, request, redirect, session, url_for
from mongo import *
from users import *
import os


app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def home():
    if (session.get("username") is None or session.get("password") is None):
        return redirect(url_for("login"))
    return render_template("index.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form['user']
        password = request.form['pw']
        auth = make_user(username, password)
        if auth[0]:
            session["username"] = username
            session["password"] = password
            return redirect(url_for("home"))
        else:
            return render_template("register.html", error = auth[1])
    return render_template("register.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['user']
        password = request.form['pw']
        auth = auth_user(username, password)
        if auth[0]:
            session["username"] = username
            session["password"] = password
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error = auth[1])
    return render_template("login.html")

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    if request.method == "POST":
        session.pop("username")
        session.pop("password")
        return redirect(url_for("login"))

@app.route("/country/<country>")
def country(country):
    if (session.get("username") is None or session.get("password") is None):
        return redirect(url_for("login"))
    if country in get_countries():
        return render_template('country.html', country = country, happiness = get_happiness_score_yearly(country), freedom = get_freedom_yearly(country), health = get_health_yearly(country), corruption = get_gov_trust_yearly(country))
    else:
        session["error"] = "Country does not have data"
        return redirect(url_for("map"))

@app.route("/map")
def map():
    if (session.get("username") is None or session.get("password") is None):
        return redirect(url_for("login"))
    error = session.pop("error", None)
    return render_template('map.html', error = error)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
