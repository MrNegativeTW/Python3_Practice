# 題目說明：

# 請使用迴圈敘述撰寫一程式，讓使用者輸入正整數n(1 < n)，計算以下公式的總和並顯示結果：
# https://jbprogramnotes.com/2020/05/tqc-%e7%a8%8b%e5%bc%8f%e8%aa%9e%e8%a8%80python-310-%e8%bf%b4%e5%9c%88%e5%85%ac%e5%bc%8f%e8%a8%88%e7%ae%97/
# 提示：輸出結果至小數點後四位。

import math

n = eval(input())
result = 0

for i in range(2, n + 1):
    result += 1 / (math.sqrt(i - 1) + math.sqrt(i))

print("%.4f" % result)