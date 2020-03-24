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

input1 = input('Enter the points of the first line segment: ')
input2 = input('Enter the points of the second line segment: ')
list_input1 = input1.split(', ')
list_input2 = input2.split(', ')
x1 = eval(list_input1[0])
y1 = eval(list_input1[1])
x2 = eval(list_input1[2])
y2 = eval(list_input1[3])
x3 = eval(list_input2[0])
y3 = eval(list_input2[1])
x4 = eval(list_input2[2])
y4 = eval(list_input2[3])

a = (y2 - y1) / (x2 - x1)
b = -1
e = y2 + a * x2
c = (y4 - y3) / (x4 - x3)
d = -1
f = y4 + d * x4

print(a,b,c,d,e,f)

result = LinearEquation(a, b, c, d, e, f)
if result.isSolvable == -1:
  print('No intersecting points')
else:
  print('The intersecting point is: ' + str(result.getX()) + ', ' + str(result.getY()))