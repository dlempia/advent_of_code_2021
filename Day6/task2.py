
def getStartingArray():
    infile = open('input2.txt')
    arr = []
    for line in infile:
        temp = line.split(',')
        for item in temp: 
            arr.append(int(item))

    return arr

def processFish(arr):
    appendMeLater = []
    index = 0
    while (index < len(arr)):
        if (arr[index] == 0):
            arr [index] = 6
            appendMeLater.append(8)
        else:
            arr[index] -= 1

        index += 1

    for fishToAppend in appendMeLater:
        arr.append(fishToAppend)

    return arr


def iterateDays(arr):
    day = 0
    while day < 80:
        processFish(arr)
        day += 1

    return len(arr)

def processFishEfficient(arr):
    fishZero = 0
    fishOne = 0
    fishTwo = 0
    fishThree = 0
    fishFour = 0
    fishFive = 0
    fishSix = 0
    fishSeven = 0
    fishEight = 0

    for val in arr:
        if (val == 0):
            fishZero += 1
        if (val == 1):
            fishOne += 1
        if (val == 2):
            fishTwo += 1
        if (val == 3):
            fishThree += 1
        if (val == 4):
            fishFour += 1
        if (val == 5):
            fishFive += 1
        if (val == 6):
            fishSix += 1
        if (val == 7):
            fishSeven += 1
        if (val == 8):
            fishEigth += 1

    day = 0
    while (day < 256):
         fishTemp = fishZero
         fishZero = fishOne
         fishOne = fishTwo
         fishTwo = fishThree
         fishThree = fishFour
         fishFour = fishFive
         fishFive = fishSix
         fishSix = fishSeven
         fishSeven = fishEight
         fishEight = fishTemp
         fishSix += fishTemp
          
         day += 1

    return fishZero + fishOne + fishTwo + fishThree + fishFour + fishFive + fishSix+ fishSeven + fishEight


print(iterateDays(getStartingArray()))
print(processFishEfficient(getStartingArray()))




