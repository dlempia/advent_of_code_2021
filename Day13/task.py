def processInput():

    foldList = []
    yList = []
    xList = []
    for line in open('input.txt'):
        if (line.split(' ')[0] != 'fold' and len(line.split(',')) == 2):
                vals = line.split(',')
                yList.append(int(vals[1]))
                xList.append(int(vals[0]))

    cols = max(xList) + 1
    rows = max(yList) + 1

    arr = [[0 for i in range(cols)] for j in range(rows)]

    for line in open('input.txt'):
        line = line.strip()
        if (line.split(' ')[0] == 'fold'):
            pointVal = line.split(' ')[2]
            pointVals = pointVal.split('=')
            pointVals[1] = int(pointVals[1])
            foldList.append(pointVals)
        else:
            vals = line.split(',')
            if (len(vals) == 2):
                arr[int(vals[1])][int(vals[0])] = 1


    #prettyPrint(arr)
    return (arr, foldList)

def prettyPrint(arr):
    print('array: ')
    for line in arr:
        print(line)

def processFolds(arrAndFoldList): 
    arr = arrAndFoldList[0]
    pointList = arrAndFoldList[1]

    pointIndex = 0
    while pointIndex < len(pointList):
        
        arr = processFold(arr, pointList[pointIndex])
        if (pointIndex == 0):
            print('part1 answer')
            print(countIndexes(arr))

        pointIndex += 1

    print('answer')
    prettyPrint(arr)


def countIndexes(arr):
    result = 0
    for line in arr:
        for value in line:
            if (value == 1):
                result += 1

    return result

def processFold(arr, point):

    if (point[0] == 'y'):
        arr = foldUp(arr, point[1])
    else:
        arr = foldOver(arr, point[1])

    return arr

def foldUp(arr, point):
    index = 0
    topArr = []
    bottomArr = []
    for line in arr:
        if (index < point):
            topArr.append(line)
        elif (index != point): 
            bottomArr.append(line)

        index += 1

    index = 0
    bottomY = len(bottomArr) - 1
    resultingArr = []

    for line in topArr:
        resultingArr.append([])
        bottomX = 0

        for val in line:
            resultingArr[index].append(val | bottomArr[bottomY][bottomX])
            bottomX += 1
        bottomY -= 1
        index += 1


    return resultingArr

def foldOver(arr, point):
    leftArr = []
    rightArr = []
    index = 0
    for line in arr:
        leftArr.append([])
        rightArr.append([])
        subIndex = 0
        for value in line:
             
            if (subIndex < point):
                leftArr[index].append(value)
            elif(subIndex != point):
                rightArr[index].append(value)
            subIndex += 1
        index += 1

    resultingArr = []

    rightIndex = 0
    for line in leftArr:
        resultingArr.append([])
        leftLine = line
        rightLine = rightArr[rightIndex]
        rightLineIndex = len(rightLine) - 1
        for val in leftLine:
            resultingArr[rightIndex].append(val | rightLine[rightLineIndex])
            rightLineIndex -=1 
        rightIndex += 1

    #prettyPrint(resultingArr)
    return resultingArr





processFolds(processInput())

