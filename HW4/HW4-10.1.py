s = input('Enter scores: ')
s_list = s.split(' ')
g_max = int(max(s_list))

for i, score in enumerate(s_list):
  score = int(score)
  if score >=  g_max - 10:
    grade = 'A'
  elif score >=  g_max - 20:
    grade = 'B'
  elif score >=  g_max - 30:
    grade = 'C'
  elif score >= g_max - 40:
    grade = 'D'
  else:
    grade = 'F'
  print('Student', i, 'score is', s_list[i], 'and grade is', grade)