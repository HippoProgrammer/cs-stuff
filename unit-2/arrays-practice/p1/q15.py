def intArrayBuilder(prompt:str, loops:int):
    array = []
    for i in range(loops):
        array.append(int(input(prompt)))
    return array
def strArrayBuilder(prompt:str, loops:int):
    array = []
    for i in range(loops):
        array.append(str(input(prompt)))
    return array
students = int(input('Number of students: '))
studentNames = strArrayBuilder('Student name: ', students)
studentScores = intArrayBuilder('Student score: ', students)
maxStudentScore = 0
for score in studentScores:
    if score > maxStudentScore:
        maxStudentScore = score
maxStudentName = studentNames[studentScores.index(maxStudentScore)]
print(maxStudentName)