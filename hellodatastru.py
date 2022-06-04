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
