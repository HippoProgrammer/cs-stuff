def intArrayBuilder(prompt:str, loops:int):
    array = []
    for i in range(loops):
        array.append(int(input(prompt)))
    return array
numbers = intArrayBuilder('Number: ',3)
newNumbers = []
for number in numbers:
    newNumbers.append(number * 2)
print(newNumbers)