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
  
# move cursor to the end of line
def cmd_e(x, pos):
  pos = x.find('\n', pos, len(x))
  if pos > 0:
    return x, pos
  else:
    return x, len(x)
  
def main():

  s_init = READ

  pos_init = random.randint(0, len(READ) - 1)
  
  print_file(s_init, pos_init)
  print("")

  s, pos = cmd_e(s_init, pos_init)
  print_file(s, pos)


main()


