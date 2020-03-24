def getPentagonalNumber(n):
  return n * (3 * n - 1) / 2

def main():
  l = []
  for i in range(1, 101):
    l.append(str(getPentagonalNumber(i)))
    if i % 10 == 0:
      print(', '.join(l))
      l = []

main()