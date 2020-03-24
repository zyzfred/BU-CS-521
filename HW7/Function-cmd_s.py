import random

READ = """the book of 
unknown 
Americans is
the book I am
reading"""

SEP = '^'

def print_list_file(l,line_id, delta):
  # if l exists
  if len(l) > 0:
    mid_line = l[line_id]
    mid_str= mid_line[0: delta] + SEP + mid_line[delta:]
    left_list = l[  : line_id]
    left_str = '\n'.join(left_list) 
    right_list = l[line_id + 1 : ]
    right_str = '\n'.join(right_list)
    print(left_str + '\n' + mid_str  + '\n' + right_str)
    print('\n ----------------- ')
  else:
    print(SEP)
  
# cursor moves to next space
def cmd_s(l, line_id, delta):
  for i in range(line_id, len(l)):
    if i == line_id:
      pos = l[i].find(' ', delta, len(l[i]))
    else:
      pos = l[i].find(' ')
    
    if pos >= 0:
      delta = pos
      line_id = i
      break
  
  return l, line_id, delta
  
def main():

  l_init = READ.split('\n')
  line_id_init = random.randint(0, len(l_init) - 1)
  delta_init = random.randint(0, len(l_init[line_id_init]) - 1)
  
  print_list_file(l_init, line_id_init, delta_init)

  l, line_id, delta = cmd_s(l_init, line_id_init, delta_init)
  print_list_file(l, line_id, delta)


main()


