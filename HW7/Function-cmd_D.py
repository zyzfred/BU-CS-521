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
  
# transpose
def cmd_D(l, line_id, delta):
  #has not to be the first and last
  is_first = is_first_char(line_id, delta)
  is_last = is_last_char(l, line_id, delta)

  if is_first == False and is_last == False:
    if delta > 0 and delta < len(l[line_id]):
      left_char = l[line_id][delta - 1]
      right_char = l[line_id][delta]
      left = l[line_id][: delta - 1]
      right = l[line_id][delta + 1:]
      l[line_id] = left + right_char + left_char + right
    else:
      if delta == 0:
        left_char = l[line_id - 1][-1]
        right_char = l[line_id][0]
        left = l[line_id - 1][:-1]
        right = l[line_id][1:]
        l[line_id] = left_char + right
        l[line_id - 1] = left + right_char
      elif delta == len(l[line_id]):
        left_char = l[line_id][-1]
        right_char = l[line_id + 1][0]
        left = l[line_id][:-1]
        right = l[line_id + 1][1:]
        l[line_id] = left + right_char
        l[line_id + 1] = left_char + right
 
  return l, line_id, delta
  
def main():

  l_init = READ.split('\n')
  line_id_init = random.randint(0, len(l_init) - 1)
  delta_init = random.randint(0, len(l_init[line_id_init]) - 1)
  
  print_list_file(l_init, line_id_init, delta_init)

  l, line_id, delta = cmd_D(l_init, line_id_init, delta_init)
  print_list_file(l, line_id, delta)

main()


