import random

counts = [None] * 10

for i in range(1000):
  # generates 1000 numbers between 0, 9
  random_number = random.randint(0, 9)
  # count
  if counts[random_number] == None:
    counts[random_number] = 1
  else:
    counts[random_number] += 1

# output 
for i, number in enumerate(counts):
  print(i, "displayed", number, "times")