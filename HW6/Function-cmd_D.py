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
  
# transpose
def cmd_D(x, pos):
  if pos > 0 and pos < len(x) - 1:
    left = x[:pos - 1]
    right = x[pos + 1:]
    front = x[pos]
    back = x[pos - 1]
    return left + front + back + right, pos
  else:
    return x, po
  
def main():

  s_init = READ
  pos_init = random.randint(0, len(READ) - 1)
  
  print_file(s_init, pos_init)
  print("")

  s, pos = cmd_D(s_init, pos_init)
  print_file(s, pos)


main()


