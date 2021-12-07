inlist = open('input1.txt')

distance = 0
depth = 0

for line in inlist:
    line = line.strip('\n')
    info = line.split(' ')

    if (info[0] == 'forward'):
        distance += int(info[1])
    if (info[0] == 'down'):
        depth += int(info[1])
    if (info[0] == 'up'):
        depth -= int(info[1])


print(distance * depth)
