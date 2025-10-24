# Print the Sum of a current number and the previous number:

previous_num = 0
for n in range(1,11):
    #print(n)

    x_sum = previous_num + n 
print("Current", n, "Previous", previous_num, "Sum:", x_sum)

print('-' * 20)

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

print('-' * 20)

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

print('-' * 20)

# All numbers divisible by 5:
num_list = [10, 20, 33, 46, 55]

for n in num_list:
    if n % 5 == 0:
        print("Divisible by 5:", n)

print('-' * 20)

# How many times does word appear:
x  = " Emma is a good developer, Emma is a writer"

name = x.count('Emma')
print("name appears", name, "times")

print('-' * 20)

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

print('-' * 20)

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

print('-' * 20)

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

print('-' * 20)

# Get each digit from a number in reverse order:
number = 7536

while number > 0:
    digit = number % 10
    number = number // 10
    print(digit)
    

print('-' * 20)
# Income Tax calculator:

income = 45000
tax_pay = 0

if income <= 10000:
    tax_pay = 0
elif income <=20000:
    x = income - 10000
    tax_pay = x * 10 / 100
else:
    tax_pay = 0
    tax_pay = 10000 * 10 / 100
    tax_pay += (income - 20000) * 20 / 100
    print('\n')
    print(tax_pay)

print('-' * 20)

# Print Multiplication table from 1 to 10:

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=',')
    print()    

print('-' * 20)

# Print a downward half-pyramid pattern of stars:

rows = 5

for i in range(rows + 1, 0, -1):
    for j in range(0, i -1):
        print('*', end= " ")
    print("")

print('-' * 20)

# Get an int value of base raises to the power of exponent:

def exponent(base, exp):
    result = base ** exp  
    print(result)

exponent(2, 5)

print('-' * 20)

# Check if number is palindrome:
def is_palindrome(num):
    original = num
    rev_num = 0
    while num > 0:
        digit = num % 10
        rev_num = rev_num *10 + digit
        num //= 10
    return original == rev_num

print(is_palindrome(121))
print(is_palindrome(123))

print('-' * 20)

# Generate Fibonacci series upto 15 terms:

def fibonacci_iterative(n):
    fib_seq = []
    a, b = 0, 1
    for _ in range(n):
        fib_seq.append(a)
        a, b = b, a + b
    return fib_seq
print(fibonacci_iterative(15))

print('-' * 20)

#Check if a given year is a leap year:

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
                        
print(is_leap_year(1900))
            
print('-' * 20)

# Print Alternate Prime Numbers till 20:

def is_prime(num):
    
    if n <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
        

n = 20
primes = []
for num in range(2, n + 1):
    if is_prime(num):
        primes.append(num)

for i in range(0, len(primes), 2):
    print(primes[i])        

print('-' * 20)

# Print reverse number pattern:

#1 1 1 1 1
#2 2 2 2 
#3 3 3
#4 4
#5   
def reverse_pyramid(rows):

    for n in range(1,rows + 1):
        for x in range(rows - n + 1):
            print(n, end=" ")
        print() 

reverse_pyramid(5)

print('-' * 20)
        
        
# Check if a user-entered string contains any digits using a for loop:

#def has_digit(user):

user = input(f"Username:")

for char in user:
    if char.isdigit():
        #return True
        print("Yes")
    else:
      # return False
      print("No")  
#print(has_digit(input()))
print('-' * 20)
# Capitalizxe the first letter of each word in a string:

def cap_words(text):


    words = text.split()
    cap_words = [word.capitalize() for word in words]
    return " ".join(cap_words)


str1 = "pynative.com is for python lovers"
cap_string = cap_words(str1)
print(cap_string)

print('-' * 20)

