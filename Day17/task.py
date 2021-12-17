def processInput():
    infile = open('input.txt')
    for line in infile:
        line = line.split(',')
        xSection = line[0].split('x')[1]
        xSection = xSection.strip('=')
        xVals = xSection.split('..')
        xStart = int(xVals[0])
        xEnd = int(xVals[1])
        
        ySection = line[1]
        ySection = ySection.strip()
        ySection = ySection.strip('y=')
        yVals = ySection.split('..')
        yStart = int(yVals[0])
        yEnd = int(yVals[1])

    return xStart, xEnd, yStart, yEnd

def modelShots(xStart, xEnd, yStart, yEnd):
    initialY, initialX = -109, -178
    shots = {}

    while initialY < 200:
        initialX = 0
        while initialX < 200:
            initialX += 1
            shotVal = modelShot(initialY, initialX, xStart, xEnd, yStart, yEnd)
            if (shotVal != None):
                shots.setdefault((initialY, initialX), shotVal[1])
        initialY += 1
    highest = 0
    for key in shots:
        val = shots[key]
        if (val > highest):
            highest = val

    print('highest y val', highest)
    print('amount of shots that make it:', len(shots))

def modelShot(y, x, xs, xe, ys, ye):
    startingy, startingx = y, x
    currentPointX, currentPointY = 0, 0
    highestYPosition = 0
    steps = 0

    while currentPointX <= xe and currentPointY >= ys:
        steps += 1
        currentPointX += x
        currentPointY += y
        if (currentPointY > highestYPosition):
            highestYPosition = currentPointY

        if (x > 0):
            x = x - 1
        y = y - 1

        if (currentPointX >= xs and currentPointX <= xe):
            if (currentPointY >= ys and currentPointY <= ye):
                return ((currentPointX, currentPointY), highestYPosition)

    return 


xs, xe, ys, ye = processInput()
modelShots(xs,xe,ys,ye)
