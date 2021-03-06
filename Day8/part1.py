def importFile():
    infile = open('fullinput.txt')
    chunklist = []

    for line in infile:
        chunks = line.split('|')
        chunklist.append(chunks)

    return chunklist


def processChunks(chunklist):
    totalChunkValuesNoticed = 0
    valuesToCareFor = [2,3,7,4]
    for chunks in chunklist:
        chunks[1] = chunks[1].strip('\n')
        chunkWeCareAbout = chunks[1].split(' ')
        for value in chunkWeCareAbout:
            if (value != '' and len(value) in valuesToCareFor):
                totalChunkValuesNoticed += 1



    print('values', totalChunkValuesNoticed)

def processChunksAndDetermineValues(chunkList):
    top = ''
    valuesToCareFor = [2,3,7,4]
    valueList = ['', '', '', '', '', '', '', '', '', '']

    returnValue = 0
    #            0   1    2   3   4   5   6   7  8    9
    # 1 has 2 values, seven has one extra so we can determine topRow
    # 7 has 3 values
    # 8 has 7 values, 0 has 6 values, 6 has 6 values
    # 4 has 4 values
    for chunks in chunkList:
        valueList = ['', '', '', '', '', '', '', '', '', '']
        chunks[1] = chunks[1].strip('\n')
        chunks[0] = chunks[0].strip('\n')
        chunkPosterior = chunks[1].split(' ')
        chunkAnterior = chunks[0].split(' ')

        for value in chunkPosterior:
            #build known value list
            if (value != '' and len(value) in valuesToCareFor):
                if (len(value) == 2):
                    valueList[1] = value
                if (len(value) == 3):
                    valueList[7] = value
                if (len(value) == 4):
                    valueList[4] = value
                if (len(value) == 7):
                    valueList[8] = value
        for value in chunkAnterior:
            #build known value list
            if (value != '' and len(value) in valuesToCareFor):
                if (len(value) == 2):
                    valueList[1] = value
                if (len(value) == 3):
                    valueList[7] = value
                if (len(value) == 4):
                    valueList[4] = value
                if (len(value) == 7):
                    valueList[8] = value
        valueList = discoverUnknownValues(valueList, chunkPosterior, chunkAnterior)

        #print(chunkPosterior)
        #print(valueList)
        result = ''
        for chunk in chunkPosterior:
            if (chunk != ''):
                for value in valueList:
                    if (value != ''):
                        if (len(value) == len(chunk)):
                            compareValues = matchesWith(chunk, value)
                            if (compareValues == len(value)): 
                                number = valueList.index(value)
                                result += str(number)
        #print(result)
        returnValue += int(result)

    print('return value', returnValue)



def discoverUnknownValues(valueList, chunkPosterior, chunkAnterior):

    finishedValues = valueList
    top = ''
    while ('' in finishedValues):
        finishedValues = checkForMatches(chunkPosterior, finishedValues, top) 
        finishedValues = checkForMatches(chunkAnterior, finishedValues, top)

    return finishedValues 

def checkForMatches(chunkList, finishedValues, top):
        for value in chunkList:
            if (value != ''):
                #check 7 for top
                if (len(value) == 3):
                    for char in value:
                        for subchar in finishedValues[1]:
                            if (char != subchar):
                                top = subchar
                # check 9 for bottom
                if (len(value) == 6):
                    matches = 0
                    notContained = ''
                    for char in value:
                        for subChar in finishedValues[4]:
                            if (char == subChar):
                                matches += 1
                            elif (char != top): 
                                notContained = char 
                    if (matches == 4 and notContained != ''):
                        finishedValues[9] = value
                # check for 6
                if (len(value) == 6):
                    matchesWithNine = matchesWith(value, finishedValues[9])
                    matchesWithSeven = matchesWith(value, finishedValues[7])
                    if (matchesWithNine == 5 and matchesWithSeven == 2):
                        finishedValues[6] = value
                if (len(value) == 5):
                    matchesWithSix = matchesWith(value, finishedValues[6])
                    matchesWithNine = matchesWith(value, finishedValues[9])
                    if (matchesWithSix == 5 and matchesWithNine == 5):
                        finishedValues[5] = value
                if (len(value) == 6):
                    matchesWithFive = matchesWith(value, finishedValues[5])
                    matchesWithSix = matchesWith(value, finishedValues[6])
                    matchesWithNine = matchesWith(value, finishedValues[9])
                    if (matchesWithFive == 4 and matchesWithSix == 5 and matchesWithNine == 5):
                        finishedValues[0] = value
                if (len(value) == 5):
                    matchesWithOne = matchesWith(value, finishedValues[1]) # 1
                    matchesWithThree = matchesWith(value, finishedValues[3]) # 4
                    matchesWithFour = matchesWith(value, finishedValues[4]) #2
                    if (matchesWithOne == 1 and matchesWithThree == 4 and matchesWithFour == 2):
                        finishedValues[2] = value
                if (len(value) == 5):
                    matchesWithOne = matchesWith(value, finishedValues[1])
                    matchesWithSeven = matchesWith(value, finishedValues[7])
                    if (matchesWithOne == 2 and matchesWithSeven == 3):
                        finishedValues[3] = value




        return finishedValues

def matchesWith(valueOne, valueTwo):
    matches = 0
    for char in valueOne:
        for subChar in valueTwo:
            if (subChar == char):
                matches += 1
    return matches


processChunks(importFile())
processChunksAndDetermineValues(importFile())
