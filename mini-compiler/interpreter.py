''' A mini interpretable language interpreting program
    Copyright (C) 2026 HippoProgrammer

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
'''
example functionality:
y = 1 + 2 
y = 1 + y;

'''
class InterpretingException(Exception):
    pass
class Interpreter:
    def __init__(self,variables:dict):
        self.variables = variables
        self.operators = ['=','+','-','*','/']
        pass
    def interpretLine(self,lineSections:list,line_no = 1): # lineSections should consist of a list derived from a str.split() method
        for section in lineSections:
            if len(lineSections) == 1: # there is no operator, so we need to eval a number or a variable
                try:
                    return int(section) # if we pass this point it must be a number
                except ValueError:
                    return self.variables[section]
            elif lineSections[lineSections.index(section) + 1] in self.operators or lineSections[lineSections.index(section) - 1] in self.operators:
                pass # individual numbers and variables will be interpreted on their own
            elif section == '=': # must be a variable assign
                self.variables[lineSections[0]] = self.interpretLine(lineSections[2:]) # assign value to variable equal to everything interpreted after the second operator (the equals)
                break # the rest of this statement must be the value of the variable, so we'd better not reinterpret it
            elif section == '+': # must be an addition
                operatorIndex = lineSections.index(section)
                return self.interpretLine([lineSections[operatorIndex - 1]]) + self.interpretLine(lineSections[(operatorIndex + 1):])
            elif section == '-':
                operatorIndex = lineSections.index(section)
                return self.interpretLine([lineSections[operatorIndex - 1]]) - self.interpretLine(lineSections[(operatorIndex + 1):])
            elif section == '*':
                operatorIndex = lineSections.index(section)
                return self.interpretLine([lineSections[operatorIndex - 1]]) * self.interpretLine(lineSections[(operatorIndex + 1):])
            elif section == '/':
                operatorIndex = lineSections.index(section)
                return self.interpretLine([lineSections[operatorIndex - 1]]) / self.interpretLine(lineSections[(operatorIndex + 1):])
            else:
                raise InterpretingException(f'Invalid command: {lineSections}')
