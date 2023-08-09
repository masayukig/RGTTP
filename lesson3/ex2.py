"""
  Lesson 3: ex2.py
"""

# 1. Create a list of number 0 to 9 using a for loop.
#
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

my_list: list[int] = []

for i in range(10):
    my_list.append(i)

print(my_list)
# 2. Create a list of number from 0 to 9 the power of 2 using a for loop.
#
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

my_list2: list[int] = [i**2 for i in range(10)]
print(my_list2)

# 3. Create a list of lists, which contains elements that are
# number, number(to the power of 2), number(to the power of 3)
#
# [[0, 0, 0], [1, 1, 1], [2, 4, 8], [3, 9, 27], [4, 16, 64],
#  [5, 25, 125], [6, 36, 216], [7, 49, 343], [8, 64, 512],
#  [9, 81, 729]]

my_list3: list[list[float]] = [[i, i**2, i**3] for i in range(10)]

print(my_list3)

# 4. Add condition in a for loop, that only numbers that are odd are added.
#
# [[1, 1, 1], [3, 9, 27], [5, 25, 125], [7, 49, 343], [9, 81, 729]]

my_list4: list[list[float]] = [[i, i**2, i**3] for i in range(10) if i % 2]

print(my_list4)

# 5. Create a nested lists in a list with a for loop:
# [['ax', 'bx', 'cx', 'dx', 'ex'],
#  ['ay', 'by', 'cy', 'dy', 'ey'],
#  ['az', 'bz', 'cz', 'dz', 'ez']]

my_list5: list[list[str]] = [[i + j for i in 'abcde'] for j in 'xyz']

print(my_list5)
