def processInput():
    cavemap = []
    for line in open('input.txt'):
        line = line.strip('\n')
        caveline = []
        for char in line:
            caveline.append(int(char))
        cavemap.append(caveline)

    #print(len(cavemap))
    #prettyPrint(cavemap)
    return cavemap

def processInputPartTwo():
    cavemap = []
    yIndex = 0
    while yIndex < 5:
        for line in open('input.txt'):
            caveline = []
            xIndex = 0
            while xIndex < 5:
                line = line.strip('\n')
                for char in line:
                    caveline.append(findValue(int(char), yIndex, xIndex))
                xIndex += 1
            cavemap.append(caveline)
        yIndex += 1

    #prettyPrint(cavemap)
    return cavemap

def findValue(val, yIndex, xIndex):
    #print('origval', val)
    #print('returnval', (val + yval + xval) % 9)
    result = val + yIndex + xIndex
    if result == 9:
        return 9
    else:
        return result % 9


def prettyPrint(arr):
    print('arr')
    for line in arr:
        print(line)

def findNeighbors(x, y, cavelength):
    result = []
    if (x - 1 >= 0):
        result.append((x-1, y))
    if (y - 1 >= 0):
        result.append((x, y-1)) 
    if (x + 1 < cavelength):
        result.append((x + 1, y))
    if (y + 1 < cavelength):
        result.append((x, y+1))

    return result


def caveCrawl(cavemap):
    costMap = {(0,0): 0}
    caveLength = len(cavemap)

    queue = [(0,0)]
    for x, y in queue:
        for xPrime, yPrime in findNeighbors(x, y, caveLength):
            alt = costMap.get((x,y)) + cavemap[yPrime][xPrime]
            if (alt < costMap.setdefault((xPrime, yPrime), 1000000000)):
                costMap[xPrime, yPrime] = alt
                queue.append((xPrime, yPrime))


    print(costMap.get((caveLength -1, caveLength -1)))

caveCrawl(processInput())
caveCrawl(processInputPartTwo())
