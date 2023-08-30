"""
  Lesson 5: ex1.py
"""

# 1. Create even() function that return "I am even!" if number is even
#    or "I am odd!" if the number is odd.


def even(n: int) -> str:
    if (n % 2):
        return "I am odd!"
    else:
        return "I am even!"


print(even(2))
print(even(3))
# print(even("asdf"))


# 2. Create safe_even() function, that will output "I am not number!" if
#    the input is not an number otherwise will work same as even()


def safe_even(n: int) -> str:
    if not isinstance(n, int):
        return "I am not a number!"
    if (n % 2):
        return "I am odd!"
    else:
        return "I am even!"


print(safe_even(2))
print(safe_even(3))
# print(safe_even("asdf"))


# 3. Create a function fizz_buzz(),
#    replacing any number divisible by three with the word "fizz",
#    and any number divisible by five with the word "buzz",
#    and any number divisible by both 3 and 5 with the word "fizzbuzz",
#    and number if number is not divisible by any.


def fizz_buzz(n: int) -> str:
    if (type(n) != int):
        return "Not a number!"
    if (n % 3 == 0) and (n % 5 == 0):
        return "fizzbuzz"
    if (n % 3 == 0):
        return "fizz"
    elif (n % 5 == 0):
        return "buzz"
    else:
        return str(n)

# 4. Execute fizz_buzz() function from 1 to the 100


for i in range(1, 101):
    print(fizz_buzz(i))
