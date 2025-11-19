# Create a program that asks for a test score (0-100). If the score is 50 or above, display "Pass". If the score is below 50, display "Fail".

score = int(input('Test score (0-100): '))

if score >= 50:
    print('Pass')
else:
    print('Fail')