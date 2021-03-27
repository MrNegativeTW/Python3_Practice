# 題目說明：

# 請撰寫一程式，讓使用者輸入兩個正整數x、y，
# 並將x與y傳遞給名為compute()的函式，此函式回傳x和y的最大公因數。

# 遞迴解法

import math

def compute(x, y):
    if y == 0:
        return x
    else:
        return compute(y, x % y)
    
a, b = eval(input())

print(compute(a, b))

# 套件解法
print(math.gcd(a,b))