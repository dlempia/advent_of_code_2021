inlist = open('input1.txt')

distance = 0
depth = 0
aim = 0

for line in inlist:
    line = line.strip('\n')
    info = line.split(' ')

    if (info[0] == 'forward'):
        forwardValue = int(info[1])
        distance += forwardValue
        if (aim != 0):
            depth += aim * forwardValue 
    if (info[0] == 'down'):
        aim += int(info[1])
    if (info[0] == 'up'):
        aim -= int(info[1])


print(depth)
print(distance)
print(aim)

print(depth * distance)
