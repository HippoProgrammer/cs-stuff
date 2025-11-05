numbers = [7, 2, 9, 4, 1, 8]
# this could be done with max(numbers), but I'll use a loop
highestNumber = 0
for number in numbers:
    if number > highestNumber:
        highestNumber = number
print(highestNumber)