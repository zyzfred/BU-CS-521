count = 0

def fib(index):
  global count
  count += 1
  if index == 0:
    return 0
  elif index == 1:
    return 1
  else:
    return fib(index - 1) + fib(index - 2)

def main():
  global count
  user_input = eval(input('Please enter a index for fibonacci number: '))
  print('Fibonacci number at this index is:', fib(user_input))
  print('\'fib\' function is called by', count, 'times')


main()