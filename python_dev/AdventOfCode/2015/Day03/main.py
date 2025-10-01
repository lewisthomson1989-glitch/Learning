#Part_1
with open("AdventOfCode/Day03/input.txt", 'r') as f:
    direction = f.read()
    #print(direction)
    history = [(0,0)]
for i in range(len(direction)):
    last = history[-1]
    if direction[i]=='v':
        history.append((last[0],last[1]-1))
    elif direction[i]=='^':
        history.append((last[0],last[1]+1))
    elif direction[i]=='>':
        history.append((last[0]+1,last[1]))
    elif direction[i]=='<':
        history.append((last[0]-1,last[1]))

print(len(set(history)))

#Part_2
history = [(0,0), (0,0)]
for i in range(len(direction)):
    last = history[-2]
    if direction[i]=='v':
        history.append((last[0],last[1]-1))
    elif direction[i]=='^':
        history.append((last[0],last[1]+1))
    elif direction[i]=='>':
        history.append((last[0]+1,last[1]))
    elif direction[i]=='<':
        history.append((last[0]-1,last[1]))

print(len(set(history)))
