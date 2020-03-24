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
  
# search 
def cmd_n(x, pos, s_input):

  left = x[:pos]
  right = x[pos:]
  # if find
  if right.find(s_input) != -1:
    pos = right.find(s_input) + len(left)
    return x, pos

  else:
    return x, pos
  
def main():

  s_init = READ
  pos_init = random.randint(0, len(READ) - 1)
  
  print_file(s_init, pos_init)
  print("")
  
  s_input = input("Enter a string: ")

  s, pos = cmd_n(s_init, pos_init, s_input)
  print_file(s, pos)


main()


