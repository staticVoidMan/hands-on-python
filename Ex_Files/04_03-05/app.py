import csv
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

with open("laureates.csv", "r", encoding="utf-8") as f:
  reader = csv.DictReader(f)
  laureates = list(reader)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/laureates/")
def filterLaureates():
  results = []

  searchString = request.args.get("flName").strip()
  for laureate in laureates:
    fullString = f'{laureate["name"]} {laureate["surname"]}'
    if searchString.lower() in fullString.lower():
      print(f"found {searchString} in {fullString}")
      results.append(laureate)
  return jsonify(results)

app.run(debug=True)

# Observations
#
# needed `from flask import requests` to access `request` arguments
# i.e. the URl hit is `"GET /laureates/?surname=abc"`
# `request.args.get("surname")` gives "abc"