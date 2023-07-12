"""
  Lesson 1: ex3.py
"""

# 1. Print out your favourite food 42 times using * operator.

print("Beer" * 42)

# 2. Insert space between each output and print it out again.

print("Beer " * 42)

# 3. Save your favourite food into a variable and print it out 42 times

my_favorite_food: str = "Beer"
print(my_favorite_food * 42)

# 4. My favourite food is "sushi", save it into a variable and using
#    fast swapping operation change it with your variable.
#    Now your favourite food should be "sushi" and mine will be yours.#

another_favorite_food: str = "sushi"
my_favorite_food, another_favorite_food = \
  another_favorite_food, my_favorite_food
print("my_favorite_food: " + my_favorite_food)
print("another_favorite_food: " + another_favorite_food)
# INSERT YOUR CODE HERE
