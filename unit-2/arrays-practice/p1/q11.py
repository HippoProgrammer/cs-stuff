prices = [2.99, 5.50, 1.25, 8.00, 3.75]
discount = 0.1
discounted = []
multiplyFactor = 1 - discount
for price in prices:
    discounted.append(price * multiplyFactor)
print(discounted)