stack:list = list(range(0,11))
print(stack)

stack.append(3)
stack.extend([40]) #リストを後ろにくっつける
stack[len(stack):] = [11] #appendに同じ
#stack[3:]=[12,13] #3番目以降を指定したリストで置き換える
#...list[n:m]でn個目からm個目の直前までを示すのだった
stack[3:5] = [44,64,7,4] #エラーにならない・・・
print(stack)

stack.pop() 
#stack.pop(0) #こうすればqueueが簡単に作れるが、遅い。collection.dequeを使うこと
print(stack, "length is ", len(stack), ",count of 3 is ", stack.count(3))
#countはその要素が出てくる数を数えるだけ、lenが長さ
stack.sort() #引数なしなら、'<'比較演算子を使ってソートを試みる
print(stack)

stack.sort(key=lambda x : x % 10) #keyで任意の比較ができる reverseでその逆順にソートできる
print(stack)

#リスト内包表記を使うと、mapやfilterを使った初期化ができる
# l = [x * x | x <- [0..10]] ←haskell流

#使わない場合
sqlist = list(map(lambda x : x ** 2, range(0,11)))
print(sqlist)

#使う場合(mapのみ)
sqlist2 = [x ** 2 for x in range(0,11)]
print(sqlist2)

#[バインドした変数を使った式 for バインドする変数 in iterableオブジェクト if フィルタ条件]
sqlist3 = [x ** 2 for x in range(0,11) if x ** 2 % 2 != 0]
print(sqlist3)


mat = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

#平坦化する
mat2 = [r[i] for r in mat for i in range(0,len(r))]
print(mat2)
#以下と同じ
res = []
for r in mat:
    for i in range(0,len(r)):
        res.append(r[i])
print(res)

#内包表記を使って、2次元配列の行と列を入れ替える
mat2 = [[r[i] for r in mat] for i in range(0,4)]
#以下と同じ
res2 = []
for i in range(0,4):
  tmp = []
  for r in mat:
      tmp.append(r[i])
  res2.append(tmp)

#実はzip(*mat)としても同じ結果になる
res3 = list(zip(*mat))
print(res3)

l = ["Apple", "Orange", "Grape"]
#zipは例えばこうしてタプルを作るために使う
for x in zip(range(0,3), l):
    print(x)

print(mat2)
print(res2)

#タプルとリストとrange
#タプル:
# 不変オブジェクト
# 中身の型はバラバラである場合が多い
# アンパックを使って、即席の構造体として使う
tup = (12456, "qwerty", "Stevenson")
id, password, name = tup
print("ID-",id," is ",name,", pass=",password)

#これは内部的にはタプルのパック・アンパックを行っているだけ
a,b = 0,1

#リスト:
# おなじみのリスト。可変オブジェクト。省略

#range:
# 不変オブジェクト
# range(0,4)とかかいていたが、これは関数じゃなくオブジェクトだった
# iterableであるので、lenなどに渡せる

print(len(range(0,10)))
print(range(0,10)[9]) #エラーにならない。x[n]で値を参照するのは、iterableすべてに対してできる?
print(range(10)) #これはそのままrange(0, 10)と表示される


#Set(集合)を扱える
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) #重複なしになる
print("orange" in basket)

#{}で初期化するか、set(iterable)を使って作成
l = [1,2,3,1,2,3,6,4,3,3,1,5]
nums = set(l)
print(nums)

#内包も使える
numsEven={x for x in l if x % 2 == 0}
print(numsEven)


#便利なdict(辞書)型
#キーが不変型
#タプルもキーにできるが、要素として可変なオブジェクトを持つタプルはダメ
#集合のそれぞれの要素に対して何かしらの値を紐づけたものと考えるといい
passlist={"tom":"qwerty", "jim":"19890123", "steve":"c1aF+Er20111118"}
passlist["alex"] = "diamond4me"
for x in passlist: #iteratorとしてはKeyのほうだけ取得する
    print(x)
for t in passlist.items(): #こうするとKeyValuePairとなるタプルとして取得するので、アンパックを使ったほうがいい
    print(t)

#その他
#reversed(x)でシーケンスの順序逆転
#enumerate(x)でリスト等に対してもインデックスと要素のタプルとして取得できる
print(enumerate(reversed(range(1,11)))) #これはenumerateオブジェクト。また別モノ
#APIリファレンスを見ても、いまいちどんな型との関連があるのかがわかりづらい
#enumerateはiterableなので、以下はエラーにならない
for t in enumerate(enumerate(reversed(range(1,11)))):
    x,y = t
    print(t)
    print(x, y)

e = enumerate(passlist)
#print(e[0]) #これは不可 値の取得ができない

for t in passlist.items(): #dictのiteratorはそのままではkeyしか返さない。
    print(t)
    x,y = t
    print(x, y)

#x.sortはlistのみ。他のiterableをsortしたかったら、sorted関数を使う
#また、sortedは新しいオブジェクトを返すが、list.insert,sort等は何も返さない
#lambdaの引数でアンパックを使いたいのだが・・・
print(sorted(passlist.items(),key=lambda x : len(x[1])))

#条件演算いろいろ
f = passlist
print(passlist is f) #equalsと同じ
str1 = "hogehoge"
str2 = "hogehoge"
print(str1 is str2) #これはtrue。不変オブジェクトだから、同じ参照しているはず

print(3 < 4 == (3+1)) #(3 < 4) and (4 == (3+1))
print((3 < 4) and (4 == (3+1)))

print("eho" in str1)
print("hogehogehoge" not in str2)
print((x := 3*4) and x == 12) #セイウチ演算子:=で、一時変数に値を束縛

#del文
#popと同じで削除するが、値を返さない
#スライスを渡して削除もできる
#リストというより、可変なシーケンス型に対して使える
#https://docs.python.org/ja/3/library/stdtypes.html?highlight=sort#mutable-sequence-types
strL = list(str1)
del(strL[2:5])
print(strL)
del(passlist["steve"])
print(passlist)


