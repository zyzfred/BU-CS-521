import math
n = eval(input('Enter the number of sides: '))
s = eval(input('Enter the number side: '))
Area = n * pow(s, 2) / (4 * math.tan(math.pi / n))
print('The area of the polygon is', Area)