# 題目說明：

# 請使用迴圈敘述撰寫一程式，讓使用者輸入兩個正整數a、b（a < b），利用迴圈計算從a開始連加到b的總和。例如：輸入a = 1、b = 100，則輸出結果為5050（1 + 2 + … + 100 = 5050）。

a = eval(input())
b = eval(input())
result = 0

for i in range(a, b+1):
    result += i

print(result)