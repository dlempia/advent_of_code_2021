inlist = open('input1.txt')

sanitizedList = []

for line in inlist:
    sanitizedList.append(int(line.strip('\n')))

calculatedPreviousValue = 0
calculatedCurrentValue = 0
index = 0
increasedCount = 0

while (index < len(sanitizedList) - 2):

    calculatedCurrentValue = sanitizedList[index] + sanitizedList[index + 1] + sanitizedList[index + 2]
    if (calculatedPreviousValue != 0):
        if (calculatedCurrentValue > calculatedPreviousValue):
            increasedCount += 1

    calculatedPreviousValue = calculatedCurrentValue

    index += 1

print(increasedCount)
