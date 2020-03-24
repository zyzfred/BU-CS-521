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
  
# write as text file and save
def cmd_wq(x):
  file_saved = open("test.txt", "w+")
  file_saved.write(x)
  file_saved.close()
  
def main():

  s_init = READ
  pos_init = random.randint(0, len(READ) - 1)
  
  print_file(s_init, pos_init)
  print("")

  cmd_wq(s_init)

main()




