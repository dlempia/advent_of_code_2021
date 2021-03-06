
def buildInitialDataSet():
    arr = [[0]*1000 for i in range(1000)]
    return arr

def sanitizeInputsAndRecordToDataSet(arr, useVerticals):
    infile = open('input5a.txt')
    for line in infile:
        line = line.strip('\n')
        line = line. split('->')
        arr = recordValues(line[0].strip(' ').split(','), line[1].strip(' ').split(','), arr, useVerticals)

    return arr

def recordValues(dataPoints1, dataPoints2, arr, useVerticals):
    pointOneX, pointOneY = int(dataPoints1[0]), int(dataPoints1[1])
    pointTwoX, pointTwoY = int(dataPoints2[0]), int(dataPoints2[1])

    if (pointOneX == pointTwoX):
        #case for vertical changes
        if (pointOneY > pointTwoY):
            arr = recordVertical(pointTwoY, pointOneY, pointOneX, arr)
        else:
            arr = recordVertical(pointOneY, pointTwoY, pointOneX, arr)

    elif (pointOneY == pointTwoY):
       #case for horizontal changes
        if (pointOneX > pointTwoX):
            arr = recordHorizontal(pointTwoX, pointOneX, pointOneY, arr)
        else:
            arr = recordHorizontal(pointOneX, pointTwoX, pointOneY, arr)

    else:
        if (useVerticals == True):
            recordDiagonal(pointOneX, pointOneY, pointTwoX, pointTwoY, arr)

    #print(pointOneX, pointOneY, pointTwoX, pointTwoY)
    #prettyPrint(arr)

    return arr


def recordVertical(rangeStart, rangeEnd, startPoint, arr):
    while rangeStart <= rangeEnd:
        (arr[rangeStart][startPoint]) += 1
        rangeStart += 1

    return arr

def recordHorizontal(rangeStart, rangeEnd, startPoint, arr):
    subArray = arr[startPoint]
    while rangeStart <= rangeEnd:
        subArray[rangeStart] += 1
        rangeStart += 1

    return arr

def prettyPrint(arr):
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    for line in arr:
        print(line)
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    

def recordDiagonal(rangeStartX, rangeStartY, rangeEndX, rangeEndY, arr):
    stop = False
    while (stop == False):
        if (rangeStartX == rangeEndX):
            stop = True
        arr[rangeStartY][rangeStartX] += 1
        if (rangeStartX > rangeEndX):
            rangeStartX -= 1
        else: 
            rangeStartX += 1
        if (rangeStartY > rangeEndY):
            rangeStartY -= 1
        else:
            rangeStartY += 1
        


def crawlAndCount(arr) -> int:
    total = 0
    zeros = 0
    for subarray in arr:
        for value in subarray:
            if (value > 1):
                total += 1
            if (value == 0 or value == 1):
                zeros += 1

    return total



print('5a: ', crawlAndCount(sanitizeInputsAndRecordToDataSet(buildInitialDataSet(), False)))
print('5b: ', crawlAndCount(sanitizeInputsAndRecordToDataSet(buildInitialDataSet(), True)))
