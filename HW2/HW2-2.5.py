subtotal, rate = eval(input('Enter the subtotal and gratuity rate: '))
rate = rate / 100
gratuity = round(subtotal * rate, 2)
total = round(subtotal + gratuity, 2)
print('The gratuity is', gratuity, 'and the total is', total)