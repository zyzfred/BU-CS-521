start = 312032846
year = 365
sec_one_year = 365 * 24 * 60 * 60
b = 7
d = 13
imm = 45
count = 0
while count < 5:
  start = start + sec_one_year//b - sec_one_year//d + sec_one_year//imm
  print(start)
  count = count + 1
  
	
