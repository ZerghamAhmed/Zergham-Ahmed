import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():

    # Request data
    name = request.form.get("name")
    house = request.form.get("house")
    car = request.form.get("car")

    # Check that every field of request has value
    if not request.form.get("name"):
        return render_template("error.html", message="Please include name")
    if not request.form.get("house"):
        return render_template("error.html", message="Please include house")
    if not request.form.get("car"):
        return render_template("error.html", message="Please include favorite car")

    # Add data to table
    with open("survey.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([request.form.get("name"), request.form.get("house"), request.form.get("car")])

    # Write on page
    return redirect("/sheet")


@app.route("/sheet", methods=["GET"])
def get_sheet():

    # Reads past submissions and displays them
    with open("survey.csv", "r") as f:
        reader = csv.reader(f)
        students = list(reader)
    return render_template("sheet.html", students=students)
