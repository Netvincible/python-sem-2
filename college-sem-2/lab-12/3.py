import math
class solid:
    def __init__(self,solid,l,h=0,b=0):
        self.solid=solid
        if self.solid=="sphere":
            self.radius=l
        elif self.solid=="cone":
            self.radius=l
            self.height=h
        elif self.solid=="cuboid":
            self.length=l
            self.height=h
            self.breadth=b
        elif self.solid=="cube":
            self.length=self.breadth=self.height=l
        elif self.solid=="cylinder":
            self.radius=l
            self.height=h
        else:
            return "invalid solid type"
        
    def volume(self):
        if self.solid=="sphere":
            return 4*math.pi*(self.radius**3)/3
        elif self.solid=="cone":
            return math.pi*self.height*(self.radius**2)/3
        elif self.solid=="cuboid":
            return self.length*self.breadth*self.height
        elif self.solid=="cube":
            return self.length**3
        elif self.solid=="cylinder":
            return math.pi*self.height*(self.radius**2)
    def surface_area(self):
        if self.solid=="sphere":
            return 4*math.pi*(self.radius**2)
        elif self.solid=="cone":
            return math.pi*self.radius*(self.radius+(self.height**2 + self.radius**2)**0.5)
        elif self.solid=="cuboid":
            return 2*(self.height*self.length+self.length*self.breadth+self.breadth*self.height)
        elif self.solid=="cube":
            return 6*self.length**2
        elif self.solid=="cylinder":
            return 2*math.pi*self.height*(self.radius)+math.pi*self.radius**2

sphere=solid("sphere",2)
print(sphere.volume())
print(sphere.surface_area())

cone=solid("cone",3,4)
print(cone.volume())
print(cone.surface_area())

cuboid=solid("cuboid",2,3,4)
print(cuboid.volume())
print(cuboid.surface_area())

cube=solid("cube",4)
print(cube.volume())
print(cube.surface_area())

cylinder=solid("cylinder",3,4)
print(cylinder.volume())
print(cylinder.surface_area())