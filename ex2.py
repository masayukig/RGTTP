"""
  Lesson 1: ex2.py
"""

# Here is my shopping list:
#
# 2.99 Apples
# 1.79 Milk
# 3.49 Bread
# 6.99 Chicken
# 2.49 Pasta

# 1. Make a python list of the 5 items above and print it out.
print("# 1. Make a python list of the 5 items above and print it out.")
my_shopping_list: list[str] = ["Apples", "Milk", "Bread", "Chicken", "Pasta"]
print(my_shopping_list)

# 2. Use python as your calculator and print out the total cost of
#    all items on shopping list.
print()
print("# 2. Use python as your calculator and print out the total cost of")
print("#    all items on shopping list.")
my_shopping_dict: dict = {"Apples": 2.99, "Milk": 1.79, "Bread": 3.49,
                          "Chicken": 6.99, "Pasta": 2.49}
total: float = 0.0
for j in my_shopping_dict.values():
    total += j
print(total)

# 3. I have decided that we need 5 cartons of milk, can you recalculate
#    it and print it out again?
print()
print("# 3. I have decided that we need 5 cartons of milk, can you"
      " recalculate it and print it out again?")
new_total: float = 0.0
for k in my_shopping_dict:
    if k == "Milk":
        new_total += my_shopping_dict[k] * 5
    else:
        new_total += my_shopping_dict[k]
print(new_total)

# 4. Print out every item of your shopping list on a new line.
print()
print("# 4. Print out every item of your shopping list on a new line.")
for m in my_shopping_dict:
    print(m)
