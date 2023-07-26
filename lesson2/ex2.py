"""
  Lesson 2: ex2.py
"""

# 1. Use string formatting with empty curly brackets {}
#    to take the argument passed into format and print a
#    sentence of your choice.

print("My firstname: {0}, family name: {1}".format("Masayuki", "Igawa"))

# 2. Use string formatting with positional arguments and
#    print the sentence: "Don't Panic!"

print("{0} {1}".format("Don't", "Panic!"))

# 3. Use string formatting with named arguments and
#    print the sentence: "[name] is really [what]!" and
#    fill in the brackets with your name and "great".

d = dict(name="Masayuki", what="great")
print("{0[name]} is really {0[what]}!".format(d))
