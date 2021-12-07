
def sanitizeInlist():
    inlist = open('input1.txt')
    arr = []
    for line in inlist:
        arr.append(line.strip('\n'))
    return arr

def determineCount(arr, index):
    oneCount = 0
    zeroCount = 0
    for line in arr:
        if (int(line[index]) > 0):
            oneCount += 1
        else:
            zeroCount += 1
        
    if (oneCount == zeroCount):
        return 0
    if (oneCount > zeroCount):
        return 1
    else: 
        return 2

def filterList(arr, val, index):
    returnlist = []
    for item in arr:
        if (int(item[index]) == val):
            returnlist.append(item)

    return returnlist


def findOxegenRating():
    arr = sanitizeInlist()
    index = 0
    while (len(arr) > 1):
        if (determineCount(arr, index) == 0 or determineCount(arr, index) == 1):
            arr = filterList(arr, 1, index)
        else:
            arr = filterList(arr, 0, index)

        index += 1

    return arr

def findCO2Rating():
    arr = sanitizeInlist()
    index = 0
    while (len(arr) > 1):
        if (determineCount(arr, index) == 0 or determineCount(arr, index) == 1):
            arr = filterList(arr, 0, index)
        else:
            arr = filterList(arr, 1, index)

        index += 1

    return arr


o2String = ''.join(str(e) for e in findOxegenRating())
co2String = ''.join(str(e) for e in findCO2Rating())
print(o2String)
print(co2String)


print(int(o2String, 2) * int(co2String, 2))


