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
if y > 3 y = 3 else y = 4
while y > 3 y = y + 1
'''
import warnings # add warnings
# add better error handling
class InterpretingException(Exception): # a basic error
    pass
class Interpreter:
    def __init__(self,variables:dict):
        self.variables = variables
        self.operators = ['=','+','-','*','/']
        pass
    def addVariable(self,variable:tuple):
        self.variables[variable[0]] = variable[1]
    def delVariable(self,variable_key:str):
        del self.variables[variable_key]
    def interpretString(self,line,line_no = 1):
        '''Method that takes line as str, splits it into constituent parts and passes it to be interpreted.'''
        return self.__interpretLine(line.split(' '),line_no)
    def __interpretLine(self,lineSections:list,line_no = 1): # lineSections should consist of a list derived from a str.split() method
        '''Private method that interprets split lines. Functions like interpretString should always be preferred for frontend usage. Note: the interpreter is very broken currently'''
        for section in lineSections:
            if len(lineSections) == 1: # there is no operator, so we need to eval a number or a variable
                try:
                    return int(section) # if we pass this point it must be a number
                except ValueError:
                    return self.variables[section]
            elif lineSections[lineSections.index(section) + 1] in self.operators or lineSections[lineSections.index(section) - 1] in self.operators:
                pass # individual numbers and variables will be interpreted on their own
            elif section == 'if': # must be an if statement
                ifOperatorIndex = lineSections.index(section) # get if operator index
                if 'else' in lineSections:
                    elseOperatorIndex = lineSections.index('else')
                if self.__interpretLine([lineSections[(ifOperatorIndex + 1):(ifOperatorIndex + 4)]]): # send the comparitive operator to the interpreter
                    if 'else' in lineSections:
                        return self.__interpretLine([lineSections[(ifOperatorIndex + 4):(elseOperatorIndex)]]) # if correct, execute the rest
                    else:
                        return self.__interpretLine([lineSections[(ifOperatorIndex + 4):]]) # if correct, execute the rest
                elif 'else' in lineSections:
                    return self.__interpretLine([lineSections[(elseOperatorIndex + 1):]])
                else:
                    return False
            elif section == 'while':
                operatorIndex = lineSections.index(section)
                while self.__interpretLine([lineSections[(operatorIndex + 1):]]):
                    pass
            elif section == '=': # must be a variable assign
                self.variables[lineSections[0]] = self.__interpretLine(lineSections[2:]) # assign value to variable equal to everything interpreted after the second operator (the equals)
                return self.variables[lineSections[0]] # the rest of this statement must be the value of the variable, so we'd better not reinterpret it. note the variable assign returns the new value
            elif section == '==':
                operatorIndex = lineSections.index(section)
                return self.__interpretLine([lineSections[operatorIndex - 1]]) == self.__interpretLine(lineSections[(operatorIndex + 1):])
            elif section == '===':
                operatorIndex = lineSections.index(section)
                return self.__interpretLine([lineSections[operatorIndex - 1]]) == self.__interpretLine(lineSections[(operatorIndex + 1):])
            elif section == '!=':
                operatorIndex = lineSections.index(section)
                return self.__interpretLine([lineSections[operatorIndex - 1]]) != self.__interpretLine(lineSections[(operatorIndex + 1):])
            elif section == '>':
                operatorIndex = lineSections.index(section)
                return self.__interpretLine([lineSections[operatorIndex - 1]]) > self.__interpretLine(lineSections[(operatorIndex + 1):])
            elif section == '<':
                operatorIndex = lineSections.index(section)
                return self.__interpretLine([lineSections[operatorIndex - 1]]) < self.__interpretLine(lineSections[(operatorIndex + 1):])
            elif section == '>=':
                operatorIndex = lineSections.index(section)
                return self.__interpretLine([lineSections[operatorIndex - 1]]) >= self.__interpretLine(lineSections[(operatorIndex + 1):])
            elif section == '<=':
                operatorIndex = lineSections.index(section)
                return self.__interpretLine([lineSections[operatorIndex - 1]]) <= self.__interpretLine(lineSections[(operatorIndex + 1):])
            elif section == '+': # must be an addition
                operatorIndex = lineSections.index(section)
                return self.__interpretLine([lineSections[operatorIndex - 1]]) + self.__interpretLine(lineSections[(operatorIndex + 1):])
            elif section == '-':
                operatorIndex = lineSections.index(section)
                return self.__interpretLine([lineSections[operatorIndex - 1]]) - self.__interpretLine(lineSections[(operatorIndex + 1):])
            elif section == '*':
                operatorIndex = lineSections.index(section)
                return self.__interpretLine([lineSections[operatorIndex - 1]]) * self.__interpretLine(lineSections[(operatorIndex + 1):])
            elif section == '/':
                operatorIndex = lineSections.index(section)
                return self.__interpretLine([lineSections[operatorIndex - 1]]) / self.__interpretLine(lineSections[(operatorIndex + 1):])
            else:
                raise InterpretingException(f'Invalid command on line {line_no}: {lineSections}. The command could not be parsed. Check for invalid keywords and syntax.') # more information helpful
