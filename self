"""
class: set of categories

objects: instances of class

self: represent the attributes and methods of a class

__init__: constructor. allowing initialization of a class

"""


class Rectangle:
    
    def __init__(self,length,breadth, unit_cost = 0):
        self.length = length
        self.breadth = breadth
        self.unit_cost = unit_cost
        
    def get_perimeter(self):
        return 2 * (self.length + self.breadth)

    def get_area(self):
        return self.length * self.breadth
    
    def calculate_cost(self):
        area = self.get_area()
        return area * self.unit_cost
    
r = Rectangle(160,120,2000)

print("area of rectangle: %s cm^2" %(r.get_area()))
print("cost of rectangular field: Rs. %s" %(r.calculate_cost()))
