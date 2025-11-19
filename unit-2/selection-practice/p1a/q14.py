# Create a tax calculator program. Ask for annual income. Calculate tax using these bands:

#£0-£12,570: 0% tax (personal allowance)
#£12,571-£50,270: 20% tax on amount above £12,570
#£50,271-£150,000: 20% on first band + 40% on amount above £50,270
#Over £150,000: 20% on first band + 40% on second band + 45% on amount above £150,000

''' A simple tax calculation program
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
print('THIS PROGRAM IS NOT LICENSED BY HMRC AND IS NOT AFFILIATED WITH HIS MAJESTY\'S GOVERNMENT OF GREAT BRITAIN AND NORTHERN IRELAND')
print('THIS PROGRAM SHOULD NOT BE USED FOR THE CALCULATION OF REAL-WORLD TAXATION AMOUNTS UNDER ANY CONDITIONS')

income = int(input('Income: '))

tax = 0

if income <= 12570:
    print('No tax, personal allowance')
elif income <= 50270:
    tax += (income - 12570) * 0.2
elif income <= 150000:
    tax += (50270 - 12570) * 0.2
    tax += (income - 50270) * 0.4
else:
    tax += (50270 - 12570) * 0.2
    tax += (150000 - 50270) * 0.4
    tax += (income - 150000) * 0.45

print(tax)