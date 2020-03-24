def gcd(m, n):
  if m % n == 0:
    return n
  else:
    return gcd(n, m % n)

def main():
  input1 = eval(input("Please enter the first number: "))
  input2 = eval(input("Please enter the second number: "))
  print("Their greatest common divisor is:", gcd(input1, input2))

main()