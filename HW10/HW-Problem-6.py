dict_dna = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

def complementary(x, y):
  for i in range(len(x)):
    if dict_dna.get(x[i]) != y[len(y) - i - 1]:
      return False
      break
  return True


user_input1 = input("Please enter the first DNA sequence: ")
user_input2 = input("Please enter the second DNA sequence: ") 

if complementary(user_input1, user_input2):
  print("Two DNA sequences match")
else:
  print("Two DNA sequences do not match")