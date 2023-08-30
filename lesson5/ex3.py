"""
  Lesson 5: ex3.py
"""

# 1. Write a for loop to iterate over list: [1, 2, 3, 'a', 'b', 'c']

for i in [1, 2, 3, 'a', 'b', 'c']:
    print(i)

# 2. Write for loop to print each character in word "orange"

for c in "orange":
    print(c)


# 3. Using following shopping list:
# shopping_list: ['orange', 'banana', 'mandarin']
# Print "Note to self, buy: " and then iterate
# over each element in the list

shopping_list: list[str] = ['orange', 'banana', 'mandarin']

# 4. Write for loop using range to print numbers from 0 to 10
# print("Note to self, buy: ")
# for index in range(0, len(shopping_list)):
#     print(f"{index}, {shopping_list[index]}")

print("Note to self, buy: ")
for index, item in enumerate(shopping_list, start=1):
    print(f"{index}, {item}")

# 5. Write for loop using range to print numbers from 10 to 20

for i in range(10, 21):
    print(i)

# 6. Write for loop using range to print even numbers from 10 to 20

for i in range(10, 21):
    if (i % 2 == 0):
        print(i)


# 7. Write for loop using range, to print every 5 numbers
#    down from 100 to 0

for i in range(100, 0, -5):
    print(i)

# 8. Write for loop using enumerate to print element and it's index

for i in enumerate(shopping_list):
    print(i[0], i[1])
