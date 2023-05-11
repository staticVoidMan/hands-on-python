NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

print("-=WHILE=-")
i = 0
while i < len(NAMES):
  print(i, NAMES[i], AGES[i])
  i += 1

print("-=FOR-IN=-")
for name in NAMES:
  print(name)

print("-=REVERSED=-")
for name in reversed(NAMES):
  print(name)

print("-=RANGE=-")
for i in range(len(NAMES)):
  print(i, NAMES[i], AGES[i])

print("-=ZIP=-")
for name, age in zip(NAMES, AGES):
  print(name, age)

print("-=ENUMERATE=-")
for i, name in enumerate(NAMES):
  print(i, name)