NAMES = ["John", "Paul", "George", "Ringo"]

first = NAMES[0]
second = NAMES[1]
print(first, second)

firstTwo = NAMES[:2]
lastTwo = NAMES[2:]
print(firstTwo, lastTwo)

reversed = NAMES[::-1]
print(reversed)

alternate = NAMES[::2]
print(alternate)

AGES = [20, 21, 22, 23]
SUM_AGES = sum(AGES)
print(SUM_AGES)

MIN_AGE = min(AGES)
MAX_AGE = max(AGES)
print(MIN_AGE, MAX_AGE)