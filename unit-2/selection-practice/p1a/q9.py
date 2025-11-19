# Write a program that asks for a year. Determine if it's a leap year using these rules:

#Divisible by 4: leap year
#BUT if divisible by 100: not a leap year
#UNLESS also divisible by 400: then it IS a leap year
''' A simple leap year calculation program
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
print(''' q9.py  Copyright (C) 2025  HippoProgrammer
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions.''')
year = int(input('Year: '))

if year % 400 == 0:
    print('Leap year')
elif year % 100 == 0:
    print('Not a leap year')
elif year % 4 == 0:
    print('Leap year')
else:
    print('Not a leap year')