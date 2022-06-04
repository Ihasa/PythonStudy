import math

class Point:
    def __init__(self, iniX:float, iniY:float):
        self.x:float=iniX
        self.y:float=iniY

    def length(self) -> float:
        return math.sqrt((self.x**2)+(self.y**2))
    
    def add(p1, p2, /):
        res=Point(p1.x, p1.y)
        res.x += p2.x
        res.y += p2.y
        return res
    
    def mul(p1, multi:float, /):
        return Point(p1.x * multi, p1.y * multi)

    def div(p1, div:float,/):
        return Point(p1.x / div, p1.y / div)
    
    def product(p1, p2, /) -> float:
        return p1.x * p2.x + p1.y * p2.y

    def normal(self,/):
        return Point.div(self,self.length())
