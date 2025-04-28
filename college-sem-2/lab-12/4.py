import math
class regular_shape:
    def __init__(self,n,len):
        self.sides=n
        self.len=len
    def area(self):
        return (self.sides*self.len**2)/(4*math.tan(math.pi/self.sides))
    def perimeter(self):
        return self.sides*self.len
square=regular_shape(4,5)
print(square.area())
print(square.perimeter())

        
