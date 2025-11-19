# Write a program that determines the season based on a month number (1-12):

#12, 1, 2: Winter
#3, 4, 5: Spring
#6, 7, 8: Summer
#9, 10, 11: Autumn 
#Include validation to check the month is between 1 and 12.

class InputNotValidException(Exception):
    pass

def isIntBetweenValues(integer:int,valueLower:int,valueHigher:int):
    if integer >= valueLower and integer <= valueHigher:
        return True
    else:
        return False

monthNum = int(input('Month: '))

if not isIntBetweenValues(monthNum,1,12):
    raise InputNotValidException('Month must be between 1 and 12')

if isIntBetweenValues(monthNum,1,2) or monthNum == 12:
    print('Winter')
elif isIntBetweenValues(monthNum,3,5):
    print('Spring')
elif isIntBetweenValues(monthNum,6,8):
    print('Summer')
else:
    print('Autumn')
