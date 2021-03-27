# 題目說明：

# 請撰寫一程式，讓使用者輸入數字，輸入的動作直到輸入值為9999才結束，然後找出其最小值，並輸出最小值。

a = eval(input())
mList = []

while a != 9999:
    mList.append(a)
    a = eval(input())

print(min(mList))