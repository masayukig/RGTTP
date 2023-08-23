"""
  Lesson 4: ex4.py
"""

# 1. Create a data variable which contains a list of objects
#    with following key and values:
#    {"category": "fruit", "name": "apple"}
#    {"category": "fruit", "name": "banana"}
#    {"category": "fruit", "name": "orange"}
#    {"category": "vegetable", "name": "carrot"}
#
#    Write a for loop to print out the fruits and vegetables.

things: list[dict] = [{"category": "fruit", "name": "apple"},
                      {"category": "fruit", "name": "banana"},
                      {"category": "fruit", "name": "orange"},
                      {"category": "vegetable", "name": "carrot"}]
print(things)
for i in things:
    print(i['name'])
