"""
  Lesson 5: ex2.py
"""

# 1. Write a while true loop to print "Forever" forever

# while True:
#     print("Forever")

# 2. Write a while loop to print numbers from 0 to 42

n: int = 0
while (n <= 42):
    print(n)
    n += 1

# 3. Write a while true loop to print numbers from 0 to 42
n: int = 0
while True:
    if (n > 42):
        break
    print(n)
    n += 1

# 4. Write a while true loop to print numbers from 0 to 45, and instead
#    of 42, print "I am 42!" break at number 45.
n: int = 0
while True:
    if (n > 45):
        break
    elif (n == 42):
        print("I am 42!")
    else:
        print(n)
    n += 1


# 5. Write a while-else loop to count to 2, and after that print
#    "It's my turn now!" using else statement.

n: int = 0
while True:
    if (n > 45):
        break
    elif (n == 42):
        print("I am 42!")
    else:
        print(n)
    n += 1
else:
    print("It's my turn now!")
