print('Kilograms      Pounds')
for i in range(1, 200):
  w = round(i * 2.2, 1)
  if i < 5:
    print(i, '               ', w)
  elif i < 10:
    print(i, '              ', w)
  elif i < 46:
    print(i, '             ', w)
  elif i < 100:
    print(i, '            ', w)
  else:
    print(i, '           ', w)