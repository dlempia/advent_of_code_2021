import math

def openFile():
    infile = open('realinput.txt')
    result = []
    for line in infile:
        line = line.strip('\n')
        result.append(line)

    return result

def valueChecker(char):
    if (char == '}'):
        return 1197
    if (char == ']'):
        return 57
    if (char == ')'):
        return 3
    if (char == '>'):
        return 25137

def valueCheckerTwo(char):
    if (char == '}'):
        return 3
    if (char == ']'):
        return 2
    if (char == ')'):
        return 1
    if (char == '>'):
        return 4

def countIncorrectTokens(infile):
    startingChars = ['[', '{',  '(', '<']
    endingChars = [']', '}', ')', '>']

    skipToNextLine = False
    result = 0

    endStringValueList = []
    
    for line in infile:
        queue = []
        #print('line', line)
        #print('result', result)
        skipToNextLine = False
        for char in line:
            if (skipToNextLine != True):
                #print('char', char)
                if (char in startingChars):
                    queue.append(char)
                    #print('queue appending', queue)
                else:
                    if (queue[len(queue) - 1] == '('):
                        if (char != ')'):
                            #print('error in paren', queue, char)
                            skipToNextLine = True
                            result += valueChecker(char)
                        else:
                            #print('popping', char)
                            queue.pop()
                    elif (queue[len(queue) - 1] == '['):
                        if (char != ']'):
                            #print('error in bracket', queue, char)
                            skipToNextLine = True
                            result += valueChecker(char)
                        else: 
                            #print('popping', char)
                            queue.pop()
                    elif (queue[len(queue) - 1] == '{'):
                        if (char != '}'):
                            #print('error in curly', queue, char)
                            skipToNextLine = True
                            result += valueChecker(char)
                        else:
                            #print('popping', char)
                            queue.pop()
                    elif (queue[len(queue) - 1] == '<'):
                        if (char != '>'):
                            #print('error in diamon', queue, char)
                            skipToNextLine = True
                            result += valueChecker(char)
                        else:
                            #print('popping', char)
                            queue.pop()


        if (skipToNextLine == False):
            value = 0
            completionArr = []
            for char in queue:
                if (char == '['):
                    line += ']'
                    completionArr.append(']')
                if (char == '('):
                    line += ')'
                    completionArr.append(')')
                if (char == '{'):
                    line += '}'
                    completionArr.append('}')
                if (char == '<'):
                    line += '>'
                    completionArr.append('>')
            #print('completionArr', completionArr)
            completionArr = completionArr[::-1]
            #print('completionArr', completionArr)
            
            for char in completionArr:
                if (char == ']'):
                    value *= 5
                    value += valueCheckerTwo(']')
                if (char == ')'):
                    value *= 5
                    value += valueCheckerTwo(')')
                if (char == '}'):
                    value *= 5
                    value += valueCheckerTwo('}')
                if (char == '>'):
                    value *= 5
                    value += valueCheckerTwo('>')

            #print('value', value)
            endStringValueList.append(value)
        
    print('part one result', result)
    endStringValueList.sort()
    print('part two result', endStringValueList[math.floor(len(endStringValueList) / 2)])

 

 
                        


countIncorrectTokens(openFile())



