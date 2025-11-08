scores = [78, 92, 65, 88, 74, 95, 82, 70, 86]

# Your code here
# Remember to:
# - Sort the scores (or make a copy to sort)
# - Find the middle value
# - Count scores above median

# First, we sort the scores
# Let's use bubble sort
maxMaxPassValue = len(scores)-1
maxPassValue = len(scores)-1
noSwapDone = True
while not maxPassValue == 0:
    for workingIndex in range(0,maxPassValue):
        workingValues = [scores.pop(workingIndex),scores.pop(workingIndex)] # remember by the time the second pop executes all indexes will move down by one
        if workingValues[1] < workingValues[0]:
            # Swap
            scores.insert(workingIndex,workingValues[1])
            scores.insert(workingIndex+1,workingValues[0])
            noSwapDone = False
        else:
            scores.insert(workingIndex,workingValues[0])
            scores.insert(workingIndex+1,workingValues[1])
    maxPassValue -= 1
    if noSwapDone:
        break

# Now we should have a sorted list
# Find the middle value
if len(scores) % 2 == 0: # If length is even, we'll have two medians
    med = scores[(((len(scores) - 1) // 2) + (((len(scores) - 1) // 2) + 1)) / 2] # This equation takes the mean of both medians
else:
    med = scores[(len(scores) - 1) // 2]

# Now we count number of students above median
aboveMedian = 0
for student in scores:
    if student > med:
        aboveMedian += 1

print(aboveMedian)