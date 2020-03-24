def displaySortedNumbers(num1, num2, num3):
  l = []
  l.append(num1)
  l.append(num2)
  l.append(num3)
  l = sorted(l)
  print('The sorted numbers are:',' '.join(l))

def main():
  user_input_s = input('Please enter three numbers separated by \', \': ')
  user_input_l = user_input_s.split(', ')
  displaySortedNumbers(user_input_l[0], user_input_l[1], user_input_l[2])

main()