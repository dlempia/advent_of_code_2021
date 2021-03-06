
def processFile():
    startingString = ''
    polymerInsertions = []
    polymerInsertionsDict = {}
    polymerStringDict = {}
    index = 0
    for line in open('input.txt'):
        if index == 0:
            startingString = line.strip()
            subindex = 0
            while subindex < len(startingString) - 1:
                polymerStringDict.setdefault(startingString[subindex: subindex + 2], 0)
                polymerStringDict[startingString[subindex: subindex + 2]] += 1
                subindex += 1

        if line != '\n' and index > 0:
            line = line.strip(' ')
            line = line.strip('\n')
            temp = line.split('->')
            temp[0] = temp[0].replace(' ', '')
            temp[1] = temp[1].replace(' ', '')
            polymerInsertionsDict.setdefault(temp[0], temp[1])
            polymerInsertions.append(temp)

        index += 1


    return (startingString, polymerInsertions, polymerInsertionsDict, polymerStringDict)

def processPolymerInsertions(startingString, polymerInsertions, polymerInsertionsDict):
    iterations = 0
    while iterations < 10:
        index = 0
        newString = ''
        while index + 1 < len(startingString):
            subChar = startingString[index: index+2]
            # this is only the naive way
            #for polymer in polymerInsertions:
            #    if polymer[0] == subChar:
            #        newSubChar = subChar[0] + polymer[1]
            #        newString += newSubChar
            #
            # we want to use the O(1) lookup time in dict instead of looping
            newSubChar = subChar[0] + polymerInsertionsDict.get(subChar)
            newString += newSubChar

            index += 1
        newString += startingString[len(startingString) - 1]
        startingString = newString
        iterations += 1

    return startingString

def processPolymerInsertionsFast(polymerDict, polymerStringDict):
    iterations = 0
    
    orig = polymerStringDict
    copy = orig.copy()

    while iterations < 40:
        for key, value in orig.items():
            value1 = key[0]+polymerDict[key] 
            value2 = polymerDict[key]+ key[1]
            copy.setdefault(value1, 0)
            copy[value1] += value
            copy.setdefault(value2, 0)
            copy[value2] += value
            copy[key]-=value

        orig = copy.copy()
        iterations += 1

        
    #print('after iterating', polymerStringDict)
    return orig

def processMostAndLeastDict(polymerDict):
    alphabetMap = {}
    for key in polymerDict:
        for char in key:
            alphabetMap.setdefault(char, 0)
            alphabetMap[char] += polymerDict[key]

    most = ('', 0)
    least = ('', 10000000000000000000)
    for keyValue in alphabetMap:
        if (alphabetMap[keyValue] > most[1]):
            most = (keyValue,alphabetMap[keyValue]) 
        if (alphabetMap[keyValue] < least[1]):
            least = (keyValue,alphabetMap[keyValue]) 


    print('most', round(most[1]/2))
    print('least', round(least[1]/2))
    print('answer parttwo', round(most[1]/2) - round(least[1]/2))
    print('might be +/- 1')



def processMostAndLeast(string):
    alphabetMap = {}
    for char in string:
        alphabetMap.setdefault(char, 0)
        alphabetMap[char] += 1
    print('alphabetMap', alphabetMap)

    most = ('', 0)
    least = ('', 10000000000000000000)
    for keyValue in alphabetMap:
        if (alphabetMap[keyValue] > most[1]):
            most = (keyValue,alphabetMap[keyValue]) 
        if (alphabetMap[keyValue] < least[1]):
            least = (keyValue,alphabetMap[keyValue]) 

    #print(most)
    #print(least)
    print('answer part1', most[1] - least[1])



processMostAndLeast(processPolymerInsertions(processFile()[0], processFile()[1], processFile()[2]))
processMostAndLeastDict(processPolymerInsertionsFast(processFile()[2], processFile()[3]))


