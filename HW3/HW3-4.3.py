a, b, c, d, e, f = eval(input('Enter a, b, c, d, e, f: '))

testVal = a * d - b * c

if testVal == 0:
  print('The equation has no solution')
else:
  x = (e * d - b * f) / (a * d - b * c)
  y = (a * f - e * c) / (a * d - b * c)
  print('x is', x, 'and y is', y)
