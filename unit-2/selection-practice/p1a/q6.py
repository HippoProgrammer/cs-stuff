# Create a program that asks for two numbers. Display which number is larger, or if they are equal.

num1 = int(input('Number: '))
num2 = int(input('Number: '))

if num1 == num2:
    print('Equal')
elif num1 > num2:
    print(num1)
else:
    print(num2)