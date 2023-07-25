"""
  Lesson 2: ex1.py
"""

# 1. Create a format string to display the name and age of a person.

name: str = "Masayuki"
age: int = 47
print("Name: {}, Age: {}".format(name, age))
print(f"Name: {name}, Age: {age}")

# 2. Print version with it's corresponding upstream codename,
#    and use padding aligned format to left, centre and right.

versions: dict[str, str] = {"13": "Queens", "16": "Train", "17": "Wallaby"}
for version, codename in versions.items():
    print(f"{version: <10} - {codename}")
    print(f"{version: ^10} - {codename}")
    print(f"{version: >10} - {codename}")

# 3. Show different representations of an integer.

types: list[str] = ['08b', 'c', 'd', 'o', 'x', 'n', '']
for t in types:
    print(t + ": " + format(10, t))
#    print("{:b}".format(10))


# 4. Format a floating-point number with fixed precision.

ftypes: list[str] = ['e', 'E', 'f', 'F', 'g', 'G', 'n', '%', '']
for t in ftypes:
    print(t + ": " + format(10, t))
