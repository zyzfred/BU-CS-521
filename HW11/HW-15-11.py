def reverseDisplay(s):
    return reverseDisplayHelper(s, len(s))

def reverseDisplayHelper(s, high):
  if high == 0:
    return ""
  else:
    return s[high - 1] + reverseDisplayHelper(s, high - 1)

def main():
  user_input = input("Please enter a string: ")
  print("The reversed string is:", reverseDisplay(user_input))

main()
