def processInputToBinary():
    infile = open('input.txt')
    lineLength = 0
    calculatedInt = 0
    for line in infile:
        line = line.strip()
        calculatedInt = int(line, 16)
        lineLength = len(line) * 4

    return bin_format(calculatedInt, lineLength)

def bin_format(integer, length):
    return f'{integer:0>{length}b}'

def processNumber(binary):
    index = 0
    result = []
    keepGoing = True
    while keepGoing:
        if (binary[index] == '0'):
            keepGoing = False
        result.append(binary[index+1: index+5])
        index += 5
    joinedValues = ''
    for value in result:
        joinedValues += value
    iterations = 5 * len(result)  # to add to index so we don't reprocess
    return iterations, int(joinedValues, 2) 


def parsePackets(binary):
    index = 0
    version = int(binary[index: index + 3], 2)
    typeId = int(binary[index + 3: index + 6], 2)
    index += 6
#handle number case and return values/index/version to add to total
    if (typeId == 4):
        iterations, number = processNumber(binary[index:])
        return index + iterations, number, version

    versionTotal = version
    resultingvalues = []

#handle subpacket counter case, this packet tells how many sets of subpackets exist
# then we can process each packet recursively
    if (binary[index] == '0'):
        subpacketlength = int(binary[index+1: index+16], base=2)
        index += 16
        iterateuntil = index + subpacketlength
        while index < iterateuntil:
            iterations, number, version = parsePackets(binary[index:])
            resultingvalues.append(number)
            versionTotal += version
            index += iterations
            print('boop', resultingvalues)

            
#process subpackets case, this case tells us how many values are part of this particular
#subpacket, so we can iterate through and process them
    else:
        subpacketlength = int(binary[index+1: index+12], 2)
        index += 12
        for i in range(subpacketlength):
            iterations, number, version = parsePackets(binary[index:])
            index += iterations
            versionTotal += version
            resultingvalues.append(number)

    if (typeId == 0):
        resultingsum = sum(resultingvalues)
        return index, resultingsum, versionTotal

    if (typeId == 1):
        resultingproduct = 1
        for item in resultingvalues:
            resultingproduct *= item
        return index, resultingproduct, versionTotal

    if (typeId == 2):
        resultingvalue = min(resultingvalues)
        return index, resultingvalue, versionTotal

    if  (typeId == 3):
        resultingvalue = max(resultingvalues)
        return index, resultingvalue, versionTotal

    if (typeId == 5):
        resultingvalue = 0
        if (resultingvalues[0] > resultingvalues[1]):
            resultingvalue = 1
        else:
            resultingvalues = 0
        return index, resultingvalue, versionTotal

    if (typeId == 6):
        resultingvalue = 0
        if (resultingvalues[0] < resultingvalues[1]):
            resultingvalue = 1
        else:
            resultingvalues = 0
        return index, resultingvalue, versionTotal

    if (typeId == 7):
        resultingvalue = 0
        if (resultingvalues[0] == resultingvalues[1]):
            resultingvalue = 1
        else:
            resultingvalues = 0
        return index, resultingvalue, versionTotal

print(parsePackets(processInputToBinary()))
