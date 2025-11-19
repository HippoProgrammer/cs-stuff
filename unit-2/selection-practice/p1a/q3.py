# Write a program that asks for a number. If the number is positive, display "Positive number". If it's negative, display "Negative number". If it's zero, display "Zero".

num = int(input('Number: '))

if num == 0:
    print('Zero')
elif abs(num) == num:
    print('Positive number')
else:
    print('Negative number')