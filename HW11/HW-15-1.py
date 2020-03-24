def sumDigits(n):
  if n < 10:
    return n
  else:
    return n % 10 + sumDigits(n // 10)

def main():
  user_input = eval(input("Please enter a number: "))
  print("Sum of its digits is:", sumDigits(user_input))

main()