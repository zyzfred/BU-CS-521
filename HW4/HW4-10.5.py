s_1 = input('Enter ten numbers: ')
list_1 = s_1.split(' ')
list_2 = []

for num in list_1:
  if num in list_2:
    continue
  else:
    list_2.append(num)
    
s_2 = (' ').join(list_2)

print('The distinct numbers are:', s_2)