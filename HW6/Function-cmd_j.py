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
  
# move up a line
def cmd_j(x, pos):
  # split two n lines
  l = x.split('\n')
  remain = pos
  # know which line it is 
  line_number, remain = find_line_helper(l, remain)
  # if not first line
  if line_number > 0:
    # init pos to 0
    pos = 0
    # plus each line
    if line_number >= 2:
      for i in range(line_number - 1):
        pos = pos + len(l[i]) + 1
    # plus remain
    if remain <= len(l[line_number])  + 1:
      pos += remain

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

  s, pos = cmd_j(s_init, pos_init)
  print_file(s, pos)


main()