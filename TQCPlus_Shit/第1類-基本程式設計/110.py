# 題目說明：

# 請撰寫一程式，讓使用者輸入兩個正數n、s，代表正n邊形之邊長為s，計算並輸出此正n邊形之面積（Area）。
# 提示1：建議使用import math模組的math.pow及math.tan
# 提示3：輸出浮點數到小數點後第四位

import math

n = eval(input())
s = eval(input())

print('Area = %.4f' % ((n * s ** 2) / (4 * math.tan(math.pi / n))))