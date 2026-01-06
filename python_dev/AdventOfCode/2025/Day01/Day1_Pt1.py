with open("python_dev/AdventOfCode/2025/input.txt", "r") as f:
    contents = f.read().split()
    #print(contents)
    
start_point = 50
result =[]
zero_count = 0


for line in contents:
    line = line.strip()
    if line and line[0].isalpha() and line[1:].isdigit():
        letter = line[0]
        number = int(line[1:])


    for _ in range(number):
        if letter == "L":
            start_point = (start_point - 1) % 100
        else:
            start_point = (start_point + 1) % 100

        if start_point == 0:
            zero_count += 1



        
print(f"The number of times stops on zero: {zero_count}")      
    
       
        

       



