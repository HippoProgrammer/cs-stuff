# Write a program for a loyalty discount system. Ask for:

#Purchase amount
#Loyalty member status (yes/no)
#Years as member (if applicable)

#Apply discounts:

#Non-members: no discount
#Members 0-2 years: 5% discount
#Members 3-5 years: 10% discount
#Members 6+ years: 15% discount
#Additional 5% if purchase is over £100

#Display original price, discount amount, and final price.


''' A simple loyalty discount calculation program
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

def getBoolFromStrInput(prompt:str):
    rawInput = input(prompt)
    if rawInput.lower() == 'y':
        return True
    else:
        return False

amount = int(input('Purchase amount: '))
loyalty = getBoolFromStrInput('Loyalty member (y/N): ')
if loyalty:
    years = int(input('Years as member: '))
    if years <= 2:
        amount *= 0.95
    elif years <= 5:
        amount *= 0.9
    else:
        amount *= 0.85


if amount > 100:
    print(amount * 0.95)
else:
    print(amount)

