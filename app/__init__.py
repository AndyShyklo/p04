# Will Nzeuton, Andy Shyklo, Kyle Lee, Margie Cao
# JOY ACROSS BORDERS 🔥🔥😵‍💫 by madeinguatemala
# SoftDev
# p04
# 2025-03-28
from flask import Flask, render_template, request, redirect, session, url_for
from app.mongo import *
from app.users import *
from app.rankings import *
import os


app = Flask(__name__)
app.secret_key = "ASKJDHHUHJHjjhJHSJKhjshIUJHIU89"

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route("/")
def home():
    if ("username" not in session):
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
        if_rank = check_if_ranking(session.get("username"), country)
        avg = calculate_rankings(country)
        stars = round(avg)
        num_reviews = num_rankings(country)
        return render_template('country.html', country = country, if_rank = if_rank, avg = avg, stars = stars, num_reviews = num_reviews, happiness = get_happiness_score_yearly(country), rank = get_happiness_rank_yearly(country), gdp = get_gdp_per_capita_yearly(country), freedom = get_freedom_yearly(country), health = get_health_yearly(country), corruption = get_gov_trust_yearly(country), family = get_family_yearly(country), generosity = get_generosity_yearly(country))
    else:
        session["error"] = "Country does not have data"
        return redirect(url_for("map"))

@app.route("/submit_rev", methods=["POST"])
def submit_rev():
    rating = request.form.get("rating")
    country = request.form.get("country")
    username = session.get("username")

    print(f"rating: {rating}", flush=True)
    print(f"country: {country}", flush=True)

    make_ranking(username, country, rating)

    return(redirect(url_for("country", country=country)))

@app.route("/profile", methods=["POST"])
def profile():
    username = session.get("username")

    docs = get_rankings(username)

    num = len(docs)

    return(render_template("profile.html", username = username, docs = docs, num = num))

@app.route("/map")
def map():
    if (session.get("username") is None or session.get("password") is None):
        return redirect(url_for("login"))
    error = session.pop("error", None)
    return render_template('map.html', error = error)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
