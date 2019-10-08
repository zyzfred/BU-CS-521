ssn = input('Enter your Social Security number in the format ddd-dd-dddd: ')
ssn_list = list(ssn)

if len(ssn_list) != 11:
  print('Invalid SSN')
else:
  isValid = True
  
  for i, n in enumerate(ssn_list):
    n_ord = ord(n)
    if n_ord > 47 and n_ord < 58:
      if i == 3 or i == 6:
        isValid = False
        break
    else:
      if i == 3 and n_ord == 45:
        continue
      elif i == 6 and n_ord == 45:
	      continue
      else:
        isValid = False
        break

  if isValid == True:
    print('Valid SSN')
  else: 
    print('Invalid SSN')