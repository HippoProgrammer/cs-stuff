def intArrayBuilder(prompt:str, loops:int):
    array = []
    for i in range(loops):
        array.append(int(input(prompt)))
    return array
def intMatrixBuilder(rows:int,columns:int):
    matrix = []
    for row in range(rows):
        matrix.append(intArrayBuilder(f'Row {row}: ',columns))
    return matrix
rows = int(input('Rows: '))
columns = int(input('Columns: '))
matrix = intMatrixBuilder(rows,columns)
rowSums = [0] * rows
for row in matrix:
    for column in row:
        rowSums[matrix.index(row)] += column
columnSums = [0] * columns
for row in matrix:
    for column in row:
        columnSums[row.index(column)] += column
print(rowSums)
print(columnSums)