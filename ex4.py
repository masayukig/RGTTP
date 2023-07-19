"""
  Lesson 1: ex4.py
"""

# 1. Create a new list with the following values:
#    Apple, Milk, Bread, Chicken and Pasta

shopping_list: list = ["Apple", "Milk", "Bread", "Chicken", "Pasta"]

# 2. Write a check to see if Orange is in the shopping list or not.

print(bool(shopping_list.count("Orange")))

# 3. Write a function "in_shopping_list" that takes a item such as
#    orange, and returns True or False.
#    Depending whether the item is in the list or not.


def in_shopping_list(item: str) -> bool:
    return bool(shopping_list.count(item))

# 4. Write a function "show_shopping_list" that will return a
#    shopping list and print it out on the screen.


def show_shopping_list() -> list:
    return shopping_list


print(show_shopping_list())
# 5. Create a list of the following values: 2.99 1.79 3.49 6.99 2.49

price_list: list = [2.99, 1.79, 3.49, 6.99, 2.49]

# 6. Create a function price_checker, and pass this list as
#    an argument and let the function return the cheapest price.#


def price_checker(prices: list) -> float:
    return min(prices)

# 7. Write another function show_price, that will call your
#    price_checker function and uses the result to
#    print the cheapest price.


def show_price():
    print(price_checker(price_list))


show_price()
