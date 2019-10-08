import math
# Compute the standard deviation of values
def deviation(x):
  mean_minor = mean(x)
  numerator = 0
  denomination = 0
  # numerator
  for number in x:
      numerator += pow(number - mean_minor, 2)
  # denomination
  denomination = len(x) - 1
  # return 
  deviation = round(math.sqrt(numerator / denomination), 6)
  return deviation
  
# Compute the mean of a list of values
def mean(x):
  # return mean
  return round(sum(x) / len(x),2)

# Main
def main():
  # input
  numbers_input = input("Enter numbers: ")
  # list
  numbers_list = numbers_input.split(' ')
  # change str to number
  for i, number in enumerate(numbers_list):
    numbers_list[i] = eval(number)

  print("The mean is", mean(numbers_list))
  print("The standard deviation is",deviation(numbers_list))

main()