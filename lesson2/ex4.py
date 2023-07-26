"""
  Lesson 2: ex4.py
"""

# 1. Print the formatted keys and values of the dictionary.
#    versions: dict[str, int] = {'Stein': 15, 'Train': 16, 'Wallaby': 17}

versions: dict[str, int] = {'Stein': 15, 'Train': 16, 'Wallaby': 17}
for k, v in versions.items():
    print("Codename: {0}, version: {1}".format(k, v))

# 2. Print {} around the version numbers.
for k, v in versions.items():
    print("Codename: {0}, version: {{{1}}}".format(k, v))

# 3. Print numbers in decimal, byte and hexadecimal form.

for k, v in versions.items():
    print("Codename: {0}, version(decimal): {1:d}, (byte): {1:b},"
          " (hexdecimal): {1:x}".format(k, v))
