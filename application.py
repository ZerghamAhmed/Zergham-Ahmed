import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

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
@login_required
def index():
    """Show portfolio of stocks"""

    # Show the stocks in the data base
    stocks = db.execute("SELECT name, symbol, SUM(shares) FROM portfolio WHERE user_id = :user_id GROUP BY symbol", user_id = session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id = :id", id = session["user_id"])

    current_cash = cash[0]["cash"]

    grand_total = cash[0]["cash"]

    # For each stock print the data
    for stock in stocks:
        stock["price"] = lookup(stock["symbol"])["price"]
        grand_total += stock["price"] * stock["SUM(shares)"]

    return render_template("index.html", stocks = stocks, grand_total = grand_total, current_cash = current_cash)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # Submit user input via buy
    if request.method == "POST":

        # Apology if input is blank or symbol doesn't exist
        if not request.form.get("symbol"):
            return apology("Must enter symbol")

        # Look up info for stock
        quote = lookup(request.form.get("symbol"))

        if not quote:
            return apology("Sorry stock doesn't exist")

        shares = request.form.get("shares")

        # Check if pos int
        if shares.isdigit() != True or int(request.form.get("shares")) < 0:
            return apology("Must enter correct number of shares")

        # Can user afford the stock
        cash = db.execute("SELECT cash FROM users WHERE id = :id", id = session["user_id"])

        shares = int(request.form.get("shares"))

        # Buy stock and input current price
        if (cash[0]["cash"]) > (quote["price"] * shares):
            rows = db.execute("INSERT INTO portfolio (symbol, shares, price, name, user_id) VALUES(:symbol, :shares, :price, :name, :user_id)", symbol = request.form.get("symbol"),
            shares = request.form.get("shares"), price = quote["price"], name = quote["name"], user_id = session["user_id"])
        else:
            return apology("Sorry not enough funds")

        # Update Cash
        cash = db.execute("UPDATE users set cash = cash - :purchase  WHERE id = :id", purchase = quote["price"] * shares, id = session["user_id"])

        # Return to homepage index after purchase
        return redirect("/")

    # Get req
    else:
        return render_template("buy.html")


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




@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Pull history of transactions
    stocks = db.execute("SELECT symbol, shares, date, price FROM portfolio WHERE user_id = :user_id", user_id = session["user_id"])

    return render_template("history.html", stocks = stocks)


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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # User comes via post
    if request.method == "POST":

        # user post to insert their data
        quote = lookup(request.form.get("symbol"))

        if not quote:
            return apology("Sorry stock doesn't exist")
        else:
            return render_template("quoted.html", quote=quote)

    # Get method to display
    else:
        return render_template("quote.html")




@app.route("/register", methods=["GET", "POST"])
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

        return redirect("/")

# User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")



@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # Submit user input via buy
    if request.method == "POST":

        # Get stock values
        stocks = db.execute("SELECT name, symbol, SUM(shares) FROM portfolio WHERE user_id = :user_id GROUP BY symbol", user_id = session["user_id"])
        previous_shares = stocks[0]["SUM(shares)"]

        # Apology if input is blank or symbol doesn't exist
        if not request.form.get("symbol"):
            return apology("Must select strock")

        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Check if pos int
        if shares.isdigit() != True or int(request.form.get("shares")) < 0:
            return apology("Must enter correct number of shares")

        if int(shares) > int(previous_shares):
            return apology("Not enough shares")

        quote = lookup(request.form.get("symbol"))

        # Remove stock from user
        db.execute("INSERT INTO portfolio (symbol, shares, price, name, user_id) VALUES(:symbol, :shares, :price, :name, :user_id)", symbol = request.form.get("symbol"),
            shares = -int(shares), price = quote["price"], name = quote["name"], user_id = session["user_id"])

        # Update cash after sale
        db.execute("UPDATE users set cash = cash + :sale  WHERE id = :id", sale = quote["price"] * int(shares), id = session["user_id"])

        # Return to homepage index after sale
        return redirect("/")

    # Get req
    else:
        stocks = db.execute("SELECT name, symbol, SUM(shares) FROM portfolio WHERE user_id = :user_id GROUP BY symbol", user_id = session["user_id"])
        return render_template("sell.html", stocks = stocks)

@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():

    if request.method == "POST":

        # Make sure is valid input
        if not request.form.get("add_cash"):
            return apology("Enter Cash to Add")

        if not request.form.get("credit_card"):
            return apology("Please Enter Credit Card Number")

        add_cash = request.form.get("add_cash")

        # Check if cash is pos int
        if add_cash.isdigit() != True or int(add_cash) < 0:
            return apology("Must enter correct number of shares")

         # Let user add cash
        cash = db.execute("UPDATE users set cash = cash + :add_cash WHERE id = :id",
                    add_cash=request.form.get("add_cash"), id=session["user_id"])

        return redirect("/")

    else:
        return render_template("add_cash.html")


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
