from alive_progress import alive_bar

def instruction2AbsoluteVal(instruction:str):
    '''Converts an L/Rint form instruction to a signed int'''
    instructionValue = int(instruction[1:]) # take value given after the direction indicator
    if instruction[0] == 'L': # if turning left, reverse number
        instructionValue *= -1
    return instructionValue

def loopOver(value:int,repeater:int): # this function is really bodged - DO NOT USE IN OTHER PROGRAMS
    if value < 0:
        value = repeater - abs(value) + 1 # if value less than repeater, set to higher
    else:
        while value >= repeater:
            value = value - 1 - repeater # until value less than repeater, decrement
    return value
     
with open('/workspaces/cs-stuff/advent-of-code/day-1/input.txt','r') as inputFile:
    inputData = inputFile.read() # read input file
inputList = inputData.split('\n') # split the input data by newlines to get raw data


with alive_bar(len(inputList)) as bar:
    currentPos = 50 # the wheel started at 50
    maxPos = 99
    timesAtZero = 0
    for instruction in inputList: # for each instruction
        #print(f'Raw: {instruction}, Parsed: {instruction2AbsoluteVal(instruction)}, currentPos Before: {currentPos}')
        currentPos = loopOver(currentPos + instruction2AbsoluteVal(instruction), maxPos)
        #print(f'currentPos After: {currentPos}')
        if currentPos == 0:
            timesAtZero += 1
        bar()

print(loopOver(timesAtZero,maxPos))


