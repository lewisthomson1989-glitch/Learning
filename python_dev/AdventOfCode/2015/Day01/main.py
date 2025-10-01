contents = open("./input.txt", "r")
contents = contents.read()

def part1(contents):
    floor = 0

    for char in contents:

        if char == "(":
            floor += 1

        if char == ")":
            floor -= 1
    
    return floor

def part2():
    pass


print(part1(contents))
