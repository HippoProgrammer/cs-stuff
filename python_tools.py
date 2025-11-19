from math import ceil
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
def strArrayBuilder(prompt:str, loops:int):
    array = []
    for i in range(loops):
        array.append(str(input(prompt)))
    return array
def arrayOppositeIndexFinder(array:list,index:int):
    return len(array) - 1 - index # subtract one to get final index, then subtract starting index
def palindromeChecker(word:str):
    wordChars = list(word)
    isPalindrome = True
    for charIndex in range(ceil(len(wordChars) / 2)):
        if wordChars[charIndex] != wordChars[arrayOppositeIndexFinder(wordChars,charIndex)]:
            isPalindrome = False
            break
    return isPalindrome
def multiSamePromptInputs(numPrompts:int, prompt:str):
    responses = []
    for i in range(numPrompts):
        responses.append(input(prompt))
    return responses
def strToIntListConverter(listToConvert:list):
    intList = []
    for item in listToConvert:
        intList.append(int(item))
    return intList
def dayInput(prompt):
    dayAliases = {
        'Mon':0,
        'Monday':0,
        'Tue':1,
        'Tues':1,
        'Tuesday':1,
        'Wed':2,
        'Weds':2,
        'Wednesday':2,
        'Thu':3,
        'Thurs':3,
        'Thursday':3,
        'Fri':4,
        'Friday':4,
        'Sat':5,
        'Saturday':5,
        'Sun':6,
        'Sunday':6
    }
    rawInput = input(prompt)
    try:
        return dayAliases[rawInput]
    except KeyError:
        return -1