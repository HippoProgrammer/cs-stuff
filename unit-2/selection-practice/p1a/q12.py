# Create a program that asks for a username and password. The username must be "admin" AND the password must be at least 8 characters long. Display appropriate messages for different failure conditions.
from getpass import getpass
''' A simple password checking program
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
print(''' q12.py  Copyright (C) 2025  HippoProgrammer
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions.''')
class UserNameNotAdminException(Exception):
    pass
class PasswordNotEightCharsPlusException(Exception):
    pass

username = input('Username: ')

if username != 'admin':
    raise UserNameNotAdminException('Username is not "admin"')

password = getpass('Password: ')

if len(password) < 8:
    raise PasswordNotEightCharsPlusException('Password must be at least eight characters long')