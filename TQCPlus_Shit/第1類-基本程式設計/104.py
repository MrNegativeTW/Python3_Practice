# 題目說明：

# 請撰寫一程式，輸入一圓的半徑，並加以計算此圓之面積和周長，最後請印出此圓的半徑（Radius）、周長（Perimeter）和面積（Area）。
# 提示1：需import math模組，並使用math.pi。
# 提示2：輸出浮點數到小數點後第二位。

import math

radius = eval(input())
print('Radius= % .2f' % radius)
print('Perimeter= % .2f' % (2 * math.pi * radius))
print('Area= % .2f' % (math.pi * radius ** 2))
