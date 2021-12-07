
def openFileAndGetArray():
    infile = open('input.txt')
    result = []
    for line in infile:
        arr = line.split(',')
        for line in arr:
            result.append(int(line))
    return result

def calculateAverageFuel(arr, weighted):
    val = 0
    for num in arr:
        val += num

    average = round(val / len(arr))
    start = 0
    end = len(arr)

    lowestFuelCost = 1000000000

    while start < end:
        fuelCost = 0
        if (weighted):
            fuelCost = calculateFuelCost(arr, start)
        else:
            fuelCost = calculateWeightedFuelCost(arr, start)
        if (fuelCost < lowestFuelCost):
                lowestFuelCost = fuelCost
        start += 1

    if (weighted == True):
        print('lowest weighted fuel cost', lowestFuelCost)
    else:
        print('lowest fuel cost', lowestFuelCost)


def calculateFuelCost(arr, alignTo):
    totalFuelCost = 0
    for val in arr:
        diff = val - alignTo
        totalFuelCost += abs(diff)

    return totalFuelCost

def calculateWeightedFuelCost(arr, alignTo):
    totalFuelCost = 0
    for val in arr:
            fuelCost = 0
            if (val < alignTo):
                iteration = 1
                while val < alignTo:
                    fuelCost += iteration
                    iteration += 1
                    val += 1
            if (val > alignTo):
                iteration = 1
                while val > alignTo:
                    fuelCost += iteration
                    iteration += 1
                    val -= 1
            totalFuelCost += abs(fuelCost)

    return totalFuelCost


calculateAverageFuel(openFileAndGetArray(), False)

calculateAverageFuel(openFileAndGetArray(), True)
