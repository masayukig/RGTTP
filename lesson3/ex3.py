"""
  Lesson 3: ex3.py
"""

# Here is my shopping list:
shopping_list: list[str] = ['apples', 'milk', 'bread', 'carrot', 'pasta']

# 1. Sort the list using built-in function sorted() and print that list

print(sorted(shopping_list))

# 2. Sort the list using .sort() method and print that list

shopping_list.sort()
print(shopping_list)

# 3. Use the built-in function reversed(), reverse the list and print that list

shopping_list.reverse()
print(shopping_list)

# 4. Reverse the list using sort() method and print the list

shopping_list.sort(reverse=True)
print(shopping_list)

# 5. Reverse the list using sorted() method and print the list

print(sorted(shopping_list, reverse=True))
