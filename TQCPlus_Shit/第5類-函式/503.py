# 題目說明：

# 請撰寫一程式，讓使用者輸入兩個整數，接著呼叫函式compute()，
# 此函式接收兩個參數a、b，並回傳從a連加到b的和。

def compute(x ,y):
    sums = 0
    for i in range(x, y + 1):
        sums += i
    return sums

a = eval(input())
b = eval(input())

print(compute(a, b))