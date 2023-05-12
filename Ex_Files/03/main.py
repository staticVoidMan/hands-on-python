import csv
from pprint import pprint

# Objective: Read CSV file laureates.csv & find person with the surname as "Einstein"
#
# Example CSV
#   name,surname,born,died,birthplace,motivation,category,year
#   'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'
#
# convert to JSON
#    {
#        "name": "Albert",
#        "surname": "Einstein",
#        "born": "1879-03-14",
#        "died": "1955-04-18",
#        "birthplace": "Germany",
#        "category": "physics",
#        "motivation": "for his services to Theoretical Physics...",
#        "category": "physics"
#        "year": 1921
#    }

with open("laureates.csv", "r") as f:
  reader = csv.DictReader(f)
  laureates = list(reader)

for laureate in laureates:
  if laureate["surname"] == "Einstein":
    pprint(laureate)
    break