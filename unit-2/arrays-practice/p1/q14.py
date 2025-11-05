numbers = [34, 12, 67, 23, 89, 45]
itemsUnsorted = len(numbers) - 1
for i in range(len(numbers)):
    for j in range(itemsUnsorted):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    itemsUnsorted -= 1
print(numbers)