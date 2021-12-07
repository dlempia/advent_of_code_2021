inlist = open('input1.txt')

zeroCounts = [0,0,0,0,0,0,0,0,0,0,0,0]
oneCounts = [0,0,0,0,0,0,0,0,0,0,0,0]

for line in inlist:
    index = 0
    line = line.strip('\n')

    for char in line:

        val = int(char)

        if (val > 0):
            oneCounts[index] += 1
        else:
            zeroCounts[index] += 1

        index += 1

print(zeroCounts)
print(oneCounts)

gamma = [0] 
epsilon = [0]

index = 0

for val in zeroCounts:
    print(val)
    print(oneCounts)
    if val > oneCounts[index]:
        gamma.append(0)
        epsilon.append(1)
    else: 
        gamma.append(1)
        epsilon.append(0)
    index += 1

gammaString = ''.join(str(e) for e in gamma)
print(gammaString)
epsilonString = ''.join(str(e) for e in epsilon)
print(epsilonString)

gammaVal = int(gammaString, 2)
epsilonVal = int(epsilonString, 2)

print(gammaVal)
print(epsilonVal)

print(gammaVal * epsilonVal)
