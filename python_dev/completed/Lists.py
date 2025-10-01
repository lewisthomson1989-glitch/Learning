to_do_list = ["Buy beer", "Go cycling", "Paint decking", "Fix car"]

# Task 1: (slicing)
# Using slicing, print the first, and last elements of the list.
print(to_do_list[0])
print(to_do_list[3])



# Task 2: (append, insert)
# Insert a new element at the end of the list.
# Insert a new elememt at a specific location in the list, such as first.
to_do_list.append("book holiday")
to_do_list.insert(0, "drink coffee")
print(to_do_list)


# Task 3: (remove, pop)
# Remove element from list, identifying by it's value.
# Remov the last element from the list.
to_do_list.remove("Paint decking")
to_do_list.pop(1)
print(to_do_list)

# Task 4:
# Modify an element in the list.
to_do_list[2] = "road trip"
print(to_do_list)


# Task 5:
# Iterate through the list.
for task in to_do_list:
    print(task)


# Task 6:
# Check if an elememnt in the list equals a given value.
def check_Value(value,data):
    if(value in data):
        return True
    else:
        return False

print(check_Value("Go cycling",to_do_list))

