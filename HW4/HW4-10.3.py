s = input('Enter integers between 1 and 100: ')
s_list = s.split(' ')
s_dict = dict()

for number in s_list:
  number = int(number)
  if number in s_dict.keys():
    s_dict[number] = s_dict[number] + 1
  else:
    s_dict[number] = 1

for number in sorted(s_dict.keys()):
  freq = s_dict[number]
  if freq < 2:
    t = 'time'
  else:
    t = 'times'
  print(number, 'occurs', freq, t)