# Create a program that asks for someone's age and whether they have a driving license (yes/no). Only display "You can drive" if they are 17 or over AND have a license. Otherwise display "You cannot drive".

def getLicense(prompt = 'License (y/N)? '):
    rawInput = input(prompt)
    if rawInput.lower() == 'y':
        return True
    else:
        return False

age = int(input('Age? '))
license = getLicense()

if age >= 17 and license:
    print('You can drive')
else:
    print('You cannot drive')