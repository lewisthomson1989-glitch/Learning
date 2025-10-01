contents = open("./input.txt", "r")
contents = contents.read()

floor = 0 
char_count = 0
basement = False
for char in contents:

        if char == "(":
            floor += 1

        if char == ")":
            floor -= 1
    
        char_count += 1
        if(floor < 0 ):
             if not basement:
                  basement = True
                  print("basement at char: "  + str(char_count))
