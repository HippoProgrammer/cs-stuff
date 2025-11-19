# Create a tax calculator program. Ask for annual income. Calculate tax using these bands:

#£0-£12,570: 0% tax (personal allowance)
#£12,571-£50,270: 20% tax on amount above £12,570
#£50,271-£150,000: 20% on first band + 40% on amount above £50,270
#Over £150,000: 20% on first band + 40% on second band + 45% on amount above £150,000

print('THIS PROGRAM IS NOT LICENSED BY HMRC AND IS NOT AFFILIATED WITH HIS MAJESTY\'S GOVERNMENT OF GREAT BRITAIN AND NORTHERN IRELAND')
print('THIS PROGRAM SHOULD NOT BE USED FOR THE CALCULATION OF REAL-WORLD TAXATION AMOUNTS UNDER ANY CONDITIONS')

income = int(input('Income: '))

tax = 0

if income <= 12570:
    print('No tax, personal allowance')
elif income <= 50270:
    tax += (income - 12570) * 0.2
elif income <= 150000:
    tax += (50270 - 12570) * 0.2
    tax += (income - 50270) * 0.4
else:
    tax += (50270 - 12570) * 0.2
    tax += (150000 - 50270) * 0.4
    tax += (income - 150000) * 0.45

print(tax)