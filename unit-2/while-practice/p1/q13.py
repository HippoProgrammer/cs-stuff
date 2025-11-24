#Write a program that implements a login system with a maximum of 3 attempts. Use a while loop to:

#Ask for username and password
#Check if credentials are correct
#Lock the account after 3 failed attempts
#Display appropriate messages throughout

#Valid credentials: username = "admin", password = "pass123"


''' A password checking program
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
print(''' q13.py  Copyright (C) 2025  HippoProgrammer
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions.''')

from getpass import getpass
attempts = 0
while attempts < 3:
  username = input('Username: ')
  password = getpass('Password: ') 
  if username == 'admin' and password == 'pass123':
    print('Correct')
    break
  else:
    attempts += 1
    print(f'Incorrect, {attempts} attempts remaining')
if attempts != 0:
  print('Account locked')
