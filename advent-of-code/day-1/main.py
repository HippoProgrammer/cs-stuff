from time import sleep
from copy import deepcopy
def instruction2AbsoluteVal(instruction:str):
    '''Converts an L/Rint form instruction to a signed int'''
    instructionValue = int(instruction[1:]) # take value given after the direction indicator
    if instruction[0] == 'L': # if turning left, reverse number
        instructionValue *= -1
    return instructionValue

def loopOver(value:int,repeater:int): # this function is really bodged - DO NOT USE IN OTHER PROGRAMS
    timesAtZero = 0
    newvalue = deepcopy(value)
    if value < 0:
        timesAtZero += abs(value) // repeater
        newvalue = repeater - (abs(value) % repeater)
    elif value >= repeater:
        timesAtZero += abs(value) // repeater
        newvalue = newvalue - repeater # until value less than repeater, decrement
        
    return [newvalue, timesAtZero]
     
with open('/workspaces/cs-stuff/advent-of-code/day-1/input.txt','r') as inputFile:
    inputData = inputFile.read() # read input file
inputList = inputData.split('\n') # split the input data by newlines to get raw data

currentPos = 51 # the wheel started at 50
maxPos = 100
timesAtZero = 0
for instruction in inputList: # for each instruction
    print(f'Raw: {instruction}, Parsed: {instruction2AbsoluteVal(instruction)}, currentPos Before: {currentPos}')
    aaaa = loopOver(currentPos + instruction2AbsoluteVal(instruction), maxPos)
    currentPos = aaaa[0]
    timesAtZero += aaaa[1]
    print(f'currentPos After: {currentPos}')
    #if currentPos == 1:
    #    timesAtZero += 1
    sleep(0.001)

print(timesAtZero)


