from alive_progress import alive_bar
from random import randint
from time import time
from math import sqrt

# Get user input
minValue = int(input('Minimum item value? '))
maxValue = int(input('Maximum item value? '))
numValues = int(input('Number of item values? '))

# Create a random list
values = []

for i in range(numValues):
    values.append(randint(minValue,maxValue))

# Output to user
print('Random list: ' + str(values))

# Sort
maxPassValue = len(values)-1
startTime = time()
print('Beginning sort... ')
with alive_bar(maxPassValue) as bar:
    while not maxPassValue == 0:
        for workingIndex in range(0,maxPassValue):
            workingValues = [values.pop(workingIndex),values.pop(workingIndex)] # remember by the time the second pop executes all indexes will move down by one
            if workingValues[1] < workingValues[0]:
                # Swap
                values.insert(workingIndex,workingValues[1])
                values.insert(workingIndex+1,workingValues[0])
            else:
                values.insert(workingIndex,workingValues[0])
                values.insert(workingIndex+1,workingValues[1])
        bar()
        maxPassValue -= 1
print('Ending sort...')
endTime = time()
timeTaken = endTime - startTime
print('Sorted list: ' + str(values))
 # print('Bubble sort has a big O of n^2. Calculated n is '+str(sqrt(timeTaken)))