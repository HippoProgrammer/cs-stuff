# Create a program that asks for the temperature in Celsius. If it's above 25, display "Hot". If it's 25 or below, display "Not hot".

temp = int(input('Temperature (*C): '))

if temp > 25:
    print('Hot')
else:
    print('Not hot')