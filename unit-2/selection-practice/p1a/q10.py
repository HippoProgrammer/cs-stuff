# Create a program that asks for three numbers. Display which is the largest of the three numbers.

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

numbers = strToIntListConverter(multiSamePromptInputs(3, 'Number: '))
print(numbers)
if (numbers[0] > numbers[1]) and (numbers[0] > numbers[2]):
    print(numbers[0])
elif (numbers[1] > numbers[0]) and (numbers[1] > numbers[2]):
    print(numbers[1])
else:
    print(numbers[2])
