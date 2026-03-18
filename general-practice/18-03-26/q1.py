''' A weather program
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
print(''' q1.py  Copyright (C) 2026  HippoProgrammer
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions.''')

def celsiusToFahrenheit(celsius:int):
    return (celsius * 1.8) + 32

temp_c_1 = int(input('Enter a temperature in degrees Celsius: '))
temp_f_1 = celsiusToFahrenheit(temp_c_1)
temp_c_2 = int(input('Enter another temperature in degrees Celsius: '))
temp_f_2 = celsiusToFahrenheit(temp_c_2)
temp_f_higher = max(temp_f_1,temp_f_2)
print(f'This is the higher temperature: {temp_f_higher}')