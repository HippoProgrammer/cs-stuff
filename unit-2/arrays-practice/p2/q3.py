numbers = [3, 7, 3, 9, 2, 7, 5, 2, 8]
unique = []

for num in numbers:
    # Check if num is already in unique array
    found = False
    for uniqueNum in unique:
        if uniqueNum == num:
            found = True
            break
    
    # If not found, add it to unique array
    if not found:
        unique.append(num)

print("Array without duplicates:", unique)
