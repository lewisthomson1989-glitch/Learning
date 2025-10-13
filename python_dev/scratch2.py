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



#Check Palindrome number:

def palindrome(num):

    n_string = str(num)
    r_string = n_string[::-1]

    if n_string == r_string:
        return True
    else:
        return False
    
print(palindrome(121))
print(palindrome(125))
print(palindrome(2245422))



# Merge two lists with odds from list one and evens from list two:
def merge_list(num_list1, num_list2):
    list = []
    
    for n in num_list1:
        if n % 2 != 0:
            list.append(n)
    for n in num_list2:
        if n % 2 == 0:
            list.append(n)
    return list
    
num_list1 = [10, 20, 25, 30, 35]
num_list2 = [40, 45, 60, 75, 90]    
    
print(merge_list(num_list1, num_list2))



# Get each digit from a number in reverse order:
number = 7536
