with open('/workspaces/cs-stuff/advent-of-code/day-12/input.txt') as file:
    inputData = file.read()
inputList = inputData.split('\n')

def hashToBin(hash:str):
    if hash == '#':
        return 1
    else:
        return 0

class PresentShape:
    def __init__(self,rows:list,matrix=[]):
        if matrix != []:
            self.matrix = matrix
        else:
            matrix = []
            for row in rows:
                matrixRow = []
                for columnIndex in range(len(row)):
                    matrixRow.append(hashToBin(row[columnIndex]))
                matrix.append(matrixRow)
            self.matrix = matrix

class Present:
    def __init__(self,index:int,shape:PresentShape):
        self.shape = shape
        self.index = index
    def shape(self,flip=False,rotate=False):
        '''Flip = True or false, Rotate = False (0), True (90)'''
        shape = self.shape.matrix
        if flip:
            newShape = []
            for row in shape:
                newRow = []
                for column in row:
                    newRow.insert(column)
                newShape.append(row)
            shape = newShape
        if rotate:
            newShape = []
            for row in shape:
                newShape.append([0,0,0])
            for rowIndex in range(len(shape)):
                for columnIndex in range(len(row)):
                    if shape[rowIndex][columnIndex] == 1:
                        if rowIndex == 0 and columnIndex == 0:
                            newShape[0][2] = 1
                        elif rowIndex == 0 and columnIndex == 1:
                            newShape[1][2] = 1
                        elif rowIndex == 0 and columnIndex == 2:
                            newShape[2][2] = 1
                        elif rowIndex == 1 and columnIndex == 0:
                            newShape[0][1] = 1
                        elif rowIndex == 1 and columnIndex == 1:
                            newShape[1][1] = 1
                        elif rowIndex == 1 and columnIndex == 2:
                            newShape[2][1] = 1
                        elif rowIndex == 2 and columnIndex == 0:
                            newShape[0][0] = 1
                        elif rowIndex == 2 and columnIndex == 1:
                            newShape[1][0] = 1
                        elif rowIndex == 2 and columnIndex == 2:
                            newShape[2][0] = 1
            shape = newShape
        return PresentShape(shape)

class Grid:
    def __init__(self,size:tuple,shapesRequired:list,shapesAvailable:list):
        self.size = dict()
        self.size['x'], self.size['y'] = size[0], size[1]
    def initializeNew(self):
        self.testGrid = []
        for y in range(self.size['y']):
            testRow = []
            for x in range(self.size['x']):
                testRow.append[0]
            self.testGrid.append(testRow)
    def returnUnusedIndices(self):
        indices = []
        for y in self.testGrid:
            for x in y:
                if x == 1:
                    indices.append((y.index(x),self.testGrid.index(y)))
        return indices
    def placeShapeAtCoords(self,x:int,y:int,shape:PresentShape):
        shape = shape.matrix
        # add placing stuff
        
def inputParser(inputByLine:list,presents=6):
    presentInput = inputByLine[0:presents*5]
    nonPresentInput = inputByLine[presents*5:]
    presentList = []
    for presentLineIndex in range(presents):
        presentList.append(Present(presentLineIndex,PresentShape([presentInput[presentLineIndex*5+1],presentInput[presentLineIndex*5+2],presentInput[presentLineIndex*5+3]])))
    gridList = []
    for gridLineIndex in range(len(nonPresentInput)):
        gridList.append(Grid((int(nonPresentInput[gridLineIndex][0:1]),int(nonPresentInput[gridLineIndex][3:4])),[int(nonPresentInput[gridLineIndex][7:8]),int(nonPresentInput[gridLineIndex][10:11]),int(nonPresentInput[gridLineIndex][13:14]),int(nonPresentInput[gridLineIndex][16:17]),int(nonPresentInput[gridLineIndex][19:20]),int(nonPresentInput[gridLineIndex][22:23])],presentList))
    return presentList, gridList

presentList, gridList = inputParser(inputList)


        


# brute force?