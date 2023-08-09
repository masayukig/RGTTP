"""
  Lesson 3: ex1.py
"""

# Here is my shopping list:
shopping_list: list[str] = ['apples', 'milk', 'bread', 'carrot', 'pasta']

# 1. Add banana to a shopping list.

shopping_list.append('banana')
print(shopping_list)

# 2. Add chocolate in the third position in your shopping list

shopping_list.insert(2, "chocolate")
print(shopping_list)


# 3. Extend shopping list by the following items:
# ['chocolate', 'carrot', 'avocado']

# INSERT CODE HERE
other_list: list[str] = ['chocolate', 'carrot', 'avocado']
shopping_list.extend(other_list)

print(shopping_list)

# 4. Remove first chocolate only

idx: int = shopping_list.index('chocolate')
print(idx)
shopping_list.remove('chocolate')
print(shopping_list)

# 5. Remove last item from the list

shopping_list.pop()

# 6. Remove third item from the list

shopping_list.pop(3)

# 7. Count how many carrots are in the shopping list?

print(shopping_list)
print(shopping_list.count('carrot'))


# 8. Get the index of the chocolate (careful can throw traceback)

try:
    print(shopping_list.index('chocolate'))
except ValueError as e:
    print(e)

# 9. Get the index of carrot, make sure this code is executed

try:
    print(shopping_list.index('carrot'))
except ValueError as e:
    print(e)
