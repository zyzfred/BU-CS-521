def reverse(number):
  return eval(str(number)[::-1])

def isPalindrome(number):
  if number == reverse(number):
    return True
  else:
    return False

def main():
  user_input = eval(input('Please enter an integer: '))
  if isPalindrome(user_input) == True:
    print(user_input, 'is palindrome')
  else:
    print(user_input, 'is not palindrome')

main()