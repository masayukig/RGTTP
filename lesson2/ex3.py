"""
  Lesson 2: ex3.py
"""

# 1. Create a list containing three elements representing the
#    name, age, and occupation of a person.
#    Then, print the sentence using the elements with .format()

person: list[str] = ["Masayuki", "47", "None"]
print("name: {0[0]}, age: {0[1]}, occupation: {0[2]}".format(person))

# 2. The dictionary should contain keys such as
#    'title', 'author', and 'publication_year'.
#    Use the .format() method with multiple positional arguments.
#    Example:
#    "The guidebook [title] by [author] was published in [publication_year]."

my_book: dict[str, str] = {"title": "Python", "author": "Masayuki",
                           "publication_year": "2023"}
print("The guidebook {0[title]} by {0[author]} was published in"
      " {0[publication_year]}.".format(my_book))

# 3. The dictionary should hold details about a spaceship, such as
#    'name', 'type', and 'purpose'.
#    Use the .format() method with named arguments.
#    Example:
#    "The spaceship is called the [name]. It is a [type] used for [purpose]."

my_spaceship: dict[str, str] = {"name": "Voyager", "type": "automatic",
                                "purpose": "getting aliens"}
print("The spaceship is called the {0[name]}. It is a {0[type]} used for"
      " {0[purpose]}.".format(my_spaceship))
