class Point:
    someValue = 10
    def __init__(self, iniX, iniY):
        self.x=iniX
        self.y=iniY
        

    def where_is(self):
        match self:
            case Point(x=0, y=0):
                print("Origin")
            case Point(x=0, y=y):
                print(f"Y={y}")
            case Point(x=x, y=0):
                print(f"X={x}")
            case Point():
                print("Somewhere else")
            case _:
                print("Not a point")

someP=Point(0,45)
someP2=Point(4,0)
someP2.y=40

someP.where_is()
someP2.where_is()
