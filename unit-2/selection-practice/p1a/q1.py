# Write a program that asks the user for their age. If they are 18 or over, display "You can vote". Otherwise, display "You cannot vote yet".

age = int(input('Age: '))
if age >= 18:
    print('You can vote')
else:
    print('You cannot vote yet')

