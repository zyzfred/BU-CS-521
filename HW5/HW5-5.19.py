# get a number
lines = eval(input("Enter the number of lines: "))
space = '   '

for i in range(lines):
  # initial a list
  x = i + 1
  list_a = []
  # append each number
  for n in range(x):
    list_a.append(str(n + 1))
  # reverse
  list_b = list_a[:0:-1]
  list_c = list_b + list_a
  
  if lines >= 10:
    if x < 10:
      print((lines - 9) * ' ' + space * (lines - x) + '  '.join(list_c))
    else:
      print((lines - x) * ' ' + space * (lines - x) + '  '.join(list_c))
  else:
    print(space * (lines - x) + '  '.join(list_c))
