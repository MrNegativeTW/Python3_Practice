# 題目說明：

# 請撰寫一程式，計算費氏數列（Fibonacci numbers），
# 使用者輸入一正整數num(num >= 2)，
# 並將它傳遞給名為compute()的函式，
# 此函式將輸出費氏數列前num個的數值。

def compute(x):
    mList = [0, 1]
    for i in range(2, x):
        mList.append(mList[i - 2] + mList[i-1])

    for i in mList:
        print(i, end=" ")

a = eval(input())

while a <= 1:
    a = eval(input())

compute(a)
