import math
class Circle():
    def __init__(self,radius):
        self.radius = float(input("ENTER THE RADIUS: "))

    def perimeter(self):
        return 2*math.pi*self.radius

    def area(self):
        return math.pi * self.radius**2

    def Display(self):
        print("The perimeter of the circle is ", self.perimeter())
        print("The area of the circle is", self.area())

measurements = Circle(input)
measurements.Display()