# Write a program that asks for a student's percentage score. Use if-elif-else to assign a grade:

# 70% or above: Grade A
# 60-69%: Grade B
# 50-59%: Grade C
# Below 50%: Grade D
''' A simple grade calculation program
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
print(''' q7.py  Copyright (C) 2025  HippoProgrammer
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions.''')
percent = int(input('Percentage (%): '))

if percent >= 70:
    print('A')
elif percent >= 60:
    print('B')
elif percent >= 50:
    print('C')
else:
    print('D')
