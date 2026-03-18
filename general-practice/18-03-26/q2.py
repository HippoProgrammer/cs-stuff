''' A password checking program
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
print(''' q2.py  Copyright (C) 2026  HippoProgrammer
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions.''')
import string
def checkPassword(password:str):
    split_password = set(password)
    if not(len(split_password.intersection(set(string.ascii_uppercase))) >= 1): # if the intersection between the unique password characters and all uppercase characters is greater than 0, i.e. there is one uppercase character or more
        return False
    if not(len(split_password.intersection(set(string.ascii_lowercase))) >= 1):
        return False
    if not(len(split_password.intersection(set(string.digits))) >= 1):
        return False
    if not(len(split_password.intersection(set(['!','@','#','$','%','^','&','*']))) >= 1):
        return False
    if not(len(password)) >= 6:
        return False
    return True