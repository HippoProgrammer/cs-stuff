''' A binary testing program
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
import random, time
print(''' binary-conversion-tester.py  Copyright (C) 2026  HippoProgrammer
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions.''')

min_val = 1
max_val = 256

print('Binary Conversion Tester')
print('Press CTRL-C to exit program.')
while True:
    try:
        print('Options:\n1.Denary -> Binary\n2.Binary -> Denary\n3.Denary -> Hex\n4.Hex -> Denary\n5.Binary -> Hex\n6.Hex -> Binary')
        option = int(input('Select an option (1/2/3/4/5/6): '))
        correct = 0
        incorrect = 0
        start_time = 0
        questions = 0
    except KeyboardInterrupt:
        print('\nExiting. Thanks for playing!')
        break
    print('Session started. Press CTRL-C to stop session.')
    while True:
        try:
            start_time = time.time()
            int_value = random.randint(min_val,max_val)
            questions += 1
            if option == 1:
                value = int_value
                print(f'Convert {value}.')
                answer = '{:b}'.format(int_value)
                if input('Answer: ') == answer:
                    print(f'Correct! It is {answer}!')
                    correct += 1
                else:
                    print(f'Incorrect. Correct answer: {answer}')
                    incorrect += 1
            elif option == 2:
                value = '{:b}'.format(int_value)
                print(f'Convert {value}.')
                answer = str(int_value)
                if input('Answer: ') == answer:
                    print(f'Correct! It is {answer}!')
                    correct += 1
                else:
                    print(f'Incorrect. Correct answer: {answer}')
                    incorrect += 1
            elif option == 3:
                value = int_value
                print(f'Convert {value}.')
                answer = '{:x}'.format(int_value)
                if input('Answer: ') == answer:
                    print(f'Correct! It is {answer}!')
                    correct += 1
                else:
                    print(f'Incorrect. Correct answer: {answer}')
                    incorrect += 1
            elif option == 4:
                value = '{:x}'.format(int_value)
                print(f'Convert {value}.')
                answer = str(int_value)
                if input('Answer: ') == answer:
                    print(f'Correct! It is {answer}!')
                    correct += 1
                else:
                    print(f'Incorrect. Correct answer: {answer}')
                    incorrect += 1
            elif option == 5:
                value = '{:b}'.format(int_value)
                print(f'Convert {value}.')
                answer = '{:x}'.format(int_value)
                if input('Answer: ') == answer:
                    print(f'Correct! It is {answer}!')
                    correct += 1
                else:
                    print(f'Incorrect. Correct answer: {answer}')
                    incorrect += 1
            elif option == 6:
                value = '{:x}'.format(int_value)
                print(f'Convert {value}.')
                answer = '{:b}'.format(int_value)
                if input('Answer: ') == answer:
                    print(f'Correct! It is {answer}!')
                    correct += 1
                else:
                    print(f'Incorrect. Correct answer: {answer}')
                    incorrect += 1
        except KeyboardInterrupt:
            end_time = time.time()
            total_time = end_time - start_time
            avg_time = round(total_time / questions,1)
            percentage_correct = round(correct * 100 / questions,1)
            print(f'Session completed. {percentage_correct}% correct. {avg_time}s per question on average.')
            break