array1 = [2, 5, 8, 12]
array2 = [3, 6, 9, 15]
merged = []

i = 0
j = 0

# Complete the merge logic
while i < len(array1) and j < len(array2):
    if array1[i] < array2[j]:
        merged.append(array1[i])
        i = i + 1
    else:
        merged.append(array2[j])
        j = j + 1

# Add remaining elements from array1
while i < len(array1):
    merged.append(array1[i])
    i = i + 1

# Add remaining elements from array2
while j < len(array2):
    merged.append(array2[j])
    j = j + 1

print("Merged array:", merged)
