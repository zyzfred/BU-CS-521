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
  
# delete the char to the left of the cursor 
def cmd_X(l, line_id, delta):
  # if not last char
  if len(l[line_id][:delta]) > 1:
    # if delta > 0
    if delta > 0:
      left = l[line_id][:delta - 1]
      right = l[line_id][delta:]
      delta -= 1
      l[line_id] = left + right

  # if last char
  else:
    # if not not first line
    if delta == 1:
      # remove this element
      l.pop(line_id)
      # if not first line
      if line_id > 0:
        line_id -= 1
        delta = len(l[line_id])
      else:
        delta = 0

  return l, line_id, delta
  
def main():

  l_init = READ.split('\n')
  line_id_init = random.randint(0, len(l_init) - 1)
  delta_init = random.randint(0, len(l_init[line_id_init]) - 1)
  
  print_list_file(l_init, line_id_init, delta_init)

  l, line_id, delta = cmd_X(l_init, line_id_init, delta_init)
  print_list_file(l, line_id, delta)

main()

