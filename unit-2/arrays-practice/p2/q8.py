numbers = [10, 20, 30, 40, 50]
reversed = []

for i in range(len(numbers)):
    reversed.append(numbers[len(numbers) - 1 - i])

print("Original:", numbers)
print("Reversed:", reversed)
# Expected output: [50, 40, 30, 20, 10]
# Actual output will be incorrect
