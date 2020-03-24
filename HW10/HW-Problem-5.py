x = [2, -6, -3, 1, 19]
minor_count = 0
print("List before sort:", x)

for e in x:
  if e < 0:
    minor_count += 1

for i in range(len(x) - 1):
  for j in range(i, len(x)):
    if x[i] > x[j]:
      x[i], x[j] = x[j], x[i]

x[:] = x[minor_count:] + x[:minor_count]

print("List after sort:", x)