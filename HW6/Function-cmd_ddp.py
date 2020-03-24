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

# transpose to adjecent lines
def cmd_ddp(x, pos):
  # split two n lines
  l = x.split('\n')
  remain = pos
  # know which line it is 
  line_number, remain = find_line_helper(l, remain)
  # if in the middle 
  if line_number != 0 and line_number != len(l) - 1:
    # init a new list
    new_l = []
    # form new list
    for i in range(len(l)):
      if i == line_number - 1:
        new_l.append(l[line_number + 1])
      elif i == line_number + 1:
        new_l.append(l[line_number - 1])
      else:
        new_l.append(l[i])
    # pos
    pos = 0
    for i in range(line_number):
      pos = pos + len(new_l[i]) + 1
    pos = pos + remain
    #form new string
    x = '\n'.join(new_l)

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

  s, pos = cmd_ddp(s_init, pos_init)
  print_file(s, pos)


main()