numbers = [5, 10, 15, 20, 25]
running_total = []
total = 0

for num in numbers:
    total = total + num
    running_total.append(total)

print("Running totals:", running_total)
# Expected output: [5, 15, 30, 50, 75]
# Actual output will be incorrect
