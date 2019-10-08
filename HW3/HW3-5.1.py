p = 0
n = 0
c = 0
total = 0
x = eval(input('Enter an integer, the input ends if it is 0: '))

if x == 0:
  print('You didn\'t enter any number')
else:
  while x != 0:
    if x > 0:
      p = p + 1
    elif x < 0:
      n = n + 1
    else:
      break
    c = c + 1
    total = total + x
    x = eval(input('Enter an integer, the input ends if it is 0: '))
	
print('The number of positives is', p)
print('The number of negatives is', n)
print('The total is', total)
print('The average is', total / c)