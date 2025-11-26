# Create a prime number checker. Ask the user for a number and use a while loop to check if it's prime. A prime number is only divisible by 1 and itself. Display the result and all numbers tested during the check.

''' A prime number checking program
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
print(''' q14.py  Copyright (C) 2025  HippoProgrammer
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions.''')

num = int(input('Number to check: '))

numCheck = num - 1
isPrime = True
print('test')
while numCheck > 1 and isPrime == True: 
    print(numCheck)
    if num % numCheck == 0:
        isPrime = False
    numCheck -= 1

print(isPrime)