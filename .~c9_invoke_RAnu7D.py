import os
import csv
import pandas as pd

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
from form import RegistrationForm, LoginForm

from helpers import apology, login_required, lookup, usd

# Configure application
# Configure application

app.config["SECRET_KEY"] = "8913482893458h9298274hv47h4j1b90"

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/")
@app.route("/home3")
def home():
    return render_template("home3.html")

@app.route("/register3", methods=["GET", "POST"])
def register():
    """Register user"""

    # User comes via post
    if request.method == "POST":

        # Ensure username is filled out
        if not request.form.get("username"):
            return apology("Missing username!", 400)

        # Ensure password is provided
        if not request.form.get("password"):
            return apology("Missing password!", 400)

        # Ensure password confirmation is provided
        if not request.form.get("confirmation"):
            return apology("Missing confirm password!", 400)

        # Make sure password and confirmation match ??better way to do this
        if (request.form.get("password") != request.form.get("confirmation")):
            return apology("Password and confirmation must match!", 400)

        username = request.form.get("username")

        hash = generate_password_hash(request.form.get("password"))

        rows = db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)", username = request.form.get("username"), hash = hash)

        if not rows:
            return apology("Username is taken")

        session["user_id"] = rows

        return redirect("/match")

# User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register3.html")

@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""

    username = request.args.get("username")

    # Check if username's length is greater than 1
    if len(username) == 0:
        return jsonify(False)


    # Check if user is in database
    result = db.execute("SELECT * FROM users WHERE username = :username",
                          username=username)
    if not result:
        return jsonify(True)
    else:
        return jsonify(False)




@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")



@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/match", methods=["GET"])
def match():

    

@app.route("/blocking", methods=["GET"])
def blocking():

    # db = pd.read_csv("totalcourses.csv")

    with open("totalcourses.csv", "r") as f:
        for line in f:
            reader = csv.reader(f)
            options = list(reader)

    return render_template("blocking.html", options=options)