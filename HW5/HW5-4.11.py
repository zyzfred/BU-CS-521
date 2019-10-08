# dict month
dict_month = { 1: 'January', 2: 'Februray', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',9: 'September', 10: 'October', 11: 'November', 12: 'December' }
# day 30
day_31 = (1, 3, 5, 7, 8, 10, 12)
# day 31
day_30 = (4, 6, 9, 11)
# user input 
user_input = input('Enter month and year separated by space (' '): ')
key, value = user_input.split(' ')

month_input = eval(key)
year_input = eval(value)

if year_input % 4 == 0:
  if month_input == 2:
    print(dict_month[month_input], value, 'has 29 days')
  elif month_input in day_30:
    print(dict_month[month_input], value, 'has 30 days')
  elif month_input in day_31:
    print(dict_month[month_input], value, 'has 31 days')
else:
  if month_input == 2:
    print(dict_month[month_input], value, 'has 28 days')
  elif month_input in day_30:
    print(dict_month[month_input], value, 'has 30 days')
  elif month_input in day_31:
    print(dict_month[month_input], value, 'has 31 days')