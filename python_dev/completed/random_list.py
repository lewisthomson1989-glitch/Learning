import random
number_list = [random.randint(1, 1000) for _ in range(100)]
print(number_list)

# Task 1:
# Step through the list, in steps of 2. (Printing them.)
print(number_list[1::2])
# Task 2:
# Slice the list, print elements 40 to 60.
print(number_list[40:60])
# Task 3:
# Slice the list, print the last 15 elements. (Remember the [-1] slicing.)
print(number_list[-1:-15:-1])
# Task 4:
# Iterate through the list, print only odd numbers.
for n in number_list:
    if n % 2 != 0:
        print(n)

