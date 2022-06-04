import math

class Point:
    def __init__(watakushi, iniX:float, iniY:float):
        watakushi.x:float=iniX
        watakushi.y:float=iniY

    def length(watakushi) -> float:
        return math.sqrt((watakushi.x**2)+(watakushi.y**2))
    
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

    def normal(watakushi,/):
        return Point.div(watakushi,watakushi.length())

if __name__ == "__main__":
    
    p1:Point = Point(3,4)
    p2:Point = Point(10,3)

    p3:Point = Point.add(p1,p2)
    print(p1.x, p1.y)
    print(p2.x, p2.y)
    print(p3.x, p3.y)

    print(p2.normal().length())
