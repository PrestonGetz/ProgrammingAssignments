import math
class Circle_Calculator:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    def perimiter(self):
        return 2*math.pi*self.radius
your_radius=int(input('What is the radius?'))
a=Circle_Calculator(your_radius)
print('area =',a.area(),' perimiter =',a.perimiter())
