# 題目說明：

# 請撰寫一程式，讓使用者輸入四個數字x1、y1、x2、y2，分別代表兩個點的座標(x1, y1)、(x2, y2)。計算並輸出這兩點的座標與其歐式距離。
# 提示1：歐式距離 = √((x1−x2)2+(y1−y2)2)
# 提示2：兩座標的歐式距離，輸出到小數點後第4位

import math

x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())

print('{}, {}'.format(x1, y1))
print('{}, {}'.format(x2, y2))
print('Distance = %.4f' % math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))
