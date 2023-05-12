import csv
from pprint import pprint
from datetime import datetime

# Objective 1: Read CSV file laureates.csv & find laureate having surname as "Einstein"
# Objective 2: Calculate the age of laureate when they received the Noble prize
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
  # Objective 1: Find laureate
  if laureate["surname"] == "Einstein":
    print("-# OBJECTIVE 1 #-")
    pprint(laureate)

    # Objective 2: Calculate age
    print("-= OBJECTIVE 2 =-")
    dateOfBirth = datetime.strptime(laureate["born"], "%Y-%m-%d")
    dateOfAward = datetime.strptime(laureate["year"], "%Y")
    age = dateOfAward.year - dateOfBirth.year
    print(f'{age}yrs in the "{laureate["category"].capitalize()}" category')
    break