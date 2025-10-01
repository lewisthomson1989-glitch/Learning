#Part_1
total_paper = 0
for line in open("AdventOfCode/2015/Day02/input.txt"):
    area = line.split('x')
    length, width, height = int(area[0]), int(area[1]), int(area[2])

    
    sideAreas = [width*length, width*height, length*height]
    total_paper += 2 * sum(sideAreas) + min(sideAreas)
    print(total_paper)

#Part_2    
total_ribbon = 0
volume = length * width * height
total_ribbon += 2 * sum(sideAreas) + volume
print(total_ribbon)