# Write a program for a cinema ticket system. Ask for age and day of the week. Apply these rules:

#Under 12: £5
#12-17: £7
#18-64: £10
#65+: £6
#On Tuesdays: everyone gets £2 off

def dayInput(prompt):
    dayAliases = {
        'Mon':0,
        'Monday':0,
        'Tue':1,
        'Tues':1,
        'Tuesday':1,
        'Wed':2,
        'Weds':2,
        'Wednesday':2,
        'Thu':3,
        'Thurs':3,
        'Thursday':3,
        'Fri':4,
        'Friday':4,
        'Sat':5,
        'Saturday':5,
        'Sun':6,
        'Sunday':6
    }
    rawInput = input(prompt)
    try:
        return dayAliases[rawInput]
    except KeyError:
        return -1

age = int(input('Age: '))
day = dayInput('Day: ')

price = 0

if age < 12:
    price += 5
elif age <=17:
    price += 7
elif age <=64:
    price += 10
else:
    price += 6

if day == 1:
    price -= 2

print(price)