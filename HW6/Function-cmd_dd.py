import random

READ = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated."""

READ_list = list(READ)

CURSOR = '^'

def print_file(x, pos):
  left = x[:pos]
  right = x[pos:]
  print(left + CURSOR + right)

# delete current line and move cursor to the begginning of the next line
def cmd_dd(x, pos):
  # split two n lines
  l = x.split('\n')
  # at list one line
  if len(l) > 0:
    # know which line it is 
    line_number, pos = find_line_helper(l, pos)
    # pos set to 0
    pos = 0
    new_l = []
    # form a new list
    for i in range(len(l)):
      # if i != line_number
      if i != line_number:
        # append to list
        new_l.append(l[i])
    # join l
    x = '\n'.join(new_l)
    
    if line_number == 0:
      pos = 0
    elif line_number == len(new_l):
      pos = x.rfind('\n')
    else:
      for i in range(line_number):
        pos = pos + len(new_l[i]) + 1
    
    return x, pos
  else:
    return x, pos
	
# helper to find a line    
def find_line_helper(l, remain):

  line_number = 0 
  # find line number
  while remain > len(l[line_number]):
    remain = remain - len(l[line_number]) - 1
    line_number += 1
  
  return line_number, remain

def main():

  s_init = READ
  pos_init = random.randint(0, len(READ) - 1)
  
  print_file(s_init, pos_init)
  print("")

  s, pos = cmd_dd(s_init, pos_init)
  print_file(s, pos)


main()