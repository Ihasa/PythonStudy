import math

class Point:
    someValue = 10
    def __init__(self, iniX, iniY):
        self.x=iniX
        self.y=iniY
        self.__xysum=self.__sumxy(self.x,self.y)
    
    def __sumxy(self,x,y):
        return x+y

    def length(self):
        return math.sqrt((self.x**2)+(self.y**2))
    
    def add(self,x,y,/):
        self.x += x
        self.y += y
        

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
        print(str(self.__xysum))

class EmptyClass:
    pass

#インスタンスごとに値を追加できたりする
#1回しか使わない(クラス定義要らない)場合にはまあ使える
i = EmptyClass()
i.name="hoge"
i.value=44
print(i.name)


someP=Point(3,4)
someP2=Point(4,4)
someP2.y=40
#print(someP.__xysum) エラー
print(someP._Point__xysum) 
#言語仕様上private変数はないが、
#継承の際の問題(変数名が子クラスと被る)に対処するため
#先頭に__を付けた変数は_クラス名__変数名になる

someP.where_is()
someP2.where_is()

someP.add(1,2)
#someP2.add(x=3,y=2) #エラー。位置指定の引数しか受け付けない

print(someP.length())
print(someP2.length())
