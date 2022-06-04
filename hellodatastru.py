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
