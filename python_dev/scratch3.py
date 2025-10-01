with open("AdventOfCode/2015/Day03/input.txt") as f:
  lines = f.readlines()

totalPaper = 0
totalRibbon = 0
  
for line in lines:
  l,w,h = map(int, line.split('x'))
  totalPaper += (2*l*w + 2*w*h + 2*h*l) + min(l*w, w*h, h*l)
  totalRibbon += 2* min(l,w,h) + 2* sorted([l,w,h])[1] + (l*w*h)
  
# answers
print(totalPaper)
print(totalRibbon)