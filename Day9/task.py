
def processInput():
    infile = open('input.txt')
    result = []
    index = 0
    for line in infile:
        line = line.strip('\n')
        result.append([])
        for char in line:
            result[index].append(char)
        index += 1

    return result

def trollForLowPoints(floorMap):
    lowPoints = []
    lowPointPoints = []

    rowLength = len(floorMap[0]) - 1
    rowHeight = -1
    for row in floorMap:
        rowHeight += 1

    rowIndex = 0
    for row in floorMap:
        itemIndex = 0
        for item in row:
            if (checkForLowPoints(rowIndex, itemIndex, floorMap, rowLength, rowHeight)):
                lowPoints.append(item)
                lowPointPoints.append((rowIndex, itemIndex))
            itemIndex += 1
        rowIndex += 1

    #print('lowPoints', lowPoints)
    return (lowPoints, lowPointPoints)

def checkForLowPoints(rowIndex, itemIndex, floorMap, rowLength, rowHeight):
    returnValue = True
    if (rowIndex - 1 >= 0):
        if (int(floorMap[rowIndex][itemIndex]) >= int(floorMap[rowIndex - 1][itemIndex])):
            returnValue = False
    if (rowIndex + 1 <= rowHeight):
        if (int(floorMap[rowIndex][itemIndex]) >= int(floorMap[rowIndex + 1][itemIndex])):
            returnValue = False
    if (itemIndex - 1 >= 0):
        if (int(floorMap[rowIndex][itemIndex]) >= int(floorMap[rowIndex][itemIndex - 1])):
            returnValue = False
    if (itemIndex + 1 <= rowLength):
        if (int(floorMap[rowIndex][itemIndex]) >= int(floorMap[rowIndex][itemIndex + 1])):
            returnValue = False

#    if (returnValue == True):
#        print('value',floorMap[rowIndex][itemIndex]) 
#        print('rowIndex', rowIndex)
#        print('itemIndex', itemIndex)
#        prettyPrint(floorMap)

    return returnValue

def calculateLowPoints(arr):
    result = 0
    for item in arr:
        result += (int(item) + 1)

    return result

def prettyPrint(floorMap):
    for line in floorMap:
        print(line)

def crawlBasins(lowPointsContainer, floorMap):
    rowLength = len(floorMap[0]) - 1
    rowHeight = -1
    for row in floorMap:
        rowHeight += 1

    resultList = []
    prettyPrint(floorMap)
    for lowPoint in lowPointsContainer[1]:
        value = len(crawlBasin(lowPoint, floorMap, rowLength, rowHeight, [], []))
        resultList.append(value)
        if (len(resultList) > 3):
            resultList.remove(min(resultList))

    print(resultList) 
    return(resultList)

def crawlBasin(lowPoint, floorMap, rowLength, rowHeight, visitedPointList, basinValues):
    if (lowPoint not in visitedPointList):
        visitedPointList.append(lowPoint)
    #print('lowPoint', lowPoint, floorMap[lowPoint[0]][lowPoint[1]], visitedPointList, endValue)
 
    if (int(floorMap[lowPoint[0]][lowPoint[1]]) == 9):
        return basinValues
    else:
        if (lowPoint not in basinValues):
            basinValues.append(lowPoint)

    if (lowPoint[0] - 1 >= 0):
        if ((lowPoint[0] - 1, lowPoint[1]) not in visitedPointList):
            crawlBasin((lowPoint[0] - 1, lowPoint[1]), floorMap, rowLength, rowHeight, visitedPointList, basinValues)
    if (lowPoint[0] + 1 <= rowHeight):
        if ((lowPoint[0] + 1, lowPoint[1]) not in visitedPointList):
            crawlBasin((lowPoint[0] + 1, lowPoint[1]), floorMap, rowLength, rowHeight, visitedPointList, basinValues)
    if (lowPoint[1] - 1 >= 0):
        if ((lowPoint[0], lowPoint[1] - 1) not in visitedPointList):
            crawlBasin((lowPoint[0], lowPoint[1] - 1), floorMap, rowLength, rowHeight, visitedPointList, basinValues)
    if (lowPoint[1] + 1 <= rowLength):
        if ((lowPoint[0], lowPoint[1] + 1) not in visitedPointList):
            crawlBasin((lowPoint[0], lowPoint[1] + 1), floorMap, rowLength, rowHeight, visitedPointList, basinValues)

    return basinValues

def processBiggestBasins(arr):
    result = 1
    for value in arr:
        result *= int(value)

    return result

print(calculateLowPoints(trollForLowPoints(processInput())[0]))
print(processBiggestBasins(crawlBasins(trollForLowPoints(processInput()), processInput())))

