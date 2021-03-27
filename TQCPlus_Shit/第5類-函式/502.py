# 題目說明：

# 請撰寫一程式，將使用者輸入的兩個整數作為參數傳遞給一個名為compute(x, y)的函式，
# 此函式將回傳x和y的乘積。

def compute(x, y):
    return x * y


a = eval(input())
b = eval(input())

print(compute(a, b))
