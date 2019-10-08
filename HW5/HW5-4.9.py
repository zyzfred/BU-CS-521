my_pack1 = dict()
my_pack2 = dict()
# enter price and package for pack 1
user_input1 = input("Enter weight and price for package 1: ")
# save value to pack 1 
key_1, value_1 = user_input1.split(",")
# enter price and package for pack 2
user_input2 = input("Enter weight and price for package 2: ")
# save value to pack 2
key_2, value_2 = user_input2.split(",")
# compare
rate_1 = eval(key_1) / eval(value_1)
rate_2 = eval(key_2) / eval(value_2)
# result 
if rate_1 < rate_2:
  print('Package 1 has the better price')
elif rate_1 == rate_2:
  print('Package 1 and Package 2 have the same price')
else:
  print('Package 2 has the better price')