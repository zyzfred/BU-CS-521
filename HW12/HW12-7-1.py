class Rectangle:

  def __init__(self, width = 1, length = 2):
    self.width = width
    self.length = length

  def getArea(self):
    return self.width * self.length

  def getPerimeter(self):
    return 2 * (self.width + self.length)

Rec_list = []
Rectangle1 = Rectangle(4, 40)
Rectangle2 = Rectangle(3.5, 35.7)

Rec_list.append(Rectangle1)
Rec_list.append(Rectangle2)

n = 1
for rec in Rec_list:
  print('The width of rectangle ' + str(n) + ': ' + str(rec.width))
  print('The length of rectangle ' + str(n) + ': ' + str(rec.length))
  print('The area of rectangle ' + str(n) + ': ' + str(rec.getArea()))
  print('The perimeter of rectangle ' + str(n) + ': ' + str(rec.getPerimeter()))
  n += 1