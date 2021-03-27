# 題目說明：

# 請撰寫一程式，讓使用者輸入兩個整數，接著呼叫函式compute()，此函式接收兩個參數a、b，
# 並回傳 a ^ b 的值。

def compute(a, b):
    return a ** b

q = eval(input())
w = eval(input())

print(compute(q, w))