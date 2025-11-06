numbers = [45, 78, 23, 90, 67, 34, 89]

# Initialize variables
largest = numbers[0]
second_largest = numbers[0]

# Complete the loop
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest number:", second_largest)
