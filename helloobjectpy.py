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
    def addAndMul(self,x,y,*,multi=1):
        self.add(x,y)
        if(multi != 0):
            self.x *= multi
            self.y *= multi
        

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

def argTest(arg1,arg2,*args1, **args2):
    print("arg1 is "+arg1)
    print("arg2 is "+arg2)
    for a in args1:
        print("args1...", a)
    for a in args2:
        print("args2["+a+"] is "+args2[a])

argTest("hoge", "foo",
 "how are you?", "this is a pen.", #*args1に入る。あふれた位置引数がここに入る。リストではなくタプルになる。(1,2,3,4,5)とか
 color="blue", size="big", length="3.4" #**args2に入る。存在しないキーワード指定引数がここに入る
 #,arg1="what" #エラー。同じ名前の引数は1回しか渡せない
 #,"What's wrong?" #エラー。位置引数はキーワード引数の前だけ
 )

for x in (1,2,3,4,5):
     print(x)


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
print((str)(someP.x)+","+(str)(someP.y))

someP.addAndMul(1,2,multi=3)

print((str)(someP.x)+","+(str)(someP.y))

print(someP.length())
print(someP2.length())
