from collections import defaultdict
"""
  Lesson 4: ex3.py
"""

# 1. Create dictionary using comprehension
# {key, value = i, i**2}

my_list: list[list[int]] = [[i, i**2] for i in range(10)]
print(my_list)

my_dict: dict[int, int] = {i: i**2 for i in range(10)}
print(my_dict)

# 2. Create another comprehension and add +1 to each key's value.
# {key, value = i, i+1}

my_dict2: dict[int, int] = {i: i+1 for i in range(10)}
print(my_dict2)

# 3. Create 'fruits' defaultdict():
# apple: 10
# orange: 2
# banana: 3
# and for any other key set it's default value to 0

fruits: dict[str, int] = defaultdict(int)
fruits['apple'] = 10
fruits['orange'] = 2
fruits['banana'] = 3
print(fruits['mandarin'])
print(fruits)

# 4. Sort the 'fruits' dictionary using sorted() method
# by keys and values, dictionary does not have .sort()

print(sorted(fruits))

# 5. Return 'sorted_fruits' dictionary using sorted() method,
# sort by values.

print(fruits)
sorted_fruits: dict[str, int] = {i: fruits[i] for i in sorted(fruits)}
print(sorted_fruits)

# 6. Reverse the 'sorted_fruits' dictionary and print the dictionary.
reverse_fruits: dict[str, int] = {i: fruits[i] for i in
                                  sorted(sorted_fruits, reverse=True)}
print(reverse_fruits)
