with open('/workspaces/cs-stuff/advent-of-code/day-12/input.txt') as file:
    inputData = file.read()
inputList = inputData.split('\n')

def hashToBin(hash:str):
    if hash == '#':
        return 1
    else:
        return 0

class PresentShape:
    def __init__(self,presentString:str):
        matrix = []
        rows = presentString.splitLines()
        for row in rows:
            matrixRow = []
            for columnIndex in len(row):
                matrixRow.append(hashToBin(row[columnIndex]))
            matrix.append(matrixRow)
        self.matrix = matrix

class Present:
    def __init__(self,index:int,shape:PresentShape):
        self.shape = shape
        self.index = index

# add grid stuff