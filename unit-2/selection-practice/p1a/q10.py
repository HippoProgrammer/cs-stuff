# Create a program that asks for three numbers. Display which is the largest of the three numbers.
''' A simple greatest number calculation program
    Copyright (C) 2025 HippoProgrammer

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.'''
print(''' q10.py  Copyright (C) 2025  HippoProgrammer
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions.''')
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
