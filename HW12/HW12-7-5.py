import math

class RegularPolygon:
  # class variables
  n = int()
  side = float()
  x = float()
  y = float()
  # constructor
  def __init__(self):
    self.n = 3
    self.side = 1
    self.x = 0
    self.y = 0
  # accessors
  def getNumberOfSides(self):
    return self.n
  
  def getLengthofSides(self):
    return self.side
  
  def getX(self):
    return self.x

  def getY(self):
    return self.y

  # mutators
  def modifyNumberOfSides(self, n):
    self.n = n

  def modifyLengthOfSides(self, n):
    self.side = n

  def modifyX(self, n):
    self.x = n

  def modifyY(self, n):
    self.y = n

  # functions
  def getPerimeter(self):
    return self.side * self.n

  def getArea(self):
    return (self.n * pow(self.side, 2)) / (4 * math.tan(math.pi/self.n))

testObj1 = RegularPolygon()
testObj2 = RegularPolygon()
testObj3 = RegularPolygon()

testObj2.modifyNumberOfSides(6)
testObj2.modifyLengthOfSides(4)

testObj3.modifyNumberOfSides(10)
testObj3.modifyLengthOfSides(4)
testObj3.modifyX(5.6)
testObj3.modifyY(7.8)

obj_list = []
obj_list.append(testObj1)
obj_list.append(testObj2)
obj_list.append(testObj3)

n = 1
for obj in obj_list:
  print('Perimeter of object ' + str(n) + ': ' + str(obj.getPerimeter()))
  print('Area of object ' + str(n) + ': ' + str(obj.getArea()))
  n += 1