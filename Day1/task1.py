inlist = open('input1.txt')

sanitizedList = []

for line in inlist: 
    sanitizedList.append(int(line.strip('\n')))


print(len(sanitizedList))
prevValue = 0
increased = 0
decreased = 0

for line in sanitizedList:
    if (prevValue != 0):
        if (prevValue < line):
            increased += 1
        else:
            decreased += 1


    prevValue = line

print(increased)
