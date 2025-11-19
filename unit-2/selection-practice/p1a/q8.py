# Create a program that asks for someone's age and whether they have a driving license (yes/no). Only display "You can drive" if they are 17 or over AND have a license. Otherwise display "You cannot drive".
''' A simple driving license checking program
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
print(''' q8.py  Copyright (C) 2025  HippoProgrammer
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions.''')
def getLicense(prompt = 'License (y/N)? '):
    rawInput = input(prompt)
    if rawInput.lower() == 'y':
        return True
    else:
        return False

age = int(input('Age? '))
license = getLicense()

if age >= 17 and license:
    print('You can drive')
else:
    print('You cannot drive')