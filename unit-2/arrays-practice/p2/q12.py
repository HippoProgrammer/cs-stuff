numbers = [64, 25, 12, 22, 11]
swap_count = 0

# STEP 1: Loop through array
for i in range(len(numbers) - 1):
    
    # STEP 2: Assume current position has minimum value
    min_index = i
    
    # STEP 3: Find the actual minimum in remaining array
    for j in range(i, len(numbers)):
        if numbers[j] < numbers[min_index]:
            min_index = j
    
    # STEP 4: Swap if a smaller element was found
    if min_index != i:
        # Perform the swap
        temp = numbers[i]
        numbers[i] = numbers[min_index]
        numbers[min_index] = temp
        
        # Increment swap counter
        swap_count = swap_count + 1

print("Sorted array:", numbers)
print("Number of swaps:", swap_count)
