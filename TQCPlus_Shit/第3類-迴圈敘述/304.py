# 題目說明：

# 請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數a，利用迴圈計算從1到a之間，所有5之倍數數字總和。

a = eval(input())
result = 0

for i in range(1, a + 1):
    if i % 5 == 0:
        result += i

print(result)
