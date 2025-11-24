# Write a program for a car insurance quote calculator. Ask for:

#Driver's age
#Years of driving experience
#Number of accidents in last 3 years
#Type of car (economy/standard/luxury)

#Base premium: £500

#Apply these rules:

#Age under 25: add £300
#Age 25-30: add £100
#Experience less than 2 years: add £200
#Each accident: add £150
#Economy car: no change
#Standard car: add £100
#Luxury car: add £300
#No accidents AND 5+ years experience: 20% discount on final price

#Display the final premium.


''' A simple car insurance quote calculator program
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
print(''' q17.py  Copyright (C) 2025  HippoProgrammer
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions.''')

age = int(input('Age: '))
exp = int(input('Years of driving experience: '))
accidents = int(input('Number of accidents in last three years: '))
car = input('Type of car (economy, standard, luxury)')

premium = 500
if age < 25:
    premium += 300
elif age <= 30:
    premium += 100

if exp < 2:
    premium += 200

if car == 'standard':
    premium += 100
elif car == 'luxury':
    premium += 300

if accidents > 0:
    premium += accidents * 150
elif exp > 5:
    premium *= 0.8

print(premium)
