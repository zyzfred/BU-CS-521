def getNumber(uppercaseLetter):
  map_letter_number = {'a': '2', 'b': '2', 'c': '2', 'd': '3', 'e': '3', 'f': '3', 'g': '4', 'h': '4', 'i': '4', 'j': '5', 'k': '5', 'l': '5', 'm': '6', 'n': '6', 'o': '6', 'p': '7', 'q': '7', 'r': '7', 's': '7', 't': '8', 'u': '8', 'v': '8',  'w': '9', 'x': '9', 'y': '9', 'z': '9'}
  phone_number_list = list(uppercaseLetter)
  for i, c in enumerate(phone_number_list):
    if c.lower() in map_letter_number:
      phone_number_list[i] = map_letter_number[c.lower()]
  return ''.join(phone_number_list)

user_input = input('Enter a string: ')
print(getNumber(user_input))
