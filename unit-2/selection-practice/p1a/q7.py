# Write a program that asks for a student's percentage score. Use if-elif-else to assign a grade:

# 70% or above: Grade A
# 60-69%: Grade B
# 50-59%: Grade C
# Below 50%: Grade D

percent = int(input('Percentage (%): '))

if percent >= 70:
    print('A')
elif percent >= 60:
    print('B')
elif percent >= 50:
    print('C')
else:
    print('D')
