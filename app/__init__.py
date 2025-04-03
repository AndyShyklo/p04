# Will Nzeuton, Andy Shyklo, Kyle Lee, Margie Cao
# JOY ACROSS BORDERS 🔥🔥😵‍💫 by madeinguatemala
# SoftDev
# p04
# 2025-03-28
from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register")
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        print(username)
        print(password)
        return redirect("/login")
    return render_template("register.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
