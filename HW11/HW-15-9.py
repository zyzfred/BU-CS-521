def reverseDisplay(s):
  if len(s) == 0:
    return ""
  return s[-1] + reverseDisplay(s[:len(s) - 1])

def main():
  user_input = input("Please enter a string: ")
  print("The reversed string is:", reverseDisplay(user_input))

main()
