# 題目說明：

# 請撰寫一程式，將使用者輸入的三個整數（代表一元二次方程式 ax^2 + bx + c = 0 的三個係數a、b、c）
# 作為參數傳遞給一個名為compute()的函式，該函式回傳方程式的解，如無解則輸出【Your equation has no root.】

# 提示：輸出有順序性

# https://priori.moe.gov.tw/download/textbook/math/grade8/book3/math-8-3-10-4.pdf

import math

def compute(a ,b, c):
    if b ** 2 - a * c >= 0:
        res1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        res2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        print("{}, {}".format(res1, res2))
    else:
        print("Your equation has no root.")


a = eval(input())
b = eval(input())
c = eval(input())

compute(a, b, c)
