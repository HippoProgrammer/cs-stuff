# Write a program that asks for a year. Determine if it's a leap year using these rules:

#Divisible by 4: leap year
#BUT if divisible by 100: not a leap year
#UNLESS also divisible by 400: then it IS a leap year

year = int(input('Year: '))

if year % 400 == 0:
    print('Leap year')
elif year % 100 == 0:
    print('Not a leap year')
elif year % 4 == 0:
    print('Leap year')
else:
    print('Not a leap year')