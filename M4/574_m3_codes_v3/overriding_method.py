class Parent: # define parent class
  def myMethod(self):
    print("Calling parent method")
class Child(Parent): # define child class
  def myMethod(self):
    print("Calling child method")
c = Child()   # instance of child
c.myMethod() # child calls overridden method


#Another Example:

class Rectangle():
  def __init__(self,length,breadth):
    self.length = length
    self.breadth = breadth
  def getArea(self):
    print(self.length*self.breadth," is area of rectangle")

class Square(Rectangle):
  def __init__(self,side):
    self.side = side
    Rectangle.__init__(self,side,side)
  def getArea(self):
    print(self.side*self.side," is area of square")

s = Square(4)
r = Rectangle(2,4)
s.getArea()
r.getArea()
