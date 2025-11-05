def strArrayBuilder(prompt:str, loops:int):
    array = []
    for i in range(loops):
        array.append(str(input(prompt)))
    return array
ids = int(input('Number of IDs: '))
studentIds = strArrayBuilder('Student ID: ', ids)
targetId = input('Target ID: ')
comparisons = 0
found = False
for studentId in studentIds:
    comparisons += 1
    print(f'Comparisons made: {comparisons}')
    if targetId == studentId:
        found = True
        index = studentIds.index(studentId)
        print(f'Found at index {index} in {comparisons} comparisons')
        break

if not found:
    print(f'ID not found in {comparisons} comparisons')