import Util.point as point

Point = point.Point #自分定義の名前にしたい場合　本当はモジュール名.関数やクラス名でアクセス

print(point.__name__)
print(dir(point))
#組み込み関数等はbuiltinsに入っている
import builtins
print(dir(builtins))
#sysには動作環境に関する変数の情報が入っている
import sys
print(dir(sys))

p1:Point = Point(3,4)
p2:Point = Point(10,3)

p3:Point = Point.add(p1,p2)
print(p1.x, p1.y)
print(p2.x, p2.y)
print(p3.x, p3.y)

print(p2.normal().length())
