numbers = [5, -3, 8, -1, 0, 7, -4, 2] 
positives = []
negatives = []
for number in numbers:
    if abs(number) == number:
        positives.append(number)
    else:
        negatives.append(number)
print(positives)
print(negatives)