# Broken and I don't know how to fix it

numbers = [64, 34, 25, 12, 22, 11, 90]

# STEP 1: Loop through each element starting from index 1
for i in range(1, len(numbers)):
    
    # STEP 2: Store the current element to be inserted
    key = numbers[i]
    # STEP 3: Initialize position to compare with previous elements
    j = i - 1
    # STEP 4: Move elements greater than key one position ahead
    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j = j - 1
    
    # STEP 5: Insert the key at its correct position
    numbers[j] = key
    print(numbers)

print("Sorted array:", numbers)
