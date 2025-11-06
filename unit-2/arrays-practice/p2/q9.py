numbers = [3, 7, 3, 9, 3, 7, 5, 9, 3]
max_count = 0
mode = 0

for i in range(len(numbers)):
    count = 0
    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count = count + 1
    
    if count > max_count:
        max_count = count
        mode = numbers[i]

print("Mode:", mode, "appears", max_count, "times")
# Expected: Mode: 3 appears 4 times
