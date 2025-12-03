with open('/workspaces/cs-stuff/advent-of-code/day-3/input.txt') as file:
    inputData = file.read()
inputList = inputData.split('\n')

def maxJoltage(batString):
    highest = 0
    for bat1 in range(len(batString)):
        for bat2 in range(int(bat1) + 1, len(batString)):
            for bat3 in range(int(bat2) + 1, len(batString)):
                for bat4 in range(int(bat3) + 1, len(batString)):
                    for bat5 in range(int(bat4) + 1, len(batString)):
                        for bat6 in range(int(bat5) + 1, len(batString)):
                            for bat7 in range(int(bat6) + 1, len(batString)):
                                for bat8 in range(int(bat7) + 1, len(batString)):
                                    for bat9 in range(int(bat8) + 1, len(batString)):
                                        for bat10 in range(int(bat9) + 1, len(batString)):
                                            for bat11 in range(int(bat10) + 1, len(batString)):
                                                for bat12 in range(int(bat11) + 1, len(batString)):
                                                    if int(batString[bat1]+batString[bat2]+batString[bat3]+batString[bat4]+batString[bat5]+batString[bat6]+batString[bat7]+batString[bat8]+batString[bat9]+batString[bat10]+batString[bat11]+batString[bat12])) > highest:
                                                        highest = int(sum(batString[bat1],batString[bat2],batString[bat3],batString[bat4],batString[bat5],batString[bat6],batString[bat7],batString[bat8],batString[bat9],batString[bat10],batString[bat11],batString[bat12]))
    return highest

total = 0
for battery in inputList:
    total += maxJoltage(battery)
print(total)