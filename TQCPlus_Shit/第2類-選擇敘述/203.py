# 題目說明：

# 請使用選擇敘述撰寫一程式，讓使用者輸入一個西元年份，然後判斷它是否為閏年（leap year）或平年。
# 其判斷規則為：每四年一閏，每百年不閏，但每四百年也一閏。

a = eval(input())

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print("{} is a leap year".format(a))
else:
    print("{} is not a leap year".format(a))
