import requests

response = requests.get(
  "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json"
)

jsonResponse = response.json()
lastTwentyYears = jsonResponse[1][:20]

for el in reversed(lastTwentyYears):
  population = el["value"]
  if population is not None:
    indicatorWidth = population // 10_000_000
    indicatorBar = "=" * indicatorWidth
    print(f'{el["date"]}:{population}:{indicatorBar}')

# Observations:
# `pip install requests` was required for import
#
# `population / 10_000_000` gives float
# `population // 10_000_000` gives int
#
# `"=" * int` repeats the string int times  
