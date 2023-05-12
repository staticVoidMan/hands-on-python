import csv
import json
from pprint import pprint

# Objective: Filter laureats whose names begin with letter "A"
# 
# CSV
#   name,surname,born,died,birthplace,motivation,category,year
#   'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'

with open("laureates.csv", "r") as f:
  reader = csv.DictReader(f)
  laureates = list(reader)

filtered = []
for laureate in laureates:
  if laureate["name"][0] == "A":
    filtered.append(laureate)

with open("filtered.json", "w") as f:
  json.dump(filtered, f, indent=2)
  print("success")
