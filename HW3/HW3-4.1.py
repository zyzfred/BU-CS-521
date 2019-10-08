import math
a, b, c = eval(input('Enter a, b, c: '))

discriminant = math.pow(b, 2) - 4 * a * c
r1 = round((-b + math.sqrt(abs(discriminant))) / (2 * a), 6)
r2 = round((-b - math.sqrt(abs(discriminant))) / (2 * a), 6)

if discriminant == 0:
  print('The root is:', r1)
elif discriminant > 0:
  print('The roots are:', r1, 'and', r2)
else:
  print('The equation has no real roots')
