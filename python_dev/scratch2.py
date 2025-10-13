# Print the Sum of a current number and the previous number:

previous_num = 0
for n in range(1,11):
    #print(n)

    x_sum = previous_num + n 
print("Current", n, "Previous", previous_num, "Sum:", x_sum)



# Print characters present at an even index number:
content = "PYnative"

even_chars = content[::2]
print("All even characters:", even_chars)



# Remove characters from a 'n' in a string:
def remove_chars(content, n):
    print("original word", content)
    x = content[n:]
    return x

print(remove_chars("pynative", 4))
print(remove_chars("badgers", 2))



# Are first and last numbers the same?:
def first_last(number_list):


    first_char = number_list[0]
    last_char = number_list[-1]

    if first_char == last_char:
        return True
    else:
        return False



numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

print(first_last(numbers_x))
print(first_last(numbers_y))



# All numbers divisible by 5:
num_list = [10, 20, 33, 46, 55]

for n in num_list:
    if n % 5 == 0:
        print("Divisible by 5:", n)



# How many times does word appear:
x  = " Emma is a good developer, Emma is a writer"

name = x.count('Emma')
print("name appears", name, "times")



# Print the pattern:
#1
#22
#333
#4444
#55555

for n in range(1,6):
    for x in range(n):
        print(n, end=" ")
    print("\n")
        