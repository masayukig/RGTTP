"""
  Lesson 3: ex4.py
"""

# 1. Create your own Shopping List type.
#
# a. Initialize the ShoppingList class with shopping_list
#    shopping_list = ['apples', 'milk', 'bread', 'carrot', 'pasta']
#
# b. Add in_list method, that checks if the item is in list or not,
#    use the format() or f-strings to return the string based on truth:
#    - 'apples' is in the shopping list.
#    - 'apples' not in the shopping list.
#
# c. Add special function when printing the list to output:
#    * Replace the list with {} and print using format().
#    My shopping list: ['apples', 'milk', 'bread', 'carrot', 'pasta']
#
# d. Add special function for comparison of two objects to output:
#    * Based on the truth.
#    - True
#    - False


class ShoppingList:
    shopping_list: list[str] = ['apples', 'milk', 'bread', 'carrot', 'pasta']

    def in_list(self, item: str) -> str:
        presence = "is" if item in self.shopping_list else "is not"
        return "{0} {1} in the shopping list".format(item, presence)


s = ShoppingList()
print(s.in_list("apples"))
