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


class ShoppingList(object):

    def __init__(self):
        self.shopping_list: list[str] = ['apples', 'milk', 'bread', 'carrot',
                                         'pasta']

    def in_list(self, item: str) -> str:
        presence = "is" if item in self.shopping_list else "is not"
        return "{0} {1} in the shopping list".format(item, presence)

    def __str__(self):
        r = "{"
        for i in self.shopping_list:
            r = r + "'" + i + "', "
        r += "}"
        return r

    def __eq__(self, other):
        if other is None or not isinstance(other, ShoppingList):
            return False
        return self.shopping_list == other.shopping_list


s = ShoppingList()
print(s.in_list("apples"))

print(s)

s2 = ShoppingList()
print(s.shopping_list)
print(s2.shopping_list)
print(s == s2)
s2.shopping_list.sort()
print(s.shopping_list)
print(s2.shopping_list)
print(s == s2)
print(s.shopping_list == s2.shopping_list)
