# Will Nzeuton, Andy Shyklo, Kyle Lee, Margie Cao
# JOY ACROSS BORDERS 🔥🔥😵‍💫 by madeinguatemala
# SoftDev
# p04
# 2025-03-28
from flask import Flask, render_template
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
