"""
  Lesson 4: ex1.py
"""

# 1. Create 'fruits' dictionary and add following key: values
# apple: 10
# orange: 2

fruits: dict[str, int] = {"apple": 10, "orange": 2}

# 2. Add banana to the dictionary and set it's value to 3

fruits['banana'] = 3

# 3. Add mandarin using dictionary method .update()

fruits.update({"mandarin": 1})
print(fruits)

# 4. Remove the mandarin from the dictionary

del fruits['mandarin']
print(fruits)

# 5. Add 10 more apples and remove 2 bananas

fruits.update({"apple": fruits['apple'] + 10})
fruits.update({"banana": fruits['banana'] - 2})
print(fruits)

# 6. Remove 'apple' from the dictionary using .pop()
#    and save it's value into a variable 'apples'

apples: int = fruits.pop('apple')
print(fruits, apples)

# 7. Remove 'mandarin' from the dictionary using .pop()
#    and save it's value into a variable 'mandarin'
#    if 'mandarin' doesn't exist set the variable to 0

mandarin: int
try:
    mandarin = fruits.pop('mandarin')
except KeyError:
    # ignore
    mandarin = 0

print(fruits, mandarin)

# 8. Remove last item from the dictionary using .popitem()
#    and save it's value into variable 'last'

last: tuple[str, int] = fruits.popitem()
print(last)

# 9. Check if the 'banana' is in the fruits dictionary.

print(fruits)
'banana' in fruits
