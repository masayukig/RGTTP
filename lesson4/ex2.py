"""
  Lesson 4: ex2.py
"""

# 1. Create 'fruits' dictionary and add following key: values
# apple: 10
# orange: 2
# banana: 3

fruits: dict[str, int] = {"apple": 10, "orange": 2, "banana": 3}

# 2. Iterate over fruits in fruits dictionary using for loop,
#    print using f-strings:
#    apple: 10
#    orange: 2
#    banana: 3

for i, j in fruits.items():
    print(f'{i}: {j}')

# 2. Iterate over the keys in 'fruits' dictionary

for i in fruits:
    print(f'{i}')

# 3. Iterate over the values in dictionary

for value in fruits.values():
    print(f"{value}")

# 4. Access value banana using .get() method

print(fruits.get("banana"))

# 5. Access value mandarin using .get() method,
#    if 'mandarin' doesn't exist, return 0

mandarin: int | None
mandarin = fruits.get("mandarin")

mandarin = fruits.get("mandarin")
if mandarin is None:
    mandarin = 0
print(mandarin)

# 6. Remove all items from the dictionary

while (fruits):
    print(fruits.popitem())

print(fruits)
