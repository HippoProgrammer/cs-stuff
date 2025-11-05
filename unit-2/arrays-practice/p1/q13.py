def intArrayBuilder(prompt:str, loops:int):
    array = []
    for i in range(loops):
        array.append(int(input(prompt)))
    return array
items = int(input('How many items in each list? '))
firstArray = intArrayBuilder('Number for A: ',items)
secondArray = intArrayBuilder('Number for B: ',items)
combinedArray = []
for i in range(items):
    combinedArray.append(firstArray[i] + secondArray[i])
print(combinedArray)