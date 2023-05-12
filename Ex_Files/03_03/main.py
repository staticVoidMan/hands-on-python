import csv
import json
from pprint import pprint

# Objective: Convert CSV to JSON; i.e. `laureates.csv`` & write to `laureates.json``
#
# CSV
#   name,surname,born,died,birthplace,motivation,category,year
#   'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'
#
# to JSON
#    {
#        "name": "Albert",
#        "surname": "Einstein",
#        "born": "1879-03-14",
#        "died": "1955-04-18",
#        "birthplace": "Germany",
#        "category": "physics",
#        "motivation": "for his services to Theoretical Physics...",
#        "category": "physics",
#        "year": 1921
#    }

print("-= as Dictionary =-")
asDict = {
  "name": "Albert",
  "surname": "Einstein",
  "born": "1879-03-14",
  "died": "1955-04-18",
  "birthplace": "Germany",
  "category": "physics",
  "motivation": "for his services to Theoretical Physics...",
  "category": "physics",
  "year": 1921
}
pprint(asDict)

print("-= as JSON =-")
asJson = json.dumps(asDict)
print(asJson)

print("-= as Dictionary from JSON =-")
backAsDict = json.loads(asJson)
pprint(backAsDict)

print("-= Read from CSV =-")
with open("laureates.csv", "r") as f:
  reader = csv.DictReader(f)
  laureates = list(reader)
  print("success")

print("-= Write to JSON =-")
with open("laureates.json", "w") as f:
  json.dump(laureates, f, indent=2)
  print("success")