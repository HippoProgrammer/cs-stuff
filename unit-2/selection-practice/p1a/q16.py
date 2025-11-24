# Create a program that validates a strong password. Check that the password:

#Is at least 8 characters long
#Contains at least one uppercase letter
#Contains at least one lowercase letter
#Contains at least one digit

#Display specific messages for each requirement that is not met, or "Strong password" if all requirements are met.


''' A simple password validation and security checking program
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
print(''' q16.py  Copyright (C) 2025  HippoProgrammer
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions.''')

from getpass import getpass
import string

password = getpass('Password: ')

conditions = {
    'overEight':False,
    'oneUpperCase':False,
    'oneLowerCase':False,
    'oneDigit':False
}

if len(password) >= 8:
    conditions['overEight'] = True

for char in password:
    if char in string.ascii_lowercase and not conditions['oneLowerCase']:
        conditions['oneLowerCase'] = True
    elif char in string.ascii_uppercase and not conditions['oneUpperCase']:
        conditions['oneUpperCase'] = True
    elif char in string.digits and not conditions['oneDigit']:
        conditions['oneDigit'] = True
    else:
        continue

conditionsTrue = 0
for condition in conditions.keys():
    if not conditions[condition]:
        if condition == 'overEight':
            print('Password must be over eight chars long ')
        elif condition == 'oneLowerCase':
            print('Must contain at least one lower case character')
        elif condition == 'oneUpperCase':
            print('Must contain at least one upper case character')
        elif condition == 'oneDigit':
            print('Must contain at least one digit')
    else:
        conditionsTrue += 1

if conditionsTrue == 4:
    print('Password OK')
    