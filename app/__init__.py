
# Will Nzeuton, Andy Shyklo, Kyle Lee, Margie Cao
# JOY ACROSS BORDERS 🔥🔥😵‍💫 by madeinguatemala
# SoftDev
# p04
# 2025-03-28
from flask import Flask, render_template, request, redirect
from mongo import *
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form['user']
        password = request.form['pw']
        return render_template("index.html")
    return render_template("register.html")

@app.route("/country/<country>")
def country(country):
    return render_template('country.html', country = country, happiness = get_happiness_score_yearly(country), freedom = get_freedom_yearly(country), health = get_health_yearly(country))

@app.route("/map")
def map():
    return render_template('map.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
