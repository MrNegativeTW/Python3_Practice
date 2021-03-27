# 題目說明：

# 請使用選擇敘述撰寫一程式，讓使用者輸入一個正整數，然後判斷它是否為偶數（even）。

a = eval(input())

if a % 2 == 0:
    print("{} is an even number.".format(a))
else:
    print("{} is not an even number.".format(a))