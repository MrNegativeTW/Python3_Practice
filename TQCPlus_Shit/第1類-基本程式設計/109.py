# 題目說明：

# 請撰寫一程式，讓使用者輸入一個正數s，代表正五邊形之邊長，計算並輸出此正五邊形之面積（Area）。
# 提示1：建議使用import math模組的math.pow及math.tan
# 提示3：輸出浮點數到小數點後第四位。

import math

s = eval(input())

print('%.4f' % ((5 * s ** 2) / (4 * math.tan(math.pi / 5))))
