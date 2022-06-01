#第3章おためし
print("hello python.")

filename="savedata"
datestr="20220525"
somevalue=2000
print(filename+datestr)
print(filename+str(somevalue + 22)) #キャスト

a,b=0,2
while a < 20:
    print(a)
    a,b = b,a+b

array=[1,3,5,6,8,10]
arr=array[1:6]
arr[0] = 100
print(array)
print(arr)

#第4章おためし
usrinput=int(input("input..."))
if(usrinput < 0): #if usrinput < 0: のほうがpython流な気がするが、これでも動く
    print("val is "+str(x))
elif(usrinput < 10):
    print("less than 10")
elif(usrinput < 20): #else ifは無い
    print("less than 20")
else:
    print("you inputed a number")

list=[1,2,3,4,5,6,7]
list.append(8)
for a in list:
    print(a)
for i, value in enumerate(list): #インデックスと値のタプルを取得
    print("list["+str(i)+"] is "+ str(value))

#スマートなfor
for i in range(0,10):
    print(i)
else:
    pass #処理なし。構文上何かしら書かないといけないが、何もしたくない場合


for i in range(10,100,20):
    print(i)
else:
    print("loop is end") #繰り返しが正常に(break等以外で)終了した場合にelseが実行される
#rangeが返すのはListではなく、iterable型のオブジェクト
#Iteratorパターン。C#ならIEnumerableに相当

mydictionary={"apple": "red", "orange": "yellow", "sky": "blue"}
print(mydictionary["apple"]) #dictionaryも簡単に作れる(pythonではdict型)
for fruits,color in mydictionary.items():#KeyValuePairを取得
    print(fruits+" is "+color)


mydictionary["grape"] = "purple" #これでAddしたことになる
for fruits,color in mydictionary.items():#KeyValuePairを取得
    print(fruits+" is "+color)

#match文
value=40
#ただのswitch文として
match value:
    case 0:
        pass
    case 10:
        print("ten")
    case 40:
        print("fourty")
    case _:
        print("something")

pointtuple=(0,40)
match pointtuple:
    case (0,0):
        print("this is 0,0")
    case (0,y):
        print(f"x is 0 and y is {y}")
    case (x,0):
        print(f"y is 0 and x is {x}")
    case (x,y):
        print(f"X={x}, Y={y}")

