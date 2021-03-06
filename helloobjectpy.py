import math

class Point:
    someValue = 10
    def __init__(self, iniX:int, iniY:int):
        self.x:int=iniX
        self.y:int=iniY
        self.__xysum=self.__sumxy(self.x,self.y)
    
    def __sumxy(self,x:int,y:int) -> int:
        return x+y

    def length(self) -> int:
        return math.sqrt((self.x**2)+(self.y**2))
    
    def add(self,x:int,y:int,/) -> None:
        self.x += x
        self.y += y
    def addAndMul(self,x:int,y:int,*,multi:float=1) -> None:
        self.add(x,y)
        if(multi != 0):
            self.x *= multi
            self.y *= multi
        

    def where_is(self) -> None:
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

def argTest(arg1:str,arg2:str,/,*args1, **args2) -> None:
    print("arg1 is "+arg1)
    print("arg2 is "+arg2)
    for a in args1:
        print("args1...", a)
    for a in args2:
        print("args2["+a+"] is "+args2[a])

argTest("hoge", "foo",
 "how are you?", "this is a pen.", #*args1に入る。あふれた位置引数がここに入る。リストではなくタプルになる。(1,2,3,4,5)とか
 color="blue", size="big", length="3.4" #**args2に入る。存在しないキーワード指定引数がここに入る
 ,arg1="what" #同じ名前の引数は1回しか渡せないが、位置引数かキーワード引数か明確なら渡せる
 #,"What's wrong?" #エラー。位置引数はキーワード引数の前だけ
 )

argTest("how","bar",**{"user":"Tom","password":"qwertyu"})
#user="Tom", password="qwertyu"と渡したのと同じ

def variadicTest(*args:iter,sep="/") -> None:
    print(sep.join(args)) #直感的でないが・・・

variadicTest("C:","Program Files", "Python", "bin")
variadicTest("C:","Program Files(x86)", "Python", "bin", sep="\\")
variadicTest(*["C:","Program Files", "Python", "bin"]) #アンパック　リスト
variadicTest(*("C:","Program Files", "Python", "bin")) #アンパック　タプル
#variadicTest(("C:","Program Files", "Python", "bin")) #これだと確かにタプル渡しになってしまう

for x in (1,2,3,4,5):
     print(x)

def printSum(ite) -> None:
    res=0
    for x in ite:
        res += x
    print("sum for ")
    print(ite)
    print("is ")
    print(res)

printSum((3,4,5))
printSum(range(3,6))
a = [3,6]
printSum(range(*a)) #range(3,6)と渡したのと同じ

def mymap(ite, f) -> list:
    """simple map function.
    
    ite : iterable, f : map function
    """
    res=[]
    for x in ite:
        res.append(f(x))
    return res

print(mymap(range(1,11), lambda x:x*2))
fn = lambda x : x**2
print(mymap(range(1,11), fn))

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
