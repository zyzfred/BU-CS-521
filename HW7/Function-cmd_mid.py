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
  
# put cursor in the middle
def cmd_middle(l):
  sum_len = 0
  for i in range(len(l)):
    sum_len += len(l[i])
  
  middle = sum_len // 2
  middle_line = 0

  while middle > 0:
    if middle - len(l[middle_line]) > 0:
      middle_line += 1
    else:
      middle_pos = middle
    middle -= len(l[middle_line])
  
  return l, middle_line, middle_pos

def main():

  l_init = READ.split('\n')
  line_id_init = random.randint(0, len(l_init) - 1)
  delta_init = random.randint(0, len(l_init[line_id_init]) - 1)
  
  print_list_file(l_init, line_id_init, delta_init)

  l, line_id, delta = cmd_middle(l_init)
  print_list_file(l, line_id, delta)

main()