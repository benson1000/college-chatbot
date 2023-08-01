from flask import Flask, redirect, render_template, session
import random, os
import sqlite3


app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True, port=3000)
    