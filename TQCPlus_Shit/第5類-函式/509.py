# 題目說明：

# 請撰寫一程式，讓使用者輸入二個分數，分別是x/y和m/n（其中x、y、m、n皆為正整數），
# 計算這兩個分數的和為p/q，接著將p和q傳遞給名為compute()函式，
# 此函式回傳p和q的最大公因數（Greatest Common Divisor, GCD）。
# 再將p和q各除以其最大公因數，最後輸出的結果必須以最簡分數表示。

import math

def compute(x, y):
    return math.gcd(x, y)

a,b = eval(input())
c,d = eval(input())

p = a * d + c * b
q = b * d

gcd = compute(p, q)

print("{}/{} + {}/{} = {}/{}".format(a, b, c, d, int(p / gcd), int(q/gcd)))

