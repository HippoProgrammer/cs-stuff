def intArrayBuilder(prompt:str, loops:int):
    array = []
    for i in range(loops):
        array.append(int(input(prompt)))
    return array
items = int(input('Number of numbers: '))
numbers = intArrayBuilder('Number: ',items)
duplicates = False
for checkItem in range(len(numbers)):
    for compareItem in range(len(numbers)):
        if not checkItem == compareItem:
            if numbers[checkItem] == numbers[compareItem]:
                duplicates = True
        if duplicates:
            break
    if duplicates:
        break
if duplicates:
    print('Duplicates found')
else:
    print('No duplicates')