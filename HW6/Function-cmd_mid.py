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
  
# put cursor in the middle
def cmd_mid(x, pos):
  
  if len(x) != 0 and len(x) != 1:
    # split to lines
    l = x.split('\n')

    sum_size = 0
    for i in range(len(l)):
      sum_size += len(l[i])

    remain = sum_size // 2
    line_number = 0
    end_line_count = 0

    while remain - len(l[line_number]) > 0:
      remain -= len(l[line_number])
      end_line_count += 1
      line_number += 1
    
    pos = sum_size // 2 + end_line_count

    return x, pos
  else:
    return x, pos
  
def main():

  s_init = READ
  pos_init = random.randint(0, len(READ) - 1)
  
  print_file(s_init, pos_init)
  print("")

  s, pos = cmd_mid(s_init, pos_init)
  print_file(s, pos)


main()