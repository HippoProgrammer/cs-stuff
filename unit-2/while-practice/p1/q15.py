# Write a program that calculates the Fibonacci sequence up to a number specified by the user. Use a while loop to generate the sequence and stop when the next number would exceed the user's limit.

''' A Fibonacci generation program
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
print(''' q15.py  Copyright (C) 2025  HippoProgrammer
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions.''')

maxValue = int(input('Max Fibonacci value: '))
fibonacci = []
nextValue = 0
nextIndex = 0
while nextValue < maxValue:
    if len(fibonacci) < 2:
        nextValue = 1
    else:
        nextValue = fibonacci[nextIndex - 1] + fibonacci[nextIndex - 2]
    nextIndex += 1
    if nextValue > maxValue:
        break
    fibonacci.append(nextValue)

print(fibonacci)
