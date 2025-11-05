from random import randint
randoms = []
for i in range(10):
    randoms.append(randint(1,100))
# this could be done using sum(), but let's use a loop
totalRandoms = 0
for number in randoms:
    totalRandoms += number

average = totalRandoms / len(randoms)
print(average)