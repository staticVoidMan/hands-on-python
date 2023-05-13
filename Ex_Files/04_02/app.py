import csv
from flask import Flask, render_template, jsonify

app = Flask(__name__)

with open("laureates.csv", "r", encoding="utf-8") as f:
  reader = csv.DictReader(f)
  laureates = list(reader)

def index():
  return render_template("index.html")

app.route("/")(index)

@app.route("/laureates/")
def laureatesResponse():
    return jsonify(laureates)

app.run(debug=True)

# Observations:
#
#   @app.route("/")
#   def hello():
#     return "Hello, World!"
#
# can also be written as:
#   def hello():
#     return "Hello, World!"
#   
#   app.route("/")(hello)
#
# `@app.route("/")`` is a function decorator that wraps the function defined below it
# while `app.route("/")(functionName)` is the non-decorator way of writing
#
###
# when using render_template, `index.html` should be in a `templates` folder