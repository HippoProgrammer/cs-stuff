numbers = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
target = 23

# STEP 1: Initialize left and right pointers
left = 0
right = len(numbers) - 1

found = False
position = -1

# STEP 2: Loop while search space is valid
while left <= right:
    
    # STEP 3: Calculate middle index
    mid = (left + right) // 2

    # STEP 4: Check if target is at mid
    if numbers[mid] == target:
        found = True
        position = mid
        break
    
    # STEP 5: If target is smaller, search left half
    elif numbers[mid] > target:
        right = mid
    
    # STEP 6: If target is larger, search right half
    else:
        left = mid

if found:
    print("Found", target, "at index", position)
else:
    print(target, "not found")
