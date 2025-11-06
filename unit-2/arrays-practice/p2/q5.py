numbers = [2, 7, 11, 4, 3, 8, 5]
target = 10

print("Pairs that sum to", target, ":")

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], "+", numbers[j], "=", target)
