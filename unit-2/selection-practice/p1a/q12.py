# Create a program that asks for a username and password. The username must be "admin" AND the password must be at least 8 characters long. Display appropriate messages for different failure conditions.
from getpass import getpass

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