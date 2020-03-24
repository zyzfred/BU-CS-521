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
  
# capitalize the left of the cursor
def cmd_C(x, pos):
  if ord(x[pos]) >= 97 and ord(x[pos]) <= 122:
    temp = chr(ord(x[pos]) - 32)
    return x[:pos - 1] + temp + x[pos:], pos
  else:
    return x, pos
  
def main():

  s_init = READ
  pos_init = random.randint(0, len(READ) - 1)
  
  print_file(s_init, pos_init)
  print("")

  s, pos = cmd_C(s_init, pos_init)
  print_file(s, pos)


main()


