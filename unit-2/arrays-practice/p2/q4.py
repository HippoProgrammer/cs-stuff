matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Complete the nested loops
for row in range(len(result)):
    for col in range(len(result[row])):
        result[row][col] = matrix1[row][col] + matrix2[row][col]

# Display result
for row in result:
    print(row)
