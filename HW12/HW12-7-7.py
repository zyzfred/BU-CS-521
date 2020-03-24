class LinearEquation:
  # class variables
  a = int()
  b = int()
  c = int()
  d = int()
  e = int()
  f = int()
  # constructor
  def __init__(self, a, b, c, d, e, f):
    self.a = a
    self.b = b
    self.c = c
    self.d = d
    self.e = e
    self.f = f
  # accessors
  def getA(self):
    return self.a

  def getB(self):
    return self.b

  def getC(self):
    return self.c

  def getD(self):
    return self.d

  def getE(self):
    return self.e

  def getF(self):
    return self.f
  # functions
  def isSolvable(self):
    result = self.getA() * self.getD() - self.getB() * self.getC()
    if result != 0:
      return True
    else:
      return False

  def getX(self):
    upper = self.getE() * self.getD() - self.getB() * self.getF()
    lower = self.getA() * self.getD() - self.getB() * self.getC()
    return upper / lower

  def getY(self):
    upper = self.getA() * self.getF() - self.getE() * self.getC()
    lower = self.getA() * self.getD() - self.getB() * self.getC()
    return upper / lower

user_input = input('Please enter values for a, b, c, d, e, f (separated by \", \"): ')
input_list = user_input.split(', ')
a = eval(input_list[0])
b = eval(input_list[1])
c = eval(input_list[2])
d = eval(input_list[3])
e = eval(input_list[4])
f = eval(input_list[5])

testObj = LinearEquation(a, b, c, d, e, f)

if testObj.isSolvable() == False:
  print('The equation has no solution.')
else:
  print('x is ' + str(testObj.getX()) + ' and y is ' + str(testObj.getY()))
