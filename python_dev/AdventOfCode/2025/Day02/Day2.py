with open("python_dev/AdventOfCode/2025/Day02/input.txt", "r") as f:
    contents = f.read()

ranges = []   


for n in contents.split(','):
    first_id, last_id = n.split('-')
    ranges.append((int(first_id), int(last_id)))

print(ranges)