# 題目說明：

# 請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數n，利用迴圈計算並輸出n!的值。

a = eval(input())
result = 1

for i in range(2, a + 1):
    result *= i

print(result)