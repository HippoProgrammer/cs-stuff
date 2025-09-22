# A simple program to play Higher or Lower across a set range with a human player
from math import floor as fl

minRange = 0 # defines the bounds between which the game will be played
maxRange = 1000

computedMinRange = minRange
computedMaxRange = maxRange
cg = 0
i = 1
numFound = False

def computerGuess():
    return fl((computedMaxRange - computedMinRange) / 2 + computedMinRange)
def userResponse(resp:int,cg:int):
    global computedMaxRange, computedMinRange
    if resp == 0: # lower
        computedMaxRange = cg
    elif resp == 1: # higher
        computedMinRange = cg
def hl2int(hl:str):
    global i
    if hl.lower() == 'h':
        return 1
    elif hl.lower() == 'l':
        return 0
    elif hl.lower() == 'c':
        raise UserException('I was right. Guesses: {i}'.format())
    else:
        raise UserException('help')

while not numFound:
    cg = computerGuess()
    i+=1
    print(cg)
    userResponse(hl2int(input('higher, lower, correct? (h/l/c) ')),cg)